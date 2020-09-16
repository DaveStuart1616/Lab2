# %% import pandas and read the csv file 
# modify the path if needed
import pandas as pd

df = pd.read_csv("DATA475_lab_rectangles_data.csv")
df["area"] = df["length"] * df["width"]

# %%
summary = [
    ("Total Count ", df["area"].shape[0]),
    ("Total Area  ", df["area"].sum()),
    ("Average Area", df["area"].mean()),
    ("Maximum Area", df["area"].max()),
    ("Minimum Area", df["area"].min()),
]

for key, value in summary:
    print(f"{key}: {str(value)}")

# %%
#dfp = pd.DataFrame(dict(summary), index=[0])
#dfp.to_csv("summary2.csv")
output_df = pd.DataFrame(dict(summary), index=[0])
output_df.to_csv("summary2.csv", index=False)
