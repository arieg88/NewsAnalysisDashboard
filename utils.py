from configurations.config import *
import pandas as pd

dfs_paths = {'final_df': './data/final_df.csv',
            'entities_df_path' : './data/entities_df.csv',
}

dfs_paths.update({company: f'./data/{company}_stock_df.csv' for company in companies})

def load_dfs():
    dfs = {key: pd.read_csv(dfs_paths[key]) for key in dfs_paths.keys()}
    dfs['final_df']['Date'] = pd.to_datetime(dfs['final_df']['Date'])
    
    return dfs
