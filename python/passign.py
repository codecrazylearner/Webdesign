import pandas as pd
import numpy as np
import regex as re

# creating Series from scalar

# IF DATA IS SCALAR VALUE , AN INDEX MUST BE PROVIDED
# AND THE VALUE IS REPEATED TO THE LENGTH OF THE Series

s = pd.Series(5, index = [ 0, 1, 2, 3 ])
print("Series from a scalar value :\n", s)

#  creating pd.Series using lists
object_series = pd.Series([10, 40, 35, 60 ])
print("Series from a list: \n", object_series)

# values of the pd.Series
print("the values of object_Series; \n", object_series.values)

# index range, start and stop with step
print("the index of object _pd.Series: \n", object_series.index)

# creating pd.Series using numpy array
data_array = np.array([ 'i', 'u', 'e', 'a', 'o' ])
Series1 = pd.Series(data_array)
print("Series from a numpy array :\n", Series1)

Series2 = pd.Series(data_array, index = [ 100, 101, 102, 103, 104 ])
print("the changed index number in Series2: \n", Series2)

"""
THIS LINE OF CODE GIVES AN ERROR
Series3=pd.Series(DATA_ARRAY,INDEX=['INDEX1','INDEX2','INDEX3','INDEX4'])
"""

# When i assigned the values passed as 3 and index as 4
# there was an error implied.So we need to pass the same
# values as the index.

Series3 = pd.Series(data_array, index = [ 'index1', 'index2', 'index3', 'index4', 'index5' ])
print("the changed index string :\n", Series3)

# creating Series from a python dictionary

ex_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
series_dict = pd.Series(ex_dict)
print("Series out of a dictionary:  \n", series_dict)

# Series from python dict where index order is persisted
# and missing element is filled with NaN

data = {'a': 0., 'b': 1., 'c': 2.}
s = pd.Series(data, index = [ 'b', 'c', 'd', 'a' ])
print("Series with missing element in dicitonary :\n", s)

# ACCESSING DATA WITHIN THE Series

# RETRIEVE ONE ELELMENT
s = pd.Series([ 1, 2, 3, 4, 5 ], index = [ 'a', 'b', 'c', 'd', 'e' ])
print("The third element of the Series : \n", s[ 2 ])

# ACCESSING POSITION IN pd.Series TO RETREIVE DATA
s = pd.Series([ 1, 2, 3, 4, 5 ], index = [ 'a', 'b', 'c', 'd', 'e' ])
print("Using slicing method to get more than one element: \n",
      s[ :3 ])

# RETREIVING DATA USING INDEX LABEL VALUE
s = pd.Series([ 1, 2, 3, 4, 5 ], index = [ 'a', 'b', 'c', 'd', 'e' ])
print("The value of the index label :\n", s[ 'a' ])

# RETREIVE DATA WHERE LABEL IS NOT PRESENT
s = pd.Series([ 1, 2, 3, 4, 5 ], index = [ 'a', 'b', 'c', 'd', 'e' ])
print("Label value is :\n", s['f'])

# use of boolean conditions in a Series

media_use = pd.Series([ 20, 80, 40, 35 ], index = [ 'instagram', 'snapchat', 'twitter', 'whatspp' ])

print("media use of instagram:\n", media_use[ 'instagram' ])
print("if media_use has more than 35 :\n", media_use[ media_use >= 35 ])

# check if facebook is in media_use
print('facebook' in media_use)

# print instgram in media_use
media_use_dict = media_use_dict.to_dict()
print("media_use_dict :\n", media_use_dict)

# nan values
index_2 = [ 'instagram', 'snapchat', 'twitter', 'whatspp', 'facebook' ]
media_use2 = pd.Series(media_use, index_2)
print("The null values present in media_use2 :\n", media_use2)

# check if it contains null values
print("Null values in media_use2:\n", pd.isnull(media_use2))
print("check for not null values: \n", pd.notnull(media_use2))

# addition of pd.Series (+)

print("Addition of both pd.Series:\n", media_use + media_use2)

# assigning names
media_use2.name = "Company media_uses"
media_use2.index.name = "Comapany Name"
print("Assigned names are :\n", media_use2)

# WAYS OF INDEXING AND SELECTING DATA IN pd.Series


# making data frame
df = pd.read_csv("nba.csv")
ser = pd.Series(df[ 'Name' ])
data = ser.head(10)

# INDEXING pd.Series USING INDEXING OPERATOR
data[ 3:6 ]

