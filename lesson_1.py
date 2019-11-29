# lists:collection of items tht are ordered ,changeable.
# dictianary:collection of items tht are unordered ,changeable and indexed.
# tuple:collection of items tht are ordered ,unchangeable.
# set:collection of items tht are unordered ,unchangeable.
#  list in python
#  varaiblename = ['item1','item2','item3']
shoppinglist =['toothpast','cake','tissue paper']
# accessing item in alist
item0 = shoppinglist[0]
print(item0)
# slicing a list
print(shoppinglist[0:2])
print(shoppinglist[:4])
print(shoppinglist)
print(type(shoppinglist))
print (type(2))
print(type(2.4))
# changing values in alist
# variablename[index] = newitem
shoppinglist[0] ='book'
print(shoppinglist)
# list lenth
print(len (shoppinglist))
 # list method
 # 1 append():adds an item in a list at the end.
# 2insert(): adds an item in a specific index
# 3 pop():removes the last item in the list.
# 4delattr():delets the whole list
# 5 clear():removes items in the list/returns an empty list.
# 6 extends :adds more than one item in a list.
shoppinglist.append('toothpest')
print(shoppinglist)
shoppinglist.insert(1,'milk')
print(shoppinglist)
shoppinglist.pop()
print(shoppinglist)
# del shoppinglist[3]
print(shoppinglist)
# del shoppinglist
print(shoppinglist)
# assignment:research on clear and extend list methods
# checking if an item exists in a list:
if 'cakes' in shoppinglist:print('cake present in the list')
else:
    print('cakes is not in the list')

