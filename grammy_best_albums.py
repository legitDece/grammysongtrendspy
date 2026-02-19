import matplotlib.pyplot as plt
import pandas as pd
# Load the dataset into dataframe
df = pd.read_csv('./grammy_winners.csv')

# Filter the dataset for "Album of the Year" category
album_of_year_df = df[df['award'] == 'Album Of The Year']
#print(album_of_year_df.head(20))

# A list for the year of 2024, in album of the year of the producers and album name in new table
album_of_year_2024 = album_of_year_df[album_of_year_df['year'] == 2024][['producers', 'song_or_album']]

#count names in producers column and add count to new column, and check for duplicate names in producers column, if duplicate names exist, count them as one producer, and add count to new column
album_of_year_2024['producer_count'] = album_of_year_2024['producers'].apply(lambda x: len(set([p.strip() for p in x.replace('&', ',').split(',') if p.strip()])))
#print(album_of_year_2024)

#print(album_of_year_2024.head(2))

#plot number of producers to each album name in bar chart, with album name on x axis and number of producers on y axis
plt.figure(figsize=(10, 6))
plt.bar(album_of_year_2024['song_or_album'], album_of_year_2024['producer_count'])
plt.xlabel('Album Name')
plt.ylabel('Number of Producers')
plt.title('Number of Producers for Album of the Year 2024')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

