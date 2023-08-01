import pandas as pd

# create a DataFrame based on the given dataset for the asked time period
data = pd.read_excel("liquorsales2016_2019.xlsx")
df = pd.DataFrame(data)

# group the DataFrame by zip codes and find the most popular item for each
grouped_zips = df.groupby(["zip_code"])
max_bottles_index = grouped_zips["bottles_sold"].idxmax()
most_popular = df.loc[max_bottles_index, ['zip_code', 'item_description', 'bottles_sold']]
most_popular = most_popular.sort_values(by="bottles_sold", ascending=False)
most_popular = most_popular.reset_index(drop=True)
most_popular.to_excel("Most popular item per zip code.xlsx", index=False)

# group the DataFrame by stores and find the contribution of each store in the total sales
total_sales = df["sale_dollars"].sum()
grouped_stores = df.groupby(["store_name"])["sale_dollars"].sum()/total_sales*100
grouped_stores.to_excel("Percentage of sales per store.xlsx", float_format='%.4f')
