"""
library for df operations
"""
from sklearn import linear_model
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# ------------------------------------------------------
# Time operations
def point_trigger():
    rdf = rdf.reset_index(drop=True)
    pwr_index = rdf[rdf['cv_dc_kw'] > 3.5].index.min()
    rdf['elapsed_sec'] = rdf["elapsed_sec"] - rdf["elapsed_sec"].iloc[pwr_index]
# ------------------------------------------------------


# ------------------------------------------------------
# Filtering
def delta(df):
    df["delta_time"] = df["elapsed_sec"].diff()
def average(df):
    avg_window = 3
    df["delta_time"] = df["delta_time"].rolling(window=avg_window).mean()
def interpolate(df):
    df = df.interpolate(method="linear", limit_direction="both")
# ------------------------------------------------------
    
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