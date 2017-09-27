# an iterator is a container of objects where items cannot be randomly accessed as with a list
# instead, one must sequentially go through the container until it is exhausted

iterator_list = iter( [1,2,3,4] )
iterator_set = iter( {1,2,3,4,4} )
iterator_dict = iter( {"key":"value", "key2":2, "key4":7654} )


for a in iterator_list:
    print(a)
print()
for a in iterator_set:
    print(a)
print()
for a in iterator_dict:
    print(a)
print()

# manual iteration
iterator_list = iter( [1,2,3,4] )
print( next(iterator_list) ) # 1
print( next(iterator_list) ) # 2
print( next(iterator_list) ) # 3
print( next(iterator_list) ) # 4
# print( next(iterator_list) ) #traceback error: StopIteration
print()