import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(''' Your dataset location''', lineterminator = '\n')
df.head()
def catigorize_col (df, col, labels):
    edges = [df[col].describe()['min'],
             df[col].describe()['25%'],
             df[col].describe()['50%'],
             df[col].describe()['75%'],
             df[col].describe()['max']]
    df[col] = pd.cut(df[col], edges, labels = labels, duplicates='drop')
    return df
labels = ['not_popular', 'below_avg', 'average', 'popular']
catigorize_col(df, 'Vote_Average', labels)
df['Vote_Average'].unique()

#Reason for doing this is that there are manu movies that are given 8+ score some with 7+ ans so on, and because of
#and because of that reading the data set gets a bit tough.

df['Genre'] = df['Genre'].str.split(', ')
df = df.explode('Genre').reset_index(drop=True)
df.head()

#Reason for doing this is that there are many movies that contains more than one type of genre and because of that
#this will make our dataset difficult to read, plus it this help help us to categorise the movies based on it's genre.

df['Release_Date'] = pd.to_datetime(df['Release_Date'])
print(df['Release_Date'].dtypes)
df['Release_Date'] = df['Release_Date'].dt.year
df['Release_Date'].dtypes
df.head()

#Analysis No.1
#types of movies that are getting produced

sns.catplot(y = 'Genre', data = df, kind = 'count', order = df['Genre'].value_counts().index, color = '#4287f5')
plt.title('Genre Distribution')
plt.show()

#Analysis No.2
#Risk % after releasing the movie

vote_counts = df['Vote_Average'].value_counts()

plt.figure(figsize=(7, 7))
plt.pie(vote_counts, labels=vote_counts.index, autopct='%1.1f%%',
        startangle=140, colors=plt.cm.Pastel1.colors)
plt.title('Risk %')
plt.axis('equal')  
plt.show()

#Analysis No.3
#Good movies are in which language

vote_counts = df['Original_Language'].value_counts()

plt.figure(figsize=(10, 6))
bars = plt.bar(vote_counts.index, vote_counts.values, color=plt.cm.Pastel1.colors[:len(vote_counts)])
plt.title('Vote Distribution')
plt.xlabel('Original Language')
plt.ylabel('Vote Count')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()

#Analysis No.4
#Genre loved most by the public

popular_df = df[df['Vote_Average'] == 'popular']
genre_counts = df['Genre'].value_counts()
plt.figure(figsize=(12, 6))
genre_counts.plot(kind='bar', color=plt.cm.Pastel1.colors[:len(genre_counts)])
plt.title('Genre Distribution for Popular Movies')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.show()

#Analysis No.5
#Movies released in 5 years

df['Release_Date'] = df['Release_Date'].astype(int)
last_5_years = df[df['Release_Date'].isin([2020, 2021, 2022, 2023, 2024])]
year_counts = last_5_years['Release_Date'].value_counts().sort_index()
plt.figure(figsize=(8, 5))
bars = plt.bar(year_counts.index.astype(str), year_counts.values, color='slateblue')
plt.title('Movies Released in the Last 5 Years (2020–2024)')
plt.xlabel('Year')
plt.ylabel('Number of Movies')
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.show()