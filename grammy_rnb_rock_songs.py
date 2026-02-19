import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset into dataframe
df = pd.read_csv('./grammy_winners.csv')

# Filter the data for "Best R&B Song" and "Best Rhythm & Blues Song" and "R&B Song" award category only. Its the same award, the name changed over the years
best_rnb_song_df = df[df['award'].isin(['Best R&B Song', 'Best Rhythm & Blues Song', 'R&B Song'])]
# Filter the data for "Rock Song" and "Best Rock Song" award category only. Also the same award
best_rock_song_df = df[df['award'].isin(['Best Rock Song', 'Rock Song'])]

#earliest date of the award
earliest_date = [best_rnb_song_df['year'].min(), best_rock_song_df['year'].min()]
print(f"Earliest date of the awards: Best R&B Song: {earliest_date[0]}, Best Rock Song: {earliest_date[1]}")


# In producers column, remove anything in the string from "songwriter" to the end of the string
best_rnb_song_df['producers'] = best_rnb_song_df['producers'].apply(lambda x: x.split(', songwriter')[0].strip() if 'songwriter' in x else x)
best_rock_song_df['producers'] = best_rock_song_df['producers'].apply(lambda x: x.split(', songwriter')[0].strip() if 'songwriter' in x else x)


# print random 5 rows of the filtered data with columns "year", "artist", "song_or_album", and "producers"
print(best_rnb_song_df[['year', 'artist', 'song_or_album', 'producers']].sample(5))
print(best_rock_song_df[['year', 'artist', 'song_or_album', 'producers']].sample(5))

# Add new column to both with the count of producers for each song, accounting for duplicate names and comma and & as separators
best_rnb_song_df['producer_count'] = best_rnb_song_df['producers'].apply(lambda x: len(set([p.strip() for p in x.replace('&', ',').split(',') if p.strip()])))
best_rock_song_df['producer_count'] = best_rock_song_df['producers'].apply(lambda x: len(set([p.strip() for p in x.replace('&', ',').split(',') if p.strip()])))

#print sample of producers and producer count for each song
print(best_rnb_song_df[['song_or_album', 'producers', 'producer_count']].sample(5))
print(best_rock_song_df[['song_or_album', 'producers', 'producer_count']].sample(5))

# New dataframes with year and average producer count across songs in that year
avg_producer_count_df = best_rnb_song_df.groupby('year')['producer_count'].mean().reset_index() 
avg_producer_count_rock_df = best_rock_song_df.groupby('year')['producer_count'].mean().reset_index() 

# Plot average producer count across years in line chart, with year on x axis and average producer count on y axis
plt.figure(figsize=(10, 6))
plt.plot(avg_producer_count_df['year'], avg_producer_count_df['producer_count'], marker='o', label='R&B')
plt.plot(avg_producer_count_rock_df['year'], avg_producer_count_rock_df['producer_count'], marker='s', label='Rock')
plt.xlabel('Year (1968-2024)')
plt.ylabel('Average Number of Songwriters credited')
plt.title('Songwriters for R&B and Rock Song Awards Over the Years')  
plt.legend()
plt.show()

