import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset into dataframe
df = pd.read_csv('./grammy_winners.csv')
# Filter the dataset for "Song Of The Year" award
song_of_year_df = df[df['award'] == 'Song Of The Year']

# Data for the 2025 (68th Annual) Grammy Awards: Song of the Year
data_2025 = {
    'annual_edition': [68] * 8,
    'year': [2025] * 8,
    'award': ['Song Of The Year'] * 8,
    'artist': [''] * 8,
    'artist_link': [''] * 8,
    'producers': [
        "Billie Eilish O'Connell & Finneas O'Connell, songwriters (Billie Eilish)",
        'Henry Walter, Lady Gaga & Andrew Watt, songwriters (Lady Gaga)',
        'Jaylah Hickmon, songwriter (Doechii)',
        'Amy Allen, Christopher Brody Brown, Rogét Chahayed, Henry Walter, Omer Fedi, Philip Lawrence, Bruno Mars, Chae Young Park & Theron Thomas, songwriters (ROSÉ, Bruno Mars)',
        'Benito Antonio Martínez Ocasio, Scott Dittrich, Benjamin Falik, Roberto José Rosado Torres, Marco Daniel Borrero, Hugo René Sención Sanabria & Tyler Thomas Spry, songwriters (Bad Bunny)',
        'EJAE, Park Hong Jun, Joong Gyu Kwak, Yu Han Lee, Hee Dong Nam, Jeong Hoon Seo, Mark Sonnenblick, songwriters (HUNTR/X: EJAE, Audrey Nuna, REI AMI)',
        'Jack Antonoff, Roshwita Larisha Bacha, Matthew Bernard, Ink, Scott Bridgeway, Sam Dew, Kendrick Lamar, Mark Anthony Spears, Solána Rowe & Kamasi Washington, songwriters (Kendrick Lamar With SZA)',
        'Amy Allen, Jack Antonoff & Sabrina Carpenter, songwriters (Sabrina Carpenter)'
    ],
    'song_or_album': [
        'WILDFLOWER', 
        'Abracadabra', 
        'Anxiety', 
        'APT.', 
        'DtMF', 
        'Golden', 
        'luther', 
        'Manchild'
    ],
    'winner': [True, False, False, False, False, False, False, False],
    'url': ['https://www.grammy.com/news/2026-grammys-nominations-full-winners-nominees-list'] * 8
}

df_2025_soty = pd.DataFrame(data_2025)

#amend the new data to the original dataframe
song_of_year_df = pd.concat([song_of_year_df, df_2025_soty], ignore_index=True)


#In the producers column string, remove anything after the word songwriter
song_of_year_df['producers'] = song_of_year_df['producers'].apply(lambda x: x.split('songwriter')[0].strip() if 'songwriter' in x else x)
#print the producers column for year 2025 to check if the string manipulation worked correctly
#print(song_of_year_df[song_of_year_df['year'] == 2025]['producers'])

#Clean up is needed on people that changed their names. Beyoncé is listed as "Beyoncé Knowles" in some rows and "Beyoncé" in others. Change all instances to "Beyoncé"
song_of_year_df['producers'] = song_of_year_df['producers'].str.replace(r'Beyoncé Knowles', 'Beyoncé', regex=True)
#Change all instances of "Kendrick Duckworth" to "Kendrick Lamar"
song_of_year_df['producers'] = song_of_year_df['producers'].str.replace(r'Kendrick Duckworth', 'Kendrick Lamar', regex=True)
# Change all instances of "Adele Adkins" to "Adele"
song_of_year_df['producers'] = song_of_year_df['producers'].str.replace(r'Adele Adkins', 'Adele', regex=True)
# Change all instances of "FINNEAS" to "Finneas O'Connell"
song_of_year_df['producers'] = song_of_year_df['producers'].str.replace(r'FINNEAS', "Finneas O'Connell", regex=True)



# Add a column to song_of_year_df to count the number of names in the producers column. Account for duplicate names , comma and ambersand
song_of_year_df['producer_count'] = song_of_year_df['producers'].apply(lambda x: len(set([p.strip() for p in x.replace('&', ',').split(',') if p.strip()])))




# Average number of producers for 2025 songs
average_producers_2025 = song_of_year_df[song_of_year_df['year'] == 2025]['producer_count'].mean()
print(f'Average number of producers for Song of the Year 2025: {average_producers_2025:.2f}')

