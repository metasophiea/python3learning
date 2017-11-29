import matplotlib, numpy

# MatPlotLib is a plotting library, a lot like GNUplot


# pyplot.plot
#   this is the main plotting tool
import matplotlib.pyplot








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
# Dimensions
matplotlib.pyplot.clf()
matplotlib.pyplot.plot(
    [1, 20, 8, 25],
)

# get the current dimensions of the graph
# Xmin, Xmax, Ymin, Ymax
print( matplotlib.pyplot.axis() ) 
matplotlib.pyplot.axis( [0, 3, 0, 25] )         # set the dimensions of the graph
matplotlib.pyplot.show()


# - Axis and Spines
matplotlib.pyplot.clf()
matplotlib.pyplot.plot( [1, 20, 8, 25] )
axis = matplotlib.pyplot.gca()                  # get axis object
axis.spines['top'].set_color('none')            # removing the top border
axis.spines['right'].set_color('none')          # removing the right border
axis.xaxis.set_ticks_position('bottom')         # place the X number markings at the bottom of the graph
axis.spines['bottom'].set_position(('data',5))  # move the bottom border (and subsequently the number markings
                                                # up to 5 on the Y axis)
axis.yaxis.set_ticks_position('left')           # place the Y number markings at the left of the graph
axis.spines['left'].set_position(('data',0.5))  # move the left border (and subsequently the number markings
                                                # over to 0.5 on the X axis)
matplotlib.pyplot.show()                        


# - Ticks
# these are the number markings on the axises
matplotlib.pyplot.clf()
matplotlib.pyplot.plot( [1, 20, 8, 25] )
axis = matplotlib.pyplot.gca()                  # get axis object
print( matplotlib.pyplot.xticks() )             # get the current X ticks on the graph
print( matplotlib.pyplot.yticks() )             # get the current Y ticks on the graph
matplotlib.pyplot.xticks( numpy.arange(4) )     # set the X ticks on the graph
matplotlib.pyplot.yticks( 
    [1, 2, 4, 8, 16, 32],
    ('Berlin', 'London', 'Hamburg', r'$+2\pi$', 'Paris', 'Dublin')
) # set the ticks on the Y axis and name them
  # (note the 'LaTeX' string, which is used for fancy formatting)

# one can also adjust the font of each item on the axis using 'get_xticklabels()'
for xtick in axis.get_xticklabels():
    xtick.set_fontsize(18)
    xtick.set_bbox(
        dict(
            facecolor='orange',
            edgecolor='red',
            alpha=0.7
        )
    )
matplotlib.pyplot.show()    

# - Legend
matplotlib.pyplot.clf()
matplotlib.pyplot.plot( [1, 20, 8, 25], label="Fanciness")
matplotlib.pyplot.legend(loc='lower left')
matplotlib.pyplot.show()






# -- Styling
# there is an option to style the drawn graph with a two (ish) character string. Below is a listing 
# of all the possible styling commands
# =============================================
# character       description
# =============================================
# '-'             solid line style
# '--'            dashed line style
# '-.'            dash-dot line style
# ':'             dotted line style
# '.'             point marker
# ','             pixel marker
# 'o'             circle marker
# 'v'             triangle_down marker
# '^'             triangle_up marker
# '<'             triangle_left marker
# '>'             triangle_right marker
# '1'             tri_down marker
# '2'             tri_up marker
# '3'             tri_left marker
# '4'             tri_right marker
# 's'             square marker
# 'p'             pentagon marker
# '*'             star marker
# 'h'             hexagon1 marker
# 'H'             hexagon2 marker
# '+'             plus marker
# 'x'             x marker
# 'D'             diamond marker
# 'd'             thin_diamond marker
# '|'             vline marker
# '_'             hline marker
# ===============================================
#
# ==================
# character   color
# ==================
# 'b'         blue
# 'g'         green
# 'r'         red
# 'c'         cyan
# 'm'         magenta
# 'y'         yellow
# 'k'         black
# 'w'         white
# ==================

# clear entire plot
matplotlib.pyplot.clf()

# multiple plotting with a single command
matplotlib.pyplot.plot(
# graphing as a red dashed line
    [0, 1, 1.75, 3],
    [1, 20, 8, 23],
    "--r",
# repeated graphing with the same data but differnet styling
    [0, 1, 1.75, 3],
    [1, 20, 8, 23],
    "oy"
)

# graphing as descrete dots of blue
matplotlib.pyplot.plot(
    [1, -4.5, 16, 23],
    "ob"
)

matplotlib.pyplot.show()








# -- Labels
matplotlib.pyplot.clf()
matplotlib.pyplot.plot(
    [1, 20, 8, 23],
)

# these are used to label the x and y axises
matplotlib.pyplot.xlabel("Days")
matplotlib.pyplot.ylabel("Funkyness")

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








