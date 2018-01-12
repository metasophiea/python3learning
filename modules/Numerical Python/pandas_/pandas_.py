import pandas, numpy
# Pandas is a software library written for the Python built ontop of Numpy. Scipy and 
# Matplotlib are considered "optional dependencies" It is used for data manipulation 
# and analysis and provides special data structures and operations for the manipulation
# of numerical tables and time series

# Series
# a one-dimensional labelled array-like object
s = pandas.Series([11, 28, 72, 3, 5, 8])
print(s)
print(s.index)
print(s.values)
print()

# series objects come into their own when one defines an object with arbitrary indices
fruits = ['apples', 'oranges', 'cherries', 'pears']
quantities = [20, 33, 52, 10]
s = pandas.Series(quantities, index=fruits)
print(s)
print('apples:',s['apples'])
print('fruits:',s[['apples', 'oranges', 'cherries']])
print( s[s>30] ) # boolean filtration
print( 'apples' in s ) # index detection
print()

fruits = ['apples', 'oranges', 'cherries', 'pears']
s1 = pandas.Series([20, 33, 52, 10], index=fruits)
s2 = pandas.Series([17, 13, 31, 32], index=fruits)
print(s1 + s2)
print("sum of S: ", sum(s1))
print()

fruits1 = ['peaches', 'oranges', 'cherries', 'pears']
fruits2 = ['raspberries', 'oranges', 'cherries', 'pears']
s1 = pandas.Series([20, 33, 52, 10], index=fruits1)
s2 = pandas.Series([17, 13, 31, 32], index=fruits2)
print(s1 + s2)
print("sum of S: ", sum(s1))
print()

# one can also define a series with a dictionary
cities = {"London":   8615246, 
          "Berlin":   3562166, 
          "Madrid":   3165235, 
          "Rome":     2874038, 
          "Paris":    2273305, 
          "Vienna":   1805681, 
          "Bucharest":1803425, 
          "Hamburg":  1760433,
          "Budapest": 1754000,
          "Warsaw":   1740119,
          "Barcelona":1602386,
          "Munich":   1493900,
          "Milan":    1350680}
print( pandas.Series(cities) )


# scaler operations
fruits = ['apples', 'oranges', 'cherries', 'pears']
s = pandas.Series([20, 33, 52, 10], index=fruits)
print( s+3 )
print( s*3 )
print( numpy.sin(s) )
print()


# Apply
#   this method will apply a function accross all the elements in a series
#   Series.apply(func, convert_dtype=True, args=(), **kwds)
#   func 	        a function, which can be a NumPy function that will be applied to the 
#                   entire Series or a Python function that will be applied to every single 
#                   value of the series
#   convert_dtype 	A boolean value. If it is set to True (default), apply will try to find 
#                   better dtype for elementwise function results. If False, leave as dtype=object
#   args 	        Positional arguments which will be passed to the function "func" 
#                   additionally to the values from the series.
#   **kwds 	        Additional keyword arguments will be passed as keywords to the function
fruits = ['apples', 'oranges', 'cherries', 'pears']
s = pandas.Series([20, 33, 52, 10], index=fruits)
print( s.apply(numpy.sin) )
print()

# even lambdas can be used
print( s.apply(lambda x: x if x > 50 else x+10 ) )
print()


# isnull and notnull
#   series' can have missing values, denoted by the entry 'NaN'
#   the methods above can be used to find these values. Setting
#   the entry to 'None' is considered a missing value
cities = {"London":   8615246, 
          "Berlin":   3562166, 
          "Madrid":   3165235, 
          "Rome":     2874038, 
          "Paris":    2273305, 
          "Vienna":   1805681, 
          "Bucharest":1803425, 
          "Hamburg":  1760433,
          "Budapest": 1754000,
          "Warsaw":   1740119,
          "Barcelona":1602386,
          "Munich":   1493900,
          "Milan":    1350680}
importantCities = ["London", "Paris", "Zurich", "Berlin", "Stuttgart", "Hamburg"]
importantCityPops = pandas.Series(cities, index=importantCities)
importantCityPops['Hamburg'] = None
print( importantCityPops.isnull() )
print( importantCityPops.notnull() )
print()


# dropna and fillna
#   the method dropna will return a series where the missing data has been removed,
#   while the method fillna is used to fill in missing data. fillna can also use
#   indexing
s = pandas.Series([11, 28, 72, None, 5, 8])
print( s.dropna() )
s = pandas.Series([11, 28, 72, None, 5, 8])
print( s.fillna(100) )
s = pandas.Series([11, 28, 72, None, 5, 8])
missingData = {3:200};
print( s.fillna(missingData) )
print()
















# DataFrame
#   this is basically a spreadsheet or database
ordinals = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eigth", "ninth", "tenth", "eleventh", "twelvth", "thirteenth"]
cities = {
    "name": 
        ["London", "Berlin", "Madrid", "Rome", "Paris", "Vienna", "Bucharest", "Hamburg", "Budapest", "Warsaw", "Barcelona", "Munich", "Milan"],
    "population": 
        [8615246, 3562166, 3165235, 2874038, 22273305, 31805681, 1803425, 1760433, 1754000, 1740119, 1602386, 1493900,1350680],
    "country": 
        ["England", "Germany", "Spain", "Italy", "France", "Austria", "Romania", "Germany", "Hungary", "Poland", "Spain","Germany", "Italy"]
}
city_frame = pandas.DataFrame(
    cities,                                     # the actual data
    columns=["name", "country", "population"],  # setting the order of the columns
    index=ordinals                              # defining the index
)
print(city_frame)

# we can go a little further; using one of the data's columns as the index
city_frame = pandas.DataFrame(
    cities,
    columns=["name", "population"],
    index=cities["country"]
)
print(city_frame)
# one can also set the index column to use afterwards
# (the boolean argument 'inplace' can be used to change the data, instead of returning a new set with the changes)
print( city_frame.set_index("name") )
print()
# you can also dynamically add a column of data
city_frame['populationBy2'] = city_frame['population']*2
city_frame['data'] = 2
print(city_frame)
print()

# accessing columns is a cinch, with two methods of doing so
print(city_frame['population'])
print(city_frame.population)
# importantly; these are views into the data, not a copy of it
print()

# row access can be done like so
print( city_frame.ix['France'] )

# filling in some data
some_areas = pandas.Series([1572, 755, 181.8],  index=['England', 'Germany', 'Italy'])
city_frame['area'] = some_areas
print(city_frame)
print()

# transposing data (a 45 degree flip)
print( city_frame.T )
print()

# generating a dataframe of random data
names = ['Frank', 'Eve', 'Stella', 'Guido', 'Lara']
index = ["January", "February", "March",
         "April", "May", "June",
         "July", "August", "September",
         "October", "November", "December"]
print( pandas.DataFrame(numpy.random.randn(12, 5)*1000, columns=names, index=index) )
print()



# Summation
#   as one might expect; this method sums all the entries in a column
#   (strings are just concattinated)
city_frame = pandas.DataFrame(
    cities,
    columns=["name", "country", "population"],
    index=ordinals
)
print( city_frame.sum() )
print()
#one can also sum an individual column
print( city_frame["population"].sum() )

# once you finish giggling; cumulative-sum or cumsum can be used to return
# entries where each entry is the sum of itself and all the entries that
# went before it (in it's column)
print( city_frame.cumsum() )
print()



# Sorting
print( city_frame.sort_values(by="population", ascending=False) )
print()



# importing CSV data (comma separated values)
data = pandas.read_csv( "data.csv" )
print(data)