# Average number of producers for 1958 songs
average_producers_1958 = song_of_year_df[song_of_year_df['year'] == 1958]['producer_count'].mean()
print(f'Average number of producers for Song of the Year 1958: {average_producers_1958:.2f}')




# New dataframe with only year and the average number of producers on the songs for that year
average_producers_by_year = song_of_year_df.groupby('year')['producer_count'].mean().reset_index()

#New dataframe with only year and the number of producers on the winning song for that year
winning_producers_by_year = song_of_year_df[song_of_year_df['winner'] == True][['year', 'producer_count']].reset_index(drop=True)

# Plot the average number of producers for Song of the Year by year in line chart
plt.figure(1, figsize=(10, 6))
plt.plot(average_producers_by_year['year'], average_producers_by_year['producer_count'], color='blue', label='Average Producers')
plt.xlabel('Year (1958-2025)')
plt.ylabel('Average Number of Songwriters')
plt.title('Number of Songwriters for Song of the Year nominations by Year')

#plt.show()



# Bar charts for number of producers for all nominated and winning
plt.figure(2, figsize=(10, 10))
producer_count_series = song_of_year_df['producer_count'].value_counts().sort_index()
winning_producer_count_series = song_of_year_df[song_of_year_df['winner'] == True]['producer_count'].value_counts().sort_index()
max_x_limit = max(producer_count_series.index.max(), winning_producer_count_series.index.max())

plt.subplot(2, 1, 1)
plt.bar(producer_count_series.index, producer_count_series.values)  
plt.title('Across all nominated songs')
plt.xlim(0, max_x_limit)

plt.subplot(2, 1, 2)
plt.bar(winning_producer_count_series.index, winning_producer_count_series.values, color='orange')
plt.xlabel('Number of Songwriters')   
plt.ylabel('Number of Songs')

plt.title('Across winning songs only')
plt.xlim(0, max_x_limit)
#add title for the whole figure
plt.suptitle('Distribution of Number of Songwriters for Song of the Year')

#Group years into decades
decades = [(1960, 1969), (1970, 1979), (1980, 1989), (1990, 1999), (2000, 2009), (2010, 2019)]


