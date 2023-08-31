"""
"""

import pandas as pd
df = pd.Dataframe()

# zero and filter a column

# converting to and replace commas...
df['column'] = pd.to_numeric(df['column'].str.replace(',', ''), errors='coerce')
cols = list(df.columns)
df.describe() 

# summing a column
sum = df['column'].sum()

# average a row
df["avg"] = df[avg_cols].mean(axis=1)

# sum / mean a row
df['column'] = df[['a', 'b']].sum(axis=1)

# truncating
df = df.nlargest(200, 'column')
df = df.nsmallest(200, 'column')

# filtering dataset
df = df[df['column']==10]
df = df.query("gender == 'Female' and 20 <= age <= 30")

# sort
df = df.sort_values("age")

# groupby('column') and aggregate values
dfg = df.groupby('Purchase Order').agg({'line_cost': 'sum', 'Order Date': 'first'})

# manipulating
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# perform arithmetic operations on the DataFrame using eval()
df.eval('C = A + B', inplace=True)

# create series that counts occurences of values in column...
count = df['column'].value_counts()

# creating time array
df["_time"] = pd.to_datetime(df["_time"])
df["elapsed_sec"] = (df["_time"] - df["_time"].iloc[0]).dt.total_seconds()
df = df.set_index("_time")
df = df.interpolate()

