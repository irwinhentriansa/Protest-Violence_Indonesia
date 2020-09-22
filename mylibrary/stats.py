import pandas as pd
import numpy as np

def summary_table(df):
    summary = pd.DataFrame(dict(dataFeatures = df.columns,
                                  dataType = df.dtypes,
                                  null = df.isna().sum(),
                                  null_pct = round(df.isna().sum() / len(df) *100,2),
                                  unique = df.nunique(),
#                                   uniqueSample = [list(df[i].drop_duplicates().sample(2)) for i in df.columns]
                               )
                           ).reset_index(drop=True)
    summary['unique_pct'] = round(summary['unique'] / len(df) *100,2)
    return summary
