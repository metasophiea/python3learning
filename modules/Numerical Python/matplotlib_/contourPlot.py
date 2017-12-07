import matplotlib, numpy
import matplotlib.pyplot


# - Data Generation
ylist = numpy.linspace(-3.0, 3.0, num=8)
xlist = numpy.linspace(-3.0, 3.0, num=6)
print(xlist)
print(ylist)
X, Y = numpy.meshgrid(xlist, ylist)
print(X)
print(Y)
Z = numpy.sqrt(X**2 + Y**2) # a straight-forward value-to-value calculation for 
                            # each element in the X and Y matrices. This particular
                            # process will create a circular contour map
print(Z)








# # - Lined Contours
# matplotlib.pyplot.figure()

# # here the first two matrices are used in combination to place the values in the third matrix on the plot
# # simply put; the value Z[0][0] is placed in position x = X[0][0] y = Y[0][0]
# contourPlot = matplotlib.pyplot.contour(
#     X, Y, Z,
#     colors=('r', 'green', 'blue', (1, 1, 0), '#afeeee', '0.5'), # for all your colouring needs
#     linewidths=numpy.arange(.5, 4, .5),
# )

# matplotlib.pyplot.clabel(
#     contourPlot, 
#     inline=False,        # true -> breaks into the line to write the text 
#     fontsize=10,
# )

# matplotlib.pyplot.title('Contour Plot')
# matplotlib.pyplot.xlabel('x')
# matplotlib.pyplot.ylabel('y')

# matplotlib.pyplot.show()






# - Filled Contours with manually selected layers
matplotlib.pyplot.figure()

contourPlot = matplotlib.pyplot.contourf(
    X, Y, Z,
    levels=numpy.arange(0, 5, 0.1),
    #colors=('#ff0000', '#ffff00', '#0000FF', '0.6', 'c', 'm', '#ff00ff', '#00ffff'), # for all your colouring needs
)

matplotlib.pyplot.colorbar(
    contourPlot
)

matplotlib.pyplot.title('Filled Contours Plot')
matplotlib.pyplot.xlabel('x')
matplotlib.pyplot.ylabel('y')

matplotlib.pyplot.show()