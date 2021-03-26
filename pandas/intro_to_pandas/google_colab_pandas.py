from __future__ import print_function
import pandas as pd

print(pd.__version__)



# DataFrame objects can be created by passing a dict mapping string column names to their respective Series.
# If the Series don't match in length, missing values are filled with special NA/NaN values.
# Example:

pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

print(pd.DataFrame({ 'City name': city_names, 'Population': population }))

# But most of the time, you load an entire file into a DataFrame.
# The following example loads a file with California housing data.
# Run the following cell to load the data and create feature definitions:

california_housing_dataframe = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
print(california_housing_dataframe.describe())

# The example above used DataFrame.describe to show interesting statistics about a DataFrame.
# Another useful function is DataFrame.head, which displays the first few records of a DataFrame:

print(california_housing_dataframe.head())

#Another powerful feature of pandas is graphing
california_housing_dataframe.hist('housing_median_age')

cities = pd.DataFrame({ 'City name': city_names, 'Population': population })
print(type(cities['City name']))
cities['City name']

print(type(cities['City name'][1]))
cities['City name'][1]

print(type(cities[0:2]))
cities[0:2]

#Manipulating Data

print(population / 1000)

#NumPy is a popular toolkit for scientific computing
import numpy as np
print(np.log(population))

#The example below creates a new Series that indicates whether population is over one million:
print(population.apply(lambda val: val > 1000000))

#Modifying DataFrames is also straightforward. For example, the following code adds two Series to an existing DataFrame:
cities['Area square miles'] = pd.Series([46.87, 176.53, 97.92])
cities['Population density'] = cities['Population'] / cities['Area square miles']
print(cities)
