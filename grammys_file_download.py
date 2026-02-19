#import kaggle
#import kagglehub
import shutil
import pandas as pd
import kagglehub
print(pd.__version__)
# Download latest version
path = kagglehub.dataset_download("johnpendenque/grammy-winners-and-nominees-from-1965-to-2024")

print("Path to dataset files:", path)

#copy csv to file in local folder
shutil.copy(path + '/grammy_winners.csv', './grammy_winners.csv')



# Load the dataset
# df = pd.read_csv(path + '/grammys.csv')
# Display the first few rows of the dataset
# print(df.head())
