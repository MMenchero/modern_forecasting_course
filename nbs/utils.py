import pandas as pd 
import numpy as np

def load_and_transform(file_name, target):
    """
    Transforms data to the format required by the nixtlaverse. 
    
    Args:
        file_name (str): Name of the file to load
        target (str): Name of the target variable

    Returns:
        df_long (pd.DataFrame): Long format dataframe with unique_id, ds, and target variable
    """
    df = pd.read_csv(f'../data/{file_name}.csv')
    df.insert(0, 'unique_id', df['Client'].astype(str)+'-'+df['Warehouse'].astype(str)+'-'+df['Product'].astype(str))
    df.drop(['Client', 'Warehouse', 'Product'], axis=1, inplace=True)

    df_long = pd.melt(
        df, 
        id_vars=['unique_id'],
        var_name='ds',
        value_name=target
    )

    df_long = df_long.sort_values(by=['unique_id', 'ds']).reset_index(drop=True)

    return df_long 

def vn1_competition_evaluation(forecasts): 
    """
    Computes competition evaluation scores
    """
    actual = load_and_transform('../data/Phase 2 - Sales', 'y') # load actual values
    actual['ds'] = pd.to_datetime(actual['ds'])

    res = actual[["unique_id", "ds", "y"]].merge(forecasts, on=["unique_id", "ds"], how="left")

    scores = {}
    
    for model in [col for col in forecasts.columns if col not in ["unique_id", "ds"]]:
        abs_err = np.nansum(np.abs(res[model] - res["y"]))
        err = np.nansum(res[model] - res["y"])
        score = abs_err + abs(err)
        score = score / res["y"].sum()
        scores[model] = round(score, 5)
    
    score_df = pd.DataFrame(list(scores.items()), columns=["model", "score"])
    score_df = score_df.sort_values(by="score")
    return score_df