import matplotlib.pyplot as plt
import pandas as pd
import re


# Load the dataset into dataframe
df = pd.read_csv('./grammy_winners.csv')
# Filter the dataset for "Record of the Year" category
best_record_df = df[df['award'] == 'Record Of The Year']

# Print the earliest date of the award
#earliest_date = best_record_df['year'].min()
#print(f"Earliest date of the award: {earliest_date}")
# Print any missing years in the dataset for the "Record of the Year" category
#missing_years = set(range(1959, 2025)) - set(best_record_df['year'])
#print(f"Missing years: {sorted(missing_years)}")




# Function to parse the producers column into three separate components
def parse_producers(producer_string):
    if pd.isna(producer_string):
        return '', '', ''
    
    # Split by semicolon first
    parts = [p.strip() for p in producer_string.split(';')]
    
    producers = ''
    engineers = ''
    mastering = ''
    
    for part in parts:
        if re.search(r',\s*producers?$', part, re.IGNORECASE):
            # Extract producers (everything before "producer" or "producers")
            match = re.search(r'^(.+?),\s*producers?$', part, re.IGNORECASE)
            if match:
                producers = match.group(1).strip()
        elif re.search(r',\s*engineers?/mixers?$', part, re.IGNORECASE):
            # Extract engineers/mixers (everything before "engineer" or "mixer")
            match = re.search(r'^(.+?),\s*engineers?/mixers?$', part, re.IGNORECASE)
            if match:
                engineers = match.group(1).strip()
        elif re.search(r',\s*mastering\s+engineers?$', part, re.IGNORECASE):
            # Extract mastering engineer (everything before "mastering engineer")
            match = re.search(r'^(.+?),\s*mastering\s+engineers?$', part, re.IGNORECASE)
            if match:
                mastering = match.group(1).strip()
    
    return producers, engineers, mastering

# Apply the function to create new columns
result = best_record_df['producers'].apply(parse_producers)
best_record_df['producers_names'] = result.apply(lambda x: x[0])
best_record_df['engineers_mixers'] = result.apply(lambda x: x[1])
best_record_df['mastering_engineer'] = result.apply(lambda x: x[2])

# Function to count the number of names in a string, accounting for duplicate names and comma and & as separators
def count_names(name_string):
    if pd.isna(name_string) or name_string.strip() == '':
        return 0
    names = set([n.strip() for n in re.split(r'[,&]', name_string) if n.strip()])
    return len(names)
# Add new column with count of producers for each song
best_record_df['producer_count'] = best_record_df['producers_names'].apply(count_names)
# Add new column with count of engineers/mixers for each song
best_record_df['engineer_mixer_count'] = best_record_df['engineers_mixers'].apply(count_names)
# Add new column with count of mastering engineers for each song
best_record_df['mastering_engineer_count'] = best_record_df['mastering_engineer'].apply(count_names)


# Create new dataframe with years and average producer count, and average engineers count. Add 1 to each producer count to account for the artist, check if their name is already listed in producers too. Average engineers count is made up of engineer_mixer_count and mastering_engineer_count
# First, create a new column with the total count of producers and artists, accounting for duplicates
best_record_df['total_producer_artist_count'] = best_record_df.apply(lambda row: row['producer_count'] + (1 if pd.notna(row['artist']) and str(row['artist']) not in row['producers_names'] else 0), axis=1)
# Then, create a new column with the total count of engineers/mixers and mastering engineers 
best_record_df['total_engineer_count'] = best_record_df['engineer_mixer_count'] + best_record_df['mastering_engineer_count']
# Create a new dataframe with years and average producer count, and average engineers count
avg_counts_df = best_record_df.groupby('year').apply(lambda x: pd.Series({
    'avg_producer_count': x['total_producer_artist_count'].mean(),
    'avg_engineer_count': x['total_engineer_count'].mean()
})).reset_index()

#print(avg_counts_df.tail(10))


# Plot average producer count and average engineer count across years in line chart, with year on x axis and average producer count and average engineer count on y axis
plt.figure(figsize=(10, 6))
plt.plot(avg_counts_df['year'], avg_counts_df['avg_producer_count'], label='Producer/Artist')
# When plotting the engineers, Do not start until 1998 since they werent credited until then
avg_counts_df_filtered = avg_counts_df[avg_counts_df['year'] >= 1998]
plt.plot(avg_counts_df_filtered['year'], avg_counts_df_filtered['avg_engineer_count'], label='Engineer/Mixer/Mastering')
# Add plot for total average contributors (producers/artists + engineers/mixers/mastering)
avg_counts_df['avg_total_contributors'] = avg_counts_df['avg_producer_count'] + avg_counts_df['avg_engineer_count']
plt.plot(avg_counts_df['year'], avg_counts_df['avg_total_contributors'], label='Total')

plt.xlabel('Year (1959-2024)')
plt.ylabel('Average Contributors on each song that year')
plt.title('Contributors credited for Record of the Year Award Over the Years')
plt.legend()
plt.show()

# Create pie chart of average percentage of producers/artists vs engineers/mixers/mastering for the years 2012 to 2024
avg_counts_recent_df = avg_counts_df[avg_counts_df['year'] >= 2012]
avg_producer_artist_percentage = avg_counts_recent_df['avg_producer_count'].mean() / avg_counts_recent_df['avg_total_contributors'].mean() * 100
avg_engineer_percentage = avg_counts_recent_df['avg_engineer_count'].mean() / avg_counts_recent_df['avg_total_contributors'].mean() * 100
plt.figure(figsize=(6, 6))  
plt.pie([avg_producer_artist_percentage, avg_engineer_percentage], labels=['Producer/Artist', 'Engineer/Mixer/Mastering'], autopct='%1.1f%%', startangle=140)
plt.title('Average Percentage of Producers/Artists vs Engineers/Mixers/Mastering for Record of the Year (2012-2024)')
plt.axis('equal')  
plt.show()
