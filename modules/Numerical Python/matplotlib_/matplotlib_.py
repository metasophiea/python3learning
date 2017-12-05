import matplotlib, numpy

# MatPlotLib is a plotting library, a lot like GNUplot

# pyplot.plot
#   this is the main plotting tool
import matplotlib.pyplot






# temporary function re-writing
tempShow = matplotlib.pyplot.show
matplotlib.pyplot.show = print
















# -- A simple plot
matplotlib.pyplot.plot(
    [-1, -4.5, 16, 23]
)
# produce graph
matplotlib.pyplot.show()
# a single array of data will cause the plotting function to map the y values to the array items, 
# and the x values to their index positions. Two arrays are plotted to x and y respectively
#   if more arrays are added; they are assumed to be additional graphs
















# -- Manipulation of the Graph

# Setting the graph window size
matplotlib.pyplot.figure(figsize=(12, 4))

# Dimensions
matplotlib.pyplot.clf()
matplotlib.pyplot.plot(
    [1, 20, 8, 25],
)

# get the current dimensions of the graph
# Xmin, Xmax, Ymin, Ymax
print( matplotlib.pyplot.axis() ) 
matplotlib.pyplot.axis( [0, 3, 0, 25] )         # set the dimensions of the graph
                                                # (one can also use 'tight' to
                                                # automatically set the axis limits)
matplotlib.pyplot.show()

# Logarithmic Scale
matplotlib.pyplot.clf()

figure = matplotlib.pyplot.figure()
plot = figure.add_subplot(1, 1, 1)
x = numpy.arange(0, 5, 0.25)
plot.plot(x, x**2, x, x**3)

plot.set_yscale("log")

matplotlib.pyplot.show()

















# - Legend
matplotlib.pyplot.clf()
matplotlib.pyplot.plot( [1, 20, 8, 25], label="Fanciness")

x = numpy.linspace(0, 3, 1000)
y = numpy.cos(x*3) * 5
matplotlib.pyplot.plot( x, y, '-r', label='$3 sin(x)$')

matplotlib.pyplot.legend(loc='upper center')
# loc   - used to select the position of the legend in the graph.
#           - "lower left"      - "upper right"     - "center"
#           - "upper center"
#         one can also use "best" which makes matplotlib figure out the
#         best location for the legend based on the data being shown

matplotlib.pyplot.show()
















# - Annotations
# the annotate command, places an arrow with text onto the graph
matplotlib.pyplot.clf()
matplotlib.pyplot.plot( [1, 20, 8, 25], label="Fanciness")

x = numpy.linspace(0, 3.14, 70, endpoint=True)
matplotlib.pyplot.scatter([x],[10 + 10 * numpy.sin(x*4)], 2, color ='blue')

matplotlib.pyplot.annotate(
    'interesting',
    xy=(1.95, 19.96),       # business end point location
    xytext=(2.3, 23.5),     # back end location
    fontsize=16,
    arrowprops=dict(
        width=10,
        headwidth=20,
        headlength=20,
        facecolor='red',
        shrink=0.01
    )
)

matplotlib.pyplot.show()









# -- Fill Between
# using this function, one is able to colour the space between two curves
# fill_between(x, y1, y2, where, interpolate, kwargs)
# x 	        An N-length array of the x data
# y1 	        An N-length array (or scalar) of the y data
# y2 	        An N-length array (or scalar) of the y data
# where 	    If None, default to fill between everywhere. If not None, it is an N-length numpy boolean
#               array and the fill will only happen over the regions where where==True.
# interpolate 	If True, interpolate between the two lines to find the precise point of intersection. 
#               Otherwise, the start and end points of the filled region will only occur on explicit values
#               in the x array.
# kwargs 	    Keyword args passed on to the PolyCollection


matplotlib.pyplot.clf()

n = 256
X = numpy.linspace(-numpy.pi,numpy.pi,n,endpoint=True)
Y = numpy.sin(2*X)

# plots the line as usual
matplotlib.pyplot.plot(
    X,
    Y, 
    color='blue',
    alpha=1.0
)

# draws in the shading
matplotlib.pyplot.fill_between(
    X,
    Y,    # primary line
    0.25, # secondary line - shading is done between this. and the line above
    color='blue',
    alpha=0.1
)

matplotlib.pyplot.show()
















# - Text
matplotlib.pyplot.clf()
matplotlib.pyplot.text(
    0.5, 0.5,                            
    'the text',              
    horizontalalignment='center',   # x
    verticalalignment='center',     # y anchor placement
    fontsize=20,                    
    alpha=0.5                        
)

matplotlib.pyplot.show()
















# - Grid Lines
matplotlib.pyplot.clf()
matplotlib.pyplot.text(
    0.5, 0.5,                            
    'the text',              
    horizontalalignment='center',   # x
    verticalalignment='center',     # y anchor placement
    fontsize=20,                    
    alpha=0.5                        
)
matplotlib.pyplot.grid(
    color='b', 
    alpha=0.5, 
    linestyle='dashed', 
    linewidth=0.5
)

matplotlib.pyplot.show()
















# - Saving to file
matplotlib.pyplot.clf()
matplotlib.pyplot.text(
    0.5, 0.5,                            
    'the text',              
    horizontalalignment='center',   # x
    verticalalignment='center',     # y anchor placement
    fontsize=20,                    
    alpha=0.5                        
)
matplotlib.pyplot.grid(
    color='b', 
    alpha=0.5, 
    linestyle='dashed', 
    linewidth=0.5
)

matplotlib.pyplot.savefig("figName.png");
# optional argument; dpi    eg. dpi=200
# output formats: PNG, JPG, EPS, SVG, PGF and PDF

matplotlib.pyplot.show()