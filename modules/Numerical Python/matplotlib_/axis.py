import matplotlib, numpy
import matplotlib.pyplot

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
















# -- Labels
matplotlib.pyplot.clf()
matplotlib.pyplot.plot(
    [1, 20, 8, 23],
)

# these are used to label the x and y axises
matplotlib.pyplot.xlabel("Days")
matplotlib.pyplot.ylabel("Funkyness")

matplotlib.pyplot.show()