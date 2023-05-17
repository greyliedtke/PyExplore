"""
Script for analyzing data to predict things...
"""

import pandas as pd
from Analysis.DF_Descriptor import *
from Analysis.Trending import *
from Analysis.Filter import *

# selecting runs
df_r26 = pd.read_csv('../ScaledData/OldMethods/RunFilesCalculated/OLD/g_SCG_026_MERGE.csv')
df_r23 = pd.read_csv('../ScaledData/OldMethods/RunFilesCalculated/OLD/SCG_023_MERGE.csv')

# setting up columns
x_cols = ['Ch1 RMS_[ m/s2 ]', 'Ch2 RMS_[ m/s2 ]']
x_factors = ['ch_1_v', 'ch_2_v']
y_factor = 'n2 speed sensor'


# playing around with speed from vibration data...
def vibs_to_speed(r_df):
    # zero out readings
    r_df[x_factors[0]] = filter_offset_df(r_df[x_cols[0]])
    r_df[x_factors[1]] = filter_offset_df(r_df[x_cols[1]])

    coef, intercept = multiple_linear(r_df, x_factors, y_factor, show_plts=False)
    return coef, intercept


c26, i26 = vibs_to_speed(df_r26)
c23, i23 = vibs_to_speed(df_r23)

# averaging coefficients
a_coef = [np.average([c26[0], c23[0]]), np.average([c26[1], c23[1]])]
a_intercept = np.average([i26, i23])


def pred_vs_actual(r_df):
    r_df['pred_vals'] = a_coef[0] * r_df[x_factors[0]] + a_coef[1] * r_df[x_factors[0]] + a_intercept
    plt.plot(r_df['Index'], r_df['pred_vals'])
    plt.plot(r_df['Index'], r_df['n2 speed sensor'], color='red')
    plt.legend(['Predicted', 'Actual'])
    plt.show()


pred_vs_actual(df_r26)
pred_vs_actual(df_r23)

