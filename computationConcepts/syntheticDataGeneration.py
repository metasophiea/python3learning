import weightedRandomChoice

#   Upon the topic of generating synthetic data; we first look at a random name generator.
# This code simply slaps together two random selections from the 'firstnames' and 'lastnames'
# and adds them to a list.
firstnames = ["John", "Eve", "Jane", "Paul", "Frank", "Laura", "Robert", "Kathrin", "Roger", "Simone", "Bernard", "Sarah", "Yvonne"]
surnames = ["Singer", "Miles", "Moore", "Looper", "Rampman", "Chopman", "Smiley", "Bychan", "Smith", "Baker", "Miller", "Cook"]
peopleCount = 15
people = []

while len(people) < peopleCount:
    people.append( " ".join( weightedRandomChoice.cartesian_choice(firstnames, surnames) ) )
print("These are the people:")
print(people)
print()








#   Next we look at a recreation of the previous code, but this time with a generator
# this one comes with extra functionality, such as the ability to assign weights to
# the data, specify a format output function and decide wether you only want unique 
# names to be generated (though the way this is implemented, if one were to generate
# enough 'unique' values, eventually the generator will run out of possibilities and
# hang up) 

firstnames_weights = [8/24, 4/24, 2/24, 1/24, 1/24, 1/24, 1/24, 1/24, 1/24, 1/24, 1/24, 1/24]
surnames_weights  = [8/24, 4/24, 2/24, 1/24, 1/24, 1/24, 1/24, 1/24, 1/24, 1/24, 1/24, 1/24]

def gen(data, dataWeights=None, formattingFunction=None, onlyUnique=False):
    pastNames = []

    def getName():
        if dataWeights == None:
            name = weightedRandomChoice.cartesian_choice( *data ) # (the asterisk character unpacks the tuple)
        else:
            inputData = []
            for a in range(len(data)):
                inputData.append( (data[a],dataWeights[a]) )
            name = weightedRandomChoice.weighted_cartesian_choice( *inputData ) 
        return name

    while True:
        name = getName()
        if onlyUnique:
            while name in pastNames:
                name = getName()
            pastNames.append(name)

        if formattingFunction: 
            yield formattingFunction(name)
        else: 
            yield name

names = gen(
    (firstnames, surnames),
    (firstnames_weights, surnames_weights),
    lambda x: " ".join(x),
    True
)

for a in range(15):
    print(next(names), end="   ")
print()








#   Another exmaple of the use of the generator function; this time to create random
# descriptions of wines.
body = ['light-bodied', 'medium-bodied', 'full-bodied']
adverbs = ['appropriately', 'assertively', 'authoritatively', 'compellingly', 'completely', 'continually', 'conveniently', 'credibly', 'distinctively', 'dramatically', 'dynamically', 'efficiently', 'energistically', 'enthusiastically', 'fungibly', 'globally', 'holisticly', 'interactively', 'intrinsically', 'monotonectally', 'objectively', 'phosfluorescently', 'proactively', 'professionally', 'progressively', 'quickly', 'rapidiously', 'seamlessly', 'synergistically', 'uniquely']
noun = ['aroma', 'bouquet', 'flavour']
aromas = ['angular', 'bright', 'lingering', 'butterscotch', 'buttery', 'chocolate', 'complex', 'earth', 'flabby', 'flamboyant', 'fleshy', 'flowers', 'food friendly', 'fruits', 'grass', 'herbs', 'jammy', 'juicy', 'mocha', 'oaked', 'refined', 'structured', 'tight', 'toast','toasty', 'tobacco', 'unctuous', 'unoaked', 'vanilla', 'velvetly']
          
def describe(data):
    body, adv, adj, noun, adj2 = data
    format_str = "This wine is %s with a %s %s %s leading to a lingering %s finish!"
    return format_str % (body, adv, adj, noun, adj2) 

criticism = gen(
    (body, adverbs, aromas, noun, aromas),
    None,
    describe,
    True
)

for a in range(15):
    print("wine",str(a)+":")
    print(next(criticism))
    print()
print()














