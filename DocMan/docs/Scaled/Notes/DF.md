# Pandas DF operations


### Imports
```python
"""
library for df operations
"""
from sklearn import linear_model
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
```

### Point Trigger and Time
```python
# ------------------------------------------------------
# Time operations
# creating time array
df["_time"] = pd.to_datetime(df["_time"])
df["elapsed_sec"] = (df["_time"] - df["_time"].iloc[0]).dt.total_seconds()
df = df.set_index("_time")
df = df.interpolate()
# ------------------------------------------------------
def point_trigger():
    rdf = rdf.reset_index(drop=True)
    pwr_index = rdf[rdf['cv_dc_kw'] > 3.5].index.min()
    rdf['elapsed_sec'] = rdf["elapsed_sec"] - rdf["elapsed_sec"].iloc[pwr_index]
# ------------------------------------------------------
```

### Filtering and Condensing
```python
# ------------------------------------------------------
df = df[df["column"] == 10]
df = df.query("gender == 'Female' and 20 <= age <= 30")
def delta(df):
    df["delta_time"] = df["elapsed_sec"].diff()
def average(df):
    avg_window = 3
    df["delta_time"] = df["delta_time"].rolling(window=avg_window).mean()
def interpolate(df):
    df = df.interpolate(method="linear", limit_direction="both")
# summing a column
sum = df['column'].sum()
# average a row
df["avg"] = df[avg_cols].mean(axis=1)
# sum / mean a row
df['column'] = df[['a', 'b']].sum(axis=1)
# sort
df = df.sort_values("age")

# groupby('column') and aggregate values
dfg = df.groupby("Purchase Order").agg({"line_cost": "sum", "Order Date": "first"})
count = df["column"].value_counts()
# ------------------------------------------------------
```

### Filtering and Condensing
```python
# ------------------------------------------------------
# Creating Linear trendline
def create_trend(df, x_col, y_col, title, x_label, y_label):
    X = df[[x_col]]
    Y = df[[y_col]]
    lr = linear_model.LinearRegression()
    lr.fit(X, Y)
    trend_text = f"{y_label} = {round(lr.coef_[0][0], 2)} * {x_label} + {round(lr.intercept_[0], 2)}"
    print(trend_text)
    df[f"{y_col}_trend"] = lr.predict(X)

    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col])
    ax.plot(df[x_col], df[f"{y_col}_trend"])
    ax.set_title(title)
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.text(0.1, 0.8, trend_text, horizontalalignment='left', verticalalignment='top', transform=ax.transAxes)
    ax.grid()
    return fig
# ------------------------------------------------------
```
