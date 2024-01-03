# Task 1 – Import required libraries
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Task 2 – Generate random data for the social media data
## Make a list of category labels
categories = ['Food', 'Travel', 'Fashion', 'Fitness',
              'Music', 'Culture', 'Family', 'Health']

## Generate Twitter-syle data across a date range randomly choosing 
## category and likes
data = {'Date': pd.date_range('2021-01-01', periods=500),
        'Category': [random.choice(categories) for _ in range(500)],
        'Likes': np.random.randint(0, 10000, size=500)}

# Task 3 – Load the data into a Pandas DataFrame and Explore the data
## Import Twitter data into a pandas DataFrame and show the top 5 lines
df = pd.DataFrame(data)
print(df.head(5))

valcounts = df.Category.value_counts()

# Task 4 – Clean the data
## Remove all the null data and any duplicate entries
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

## Caste the 'Date' value into datetime format
df['Date'] = pd.to_datetime(df['Date'])

## Caste all 'Likes' values as integer
df = df.astype({"Likes": int})

## Set a visual theme, and display the data graphically
sns.set_theme()
sns.boxplot(x=df['Category'], y=df['Likes'])
plt.show()

## Find the mean value for the 'Likes' column
meanlist = df["Likes"].tolist()
print(f"Likes mean val: {sum(meanlist)/len(meanlist)}\n=========")

means = df.groupby("Category")["Likes"].mean()
for x in means:
    print(x)
