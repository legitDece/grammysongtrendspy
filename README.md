# Grammy Song Trends 
Data Analysis of Grammy award nominated songs using python

Is it taking more people to write the best song? 

In this video https://www.youtube.com/watch?v=YXzB4v1Toj4 Rick Beato compares 1984 Grammy Songs of the year nominations to 2025. One thing that stands out is that the recent songs have an increasing number of songwriters (and in his opinion they are less memorable). 

So I was curious to know if this was an actual trend, that the Songs of the year according to the Grammy Award nominations are increasing in songwriters on each song, or if the difference was pronounced in the 2 years that Beato chose. Then depending on the results, what would this say about the music industry. 

## Getting the data
I found this dataset from Kaggle, thanks to John Pendenque for compiling the data from the Grammys - https://www.kaggle.com/datasets/johnpendenque/grammy-winners-and-nominees-from-1965-to-2024. There were a few different datasets available, but I chose this since it had more granular detail around the people contributing to each nomination. 

Imported the Kaggle library and downloaded the dataset, and added it into a dataframe. 

Then filtered the dataset to just the Song of the Year nominations.

Amending
This dataset was missing the most recent year's nominations, so I manually added the data from the Grammy's website

## Cleaning
Later on during the plotting I uncovered that were some numbers that werent adding up when I was double checking online. The biggest problem was songwriters changing the name they were credited between the years. I didn't try to fix this across the whole dataset, but consolidated some of the most occuring producers like "FINNEAS" and "Finneas O'Connel. 

Splitting out the Songwriters
I wanted to break up the string in the "producers" column so I work with them more easily and get counting. This involved disregarding everything at the end of the string that wasnt needed, and using the comma and & characters to split each person's name. 

Now its in a state to plot! 

## SotY Plot 1 

<img width="1000" height="600" alt="Figure_1 Songwriters by year" src="https://github.com/user-attachments/assets/d4d573d7-a33d-4c05-a1ca-8e0a5a2bdb17" />


Yes there is a general upwards trend, especially from the late 90s

Its a bit noisy though, maybe we can condense it further

## SotY Plot 2

<img width="1000" height="600" alt="Figure_3 By decade" src="https://github.com/user-attachments/assets/986f9108-16ed-4569-82a5-4d7cd44759e7" />

Lets get the average over a decade to see it a bit clearer and see if its the same trend for all nominations and the winner. Yes we can see the upward trend from the 90s. However the winners don't seem to follow the trend, and the most recent ones have had much less than the average

So are winners different much to the rest of the nominations?

## SotY Plot 3 

<img width="1000" height="603" alt="Figure_2 winners vs noms" src="https://github.com/user-attachments/assets/5f3d04f7-dbd9-43a9-ac22-a04213f34bf0" />

Spread of number of writers different between the winner and rest of the nominations? Yes! It still seems more likely to take the award if you have the lower amount of writers

Now that I've worked out a good way to parse the producers, what can we find out about each unique one. Lets count all the nominations each has

## SotY Plot 4

<img width="1000" height="564" alt="Figure_4 top writers by nominations" src="https://github.com/user-attachments/assets/e3520198-4402-458a-8ea7-75ed15cea4d6" />


Top Songwriters by number of appearances. All but two here have been in the last 25 years. So its hard to get in the top songs of the year multiple times, and for the recent period there have been some dominant forces that have stuck around longer than usual. 

Its hard to get nominated more than once, but even harder to get more than one win. 

## SotY Plot 5

<img width="800" height="508" alt="Figure_5 Pie wins" src="https://github.com/user-attachments/assets/6b81d0ae-26c3-4f30-b2c7-a713794d3efd" />

Percentage won 2 or 3 times
Only 2 people (Billie and Finneas) have won a record 3 times, and less than 1 in every 10 of the songwriters have contributed to more than 1 winning song. 

With these multiple appearances, and dominating forces in recent times, it makes me curious to see who has had the longest time between first and last time, who has appeared in popular songs across generations of music 

## SotY Plot 6

<img width="966" height="464" alt="Figure_6 Longest reign" src="https://github.com/user-attachments/assets/95942a74-5bab-4347-9d53-34b46f84913c" />

Timelines
Seemed to be longest reigning artists between 60s to 80s and then since the year 2000, with a gap in the 90s. Some recognisable names there and some I havent seen

Does this trend follow into other song categories?

How about in a different category, same trend

## RnB and rock

<img width="1000" height="551" alt="Figure_1 rnb and rock songs" src="https://github.com/user-attachments/assets/56ca6800-e691-41e6-93c9-d44bf22ccfec" />

Rhythm and Blues seems to follow the same trend
Rock doesnt on the other hand, this could be due to rock regularly having bands rather than singular artists. 

Then how about record of the year - the other major song category. 
Rather than just looking at the songwriting of the song, this category acknowledges the whole production of the song, and over time has been adding mixers, audio engineers and mastering engineers to the list of contributors

This needed some heavier string parsing to split out the different areas and then get counts on each. 

## Record of the year Plot 1 

<img width="1000" height="518" alt="Figure_1 RotY teams" src="https://github.com/user-attachments/assets/cb0c0935-28cd-4c00-9942-75496c842d35" />

See the average number of contributors change over the years. Whilst the total has grown, I wouldn't be confident saying this means the production team has been growing, since previously those team members were not included. 

## Record of the year Plot 2

<img width="1008" height="422" alt="Figure_1 RotY Pie" src="https://github.com/user-attachments/assets/e1c2d5ed-0a3e-4b72-b1d3-37fc47f53245" />

Since the last addition of mastering engineer, lets look at the average break up of the team. It appears that it weighs more heavily on the engineering side of total names. 





## Wrap up

In conclusion, Grammy Award Song of the Year nominations are involving an increasing number of producers. Are these popular songs bigger than ever before because of it? Will we see this trend continue? In an industry where its now easier than ever to make music, but likely more difficult to rise above the noise - it's hard to predict. 

