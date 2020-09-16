# %% Import excel to dataframe
import pandas as pd
import numpy as np

df = pd.read_excel("Online Retail.xlsx")

# %%  Show the first 10 rows
df.head(10)


# %% Generate descriptive statistics regardless the datatypes
df.describe()


# %% Remove all the rows with null value and generate stats again
df.drop.na()
df.describe()

# %% Remove rows with invalid Quantity (Quantity being less than 0)
df[(df["Quantity"] > 0)]


# %% Remove rows with invalid UnitPrice (UnitPrice being less than 0)
df[~(df["UnitPrice"] < 0)]


# %% Only Retain rows with 5-digit StockCode
df.drop(~("StockCode", numeric_only))


# %% strip all description
df = pd.read_excel("Online Retail.xlsx")



# %% Generate stats again and check the number of rows
df.describe()
d.shape

# %% Plot top 5 selling countries
import matplotlib.pyplot as plt
import seaborn as sns

top5_selling_countries = df["Country"].value_counts()[:5]
sns.barplot(x=top5_selling_countries.index, y=top5_selling_countries.values)
plt.xlabel("Country")
plt.ylabel("Amount")
plt.title("Top 5 Selling Countries")


# %% Plot top 20 selling products, drawing the bars vertically to save room for product description

top_20_products = df["StockCode"].value_counts()[:20]
sns.countplot(x=top_20_products.values, y=top_20_products.index)
plt.xlabel("Amount")
plt.ylabel("Product")
plt.title("Top 20 Selling Products")


# %% Focus on sales in UK
df.loc["Country" == "United Kingdom"]
# df = df.loc[(df.Country == "United Kingdom")

#%% Show gross revenue by year-month
from datetime import datetime

df["YearMonth"] = df["InvoiceDate"].apply(
    lambda dt: datetime(year=dt.year, month=dt.month, day=1)
)



# %% save df in pickle format with name "UK.pkl" for next lab activity
# we are only interested in InvoiceNo, StockCode, Description columns
