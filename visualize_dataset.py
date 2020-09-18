# %% Import excel to dataframe
import pandas as pd
import numpy as np

df = pd.read_excel("Online Retail.xlsx")

# %%  Show the first 10 rows
df.head(10)


# %% Generate descriptive statistics regardless the datatypes
df.describe(include="all")


# %% Remove all the rows with null value and generate stats again
df = df.dropna()
df.describe(include="all")

# %% Remove rows with invalid Quantity (Quantity being less than 0)
df = df[df["Quantity"] > 0]
df.describe(include="all")

# %% Remove rows with invalid UnitPrice (UnitPrice being less than 0)
df = df[df["UnitPrice"] > 0]
df.describe(include="all")

# %% Only Retain rows with 5-digit StockCode
is_length_5 = df["StockCode"].astype(str).apply(len) == 5
is_numeric = df["StockCode"].astype(str).str.isnumeric()
df = df[is_length_5 & is_numeric]
df.describe(include="all")

# %% strip Description - remove white space
df["Description"] = df["Description"].str.strip()
df.describe(include="all")

# %% Generate stats again and check the number of rows
df.describe(include="all")

# %% Plot top 5 selling countries
import matplotlib.pyplot as plt
import seaborn as sns

top5_selling_countries = df["Country"].value_counts()[:5]
sns.barplot(x=top5_selling_countries.index, y=top5_selling_countries.values)
plt.xlabel("Country")
plt.ylabel("Amount")
plt.title("Top 5 Selling Countries")


# %% Plot top 20 selling products, drawing the bars vertically to save room for product description

top20_selling_products = df["Description"].value_counts()[:20]
sns.barplot(
    y=top20_selling_products.index, 
    x=top20_selling_products.values
)
plt.ylabel("Product")
plt.xlabel("Amount")
plt.title("Top 20 Selling Products")

# %%
#same as above but with countplot
#sns.countplot(
#   data=df,
#   y="Description",
#   order=df["Description"].value_counts().index[:20]
#)
     

# %% Focus on sales in UK
df = df[df["Country"] == "United Kingdom"]


#%% Show gross revenue by year-month
from datetime import datetime

df["YearMonth"] = df["InvoiceDate"].apply(
    lambda dt: datetime(year=dt.year, month=dt.month, day=1)
)
#%%
df["GrossRevenue"] = df["Quantity"] * df["UnitPrice"]
df_y_m = df.groupby(["YearMonth"]).sum()["GrossRevenue"].reset_index()

#%%
sns.lineplot(x="YearMonth" , y="GrossRevenue" , data=df_y_m) 

# %% save df in pickle format with name "UK.pkl" for next lab activity
# we are only interested in InvoiceNo, StockCode, Description columns
#df.to_pickle("UK.pkl")
df[["InvoiceNo", "StockCode", "Description"]].to_pickle("UK.pkl")
# %%
