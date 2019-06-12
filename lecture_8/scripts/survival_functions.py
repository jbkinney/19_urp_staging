import pandas as pd
from lifelines import KaplanMeierFitter

import matplotlib.pyplot as plt
import seaborn as sns


def survival_plot(df, grouping_col, time_col, event_col):
    grouped_df = df.groupby(grouping_col)
    fig, ax = plt.subplots()
    for name, index in grouped_df.groups.items():
        kmf = KaplanMeierFitter()
        kmf.fit(df.loc[index, time_col], df.loc[index, event_col], label=name)
        kmf.plot(ax=ax)
    sns.despine()
    plt.show()
    
def survival_plot_w_type_hints(df : pd.DataFrame, grouping_col : str, time_col: str, event_col : str):
    grouped_df = df.groupby(grouping_col)
    fig, ax = plt.subplots()
    for name, index in grouped_df.groups.items():
        kmf = KaplanMeierFitter()
        kmf.fit(df.loc[index, time_col], df.loc[index, event_col], label=name)
        kmf.plot(ax=ax)
    sns.despine()
    plt.show()