# Average number of producers for each decade
average_producers_by_decade = song_of_year_df.groupby((song_of_year_df['year'] // 10) * 10)['producer_count'].mean().reset_index()
average_producers_by_decade['decade'] = average_producers_by_decade['year'].apply(lambda x: f'{x}s')
# Average number of producers on winning songs for each decade
winning_producers_by_decade = song_of_year_df[song_of_year_df['winner'] == True].groupby((song_of_year_df['year'] // 10) * 10)['producer_count'].mean().reset_index()
winning_producers_by_decade['decade'] = winning_producers_by_decade['year'].apply(lambda x: f'{x}s')

# Plot the average number of producers for each decade in line chart, skip the decade of the 1950s since it only has one data point and would skew the chart
plt.figure(3, figsize=(10, 6))
plt.plot(average_producers_by_decade['decade'][average_producers_by_decade['decade'] != '1950s'], average_producers_by_decade['producer_count'][average_producers_by_decade['decade'] != '1950s'], color='green', marker='o', label='All Songs')
plt.plot(winning_producers_by_decade['decade'][winning_producers_by_decade['decade'] != '1950s'], winning_producers_by_decade['producer_count'][winning_producers_by_decade['decade'] != '1950s'], color='red', marker='s', label='Winning Songs')
plt.xlabel('Decade')    
plt.ylabel('Average Number of Songwriters')
plt.title('Average Number of Songwriters for SotY by Decade') 
plt.legend()


#plt.show()


# Make a new table with all the unique producer names and the number of times their name appears in the producers column for all songs
from collections import Counter
def extract_producer_names(producers_str):
    producers = set()
    for part in producers_str.replace('&', ',').split(','):
        name = part.strip()
        if name:
            producers.add(name)
    return producers

all_producers = set()
for producers_str in song_of_year_df['producers']:
    all_producers.update(extract_producer_names(producers_str))
producer_name_counts = Counter()
for producers_str in song_of_year_df['producers']:
    producer_name_counts.update(extract_producer_names(producers_str))
producer_counts_df = pd.DataFrame(producer_name_counts.items(), columns=['producer', 'count']).sort_values(by='count', ascending=False).reset_index(drop=True)
#print("Top 20 Producers by Number of Songs Produced:")
#print(producer_counts_df.head(30))

# Bar chart of top producers by number of songs produced
plt.figure(4, figsize=(10, 6))
top_producers = producer_counts_df.head(8)
plt.bar(top_producers['producer'], top_producers['count'], color='purple')
plt.xlabel('Songwriter')
plt.ylabel('Total Number of Songs Nominated')
plt.title('Top Songwriters by Number of SotY Nominations')
plt.xticks(rotation=45, ha='right')


# Make a new table with all the unique producer names and the number of times their name appears in the producers column for winning songs only
winning_producer_name_counts = Counter()
for producers_str in song_of_year_df[song_of_year_df['winner'] == True]['producers']:
    winning_producer_name_counts.update(extract_producer_names(producers_str))
winning_producer_counts_df = pd.DataFrame(winning_producer_name_counts.items(), columns=['producer', 'count']).sort_values(by='count', ascending=False).reset_index(drop=True)

#print("Top 20 Producers by Number of Winning Songs Produced:")
#print(winning_producer_counts_df.head(20))

# Percent of total producers on winning songs that have won more than one song of the year
total_winning_producers = len(winning_producer_counts_df)
multiple_winners = winning_producer_counts_df[winning_producer_counts_df['count'] > 1]
percent_multiple_winners = (len(multiple_winners) / total_winning_producers * 100) if total_winning_producers > 0 else 0

#print(f"Percentage of producers who have won more than one Song of the Year: {percent_multiple_winners:.2f}%")
#print(f"Total number of winning producers: {total_winning_producers}")

# Create pie chart of percentage of producers who have won one, two or three or more songs of the year 
winning_producer_counts_df['win_category'] = winning_producer_counts_df['count'].apply(lambda x: '1 Win' if x == 1 else ('2 Wins' if x == 2 else '3+ Wins'))
win_category_counts = winning_producer_counts_df['win_category'].value_counts().sort_index()

plt.figure(5, figsize=(8, 6))
plt.pie(win_category_counts.values, labels=win_category_counts.index, autopct='%1.1f%%', colors=['green', 'orange', 'blue'])


plt.title('Distribution of number of times songwriters have won SotY')
plt.tight_layout()
#plt.show()


# Find the producer that has the longest time span between their first appearance and most recent appearance in the producers column. Print the producer name and the time span in years
producer_years = {}
for index, row in song_of_year_df.iterrows():
    producers_str = row['producers']
    year = row['year']
    producers = extract_producer_names(producers_str)
    for producer in producers:
        if producer not in producer_years:
            producer_years[producer] = {'first_year': year, 'last_year': year}
        else:
            producer_years[producer]['first_year'] = min(producer_years[producer]['first_year'], year)
            producer_years[producer]['last_year'] = max(producer_years[producer]['last_year'], year)
producer_time_spans = {producer: years['last_year'] - years['first_year'] for producer, years in producer_years.items()}
longest_time_span_producer = max(producer_time_spans, key=producer_time_spans.get)
longest_time_span = producer_time_spans[longest_time_span_producer]
#print(f'Producer with the longest time span between first and most recent appearance: {longest_time_span_producer} with a time span of {longest_time_span} years')

# Create new dataframe with all producer names, the first year they appeared in the producers column, the last year they appeared in the producers column, and the time span between their first and last appearance
producer_time_span_df = pd.DataFrame({
    'producer': producer_years.keys(),
    'first_year': [years['first_year'] for years in producer_years.values()],
    'last_year': [years['last_year'] for years in producer_years.values()],
    'time_span': [producer_time_spans[producer] for producer in producer_years.keys()]
}).sort_values(by='time_span', ascending=False).reset_index(drop=True)
#print(producer_time_span_df.head(20))

# Plot line chart of the time span between first and last appearance for the top 20 producers with the longest time span with legend of name of the producer. Each line is a different producer, and the x axis is the date range from their first appearance to their last appearance, and the y axis is the producer name. The line should be horizontal since the y value is the same for each producer, but the x value should range from the first year to the last year of their appearance in the dataset.
plt.figure(6, figsize=(10, 6))
top_20_producers_time_span = producer_time_span_df.head(10)
for index, row in top_20_producers_time_span.iterrows():
    plt.plot([row['first_year'], row['last_year']], [index, index], marker='o', label=row['producer'] + f' ({row["time_span"]} years)')
    
plt.xlabel('Year')
plt.ylabel('Producer')
plt.title('Top 10 Songwriters by Longest Reign in nominations for SotY')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()


#Plot them all!
plt.show()