# INDEXING A pd.Series USING .iloc[]
data.iloc[ 3:6 ]

Series1 = pd.Series([ 10, 20, 30, 40 ], index = [ 'a', 'b', 'c', 'd' ])
print("Series1 values:\n", Series1)

index1 = Series1.index
print("The index of the Series is :\n", index1)
# print all the elements from the 3rd element
print("The Series from the third element: \n", index1[ 2: ])

# negative indexes
print("The elements from last twoindex :\n", index1[ -2: ])
print("All the elements of the Series until lst two:\n", index1[ :-2 ])
print("Elements at position 3 and 4:\n", index1[ 2:4 ])

# interesting
index1[ 0 ] = 'e'
print("Element at the first posion:\n  ", index1)

# BINARY METHODS ON pd.Series


# creating a pd.Series
data = pd.Series([ 5, 2, 3, 7 ], index = [ 'a', 'b', 'c', 'd' ])

# creating a pd.Series
data1 = pd.Series([ 1, 6, 4, 9 ], index = [ 'a', 'b', 'd', 'e' ])
print(data, "\n\n", data1)

# adding two Series using .add
data.add(data1, fill_value = 0)

# subtracting two Series using .sub
data.sub(data1, fill_value = 0)

# multiplication of two Series
data.mul(data1, fill_value = 0)

# PANDA Series METHOD
Series1 = pd.Series([ 70, 5, 0, 225, 1, 16, np.nan, 10, np.nan ])

# creating pd.Series 2
Series2 = pd.Series([ 27, np.nan, 2, 23, 1, 95, 53, 10, 5 ])

# combining and returning results to variable

# calling on pd.Series1
result1 = Series1.combine_first(Series2)
# calling on pd.Series2
result2 = Series2.combine_first(Series1)
print('Result 1:\n', result1, '\n\nResult 2:\n', result2)

# CONVERSION OPERATIONS ON pd.Series
data = pd.read_csv("nba.csv")

# dropping null value columns to avoid errors
data.dropna(inplace = True)

# storing dtype before converting
before = data.dtypes

# converting dtypes using astype
data[ "Salary" ] = data[ "Salary" ].astype(int)
data[ "Number" ] = data[ "Number" ].astype(str)

# storing dtype after converting
after = data.dtypes

# printing to compare
print("BEFORE CONVERSION\n", before, "\n")
print("AFTER CONVERSION\n", after, "\n")

# CONVERTING Series INTO LISTS
# making data frame
data = pd.read_csv("nba.csv")

# removing null values to avoid errors
data.dropna(inplace = True)

# storing dtype before operation
dtype_before = type(data[ "Salary" ])

# converting to list
salary_list = data[ "Salary" ].tolist()

# storing dtype after operation
dtype_after = type(salary_list)

# printing dtype
print("Data type before converting = {}\nData type after converting = {}"
      .format(dtype_before, dtype_after))

# METHOD ONLY WORKS ON Series
# making data frame from csv file
data = pd.read_csv("employees.csv")

# storing unique value in a variable
arr = data[ "Team" ].unique()

# printing array
print("The unique value in a dataframe:", arr)

# from video

#  DATAFRAMES

#  - Revenue of companies

revenue_df = pd.read_clipboard()
print("dataframe created from reading a clipboard:\n", revenue_df)

# index  and columns
print("the columns of dataframes:\n", revenue_df.columns)
print("the index of the dataframe:\n", revenue_df[ 'Rank ' ])

# multiple columns
print("Multiple columns of DataFrame:\n",
      pd.DataFrame(revenue_df, columns = [ 'Rank', 'Name', 'Industry' ]))

# Nan Values
revenue_df2 = pd.DataFrame(revenue_df, columns = [ 'Rank', 'Name', 'Industry', 'Profit' ])
print("Not a null value: \n", revenue_df2)

# head and tail
print("The first two rows of DataFrame:\n", revenue_df.head(2))
print("The last two rows of the DataFrame:\n", revenue_df.tail(2))

# access rows in df
print("Access rows with .ix function:\n", revenue_df.ix[ 0 ])  # row 1
print("Access rows with .ix function:\n", revenue_df.ix[ 5 ])  # row 6

# assign numpy values to df
array1 = np.array([ 1, 2, 3, 4, 5, 6 ])
revenue_df2[ 'Profit' ] = array1
print("The Profit column: \n", revenue_df2)

