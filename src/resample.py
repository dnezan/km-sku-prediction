#Copyright (C) Mallow Technologies Pvt Ltd. - All Rights Reserved
#Unauthorized copying of this file, via any medium is strictly prohibited
#Proprietary and confidential
#Written by Dinesh Sreekanthan <dinesh.sreekanthan@mallow-tech.com>, December 2021

import numpy as np 
import pandas as pd

#Enter sku number
a=0
product_name_x = str(df_new.SKU[a])

sales_x = df_new.iloc[a].tolist()
del sales_x[0] #remove item_id
dates_list = df_new.columns.tolist()
del dates_list[0] #remove column name

df_x = pd.DataFrame(np.transpose([dates_list, sales_x]))
df_x.columns = ["ds", "y"]
df_x["ds"]= pd.to_datetime(df_x["ds"])

df_var = df_x

df_var['ds'] = pd.to_datetime(df_var['ds'])
weekly_df = df_var.resample('W', on='ds').apply(sum)
monthly_df = df_var.resample('M', on='ds').apply(sum)
daily_df = df_var.resample('D', on='ds').apply(sum)
