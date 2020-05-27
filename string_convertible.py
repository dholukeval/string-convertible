# Provided solution is universal. As it is not strickly mentioned whether the length of both 
# strings are same or different, i came up with the universal solution which works for both 
# the scenario.

def string_convertible(s1,s2):
    list1 = []
    list2 = []
    # Adding two for-loops for two different length of strings
    for i in range(len(s1)):
        list1.append(s1[i])

    for i in range(len(s2)):
        list2.append(s2[i])   

    # Swapping the list name if the length of list1 is smaller than the length of list2 
    if len(list1) < len(list2):
        list1,list2 = list2,list1

    x =[]
    
    for item in list2:                  # iterating over the smaller length of list (here list2). 
        if item in list1:               # We check if each item from list2 is available in list1
            x.append(True)              # we append boolean True to the list x and removed that item from list1 to avoid checking redundant items.
            list1.remove(item)
        elif not list1:                 # if list1 is empty appending True to list x
            x.append(True)
        else:
            x.append(False)
    
    if all(x):                          # if the list x contains all True, print True, else False
        print("True")
    else:
        print("False")
        



if __name__ == '__main__':
    s1,s2 = "qwerty","wqeyrt"
    #s1,s2 = "aab","bba"

    string_convertible(s1,s2)