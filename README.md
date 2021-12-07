[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qIl619KUAgBG2nD1lZzUwwVBwgqiyfDV?usp=sharing)

# SKU Sales Prediction using Prophet
Predict the daily and monthly demand for SKUs being sold by a vendor based on history of sales as well as other external factors such as weather and holidays. 

## Preqrequisites
- Python 
- Pandas
- Numpy
- Prophet by Facebook
- Plotly
- Matplotlib
- pywt

## Dataset
The data was collected by the vendor's sales data over different periods of time. For testing purposes, the datasets used for testing were
- 3786 unique items being sold daily over a period of 01.01.2021 - 25.11.2021 (11 months)
- 3 top selling items sold daily over a period of 2016-05-08 - 2021-12-06 (67 months)
- 15 top selling items being sold monthly over 3 years 

It is assumed that the csv data is exported in the format of 
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
We can visualise the initial dataset as well as denoised dataset using matplotlib/Plotly.

Daily Data :

![daily_viz](https://raw.githubusercontent.com/dnezan/km-sku-prediction/main/data_images/Unknown-6.png)

Monthly Data :

![monthly_viz](https://raw.githubusercontent.com/dnezan/km-sku-prediction/main/data_images/Unknown-4.png)

## Denoising
We apply denoising with Direct Wavelet Transform on the data. This proved only useful for highly noisy, daily data and not for monthly data points.

Denoised Daily Data :

![denoise_daily_viz](https://raw.githubusercontent.com/dnezan/km-sku-prediction/main/data_images/Unknown-5.png)

## Modeling
For modeling, we use Prophet by Facebook, a time series model for forecasting. We include US holiday features as additional regressors.

## Predicting
We train data on 1900 days and predict on 30 days.

## Evaluating
we found a spike because of promotions



