import pandas as pd

# Load the DataFrame
df = pd.read_csv('./data/final_df.csv', parse_dates=['Date'])
entities_df = pd.read_csv('./data/entities_df.csv')
emotions_df = pd.read_csv('./data/emotions_df.csv')

# Group by 'Company' and 'Month', then apply a function to sample articles
small_df = df.groupby(['Company', 'Month']).apply(lambda x: x.sample(n=min(len(x), 5), random_state=1)).reset_index(drop=True)
small_df.rename({'Unnamed: 0': 'Original_index'}, axis=1, inplace=True)

small_entities_df = entities_df[entities_df['Original_index'].isin(small_df['Original_index'])]

small_emotions_df = emotions_df[emotions_df['Original_index'].isin(small_df['Original_index'])]

print(small_df.shape)
print(small_entities_df.shape)
print(small_emotions_df.shape)

small_df.to_csv('./tmp/data/final_df.csv')
small_entities_df.to_csv('./tmp/data/entities_df.csv')
small_emotions_df.to_csv('./tmp/data/emotions_df.csv')