import numpy
import matplotlib.pyplot
import collections



# Setup, were we create two classes of items on a 2D plane. The two types are 
# well grouped in the corners of the plot
npoints = 50
X, Y = [], []

# class 0
X.append( numpy.random.uniform(low=-2.5, high=2.3, size=(npoints)) )
Y.append( numpy.random.uniform(low=-1.7, high=2.8, size=(npoints)) )

# class 1
X.append( numpy.random.uniform(low=-7.2, high=-4.4, size=(npoints)) )
Y.append( numpy.random.uniform(low=3,    high=6.5,  size=(npoints)) )


# adding points of class i to learnset
learnset = []
for i in range(2):
    points = zip(X[i], Y[i])
    for p in points:
        learnset.append( (p, i) )
# this learnset is a list of all the items created above, but it a nicer format
# ( (x,y), type )

# now for some simple plotting
colours = ["b", "r"]
for i in range(2):
    matplotlib.pyplot.scatter(X[i], Y[i], c=colours[i])
matplotlib.pyplot.show()














class Perceptron:
    def __init__(self, input_length, weights=None):
        if weights is None:
            self.weights = numpy.random.random(input_length)*2 - 1
        else:
            self.weights = weights

        self.learning_rate = 0.1
        
    @staticmethod
    def unit_step_function(x):
        return 0 if x < 0 else 1

    def __call__(self, in_data):
        weighted_input = self.weights * in_data
        weighted_sum = weighted_input.sum()
        return Perceptron.unit_step_function(weighted_sum)
    
    def adjust(self, target_result, calculated_result, in_data):
        error = target_result - calculated_result

        for i in range(len(in_data)):
            self.weights[i] += error * in_data[i] * self.learning_rate




#create and train a Perceptron
p = Perceptron(2)
for point, label in learnset:
    p.adjust(label, p(point), point)

#evalute it's performance
evaluation = collections.Counter()
for point, label in learnset:
    if p(point) == label:
        evaluation["correct"] += 1
    else:
        evaluation["wrong"] += 1
print(evaluation.most_common())

#plot out the points again, and create the decision line
colours = ["b", "r"]
for i in range(2):
    matplotlib.pyplot.scatter(X[i], Y[i], c=colours[i])

XR = numpy.arange(-8, 4)  
m = -p.weights[0] / p.weights[1]

print(m)

matplotlib.pyplot.plot(XR, m*XR, label="decision boundary")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()























class Perceptron:
    def __init__(self, input_length, weights=None):
        if weights is None:
            self.weights = numpy.random.random(input_length)*2 - 1
        else:
            self.weights = weights
        self.learning_rate = 0.05
        self.bias = 1
    
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




p = Perceptron(2)
for point, label in learnset:
    p.adjust(label, p(point), point)


evaluation = collections.Counter()
for point, label in learnset:
    if p(point) == label:
        evaluation["correct"] += 1
    else:
        evaluation["wrong"] += 1
print(evaluation.most_common())


colours = ["b", "r"]
for i in range(2):
    matplotlib.pyplot.scatter(X[i], Y[i], c=colours[i])
    
XR = numpy.arange(-8, 4)  
m = -p.weights[0] / p.weights[1]
b = -p.weights[-1]/p.weights[1]

print(m, b)

matplotlib.pyplot.plot(XR, m*XR + b, label="decision boundary")
matplotlib.pyplot.legend()
matplotlib.pyplot.show()