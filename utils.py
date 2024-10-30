from configurations.config import *
import pandas as pd
import ast
import os
import requests
import zipfile

# List of company filenames excluding 'Berkshire Hathaway' and 'Eli Lilly'
companies_file_names = companies.copy()
companies_file_names.remove('Berkshire Hathaway')
companies_file_names.remove('Eli Lilly')
companies_file_names += ['Berkshire_Hathaway', 'Eli_Lilly']

# Paths to the required DataFrames
dfs_paths = {
    'final_df': './data/final_df.csv',
    'entities_df': './data/entities_df.csv',
    'emotions_df': './data/emotions_df.csv'
}

# # Update dfs_paths with stock DataFrame paths for each company
# dfs_paths.update({company: f'./data/{company}_stock_df.csv' for company in companies_file_names})

def download_dfs(data_dir='./data'):
    """
    Downloads a zip file containing DataFrames from Google Drive, 
    extracts the content, and saves it to the specified directory.

    Parameters:
        data_dir (str): Directory where the data will be stored.
    """
    os.makedirs(data_dir)

    # Google Drive file link (ensure it's the direct download link)
    zip_file_url = os.getenv('ZIP_FILE_URL')

    # Download the zip file
    response = requests.get(zip_file_url)

    # Save the content as a zip file
    zip_file_path = os.path.join(data_dir, 'data.zip')
    with open(zip_file_path, 'wb') as f:
        f.write(response.content)

    # Unzip the file and extract its contents
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(data_dir)
    print('File extracted successfully.')

def load_dfs():
    """
    Loads the required DataFrames from CSV files. 
    Downloads the data if the files do not exist.

    Returns:
        dict: A dictionary containing the loaded DataFrames.
    """
    data_dir = './data'
    if not os.path.exists(data_dir):
        download_dfs(data_dir)

    # Read the DataFrames from the specified paths
    dfs = {key: pd.read_csv(dfs_paths[key]) for key in dfs_paths.keys()}
    
    # Process the final_df DataFrame
    dfs['final_df']['Date'] = pd.to_datetime(dfs['final_df']['Date'])
    dfs['final_df']['Finbert_sentence_list'] = dfs['final_df']['Finbert_sentence_list'].apply(ast.literal_eval)
    dfs['final_df'].rename({'Unnamed: 0': 'id'}, axis=1, inplace=True)
    dfs['final_df'].sort_values('Date', inplace=True)
    
    if 'Original_index' in dfs['final_df'].columns:
        dfs['final_df']['Original_index'] = dfs['final_df']['Original_index'].astype(int)
        dfs['final_df'].set_index('Original_index', inplace=True)
    
    # Clean up unnecessary columns from entities_df and emotions_df
    dfs['entities_df'].drop('Unnamed: 0', axis=1, inplace=True)
    dfs['emotions_df'].drop('Unnamed: 0', axis=1, inplace=True)
    dfs['emotions_df']['text_sentences'] = dfs['emotions_df']['text_sentences'].apply(ast.literal_eval)

    return dfs
