import matplotlib, numpy
import matplotlib.pyplot


# data, bins, patches = matplotlib.pyplot.hist( 
#     numpy.random.normal(size=100),          # data to place in the histogram
#     bins=10,                                # how many bars to make
#     normed=True,                            # normalises the values
#     edgecolor="#6a9662",                    # border colour of a bar
#     color="#ddffdd",                        # internal bar colour
#     cumulative=True                         # create cumulative histogram
# )

# matplotlib.pyplot.title("Gaussian Histogram")

# matplotlib.pyplot.xlabel("Value")
# matplotlib.pyplot.ylabel("Frequency")

# matplotlib.pyplot.show()

# # 'data' the value of each bar  (note how they sum to 100 here;
# # the value defined in the random number generator)
# print("data: ", data, sum(data))

# # 'bins' are the x coordinates where the bars touch the graph. This
# # loop shows how all the bars are the same width
# print("bins: ", bins)
# for i in range(len(bins)-1):
#     print(bins[i+1] -bins[i])

# # 'patches' are objects that contain all the data above, plus the calculated
# # width and angle (they're more about graphics than math)
# print("patches: ", patches)
# for patch in patches:
#     print(patch)
















# Bar Plots
bars = matplotlib.pyplot.bar(
    [1,2,3,"four"],         # naming the values
    [1,4,9,16]              # the values
)

bars[0].set_color('green')

matplotlib.pyplot.show()