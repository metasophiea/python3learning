import numpy
from sklearn import datasets
from collections import Counter


# here we're loading a a data set all about flowers
iris = datasets.load_iris()
iris_data = iris.data
iris_labels = iris.target
# these are two lists. The first contains arrays of four pieces of data for each flower:
# sepals length, sepals width, petal length and sepals length
# the second list is connected to the first by index, where each element represents
# what type of flower it is: Iris setosa, Iris virginica or Iris versicolor

# print(iris_data[0], iris_data[50], iris_data[100])
# print(iris_labels[0], iris_labels[50], iris_labels[100])
# print()

numpy.random.seed(42)
indices = numpy.random.permutation(len(iris_data)) # this produces a list of random numbers of the length provided

# here, we are taking a number of the items from the samples set and setting them aside into a 'test set'
# the rest are placed into a 'training set'
n_training_samples = 12
learnset_data = iris_data[indices[:-n_training_samples]]
learnset_labels = iris_labels[indices[:-n_training_samples]]
    # using the all but the last 'n_training_samples' random numbers that were 
    # generated above; gather the flower data and labels for these indexes

testset_data = iris_data[indices[-n_training_samples:]]
testset_labels = iris_labels[indices[-n_training_samples:]]
    # using the last 'n_training_samples' random numbers that were 
    # generated above; gather the flower data and labels for these indexes




# # next we're going to visualise the data just for us to view now
# import matplotlib.pyplot
# from mpl_toolkits.mplot3d import Axes3D

# # first thing we're going to do it combine the 3rd and 4th pieces of data from each entry in the set, 
# # so that it will be possible to plot the set on a 3d plot.
# # So we recreate the dataset as 'X' like: [ [[][][]] [[][][]] [[][][]] ]
# # each of the three 2d arrays has one type of flower each
# # the subsequent lists within those 2d arrays contain the three pieces of data from that entry
# X = []
# for iclass in range(3):
#     X.append([[], [], []])

#     for i in range(len(learnset_data)):
#         if learnset_labels[i] == iclass:
#             X[iclass][0].append(learnset_data[i][0])
#             X[iclass][1].append(learnset_data[i][1])
#             X[iclass][2].append(sum(learnset_data[i][2:]))

# # now this 3d array is simply handed to the plotter, where each flower type will be coloured differently
# colours = ("r", "g", "b")
# fig = matplotlib.pyplot.figure()
# ax = fig.add_subplot(111, projection='3d')
# for iclass in range(3):
#     ax.scatter(X[iclass][0], X[iclass][1], X[iclass][2], c=colours[iclass])
# matplotlib.pyplot.show()




# to perform 'nearest-neighbour' we're going to need a function that determines the distance between two items
def distance(instance1, instance2):
    instance1 = numpy.array(instance1) #cleaning
    instance2 = numpy.array(instance2) #cleaning
    
    return numpy.linalg.norm(instance1 - instance2)

# # testing that function
# print( distance([0], [1]) )                 # -> 1.0
# print( distance([0, 0], [1, 1]) )           # -> 1.41421356237 (square root of 2)
# print( distance([1, 5], [1, 1]) )           # -> 4.0
# print( distance([3, 5], [1, 1]) )           # -> 4.472135955
# print( distance([0, 0, 0], [1, 1, 1]) )     # -> 1.73205080757 (square root of 2)
# print()




# the following function will take a new point and all the collected data, and return the 'k' nearest points
def get_neighbours(training_set, labels, test_instance, k, distance=distance):
    distances = []

    for index in range(len(training_set)):
        # we compare the 'test_instance' with every item in the 'training_set', 
        # the resulting data is placed in a tuple, which is appended into a list
        distances.append(
            (
                training_set[index],                            # first, the data iteslf
                distance(test_instance, training_set[index]),   # the calculated/compared distance
                labels[index]                                   # the corresponding flower type
            )
        )

    # sorts the list of distances, and returns the 'k' smallest
    distances.sort(key=lambda x: x[1]) # (the sort 'key' is number 1 in the sublists of this list which we are sorting)
    return distances[:k]

# # testing that function
# nearestLimit = 3
# for i in range(5):
#     neighbours = get_neighbours(
#         learnset_data, 
#         learnset_labels, 
#         testset_data[i], 
#         nearestLimit, 
#         distance=distance
#     )

#     print('test:',i)
#     print('element data:', testset_data[i])
#     print('(it\'s real type is', testset_labels[i], 'but don\'t tell the function that)')
#     print('the', nearestLimit, 'nearest elements are:')
#     for neighbour in neighbours:
#         print('\t item data:', neighbour[0], '\tdistance:', neighbour[0], '\ttype:', neighbour[2])
#     print()



# # the following function takes the results produced by the 'get_neighbours' function
# # and goes through them to determine what the most common flower type is
# from collections import Counter
# def vote(neighbours):
#     class_counter = Counter() # this is used essentially as a keyed set

#     for neighbour in neighbours:
#         class_counter[neighbour[2]] += 1

#     return class_counter.most_common(1)[0][0] # get the top '1' most common occurrences, first item in returned list (of one item) then the key of the set

# # the function does the same as above, except it also returns the probability
# def vote_prob(neighbours):
#     class_counter = Counter()

#     for neighbour in neighbours:
#         class_counter[neighbour[2]] += 1

#     labels, votes = zip(*class_counter.most_common())
#         # this crazy function takes a list of 2 item tuples, and splits them into
#         # two list ( tuple[0] -> lables, tuple[1] -> votes )

#     winner_label = class_counter.most_common(1)[0][0]
#     winner_voteCount = class_counter.most_common(1)[0][1]

