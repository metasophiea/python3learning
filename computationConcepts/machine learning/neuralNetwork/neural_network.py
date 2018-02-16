import numpy
from collections import Counter
from matplotlib import pyplot
from itertools import chain
from mpl_toolkits.mplot3d import Axes3D


# this first foray into neural networking brings us an implementation of an AND gate
# This AND gate uses a single node of a network, here called a 'perceptron' Perceptrons
# can take multiple input values and produce a single output value. These input values
# can be weighted before they are summed and compared to a threshold. 

class Perceptron:
    # __init__(self, input_length, weights=None)
    #       here the number of input's and their weights are defined
    #       (if no weights are provided, all are set to 0.5)
    # unit_step_function(x)
    #       this is the threshold judgement function
    # __call__(self, in_data)
    #       this is where the work happens. The input values are taken
    #       in, multiplied by their weights, summed and passed though
    #       the threshold judgement function

    def __init__(self, input_length, weights=None):
        if weights is None:
            self.weights = numpy.ones(input_length) * 0.5
        else:
            self.weights = weights
        
    @staticmethod
    def unit_step_function(x):
        return 1 if x > 0.5 else 0

    def __call__(self, in_data):
        weighted_input = self.weights * in_data
        weighted_sum = weighted_input.sum()
        return Perceptron.unit_step_function(weighted_sum)
    



# now we create a single node that has two inputs
# (their weights are defaulted to 0.5)
p = Perceptron(2)
# in this implementation, no single input (of max value 1) could activate
# the output value - at least 2 are required to overcome the threshold value
# Since there are only two inputs anyway; this means that the output will
# only activate when all the inputs are active; thus; an AND gate




# now for some testing:
testArray = [
    numpy.array([0, 0]),
    numpy.array([0, 1]),
    numpy.array([1, 0]),
    numpy.array([1, 1])
]

for x in testArray:
    print( x, p(numpy.array(x)) )
print()
















# Lets try a more complicated one; where we create a scatter plot of points, draw an arbitrary line
# through the data which splits the points in half. We then define the points on either side of the 
# line to be of different types; and attempt to train the node into knowing which type a point is;
# without telling it about the line. 
#   First the preceptron. This time, it comes with a training function which can be used to adjust
# the input weights automatically

class Perceptron:
    # __init__(self, input_length, weights=None)
    #       here the number of input's and their weights are defined
    #       (if no weights are provided, they are all assigned a random
    #       value between -1 and 1)
    #       the 'learning_rate' is also defined here
    # unit_step_function(x)
    #       this is the threshold judgement function
    #       summed value must be grater than or equal to zero
    # __call__(self, in_data)
    #       this is where the work happens. The input values are taken
    #       in, multiplied by their weights, summed and passed though
    #       the threshold judgement function
    # adjust(self, target_result, calculated_result, in_data)
    #       the code here is used to train the node to make the correct decision
    #       It takes the correct result and its produced result along with the
    #       input data used to make both these things. From the correct and produced
    #       result, a error value is produced. 
    #       After this; corrections are made to each of the inputs. A 'correction'
    #       is the sum of the original weighting with the error value multiplied by 
    #       the input data for this input, by the learning rate 

    def __init__(self, input_length, weights=None):
        if weights is None:
            self.weights = numpy.random.random(input_length)*2 - 1
        else:
            self.weights = weights

        self.learning_rate = 0.1
        
    @staticmethod
    def unit_step_function(x):
        return 1 if x >= 0 else 0

    def __call__(self, in_data):
        weighted_input = self.weights * in_data
        weighted_sum = weighted_input.sum()
        return Perceptron.unit_step_function(weighted_sum)
    
    def adjust(self, target_result, calculated_result, in_data):
        error = target_result - calculated_result

        for i in range(len(in_data)):
            self.weights[i] += error * in_data[i] * self.learning_rate




# these two functions are used to define whether a point is above or below the line
def lin1(x):
    return x + 4
def above_line(point, line_func):
    x, y = point
    return 1 if y > line_func(x) else 0


  

#creation of the random data
points = numpy.random.randint(1, 100, (100, 2)) # make a 100x2 array of random ints between 1 and 100




# creation of a single node
p = Perceptron(2)
# training that node with the random data
for point in points:
    p.adjust(
        above_line(point, lin1), 
        p(point), 
        point
    )




# testing the node with the same data, to see if it can correctly judge the data points
evaluation = Counter()
for point in points:
    if p(point) == above_line(point, lin1):
        evaluation["correct"] += 1
    else:
        evaluation["wrong"] += 1

print(evaluation.most_common())








# Draw out all the points on a graph and colour them by type
for point in points:
    pyplot.scatter(
        point[0], 
        point[1], 
        c='r' if above_line(point, lin1) == 1 else 'b'
    )

# based on the input weights within the neural node, compute the slop of the
# dividing line it thinks is correct
m = -p.weights[0] / p.weights[1]

# draw the real division line and the generated one
X = numpy.arange(-3, 120)
pyplot.plot(X, lin1(X), label="real line")
pyplot.plot(X, m*X, label="neural line")
pyplot.grid(color='black', alpha=0.5, linestyle='dashed', linewidth=0.5)
pyplot.legend()
pyplot.show()

# one can notice from the graph, that the neural node's line always passed through the origin, 
# where as the true line doesn't. In fact we rely on this fact to calculate the slope. This is
# due to the lack of a post-summation constant within the perceptron. This value would move the
# generated line up or down the Y axis
















