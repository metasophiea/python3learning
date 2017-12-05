import matplotlib, numpy
import matplotlib.pyplot



# temporary function re-writing
tempShow = matplotlib.pyplot.show
matplotlib.pyplot.show = print



# - Subplot
# here, a simple gridding system is used to layout graphs. Before each plot, the subplot command
# is called, with the desired grid layout, and it's position in it.

matplotlib.pyplot.subplot(2, 2, 1)
matplotlib.pyplot.text(
    0.5, 0.5,
    'subplot(2,2,1)',
    horizontalalignment='center',    
    verticalalignment='center',     
    fontsize=20,
    alpha=0.5                        
)

matplotlib.pyplot.subplot(2, 2, 4)
matplotlib.pyplot.text(
    0.5, 0.5, 
    'subplot(2,2,4)', 
    ha='center', 
    va='center'
)

matplotlib.pyplot.show()


# one can also use this method with a more object-oriented approach by using the 
# 'add_subplot' command.
matplotlib.pyplot.close()

figure = matplotlib.pyplot.figure(figsize=(8, 8))
sub_1 = figure.add_subplot(2, 2, 1)
sub_1.text(
    0.5, 0.5,
    'subplot(2,2,1)',
    horizontalalignment='center',    
    verticalalignment='center',     
    fontsize=20,                    
    alpha=0.5                        
)

sub_2 = figure.add_subplot(2, 2, 4)
sub_2.text(
    0.5, 0.5, 
    'subplot(2,2,4)', 
    ha='center', 
    va='center'
)

matplotlib.pyplot.show()


# and now, a more complex layout
matplotlib.pyplot.close()

figure = matplotlib.pyplot.figure(figsize=(8, 4))

matplotlib.pyplot.subplot(2, 1, 1)
matplotlib.pyplot.text(
    0.5, 0.5,
    'subplot(2,2,1)',
    horizontalalignment='center',    
    verticalalignment='center',     
    fontsize=20,
    alpha=0.5                        
)

matplotlib.pyplot.subplot(2, 3, 4)
matplotlib.pyplot.text(
    0.5, 0.5,
    'subplot(2,2,1)',
    horizontalalignment='center',    
    verticalalignment='center',     
    fontsize=20,
    alpha=0.5                        
)
matplotlib.pyplot.subplot(2, 3, 5)
matplotlib.pyplot.text(
    0.5, 0.5,
    'subplot(2,2,1)',
    horizontalalignment='center',    
    verticalalignment='center',     
    fontsize=20,
    alpha=0.5                        
)
matplotlib.pyplot.subplot(2, 3, 6)
matplotlib.pyplot.text(
    0.5, 0.5,
    'subplot(2,2,1)',
    horizontalalignment='center',    
    verticalalignment='center',     
    fontsize=20,
    alpha=0.5                        
)
matplotlib.pyplot.show()
















# - Gridspec
# gridspec is a lot like subplot, except that the grid layout is set at the start, and
# each graph has to declare which of these subsections it wants to take up

# simple example
import matplotlib.gridspec
matplotlib.pyplot.close()

figure = matplotlib.pyplot.figure()
gridspec = matplotlib.gridspec.GridSpec(
    1, 1,
    bottom = 0.4,
    left = 0.05,
    top = 0.99
)
plot = figure.add_subplot( gridspec[0, 0] )

matplotlib.pyplot.show()




# more complex example
matplotlib.pyplot.close()

figure = matplotlib.pyplot.figure()
gridspec = matplotlib.gridspec.GridSpec(3, 3)

plot_1 = figure.add_subplot( gridspec[0, :] )
plot_1.text(0.5, 0.5, 'Axes 1', ha='center', va='center', size=24, alpha=.5)

plot_2 = figure.add_subplot( gridspec[1, :-1] )
plot_2.text(0.5, 0.5, 'Axes 2', ha='center', va='center', size=24, alpha=.5)

plot_3 = figure.add_subplot( gridspec[1:, -1] )
plot_3.text(0.5, 0.5, 'Axes 3', ha='center', va='center', size=24, alpha=.5)

plot_4 = figure.add_subplot( gridspec[-1, 0] )
plot_4.text(0.5, 0.5, 'Axes 4', ha='center', va='center', size=24, alpha=.5)

plot_5 = figure.add_subplot( gridspec[-1, -2] )
plot_5.text(0.5, 0.5, 'Axes 5', ha='center', va='center', size=24, alpha=.5)

figure.tight_layout()

matplotlib.pyplot.show()