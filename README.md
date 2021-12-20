[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qIl619KUAgBG2nD1lZzUwwVBwgqiyfDV?usp=sharing)

# SKU Sales Prediction using Prophet
## How to use Prophet for time series sales forecasting using historical data, seasonality features and other regressors 
These are my notebooks I used while designing a pipeline for our commercial web app used to predict the daily, weekly, and monthly demand for SKUs being sold by a vendor based on history of daily sales as well as other external features such as weather, holidays, and promotional data. 

## Preqrequisites
- Python                        3.6.9
- pandas                        1.1.5
- numpy                         1.19.5
- prophet                       1.0.1
- plotly                        4.4.1
- matplotlib                    3.2.2
- pystan                        2.19.1.1
- scikit-learn                  1.0.1 (optional)
- scipy                         1.4.1 (optional)

Run KM_forecast_main_clean.ipynb

## Pipeline
![ml_pipeline](https://github.com/dnezan/km-sku-prediction/blob/main/data_images/KwickMetrics%20Forecast%20Pipeline-9.png?raw=true)
Chart produced in Lucidchart

## Dataset
The data was collected by the vendor's sales data over different periods of time. For testing purposes, the datasets used for testing were
- 3786 unique items being sold daily over a period of 01.01.2021 - 25.11.2021 (11 months)
- 15 top selling items being sold monthly over 3 years 
- 3 top selling items sold daily over a period of 2016-05-08 - 2021-12-06 (67 months)
The last dataset is utilised for the final implementation of the pipeline.

It is assumed that the csv data is exported sorted in ascending order by item_id in the format of 
```
item_id | timestamp (yy-mm-dd) | demand
```
To run the notebook in Collab, make sure your dataset is saved with the right name in your Google Drive. Instructions are included in the notebooks to integrate your Google Drive with Collab.

*Unfortunately access to the datasets used cannot be provided under license.*

## Data Preprocessing
The data is preprocessed to deal with missing dates for every SKU as well as reformatting the data in such a way that each day is stored column-wise and the sales of each SKU is row-wise, grouped by every unique SKU in the dataset. The new dataset is also populated with existing sales data as well as storing 0 sales for missing dates.
```
SKU            | start_date | ... | end_date
--------------------------------------------
(name of SKU1) | (demand)   | ... | (demand)
(name of SKU2) | (demand)   | ... | (demand)
```
## Visualising
We can visualise the initial dataset as well as denoised dataset using Plotly.

The Colab code contains snippets to visualise all 3 SKUs from our dataset but for the purpose of documentation, let us use a single SKU as reference. 

Daily Data :

![daily_viz](https://raw.githubusercontent.com/dnezan/km-sku-prediction/main/data_images/Unknown-14.png)

In order to better visualize the change in trends as well as predict sales over different periods of time, we can bin the daily data into weekly and monthly data.

![monthly_viz](https://github.com/dnezan/km-sku-prediction/blob/main/data_images/Unknown-22.png?raw=true)

## Denoising
We apply denoising with Direct Wavelet Transform on the data. Since our data contains many 0 values, we cannot use Box-Cox or any other power transformation techniques to denoise the data.

Denoised Daily Data :

![denoise_daily_viz](https://raw.githubusercontent.com/dnezan/km-sku-prediction/main/data_images/Unknown-16.png)

## Modeling
For modeling, we use Prophet by Facebook, a time series model for forecasting. We include US holiday features as additional regressors.  
Prophet requires data to be in the format of 
```
ds        |   y    
-----------------------
date1     | (demand)   
date2     | (demand)   
```
For the purpose of testing the effect of specific days on sales, we will use daily sales data to train the model. We then take the sum of all the predicted days of the month and compare this against the month bin of our training data. This way, we eliminate a lot of the noise of the high frequency data and provide the user with a monthly sales forecast with an upper and lower bound.
We can add additional features such as regional holidays and historical promotional data. We include the following US holidays while fitting the model.
```
0                 New Year's Day
1     Martin Luther King Jr. Day
2          Washington's Birthday
3                   Memorial Day
4               Independence Day
5                      Labor Day
6                   Columbus Day
7                   Veterans Day
8                   Thanksgiving
9                  Christmas Day
10      Christmas Day (Observed)
11     New Year's Day (Observed)
12       Veterans Day (Observed)
```

## Predicting
There are two ways to approach this problem. We will first train the model on the first 900 days of sales. Now we can either predict the next 2039-900 days all at once or we can predict for iterative months while updating the trained model every month. The first approach has the problem of not being able to accurately account for spikes in sales caused by features we do not have control over. For example, a pandemic like COVID-19 or even aggressive sales marketing will impact the sales without us being able to account for it. Therefore, we try the second approach of training for 0 to x months, testing for x+1 month, updating till x+1 month, training for x+2 month, and so on.

![simulation](https://raw.githubusercontent.com/dnezan/km-sku-prediction/main/data_images/results_4.gif)
Simulating a user adding new daily data and the model being refitted every month

## Evaluating
we found a spike because of promotions