# # Lets go with another data set
# class1 = [(3, 4), (4.2, 5.3), (4, 3), (6, 5), (4, 6), (3.7, 5.8),(3.2, 4.6),(5.2, 5.9), (5, 4), (7, 4),(3, 7),(4.3, 4.3)] 
# class2 = [(-3, -4), (-2, -3.5), (-1, -6), (-3, -4.3), (-4, -5.6), (-3.2, -4.8), (-2.3, -4.3), (-2.7, -2.6), (-1.5, -3.6), (-3.6, -5.6), (-4.5, -4.6), (-3.7, -5.8)]

# # fresh perceptron
# p = Perceptron(2)

# # training the perceptron node with the new data
# for point in class1:
#     p.adjust(
#         1, 
#         p(point), 
#         point
#     )

# for point in class2:
#     p.adjust(
#         0, 
#         p(point), 
#         point
#     )
    
# # now to test it out
# evaluation = Counter()
# for point in class1:
#     if p(point) == 1:
#         evaluation["correct"] += 1
#     else:
#         evaluation["wrong"] += 1
# for point in class2:
#     if p(point) == 0:
#         evaluation["correct"] += 1
#     else:
#         evaluation["wrong"] += 1
        
# print(evaluation.most_common())

# # drawing the points with the colour selected by their colour
# # then drawing the dividing line generated by the node
# X, Y = zip(*class1)
# pyplot.scatter(X, Y, c="r")
# X, Y = zip(*class2)
# pyplot.scatter(X, Y, c="b")

# x = numpy.arange(-7, 10)
# m = -p.weights[0] / p.weights[1]

# pyplot.grid(color='black', alpha=0.5, linestyle='dashed', linewidth=0.5)
# pyplot.plot(x, m*x)
# pyplot.show()
# # one can notice again that the generated line passes through the origin
















# Let's have another crack at the original data set; but with a modified Perceptron
class Perceptron:
    # __init__(self, input_length, weights=None)
    #       here the number of input's and their weights are defined
    #       (if no weights are provided, they are all assigned a random
    #       value between -1 and 1)
    #       the 'learning_rate' is also defined here along with the bias
    # sigmoid_function(x)
    #       this is the threshold judgement function
    #       the provided value is placed on the sigmoid function line,
    #       if the result is above 0.5, 'True' is returned
    # __call__(self, in_data)
    #       first, all but the last value in weights are multiplied by 'in_data'
    #       these values are summed. Then the last value of the weights is multiplied
    #       by the bias and added to the sum. The resulting value is passed through 
    #       the thresholding function
    # adjust(self, target_result, calculated_result, in_data)
    #       this method is used to change the input weights. First the difference 
    #       between the desired output and the produced output is calculated. Then,
    #       for each input the difference is multiplied by the learning rate and a 
    #       corresponding value from input data, and added to the weight.
    #           The final weight set to itself plus the difference, by the learning 
    #       rate by the bias

    def __init__(self, input_length, weights=None):
        if weights is None:
            self.weights = numpy.random.random(input_length+1)*2 - 1
        else:
            self.weights = weights

        self.learning_rate = 0.1
        self.bias = 10
        
    @staticmethod
    def sigmoid_function(x):
        res = 1 / (1 + numpy.power(numpy.e, -x))
        return 0 if res < 0.5 else 1

    def __call__(self, in_data):
        weighted_input = self.weights[:-1] * in_data
        weighted_sum = weighted_input.sum() + self.bias*self.weights[-1]
        return Perceptron.sigmoid_function(weighted_sum)
    
    def adjust(self, target_result, calculated_result, in_data):
        error = target_result - calculated_result

        for i in range(len(in_data)):
            self.weights[i] += error * in_data[i] * self.learning_rate

        self.weights[-1] += error * self.bias * self.learning_rate 
        print(self.weights[-1])




# creation of a single node
p = Perceptron(2)
# training that node with the random data
for point in points:
    p.adjust(
        above_line(point, lin1), 
        p(point), 
        point
    )

# testing the node with the same data, to see if it can correctly judge the data points
evaluation = Counter()
for point in points:
    if p(point) == above_line(point, lin1):
        evaluation["correct"] += 1
    else:
        evaluation["wrong"] += 1

print(evaluation.most_common())


# Draw out all the points on a graph and colour them by correct type
for point in points:
    pyplot.scatter(
        point[0], 
        point[1], 
        c='#ff0000' if above_line(point, lin1) == 1 else '#0000ff',
        marker='o'
    )
# Draw out all the points again but colour them by what the node thinks
for point in points:
    pyplot.scatter(
        point[0], 
        point[1], 
        c='#ff8888' if p(point) == 1 else '#8888ff',
        marker='x'
    )

# based on the input weights within the neural node, compute the slop and offset 
# of the dividing line it thinks is correct (I've no idea how this works)

X = numpy.arange(-3, 120)
m = -p.weights[0]  / p.weights[1]
b = -p.weights[-1] / p.weights[1]

pyplot.plot(X, lin1(X), label="real line")
pyplot.plot(X, ((m*X) + b), label="decision boundary")
pyplot.grid(color='black', alpha=0.5, linestyle='dashed', linewidth=0.5)
pyplot.legend()
pyplot.show()