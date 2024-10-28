from configurations.config import *
import pandas as pd
import ast
import os
import zipfile
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


companies_file_names = companies.copy()
companies_file_names.remove('Berkshire Hathaway')
companies_file_names.remove('Eli Lilly')
companies_file_names += ['Berkshire_Hathaway', 'Eli_Lilly']

dfs_paths = {'final_df': './data/final_df.csv',
            'entities_df' : './data/entities_df.csv',
            'emotions_df':'./data/emotions_df.csv'
}

dfs_paths.update({company: f'./data/{company}_stock_df.csv' for company in companies_file_names})
            
def load_dfs():
    data_dir = './data'
    # Check if the data directory exists
    if not os.path.exists(data_dir):
        # Google Drive file link
        zip_file_url = os.getenv('ZIP_FILE_URL')  # Ensure this environment variable is set

        # Setup Chrome options
        options = Options()
        options.add_experimental_option("prefs", {
            "download.default_directory": data_dir,  # Set download directory to current folder
            "download.prompt_for_download": False,    # Disable download prompt
            "directory_upgrade": True,                # Automatically upgrade to specified folder
            "safebrowsing.enabled": True              # Enable Safe Browsing (might be required)
        })

        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        # Initialize WebDriver
        driver = webdriver.Chrome(options=options)

        try:
            # Open the Google Drive link
            driver.get(zip_file_url)

            # Wait for the download link to appear and click it
            time.sleep(5)  # Adjust if necessary
            download_link = driver.find_element(By.ID, "uc-download-link")
            download_link.click()

            # Wait for the download to complete; adjust this based on file size
            time.sleep(10)  
        finally:
            driver.quit()  # Close the browser

        # Find and unzip the downloaded file
        zip_file_path = os.path.join(data_dir, 'data.zip')
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(data_dir)


    dfs = {key: pd.read_csv(dfs_paths[key]) for key in dfs_paths.keys()}
    
    dfs['final_df']['Date'] = pd.to_datetime(dfs['final_df']['Date'])
    dfs['final_df']['Finbert_sentence_list'] = dfs['final_df']['Finbert_sentence_list'].apply(ast.literal_eval)
    dfs['final_df'].rename({'Unnamed: 0': 'id'}, axis=1, inplace=True)
    dfs['final_df'].sort_values('Date', inplace=True)

    dfs['entities_df'].drop('Unnamed: 0', axis=1, inplace=True)
    dfs['emotions_df'].drop('Unnamed: 0', axis=1, inplace=True)
    dfs['emotions_df']['text_sentences'] = dfs['emotions_df']['text_sentences'].apply(ast.literal_eval)

    return dfs
