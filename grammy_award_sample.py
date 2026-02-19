#print one sample of the data from each award category in 2024
import pandas as pd

# Load the dataset into dataframe
df = pd.read_csv('./grammy_winners.csv')
# Filter the dataset for only data from year 2024 and one sample from each award category
df_2024_sample = df[df['year'] == 2024].groupby('award').apply(lambda x: x.sample(1)).reset_index(drop=False)
# Print award category, artist and producers for each sample
for index, row in df_2024_sample.iterrows():
    print(f"Award: {row['award']}, Artist: {row['artist']}, Producers: {row['producers']}")
