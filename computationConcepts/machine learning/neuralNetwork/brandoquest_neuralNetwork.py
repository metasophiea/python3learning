import numpy
import matplotlib.pyplot
import time
from collections import Counter


data = (
    ((-0.1,0),    0),
    ((0.1,0),    0),
    ((1,1),    0),
    ((1.5,1.5),0),
    ((1.3,0.9),0),
    ((2,2),    0),
    ((1.9,1.8),0),
    ((1.2,1),  0),
    ((1,1.2),  0),

    ((0,2.7),  0),
    ((0,2.65),  0),
    ((0,2.6325),  0),
    ((0,2.63),  0),
    ((0,2.6315),  0),
    ((0,2.625),  0),
    ((0,2.6),  0),

    ((2.2,0),  0),
    ((2.3,0),  0),
    ((2.325,0),  0),
    ((2.3256,0),  0),
    ((2.35,0),  0),
    ((2.4,0),  0),
    ((2.5,0),  0),


    ((2,1),    1),
    ((2.5,1.5),1),
    ((2.3,0.9),1),
    ((3,2),    1),
    ((2.9,1.8),1),
    ((2.2,1),  1)
)













class node:
    def __init__(self, input_length, weights=None):
        if weights is None:
            self.weights = numpy.ones(input_length) * 0.5
        else:
            self.weights = weights
        
        self.learning_rate = 0.1
        self.unitStep = 0.5

    def unit_step_function(self, x):
        return 1 if x > self.unitStep else 0

    def __call__(self, in_data):
        weighted_input = self.weights * in_data
        weighted_sum = weighted_input.sum()
        return self.unit_step_function(weighted_sum)

    def adjust(self, target_result, calculated_result, in_data):
        error = target_result - calculated_result

        for i in range(len(in_data)):
            self.weights[i] += error * in_data[i] * self.learning_rate






# Single Layer
# machine = node(2)

# print('- machine details -')
# print('inputs:', machine.weights)
# print()

# for a in range(10):
#     for point, kind in data:
#         machine.adjust( kind,  machine(point), point )

# print('- machine details -')
# print('inputs:', machine.weights)
# print()


# evaluation = Counter()
# for point, kind in data:
#     if machine(point) == kind:
#         evaluation["correct"] += 1
#     else:
#         evaluation["wrong"] += 1

# print(evaluation.most_common())


# # Draw out all the points on a graph and colour them by correct type
# for point, kind in data:
#     matplotlib.pyplot.scatter(
#         point[0], 
#         point[1], 
#         c='#ff0000' if kind == 1 else '#0000ff',
#         marker='o'
#     )
# # Draw out all the points on a graph and colour them by what the machine thinks
# for point, kind in data:
#     matplotlib.pyplot.scatter(
#         point[0], 
#         point[1], 
#         c='#ff8888' if machine(point) else '#8888ff',
#         marker='x'
#     )
# #draw in machine's decision line
# m = -machine.weights[0] / machine.weights[1]
# X = numpy.arange(-1, 4)
# matplotlib.pyplot.plot(X, ( (1/machine.weights[1])*machine.unitStep ) +m*X)
# matplotlib.pyplot.grid(color='black', alpha=0.5, linestyle='dashed', linewidth=0.5)
# matplotlib.pyplot.show()








# Double Layer
# machine_1 = node(2)
# machine_2 = node(2)
# machine_3 = node(2)

# for point, kind in data:
#     temp = machine_3( (machine_1(point), machine_2(point)) )

#     machine_1.adjust( kind,  temp, point )
#     machine_2.adjust( kind,  temp, point )
#     machine_3.adjust( kind,  temp, point )


# evaluation = Counter()
# for point, kind in data:
#     if machine_3( (machine_1(point), machine_2(point)) ) == kind:
#         evaluation["correct"] += 1
#     else:
#         evaluation["wrong"] += 1

# print(evaluation.most_common())







# # Draw out all the points on a graph and colour them by correct type
# for point, kind in data:
#     matplotlib.pyplot.scatter(
#         point[0], 
#         point[1], 
#         c='#ff0000' if kind == 1 else '#0000ff',
#         marker='o'
#     )
# # Draw out all the points on a graph and colour them by what the machine thinks
# for point, kind in data:
#     matplotlib.pyplot.scatter(
#         point[0], 
#         point[1], 
#         c='#ff8888' if machine_3( (machine_1(point), machine_2(point)) ) else '#8888ff',
#         marker='x'
#     )

# #draw in decision lines
# m = -machine_1.weights[0] / machine_1.weights[1]
# X = numpy.arange(-1, 4)
# matplotlib.pyplot.plot(X, ( (1/machine_1.weights[1])*machine_1.unitStep ) +m*X)

# m = -machine_2.weights[0] / machine_2.weights[1]
# X = numpy.arange(-1, 4)
# matplotlib.pyplot.plot(X, ( (1/machine_2.weights[1])*machine_2.unitStep ) +m*X)

# matplotlib.pyplot.grid(color='black', alpha=0.5, linestyle='dashed', linewidth=0.5)
# matplotlib.pyplot.show()