#     return winner_label, winner_voteCount/sum(votes) # this second bit, divides the number of votes for this label, by the total number of votes

# # now, lets run the test! can the machine correctly identify the test elements?
# nearestLimit = 3
# for i in range(n_training_samples):
#     neighbours = get_neighbours(
#         learnset_data, 
#         learnset_labels, 
#         testset_data[i], 
#         nearestLimit, 
#         distance=distance
#     )

#     print(
#         'test: ' + str(i) + ' ' +
#         '\tmachine thinks: ' + str(vote_prob(neighbours)[0]) + ' (and is ' + str(vote_prob(neighbours)[1]*100) + '% sure about that)' + 
#         '\t\ttrue answer: ' + str(testset_labels[i]) + 
#         '\t' + ( '_/' if vote(neighbours)==testset_labels[i] else 'X' ) 
#     )

# all the code above has limited use of course. The problem is that the functions treat every item in the 
# data set equally. This becomes a problem when you want to use more than just the 3 nearest neighbours 
# in the machine's thought processes. If tell it to include the entire set; the result is that all the items
# are returned, thus the vote counting functions say that all types are equally likely with no regard to the
# distance between the two elements
#   lets try it again, but with a weighted system

def vote_distance_weights(neighbours, all_results=True):
    # neighbours = a list of tuples, which contain numbers which represent:
    #   the item's data iteslf | the calculated/compared distance | the item's flower type
    class_counter = Counter()

    for a in range(len(neighbours)):
        class_counter[neighbours[a][2]] += 1/(neighbours[a][1]**2 + 1)
        # what occurs here, is that each item in the set is being incremented
        # by a value proportional to the distance squared. Obviously, the futher
        # away the item is; the lower it's contribution

    labels, votes = zip(*class_counter.most_common())

    winner_label = class_counter.most_common(1)[0][0]

    if all_results:
        # this section will return all the types and their weighted likelyhood
        # it does this be getting the total number of elements, then dividing
        # each vote count in the 'class_counter' by this
        total = sum(class_counter.values())
        for key in class_counter:
             class_counter[key] /= total
        return winner_label, class_counter.most_common()
    else:
        return winner_label, class_counter.most_common(1)[0][1] / sum(votes)

# nearestLimit = 150
# for i in range(n_training_samples):
#     neighbours = get_neighbours(
#         learnset_data, 
#         learnset_labels, 
#         testset_data[i], 
#         nearestLimit, 
#         distance=distance
#     )

#     print(
#         'test: ' + str(i) + ' ' +
#         '\tmachine thinks: ' + str(vote_distance_weights(neighbours)[0]) +
#         '\t\ttrue answer: ' + str(testset_labels[i]) + ' (and is ' + str(vote_distance_weights(neighbours,all_results=False)[1]*100) + '% sure about that)' +
#         '\t' + ( '_/' if vote_distance_weights(neighbours,all_results=False)[0]==testset_labels[i] else 'X' ) 
#     )

# we see here that the machine gives mostly the same answers, but gives better answers when we include
# the entire dataset into the limit then it did with the unweighted system











# -- lets try a fresh data set --







# things get a little more abstract here: we have tree types of object 'apple', 'orange' and 'banana'
# in our training set we can see that these fruits have three items of data. There is no archetype
# of each fruit, but we do have a couple of examples of each.
#   From this, we are trying to figure out what fruits are contained in the 'test_set'. We have no
# correct labelling list; so the machine's guess will be what we're going with

train_labels = [
    'apple', 'banana', 
    'apple', 'banana', 
    'apple', 'orange',
    'orange','orange'
]
train_set = [
    (1,    2,   2   ), (-3, -2,  0  ),
    (1,    1,   3   ), (-3, -3,  -1 ),
    (1,    0,   3   ), (0 , 0.3, 0.8),
    (-0.5, 0.6, 0.7 ), (0,  0,   0  )
]
test_labels = [
]
test_set = [
    ( 0, 0,   0  ), (2,   2,   2), 
    (-3, -1,  0  ), (0,   1,   0.9),
    ( 1, 1.5, 1.8), (0.9, 0.8, 1.6)
]




# lets visualise the data
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D

colour = {'apple':'green', 'banana':'yellow', 'orange':'orange'}
fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111, projection='3d')
for index, item in enumerate(train_set):
    ax.scatter(item[0], item[1], item[2], c=colour[train_labels[index]])
    
for index, item in enumerate(test_set):
    ax.scatter(item[0], item[1], item[2], c='black')
matplotlib.pyplot.show()




nearestLimit = 3
for test_instance in test_set:
    neighbours = get_neighbours(
        train_set, 
        train_labels, 
        test_instance, 
        nearestLimit
    )

    print("vote distance weights: ", vote_distance_weights(neighbours))
    test_labels.append(vote_distance_weights(neighbours)[0])




# new lets visualise the processed data
import matplotlib.pyplot
from mpl_toolkits.mplot3d import Axes3D

colour = {'apple':'green', 'banana':'yellow', 'orange':'orange'}
testcolour = {'apple':'lightgreen', 'banana':'#eef4ad', 'orange':'#ffbd3a'}
fig = matplotlib.pyplot.figure()
ax = fig.add_subplot(111, projection='3d')
for index, item in enumerate(train_set):
    ax.scatter(item[0], item[1], item[2], c=colour[train_labels[index]])
    
for index, item in enumerate(test_set):
    ax.scatter(item[0], item[1], item[2], c=testcolour[test_labels[index]])
matplotlib.pyplot.show()

# it seems the machine did a pretty good job at classifying this data. Good job machine




