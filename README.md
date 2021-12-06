[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1qIl619KUAgBG2nD1lZzUwwVBwgqiyfDV?usp=sharing)

# SKU Inventory Prediction using Prophet
I am trying to predict the demand for an SKU being sold on an ecommerce website based on history of sales as well as other external factors such as weather and holidays. 

- Preqrequisites
- Data Collection
- Data Preparation/Preprocessing
- Denoising
- Visualising
- Modeling
- Predicting
- Evaluating

## Preqrequisites
Python (IDE is Google Collab)
Pandas
Numpy
Prophet by Facebook
Plotly
Matplotlib

## Data Collection
The initial data was collected by the vendor from 3786 unique items being sold daily over a period of about 1 year (01.01.2021 - 25.11.2021). After showcasing proof of concept, the final dataset consisted of the top 15 most sold items being sold weekly over 3 years.

## Data Preparation/Preprocessing
Currently, the data is being preprocessed to deal with missing dates for every SKU as well as reformatting the data in such a way that each day is stored column-wise and the sales of each SKU is row-wise, grouped by every unique SKU in the dataset.

## Denoising
We apply denoising with Direct Wavelet Transform on the data.

## Visualising
Visualise the initial dataset as well as denoised dataset using Plotly
## Modeling

## Predicting

## Evaluating




