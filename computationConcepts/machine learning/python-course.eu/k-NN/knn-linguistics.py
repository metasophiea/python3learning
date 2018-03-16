import numpy
from collections import Counter

def distance(instance1, instance2):
    instance1 = numpy.array(instance1) #cleaning
    instance2 = numpy.array(instance2) #cleaning
    
    return numpy.linalg.norm(instance1 - instance2)
def LevenshteinDistance_Recursive(s, t):
    if   s == "": return len(t)
    elif t == "": return len(s)

    cost = 0 if s[-1] == t[-1] else 1
       
    return min(
        [
            LevenshteinDistance_Recursive(s[:-1], t)+1,
            LevenshteinDistance_Recursive(s, t[:-1])+1, 
            LevenshteinDistance_Recursive(s[:-1], t[:-1]) + cost
        ]
    )
    

def get_neighbours(training_set, labels, test_instance, k, distance=distance):
    distances = []

    for index in range(len(training_set)):
        # we compare the 'test_instance' with every item in the 'training_set', 
        # the resulting data is placed in a tuple, which is appended into a list
        distances.append(
            (
                training_set[index],                            # first, the data iteslf
                distance(test_instance, training_set[index]),   # the calculated/compared distance
                labels[index]                                   # the corresponding flower type
            )
        )

    # sorts the list of distances, and returns the 'k' smallest
    distances.sort(key=lambda x: x[1]) # (the sort 'key' is number 1 in the sublists of this list which we are sorting)
    return distances[:k]

def vote_distance_weights(neighbours, all_results=True):
    # neighbours = a list of tuples, which contain numbers which represent:
    #   the item's data iteslf | the calculated/compared distance | the item's flower type
    class_counter = Counter()

    for a in range(len(neighbours)):
        class_counter[neighbours[a][2]] += 1/(neighbours[a][1]**2 + 1)
        # what occurs here, is that each item in the set is being incremented
        # by a value proportional to the distance squared. Obviously, the futher
        # away the item is; the lower it's contribution

    labels, votes = zip(*class_counter.most_common())

    winner_label = class_counter.most_common(1)[0][0]

    if all_results:
        # this section will return all the types and their weighted likelyhood
        # it does this be getting the total number of elements, then dividing
        # each vote count in the 'class_counter' by this
        total = sum(class_counter.values())
        for key in class_counter:
             class_counter[key] /= total
        return winner_label, class_counter.most_common()
    else:
        return winner_label, class_counter.most_common(1)[0][1] / sum(votes)








# in this little experiment; we're going to take city names and compare them to a list of 
# city names. We will use the LevenshteinDistance function to determime the distance between 
# two words; then the nearest neighbour algorithm will dirtermine which word from the list
# is most likely the word in the test list

cities = []
with open("city_names.txt") as fh:
    for line in fh:
        city = line.strip()
        if " " in city:
            cities.append(city.split()[0])
        cities.append(city)

testList = ["Freiburg", "Frieburg", "Freiborg", "Hamborg", "Sahrluis", 'Doblun', 'Wancovre']

nearsetLimit = 3
for city in testList:
    neighbours = get_neighbours(
        cities, 
        cities,  
        city, 
        nearsetLimit,
        distance=LevenshteinDistance_Recursive
    )

    result = vote_distance_weights(neighbours)
    print('input:', city)
    print('\tI think you tried to spell:', result[0], '(I\'m', str(round(result[1][0][1]*100,2)) + '% sure)')
    for a in range(nearsetLimit-1):
        print('\t(perhaps "' + result[1][a+1][0] + '"? I\'m only ' + str(round(result[1][a+1][1]*100,2)) + '% sure about that)')
