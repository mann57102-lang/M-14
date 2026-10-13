# movie-ratings-analyser.py
# Activity: Movie Ratings Analyser
# Lesson: Introduction to Pandas

import pandas as pd

# PART 1 - Create a Pandas Series of movie ratings
print('--- PART 1: Pandas Series ---')

ratings = [9.2, 8.8, 8.5, 8.1, 7.9]

movies = pd.Series(
    ratings,
    index=['Inception', 'Interstellar', 'Avatar', 'Titanic', 'Joker']
)

print(movies)

# PART 2 - Create a DataFrame of movie details
print()
print('--- PART 2: Pandas DataFrame ---')

data = {
    'Movie': ['Inception', 'Interstellar', 'Avatar', 'Titanic', 'Joker'],
    'Year': [2010, 2014, 2009, 1997, 2019],
    'Rating': [9.2, 8.8, 8.5, 8.1, 7.9],
    'Votes': [2500, 2200, 2000, 1800, 1600]
}

df = pd.DataFrame(data)
print(df)

# PART 3 - Access rows using .loc
print()
print('--- PART 3: Accessing Rows ---')

print('Row 0 (first movie):')
print(df.loc[0])

print()
print('Rows 2 and 3:')
print(df.loc[2:3])

# PART 4 - Load movies.csv and view the data
print()
print('--- PART 4: Reading a CSV File ---')

full_df = pd.read_csv('movies.csv')

print('First 5 rows (head):')
print(full_df.head())

print()
print('Last 3 rows (tail):')
print(full_df.tail(3))

print()
print('Dataset info:')
print(full_df.info())

# PART 5 - Clean the data
print()
print('--- PART 5: Cleaning Data ---')

print('Rows with missing values removed (dropna):')
clean_df = full_df.dropna()
print(clean_df.to_string())

print()
print('Missing values filled with 0 (fillna):')
filled_df = full_df.fillna(0)
print(filled_df.to_string())