# Series
profits = pd.Series([ 900, 1000 ], index = [ 3, 5 ])
revenue_df2[ 'Profit' ] = profits
print("Profit column of the Series:\n", revenue_df2)

# deletion
del (revenue_df2[ 'Profit' ])
print("Dataframe after profit column is deleted:\n", revenue_df2)

# convert a dictionary function to dataframe
sample = {
    'company': [ 'A', 'B' ],
    'Profit': [ 1000, 5000 ]
}
print("Dictionary contents:\n", sample)
sample_df = pd.DataFrame(sample)
print("DataFrame from a dicitonary:\n", sample_df)

# end of the video
# CREATE DATAFRAME FROM LISTS

# DataFrame from a single list
data = [ 1, 2, 3, 4, 5 ]
df = pd.DataFrame(data)
print("Dataframe from a single list:\n", df)

# DataFrame from a list of lists

data = [ [ 'Alex', 10 ], [ 'Bob', 12 ], [ 'Clarke', 13 ] ]
df = pd.DataFrame(data, columns = [ 'Name', 'Age' ], dtype = float)
print("DataFrame from a list of lists:\n", df)

# DataFrame from Dict of ndarrays

# All the ndarrays must be of same length. If index is passed,
# then the length of the index should equal to the length of the arrays.
# If no index is passed, then by default, index will be range(n),
# where n is the array length.
data = {'Name': [ 'Tom', 'Jack', 'Steve', 'Ricky' ], 'Age': [ 28, 34, 29, 42 ]}
df = pd.DataFrame(data)
print("DataFrame from dict of ndarrays:\n", df)

# DataFrame indexed using arrays
data = {'Name': [ 'Tom', 'Jack', 'Steve', 'Ricky' ], 'Age': [ 28, 34, 29, 42 ]}
df = pd.DataFrame(data, index = [ 'rank1', 'rank2', 'rank3', 'rank4' ])
print("Indexed Dataframe susing ndarrays:\n", df)

