import numpy as np
import matplotlib.pyplot as plt  # To visualize
import pandas as pd  # To read data
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def create_linear(df, x_col, y_col, intercept=True):
    x_data = df[x_col].values.reshape(-1, 1)
    y_data = df[y_col].values.reshape(-1, 1)

    linear_regressor = LinearRegression(fit_intercept=intercept)  # create object for the class
    linear_regressor.fit(x_data, y_data)  # perform linear regression
    y_pred = linear_regressor.predict(x_data)  # make predictions

    coef = linear_regressor.coef_
    print(f"Coefficients: {coef}")

    intercept = linear_regressor.intercept_
    print(f"Intercept: {intercept}")

    score = r2_score(y_data, y_pred)
    print(f"Score: {score}")

    # plot to see correlation
    plt.scatter(x_data, y_data)
    plt.plot(x_data, y_pred, color='red')
    plt.show()


def multiple_linear(df, x_cols, y_col, intercept=True, show_plts=True):
    # x_data = df[x_cols].values.reshape(-1, 1)
    # # handle categorical variable
    # states = pd.get_dummies(x_data, drop_first=True)
    # # dropping extra column
    # # x_data = x_data.drop(‘State’, axis = 1)
    # # concatation of independent variables and new cateorical variable.
    # x_data = pd.concat([x_data, states], axis=1)
    # print(x_data.head())

    x_data = df[x_cols]
    y_data = df[y_col]

    linear_regressor = LinearRegression(fit_intercept=intercept)  # create object for the class
    linear_regressor.fit(x_data, y_data)  # perform linear regression
    y_pred = linear_regressor.predict(x_data)  # make predictions

    coef = linear_regressor.coef_
    print(f"Coefficients: {coef}")

    intercept = linear_regressor.intercept_
    print(f"Intercept: {intercept}")

    score = r2_score(y_data, y_pred)
    print(f"Score: {score}")

    # plot to see correlation on individual variables
    if show_plts is True:
        for x_col in x_cols:
            plt.scatter(df[x_col], y_data)
            plt.plot(df[x_col], y_pred, color='red')
            plt.show()

    # plotting from coefficients
    index = df['Index']
    return coef, intercept





