import numpy
import sklearn.linear_model
import pylab
import pandas
import seaborn
import matplotlib



# -- Beginning example
# http://devarea.com/machine-learning-with-python-introduction/#.WqoiL-aYNjU
# model = sklearn.linear_model.LinearRegression()
# ## straightforward input and output
# # x_val = numpy.array([1,2,3,4,5]).reshape(-1,1)
# # y_val = [1,2,3,4,5]
# ## more unusual (incorrect) input and output
# x_val = numpy.array([1,2,3,3,4,3,6,8,9,10]).reshape(-1,1)
# y_val = [1,2,3,4,5,6,7,7,9,10]

# model.fit(x_val,y_val)

# pylab.scatter(x_val,y_val)
# pylab.show()



# -- Further dimensional examples
# sample = numpy.array(
#     [
#         [1,2,300,14],
#         [9,3,1,95],
#         [5,7,11,58],
#         [4,8,14,57],
#         [2,1,2,27],
#         [9,9,7,100],
#         [12,3,21,126],
#         [29,12,3,309],
#         [2,40,11,90],
#         [21,32,4,270],
#         [7,13,8,79],
#         [17,2,19,172],
#         [13,24,13,159]
#     ]
# )
# dataframe = pandas.DataFrame(sample, columns=['in_1','in_2','in_3','out'])
# # print(dataframe)
# seaborn.pairplot(dataframe)
# # matplotlib.pyplot.show()


# #splitting the data into 'train' and 'test' sets
# x_val = dataframe[:8][['in_1','in_2','in_3']]
# y_val = dataframe[:8][['out']]
# print('--- training data ---\n', dataframe[:8][['in_1','in_2','in_3','out']])

# model = sklearn.linear_model.LinearRegression()
# model.fit(x_val,y_val)

# print('--- test data (with answers) ---\n', dataframe[8:][['in_1','in_2','in_3','out']])

# x_val = dataframe[8:][['in_1','in_2','in_3']]
# y_val = model.predict(x_val)
# dataframe['out'][8:] = y_val.reshape(1,-1)[0]

# print('--- test data (with predictions) ---\n', dataframe[8:][['in_1','in_2','in_3','out']])
# print()
# print( '--- generated input coefficients ---' )
# for a, item in enumerate(model.coef_[0]):
#     print( 'in_'+str(a+1)+':' , item)
# #notice how in_3's coefficient is very small; perhaps this is reason to remove it entirely from the inputs




# -- Bigger Dataset
# http://devarea.com/python-machine-learning-example-linear-regression/
# here, we're using a dataset that documents a number of restaurant transactions over the
# course of a few days. From this data, we task ourselves with determining what situation
# provides a server with the highest tip
 
dataframe = seaborn.load_dataset('tips')
print( dataframe.head() )     # provides the first few entires
# print( dataframe.info() )     # a description of the data columns
# print( dataframe.describe() ) # an overview of the dataset
# print( dataframe.sample(5) )  # provides a random sample

### First, some exploration of the data
#Tips as a percentage of the bill
print('-> sum per day')
dataframe2 = dataframe.groupby('day').sum()
print(dataframe2,'\n')
print('-> remove sum of size column as its not relevant')
dataframe2.drop('size',inplace=True,axis=1)
print(dataframe2,'\n')
print('-> add percent column')
dataframe2['percent'] = (dataframe2['tip']/dataframe2['total_bill'])*100
print(dataframe2,'\n')
#evidentally, Friday is the best day and Saturday is the worst for tips


#Grouping by smoker status
dataframe3 = dataframe.groupby('smoker').sum()
dataframe3['percent'] = (dataframe3['tip']/dataframe3['total_bill'])*100
print(dataframe3,'\n')
#clearly, non-smokers are better tippers


#Grouping the data by day and table size
dataframe4 = dataframe.groupby(['day','size']).sum()
dataframe4['percent'] = (dataframe4['tip']/dataframe4['total_bill'])*100
print(dataframe4,'\n')
#a quick look over things reveals that tables of 2 are the best business for this restaurant


## some visualization	
#a bar chart of how many people turned up each day
# seaborn.countplot(x='day' ,data=dataframe)

#how many tables of each kind were used each day
# seaborn.countplot(x='day',hue='size' ,data=dataframe)

#how many people were smokers or non-smokers each day
# seaborn.countplot(x='day',hue='smoker' ,data=dataframe)

# matplotlib.pyplot.show()
print()





### Now for the actual machine learning
## first, we must augment the data, to be all numerical

# replace the gender and smoker status with numbers
dataframe.replace(
    { 
        'sex': {'Male':0 , 'Female':1}, 
        'smoker' : {'No': 0 , 'Yes': 1}
    },
    inplace=True
)

# converting the day and time into a collection of boolean values
# thursday => 1 0 0 0
# friday   => 0 1 0 0 etc.
# we can take this a step further by dropping the first column,
# in this way, 'everything being zero' means thursday
# thursday => 0 0 0
# friday   => 1 0 0 etc.
days =  pandas.get_dummies(dataframe['day'], drop_first=True)
times = pandas.get_dummies(dataframe['time'], drop_first=True)
dataframe = pandas.concat([dataframe,days,times], axis=1)
#obviously, having these new values removes the need for the original columns
dataframe.drop(['day','time'] ,inplace=True, axis=1)
print(dataframe.sample(5), '\n')


## and now the machine
# gather together the input and output data
x = dataframe[['sex','smoker','size','Fri','Sat','Sun','Dinner']]
y = dataframe[['tip']]
# split these into training and test sets
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=1/4, random_state=26)

#create and train the model
model = sklearn.linear_model.LinearRegression()
model.fit(x_train, y_train)

# now for some testing
y_predicted = model.predict(x_test)

# results compared to the true answer
#   index trueAnswer predictedAnswer difference
for a, item in enumerate(y_test.tip):
    print(a, '\t', item, '\t', y_predicted[a][0], '\t', (item-y_predicted[a][0]))

# the same data from above, but visualised. Here, one can see the difference between the 
# true and predicted answers mapped out into bars, with a smoothening line ontop.
seaborn.distplot(y_test-y_predicted)
matplotlib.pyplot.show()
# from the data, we can see that the model has become quite accurate; to within +-2% at worst
# (which isn't that great, because tips seem to be around 3% anyway, but those are the edge 
# cases...right?)