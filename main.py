import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


categories = ['Food', 'Travel', 'Fashion', 'Fitness',
              'Music', 'Culture', 'Family', 'Health']


data = {'Date': pd.date_range('2021-01-01', periods=500),
        'Category': [random.choice(categories) for _ in range(500)],
        'Likes': np.random.randint(0, 10000, size=500)}

df = pd.DataFrame(data)

print(df.head(5))

valcounts = df.Category.value_counts()

df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

df['Date'] = pd.to_datetime(df['Date'])

df = df.astype({"Likes": int})

sns.set_theme()
sns.boxplot(x=df['Category'], y=df['Likes'])
plt.show()

meanlist = df["Likes"].tolist()
print(f"Likes mean val: {sum(meanlist)/len(meanlist)}\n=========")

means = df.groupby("Category")["Likes"].mean()
for x in means:
    print(x)
