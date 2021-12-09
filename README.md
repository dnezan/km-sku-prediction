[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qIl619KUAgBG2nD1lZzUwwVBwgqiyfDV?usp=sharing)

# SKU Sales Prediction using Prophet
Predict the daily, weekly, and monthly demand for SKUs being sold by a vendor based on history of daily sales as well as other external features such as weather, holidays, and promotional data. 

## Preqrequisites
- Python 
- Pandas
- Numpy
- Prophet by Facebook
- Plotly
- Matplotlib
- pywt

Run KM_forecast_main.ipynb

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

Daily Data :
The Colab code contains snippets to visualise all 3 SKUs from our dataset but for the purpose of documentation, let us use a single SKU as reference. 
![daily_viz](https://raw.githubusercontent.com/dnezan/km-sku-prediction/main/data_images/Unknown-14.png)

In order to better visualize the change in trends as well as predict sales over different periods of time, we can bin the daily data into weekly and monthly data.

![monthly_viz](https://raw.githubusercontent.com/dnezan/km-sku-prediction/main/data_images/Unknown-15.png)

## Denoising
We apply denoising with Direct Wavelet Transform on the data. Since our data contains many 0 values, we cannot use Box-Cox or any other power transformation techniques to denoise the data.

Denoised Daily Data :

![denoise_daily_viz](https://raw.githubusercontent.com/dnezan/km-sku-prediction/main/data_images/Unknown-5.png)

## Modeling
For modeling, we use Prophet by Facebook, a time series model for forecasting. We include US holiday features as additional regressors.
Prophet requires data to be in the format of 
```
ds        |   y    
-----------------------
date1     | (demand)   
date2     | (demand)   
```

## Predicting
We train data on 1900 days and predict on 30 days.

## Evaluating
we found a spike because of promotions



