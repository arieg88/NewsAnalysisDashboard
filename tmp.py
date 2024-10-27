import pandas as pd

# Load the DataFrame
df = pd.read_csv('./data/final_df.csv', parse_dates=['Date'])

# Count duplicates by Title and Date
duplicate_counts = df.groupby(['Title', 'Date']).size().reset_index(name='Count')

# Filter to get only those with more than one occurrence
duplicates = duplicate_counts[duplicate_counts['Count'] > 1]

# Print results with associated companies for each duplicate
if duplicates.empty:
    print("No duplicates found based on Title and Date.")
else:
    print("Duplicate articles by Title, Date, and Company:")
    for _, row in duplicates.iterrows():
        # Filter the original DataFrame to get companies for this Title and Date
        title, date = row['Title'], row['Date']
        companies = df[(df['Title'] == title) & (df['Date'] == date)]['Company'].tolist()
        
        # Print Title, Date, Count, and associated companies
        print(f"Title: {title}, Date: {date.strftime('%d/%m/%Y %H:%M:%S')}, Count: {row['Count']}, Companies: {', '.join(companies)}")


print()
print()
print(len(df))
print(len(duplicates))