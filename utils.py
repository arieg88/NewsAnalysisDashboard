from configurations.config import *
import pandas as pd
import ast


companies_file_names = companies.copy()
companies_file_names.remove('Berkshire Hathaway')
companies_file_names.remove('Eli Lilly')
companies_file_names += ['Berkshire_Hathaway', 'Eli_Lilly']

dfs_paths = {'final_df': './data/final_df.csv',
            'entities_df' : './data/entities_df.csv',
}

dfs_paths.update({company: f'./data/{company}_stock_df.csv' for company in companies_file_names})

def load_dfs():
    dfs = {key: pd.read_csv(dfs_paths[key]) for key in dfs_paths.keys()}
    dfs['final_df']['Date'] = pd.to_datetime(dfs['final_df']['Date'])
    dfs['final_df']['Finbert_sentence_list'] = dfs['final_df']['Finbert_sentence_list'].apply(ast.literal_eval)
    dfs['final_df'].rename({'Unnamed: 0': 'id'}, axis=1, inplace=True)
    dfs['entities_df'].drop('Unnamed: 0', axis=1, inplace=True)

    return dfs
