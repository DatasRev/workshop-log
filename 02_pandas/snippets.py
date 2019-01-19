import numpy as np
import pandas as pd

###
# IMPORT some data from a CSV formatted file
# download the source file: https://raw.githubusercontent.com/DatasRev/source-files/master/csv/movie.csv
###


df = pd.read_csv('movie.csv',delimiter=',',header=[0],nrows=500)


###
# DATAFRAME and SERIES
###

print(type(df))
print(df.info())
print(df.head())
print(type(df['movie_title']))
print(df['movie_title'].head())

movie_titles = df['movie_title']
my_list = list(movie_titles)
print("a simple python list(a long one):\n{}\n".format(my_list))

###
# INDEX and COLUMN
###

directored_df = df.set_index('director_name')
print("watch the index column on the left:\n{}\n".format(directored_df.head()))
titled_df = df.set_index('movie_title')
print("watch the index column on the left:\n{}\n".format(titled_df.head()))

###
# .loc and .iloc
###

print("first row with .loc method\n{}\n".format(df.loc[0]))
print("first row with .iloc method\n{}\n".format(df.iloc[0]))


print("C. Nolan row(s) with .loc method\n{}\n".format(directored_df.loc['Christopher Nolan']))
print("first row with .iloc method\n{}\n".format(directored_df.iloc[0]))


print("Avengers row(s) with .loc method\n{}\n".format(titled_df.loc['Avengers: Age of Ultron']))
print("first row with .iloc method\n{}\n".format(titled_df.iloc[0]))

###
# boolean indexing
###

bool_series = df['director_name'] == 'James Cameron'
filtered_df = df[bool_series]
print("movies directed by Cameron\n{}\n".format(filtered_df))

# you can index it in 1 step:
print("facebook likes greater than 1000\n{}\n".format(df[df['actor_1_facebook_likes'] > 1000.0]))

