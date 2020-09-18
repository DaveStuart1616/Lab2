# %% import dataframe from pickle file
import pandas as pd

df = pd.read_pickle("UK.pkl")

df.head(10)


# %% convert dataframe to invoice-based transactional format
dataset = df.groupby("InvoiceNo").apply(
    lambda d: d["Description"].to_list()) #list(d["Description"])

# %% apply apriori algorithm to find frequent items and association rules

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori


te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)

from mlxtend.frequent_patterns import association_rules
rules = association_rules(frequent_itemsets, min_threshold=0.6)
rules
# %% count of frequent itemsets that have more then 1/2/3 items,
# and the frequent itemsets that has the most items

length = frequent_itemsets["itemsets"].apply(len)

frequent_itemsets[length > 1]

# %% top 10 lift association rules
rules.sort_values("lift", ascending=False).head(10)


# %% scatterplot support vs confidence
import seaborn as sns
import matplotlib.pyplot as plt

sns.scatterplot(data=rules, x="support", y="lift", alpha=0.5)
plt.xlabel("Support")
plt.ylabel("Confidence")
_ =plt.title("Support vs Lift")


# %% scatterplot support vs lift
