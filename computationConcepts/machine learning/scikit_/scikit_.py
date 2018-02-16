import numpy
import matplotlib.pyplot



pointCount = 50
X, Y = [], []
learnset = []
testset = []

# class 0
X = numpy.random.uniform(low=-2.5, high=2.3, size=(pointCount))
Y = numpy.random.uniform(low=-1.7, high=4.8, size=(pointCount))
for item in zip(X,Y):
    learnset.append( (item,0) )

# class 1
X = numpy.random.uniform(low=-7.2, high=4.4, size=(pointCount))
Y = numpy.random.uniform(low=3,    high=6.5, size=(pointCount))
for item in zip(X,Y):
    learnset.append( (item,1) )


# Test Data
X = numpy.random.uniform(low=-7.2, high=5, size=(3*pointCount) ) 
Y = numpy.random.uniform(low=-4,   high=9, size=(3*pointCount) )
testset = list(zip(X,Y))


# Plot all this data
for point, kind in learnset:
    matplotlib.pyplot.scatter(
        point[0], 
        point[1], 
        c='#ff0000' if kind == 1 else '#0000ff',
        marker='o'
    )

# for point in testset:
#     matplotlib.pyplot.scatter(
#         point[0], 
#         point[1], 
#         c='#00ff00',
#         marker='o'
#     )

matplotlib.pyplot.show()











# from sklearn.datasets import fetch_mldata
# from sklearn.neural_network import MLPClassifier
import sklearn.neural_network

mlp = sklearn.neural_network.MLPClassifier(
    hidden_layer_sizes=(20, 3),
    max_iter=150,
    alpha=1e-4,
    solver='sgd',
    verbose=10,
    tol=1e-4,
    random_state=1,
    learning_rate_init=.1
)

mlp.fit(
    list(zip(*learnset))[0],
    list(zip(*learnset))[1]
)

print("Training set score: %f" % mlp.score(list(zip(*learnset))[0], list(zip(*learnset))[1]))

for point, kind in learnset:
    matplotlib.pyplot.scatter(
        point[0], 
        point[1], 
        c='#ff8888' if kind == 1 else '#8888ff',
        marker='o'
    )
# for point in testset:
#     matplotlib.pyplot.scatter(
#         point[0], 
#         point[1], 
#         c='#00ff00',
#         marker='o'
#     )

predictions = mlp.predict( list(zip(*learnset))[0] )
testset = zip(list(zip(*learnset))[0], predictions)

for point, kind in testset:
    matplotlib.pyplot.scatter(
        point[0], 
        point[1], 
        c='#ff0000' if kind == 1 else '#0000ff',
        marker='x'
    )

matplotlib.pyplot.show()