#   This final example produces a table of personnel data, complete with unique ID number, 
# country of origin, profession, and a name typical of someone from their country
w_firstnames = {
    "France" : [ ("Marie", 10), ("Thomas", 10), ("Camille", 10), ("Nicolas", 9),("Léa", 10), ("Julien", 9), ("Manon", 9), ("Quentin", 9), ("Chloé", 8), ("Maxime", 9), ("Laura", 7), ("Alexandre", 6),("Clementine", 2), ("Grégory", 2), ("Sandra", 1), ("Philippe", 1) ],
    "Switzerland": [ ("Sarah", 10), ("Hans", 10), ("Laura", 9), ("Peter", 8),("Mélissa", 9), ("Walter", 7), ("Océane", 7), ("Daniel", 7), ("Noémie", 6), ("Reto", 7), ("Laura", 7), ("Bruno", 6),("Eva", 2), ("Urli", 4), ("Sandra", 1), ("Marcel", 1) ],
    "Germany": [ ("Ursula", 10), ("Peter", 10), ("Monika", 9), ("Michael", 8),("Brigitte", 9), ("Thomas", 7), ("Stefanie", 7), ("Andreas", 7), ("Maria", 6), ("Wolfgang", 7), ("Gabriele", 7), ("Manfred", 6),("Nicole", 2), ("Matthias", 4), ("Christine", 1), ("Dirk", 1) ],
    "Italy" : [ ("Francesco", 20), ("Alessandro", 19), ("Mattia", 19), ("Lorenzo", 18),("Leonardo", 16), ("Andrea", 15), ("Gabriele", 14), ("Matteo", 14), ("Tommaso", 12), ("Riccardo", 11), ("Sofia", 20), ("Aurora", 18),("Giulia", 16), ("Giorgia", 15), ("Alice", 14), ("Martina", 13) ]
}
w_surnames = { 
    "France" : [ ("Matin", 10), ("Bernard", 10), ("Camille", 10), ("Nicolas", 9), ("Dubois", 10), ("Petit", 9), ("Durand", 8), ("Leroy", 8), ("Fournier", 7), ("Lambert", 6), ("Mercier", 5), ("Rousseau", 4), ("Mathieu", 2), ("Fontaine", 2), ("Muller", 1), ("Robin", 1) ],
    "Switzerland": [ ("Müller", 10), ("Meier", 10), ("Schmid", 9), ("Keller", 8) ,("Weber", 9), ("Huber", 7), ("Schneider", 7), ("Meyer", 7), ("Steiner", 6), ("Fischer", 7), ("Gerber", 7), ("Brunner", 6), ("Baumann", 2), ("Frei", 4), ("Zimmermann", 1), ("Moser", 1) ],
    "Germany": [ ("Müller", 10), ("Schmidt", 10), ("Schneider", 9), ("Fischer", 8), ("Weber", 9), ("Meyer", 7), ("Wagner", 7), ("Becker", 7), ("Schulz", 6), ("Hoffmann", 7), ("Schäfer", 7), ("Koch", 6), ("Bauer", 2), ("Richter", 4), ("Klein", 2), ("Schröder", 1) ],
    "Italy" : [ ("Rossi", 20), ("Russo", 19), ("Ferrari", 19), ("Esposito", 18) ,("Bianchi", 16), ("Romano", 15), ("Colombo", 14), ("Ricci", 14), ("Marino", 12), ("Grecco", 11), ("Bruno", 10), ("Gallo", 12), ("Conti", 16), ("De Luca", 15), ("Costa", 14), ("Giordano", 13), ("Mancini", 14), ("Rizzo", 13), ("Lombardi", 11), ("Moretto", 9) ]
}

# separate names and weights
countryGen = {}

for country in w_firstnames:
    # for each country, recalculate the weights to be fractions relative to 
    # the sum of the weights for the names in that country
    # ie. 1 2 3 => 1/6 1/3 1/2

    firstnameStrings, firstnameWeights = zip(*w_firstnames[country])
    surnameStrings,   surnameWeights   = zip(*w_surnames[country])

    firstnameWeightsSum = sum(firstnameWeights)
    surnameWeightsSum   = sum(surnameWeights)

    firstnameWeights = [ x / firstnameWeightsSum for x in firstnameWeights]
    surnameWeights   = [ x / surnameWeightsSum   for x in surnameWeights]

    w_firstnames[country] = (firstnameStrings, firstnameWeights)
    w_surnames[country]   = (surnameStrings,   surnameWeights)

    # produce a 'gen' generator which uses all the data collected above
    countryGen[country] = gen( 
        (firstnameStrings, surnameStrings),
        dataWeights=(firstnameWeights, surnameWeights),
        formattingFunction=lambda x: " ".join(x),
        onlyUnique=False
    )

nation_prob = [
    ("Germany", 0.3), 
    ("France", 0.4), 
    ("Switzerland", 0.2),
    ("Italy", 0.1)
]
profession_prob = [
    ("Medical Aid", 0.3), 
    ("Social Worker", 0.6), 
    ("Security Aid", 0.1)
]

helpers = []
identifier = 1
for _ in range(200):
    # based on their weightings; select a country and profession
    country, profession = weightedRandomChoice.weighted_cartesian_choice( zip(*nation_prob), zip(*profession_prob) )

    # get the next unique ID number
    uid = "{id:05d}".format(id=identifier)
    
    # create a helper, from this country with this profession with this uid, and produce a name
    # for this person with the generator of their country
    helpers.append((uid, country, next(countryGen[country]), profession ))
    identifier += 1
    
for helper in helpers:
    print(helper)
