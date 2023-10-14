# approch1 slicing techniq
mylist = [4,8,2,10,15,16]
mylist_copy = mylist[:]
print(mylist_copy)
# by using extend method
mylist = [4,8,2,10,15,16]
mylist_copy = [] # if it have any value it will extend with those value
mylist_copy.extend(mylist)
print(mylist_copy)
# by using list() method
mylist = [4,8,2,10,15,16]
mylist_copy = list(mylist)
print(mylist_copy)
# by using copy() method
mylist = [4,8,2,10,15,16]
mylist_copy = mylist.copy()
print(mylist_copy)
# by using list comprehention # have to write the loop statement
mylist = [4,8,2,10,15,16]
mylist_copy= [i for i in mylist]
    
    



