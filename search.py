####how to search an element in list
my_list = [1,6,3,5,3,4] #given list
ele = 1 # searching element
flag =0
for i in my_list:
    if (i == ele) :
        print(ele,' is available in the list')
        flag = 1 # to avaoid to print the both the flags
        break
if (flag == 0):
    print('element not found')

#############################
# another approch using in operator
if(ele in my_list):
    print('element found')
else:
    print("element not found")
