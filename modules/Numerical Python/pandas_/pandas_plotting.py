import pandas, matplotlib, matplotlib.pyplot




# # simple line-plot example
# data = [100, 120, 140, 180, 200, 210, 214]
# s = pandas.Series(data, index=range(len(data)))
# s.plot()
# matplotlib.pyplot.show()



# # graph where the index is a list of strings
# fruits = ['apples', 'oranges', 'cherries', 'pears']
# quantities = [20, 33, 52, 10]
# S = pandas.Series(quantities, index=fruits)
# S.plot()
# matplotlib.pyplot.show()




# # plotting the data of a DataFrame
# cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
#                    "Paris", "Vienna", "Bucharest", "Hamburg", 
#                    "Budapest", "Warsaw", "Barcelona", 
#                    "Munich", "Milan"],
#           "population": [8615246, 3562166, 3165235, 2874038,
#                          2273305, 1805681, 1803425, 1760433,
#                          1754000, 1740119, 1602386, 1493900,
#                          1350680],
#           "area" : [1572, 891.85, 605.77, 1285, 
#                     105.4, 414.6, 228, 755, 
#                     525.2, 517, 101.9, 310.4, 
#                     181.8]
# }
# city_frame = pandas.DataFrame(
#     cities,
#     columns=["population", "area"],
#     index=cities["name"]
# )
# city_frame["area"] *= 1000  # just to get this data into a scale similar to population
# city_frame.plot(
#     xticks=range(len(city_frame.index)),    # defining the X axis marks
#     use_index=True, 
#     rot=90                                  # rotate the X axis markings by 90 degrees
# )
# matplotlib.pyplot.show()




# # here, we see the same data as before; but instead of changing the area data
# # to suit the population data; we use a second Y axis with new markings 
# cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
#                    "Paris", "Vienna", "Bucharest", "Hamburg", 
#                    "Budapest", "Warsaw", "Barcelona", 
#                    "Munich", "Milan"],
#           "population": [8615246, 3562166, 3165235, 2874038,
#                          2273305, 1805681, 1803425, 1760433,
#                          1754000, 1740119, 1602386, 1493900,
#                          1350680],
#           "area" : [1572, 891.85, 605.77, 1285, 
#                     105.4, 414.6, 228, 755, 
#                     525.2, 517, 101.9, 310.4, 
#                     181.8]
# }
# city_frame = pandas.DataFrame(
#     cities,
#     columns=["population", "area"],
#     index=cities["name"]
# )


# fig, ax = matplotlib.pyplot.subplots()

# fig.suptitle("City Statistics")
# ax.set_xlabel("Citites")

# # left axis
# ax.set_ylabel("Population")
# city_frame["population"].plot(
#     ax=ax, 
#     style="b-",
#     use_index=True, 
#     rot=90
# )

# # right axis
# ax2 = ax.twinx()
# ax2.set_ylabel("Area")
# city_frame["area"].plot(
#     ax=ax2, 
#     style="g-",
#     use_index=True, 
#     rot=90
# )

# matplotlib.pyplot.show()




# # extending on from the last example; this one creates a third column of data,
# # and adds another Y axis to the right, and maps the new column to that
# cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
#                    "Paris", "Vienna", "Bucharest", "Hamburg", 
#                    "Budapest", "Warsaw", "Barcelona", 
#                    "Munich", "Milan"],
#           "population": [8615246, 3562166, 3165235, 2874038,
#                          2273305, 1805681, 1803425, 1760433,
#                          1754000, 1740119, 1602386, 1493900,
#                          1350680],
#           "area" : [1572, 891.85, 605.77, 1285, 
#                     105.4, 414.6, 228, 755, 
#                     525.2, 517, 101.9, 310.4, 
#                     181.8]
# }
# city_frame = pandas.DataFrame(
#     cities,
#     columns=["population", "area"],
#     index=cities["name"]
# )
# city_frame["density"] = city_frame["population"] / city_frame["area"]


# fig, ax = matplotlib.pyplot.subplots()

# fig.suptitle("City Statistics")
# ax.set_xlabel("Citites")
# ax.set_ylabel("Population")

# ax_area, ax_density = ax.twinx(), ax.twinx() 

# ax_area.set_ylabel("Area")

# ax_density.set_ylabel("Density")
# ax_density.set_frame_on(True)
# ax_density.patch.set_visible(False)
# rspine = ax_density.spines['right']
# rspine.set_position(('axes', 1.25))

# fig.subplots_adjust(right=0.75)


# city_frame["population"].plot(
#     ax=ax, 
#     style="b-",
#     use_index=True, 
#     rot=90
# )
# city_frame["area"].plot(
#     ax=ax_area, 
#     style="g-",
#     use_index=True, 
#     rot=90
# )
# city_frame["density"].plot(
#     ax=ax_density, 
#     style="r-",
#     use_index=True, 
#     rot=90
# )

# matplotlib.pyplot.show()
















# # plotting bar charts
# data = [100, 120, 140, 180, 200, 210, 214]
# s = pandas.Series(data, index=range(len(data)))
# s.plot(kind="bar")
# matplotlib.pyplot.show()




# # plotting bar charts of DataFrames
# cities = {"name": ["London", "Berlin", "Madrid", "Rome", 
#                    "Paris", "Vienna", "Bucharest", "Hamburg", 
#                    "Budapest", "Warsaw", "Barcelona", 
#                    "Munich", "Milan"],
#           "population": [8615246, 3562166, 3165235, 2874038,
#                          2273305, 1805681, 1803425, 1760433,
#                          1754000, 1740119, 1602386, 1493900,
#                          1350680],
#           "area" : [1572, 891.85, 605.77, 1285, 
#                     105.4, 414.6, 228, 755, 
#                     525.2, 517, 101.9, 310.4, 
#                     181.8]
# }

# city_frame = pandas.DataFrame(
#     cities,
#     columns=["population", "area"],
#     index=cities["name"]
# )

# city_frame["area"] *= 1000

# city_frame.plot(
#     xticks=range(len(city_frame.index)),    # defining the X axis marks
#     use_index=True, 
#     rot=90,                                 # rotate the X axis markings by 90 degrees
#     kind="bar"
# )

# matplotlib.pyplot.show()




# # adding colour to bar charts
# data = [100, 120, 140, 180, 200, 210, 214]
# s = pandas.Series(data, index=range(len(data)))
# s.plot(
#     kind="bar",
#     color= ['b', 'r', 'c', 'y', 'g', 'm']
# )
# matplotlib.pyplot.show()
















# plotting pie charts
fruits = ['apples', 'pears', 'cherries', 'bananas']
series = pandas.Series(
    [20, 30, 40, 10], 
    index=fruits, 
    name='series'
)
series.plot.pie(
    figsize=(6, 6),
    explode=[0.2, 0.02, 0.02, 0.4]         #explode!
)
matplotlib.pyplot.show()