# DataFrame from list of Dicts
data = [ {'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20} ]
df = pd.DataFrame(data)
print("DataFrame from passing a list of dictionaries:\n", df)

# DataFrame passing dictionaries and row indicies
data = [ {'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20} ]
df = pd.DataFrame(data, index = [ 'first', 'second' ])
print("DataFrame from passing a list of dictionaries and row indices:\n", df)

# DataFrame with a list of dictionaries ,row and columnd indices

data = [ {'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20} ]
# With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index = [ 'first', 'second' ], columns = [ 'a', 'b' ])
# With two column indices with one index with other name
df2 = pd.DataFrame(data, index = [ 'first', 'second' ], columns = [ 'a', 'b1' ])
print("DataFrame with 2 cols with same keys having values:\n", df1)
print("DataFrame with 2 col indices: \n", df2)

# CREATE A DATAFRAME FROM DICT OF Series

# Dictionary of Series can be passed to form a DataFrame.
# The resultant index is the union of all the Series indexes passed.

d = {'one': pd.Series([ 1, 2, 3 ], index = [ 'a', 'b', 'c' ]),
     'two': pd.Series([ 1, 2, 3, 4 ], index = [ 'a', 'b', 'c', 'd' ])}
df = pd.DataFrame(d)
print("Dataframe of dictionary of Series:\n", df)

# column selection from the Dataframe
d = {'one': pd.Series([ 1, 2, 3 ], index = [ 'a', 'b', 'c' ]),
     'two': pd.Series([ 1, 2, 3, 4 ], index = [ 'a', 'b', 'c', 'd' ])}
df = pd.DataFrame(d)
print("Column Selection from the dataframe:\n", df[ 'one' ])

# Column Addition to an existing data frame
# Adding a new column to an existing DataFrame object
# with column label by passing new Series
print("Adding a new column by passing as Series:")
df[ 'three' ] = pd.Series([ 10, 20, 30 ], index = [ 'a', 'b', 'c' ])
print("The new dataframe with added column by passing Series:\n", df)
print("Adding a new column using the existing columns in DataFrame:")
df[ 'four' ] = df[ 'one' ] + df[ 'three' ]
print(df)

# Column Deletion using del and pop function

# Using the previous DataFrame, we will delete a column
# using del function


d = {'one': pd.pd.Series([ 1, 2, 3 ], index = [ 'a', 'b', 'c' ]),
     'two': pd.pd.Series([ 1, 2, 3, 4 ], index = [ 'a', 'b', 'c', 'd' ]),
     'three': pd.pd.Series([ 10, 20, 30 ], index = [ 'a', 'b', 'c' ])}
df = pd.DataFrame(d)
print("Our dataframe is: \n", df)

# using del function
del df[ 'one' ]
print("Deleting the first column using DEL function:", df)

# using pop function
df.pop('two')
print("Deleting another column using POP function:\n", df)

# ROW SELECTION, ADDITION, AND DELETION

# SELECTION BY LABEL
d = {'one': pd.Series([ 1, 2, 3 ], index = [ 'a', 'b', 'c' ]),
     'two': pd.Series([ 1, 2, 3, 4 ], index = [ 'a', 'b', 'c', 'd' ])}
df = pd.DataFrame(d)
print("selection of row by label:\n", df.loc[ 'b' ])

# The result is a Series with labels as column names of the DataFrame.
# And, the Name of the Series is the label with which it is retrieved.

# SELECTION BY INTEGER LOCATION
# Rows can be selected by passing integer location to an iloc function.

d = {'one': pd.Series([ 1, 2, 3 ], index = [ 'a', 'b', 'c' ]),
     'two': pd.Series([ 1, 2, 3, 4 ], index = [ 'a', 'b', 'c', 'd' ])}
df = pd.DataFrame(d)
print("Selection of rows by integer location:\n", df.iloc[ 2 ])

# SLICING MULTIPLE ROWS USING ',' OPERATOR

d = {'one': pd.Series([ 1, 2, 3 ], index = [ 'a', 'b', 'c' ]),
     'two': pd.Series([ 1, 2, 3, 4 ], index = [ 'a', 'b', 'c', 'd' ])}
df = pd.DataFrame(d)
print("Sliced rows of dataframe:\n", df[ 2:4 ])

# ADDITION OF ROWS USING APPEND FUNCTION
# This function will append the rows at the end.

df = pd.DataFrame([ [ 1, 2 ], [ 3, 4 ] ], columns = [ 'a', 'b' ])
df2 = pd.DataFrame([ [ 5, 6 ], [ 7, 8 ] ], columns = [ 'a', 'b' ])
df = df.append(df2)
print("The appended dataframe :\n", df)

# DELETION OF ROWS
# Use index label to delete or drop rows from a DataFrame.
# If label is duplicated, then multiple rows will be dropped.

df = pd.DataFrame([ [ 1, 2 ], [ 3, 4 ] ], columns = [ 'a', 'b' ])
df2 = pd.DataFrame([ [ 5, 6 ], [ 7, 8 ] ], columns = [ 'a', 'b' ])
df = df.append(df2)
# Drop rows with label 0
df = df.drop(0)
print("Drop the first row:\n", df)

# REINDEXING IN PANDAS DATAFRAME

Series1 = pd.Series([ 1, 2, 3, 4 ], index = [ 'e', 'f', 'g', 'h' ])
print("pd.Series1 :\n", Series1)

# creating new indexes using reindex
Series2 = pd.Series1.reindex([ 'e', 'f', 'g', 'h', 'i', 'j' ])
print("New indexes in pd.Series:\n", Series2)

# using fillvalue
Series2 = pd.Series2.reindex([ 'e', 'f', 'g', 'h', 'i', 'j', 'k' ], fill_value = 10)
print("Series using fill value:\n", Series2)

# using reindex methods => ffill
cars = pd.Series([ 'Audi', 'Merc', 'BMW' ], index = [ 0, 4, 8 ])
print("Series before ffill:\n", cars)
ranger = range(13)
print("Range of numbers: \n", ranger)
cars = cars.reindex(ranger, method = "ffill")  # forward fill
print("Reindex methods ffill in Series:\n", cars)

# create new dataframe using randn
df_1 = pd.DataFrame(randn(25).reshape(5, 5), index = [ 'a', 'b', 'c', 'd', 'e' ],
                    columns = [ 'c1', 'c2', 'c3', 'c4', 'c5' ])
print("DataFrame using randn function: \n", df_1)
df_2 = df_1.reindex([ 'a', 'b', 'c', 'd', 'e', 'f' ])
print("Dataframe after reindexing rows: \n", df_2)

# reindex rows of dataframe
# reindex columns of dataframe

df_3 = df_2.reindex(columns = [ 'c1', 'c2', 'c3', 'c4', 'c5', 'c6' ])
print("DataFrame after reindexing columns :\n", df_3)

# using .ix[] to reindex
df_4 = df_1.ix[ [ 'a', 'b', 'c', 'd', 'e', 'f' ], [ 'c1', 'c2', 'c3', 'c4', 'c5', 'c6' ] ]
print("using .ix[] to reindex : \n", df_4)

# REINDEXING THE COLUMNS USING AXIS KEYWORD

# One can reindex a single column or multiple columns by using reindex()
# method and by specifying the axis we want to reindex.
# Default values in the new index that are not present in the dataframe
# are assigned NaN.

column = [ 'a', 'b', 'c', 'd', 'e' ]
index = [ 'A', 'B', 'C', 'D', 'E' ]

# create a dataframe of random values of array
df1 = pd.DataFrame(np.random.rand(5, 5),
                   columns = column, index = index)
colum = [ 'e', 'a', 'b', 'c', 'd' ]
# create the new index for columns
print("New index for columns : \n", df1.reindex(colum, axis = 'columns'))

# REPLACING MISSING VALUES

# Missing values from the dataframe can be filled by passing a value
# to the keyword fill_value. This keyword replaces the NaN values.

column = [ 'a', 'b', 'c', 'd', 'e' ]
index = [ 'A', 'B', 'C', 'D', 'E' ]
# create a dataframe of random values of array
df1 = pd.DataFrame(np.random.rand(5, 5),
                   columns = column, index = index)
colum = [ 'a', 'b', 'c', 'g', 'h' ]

# create the new index for columns AND REPLCE THE MISSING VALUES
print(df1.reindex(colum, axis = 'columns', fill_value = 1.5))

# create the new index for columns AND REPLACE MISSING DATA WITH STRING
print(df1.reindex(colum, axis = 'columns', fill_value = 'data missing'))

# using dropna on pd.Series
cars = pd.Series([ 'BMW', 'Audi', 'Merc' ], index = [ 'a', 'b', 'c' ])
print("Series before dropping :\n", cars)
cars = cars.drop('a')
print("Series after dropping an index 'a':\n", cars)

# dataframes
cars_df = DataFrame(np.arange(9).reshape(3, 3), index = [ 'BMW', 'Audi', 'Merc' ],
                    columns = [ 'rev', 'pro', 'exp' ])
print("Cars dataframe :\n", cars_df)

# dropping along axis 0
cars_df = cars_df.drop('BMW', axis = 0)
print("Cars dataframe after dropping an row element :\n", cars_df)

# dropping along axis 1
cars_df = cars_df.drop('pro', axis = 1)
print("Cars DataFrame after dropping the column element :\n", cars_df)

# HANDLING NULL DATA

Series1 = pd.Series([ 'A', 'B', 'C', 'D', np.nan ])
# validate
print("Series is null:\n", Series1.isnull())
print("Series1 after dropping null values:\n", Series1.dropna())

df1 = pd.DataFrame([ [ 1, 2, 3 ], [ 5, 6, np.nan ], [ 7, np.nan, 10 ], [ np.nan, np.nan, np.nan ] ])
print("Dataframe with nan values:\n", df1)
# dropna when used in Dataframe drops rows by default,
# but the entire rows are deleted if there is one null value
print("Dataframe after dropping null values:\n", df1.dropna())

#  When how argument is used in dropna(),
# it drops a row or column only when the entire row or columns is null
print("Dataframe values dropped if the entire row or column has null values:\n",
      df1.dropna(how = 'all'))
#  When how argument is used in dropna(),
# it drops a row or column only when any value  is null
print("Dataframe values dropped if any value is null:\n",
      df1.dropna(how = 'any'))

# for column wise drop in dropna function
# should be explicitly specified as row is dropped by default
print("Dataframe after column wise drop performed:\n",
      df1.dropna(axis = 1))  # column wise drop6,

df2 = pd.DataFrame([ [ 1, 2, 3, np.nan ], [ 4, 5, 6, 7 ], [ 8, 9, np.nan, np.nan ], [ 12, np.nan, np.nan, np.nan ] ])
print("Dataframe that has null values :\n", df2)

# threshold argument tells minimum amount of na values to drop
print("Drop the rows if the data value present is less than 3 values:\n",
      df2.dropna(thresh = 3))
print("Drop the rows if the data value present is less than 2 values:\n",
      df2.dropna(thresh = 2))

# fillna
print("Replaces all null values by 0:\n", df2.fillna(0))
print("Passing the dicitonary where the values are specified for column value to be replaced:\n",
      df2.fillna({0: 0, 1: 50, 2: 100, 3: 200}))
