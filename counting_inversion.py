
def merge(list1, list2):    
    if list1 is None:
        list1 = []
    if list2 is None:
        list2 = []
   
    global inv
    
    m = len(list1)+len(list2)
    
    list = [0 for i in range(m)]
    for k in range(m):
        if not list1:
            list[k] = list2[0]
            list2 = list2[1:]
        elif not list2:
            list[k] = list1[0]
            list1 = list1[1:]
        elif list1[0] <= list2[0]:
            list[k] = list1[0]
            list1 = list1[1:]
        else:
            list[k] = list2[0]
            list2 = list2[1:]
            inv = inv + len(list1)
            
    return list

def split(list):
    x = int(round(len(list)/2,0))
    list1 = list[:x]
    list2 = list[x:]
    return list1, list2

def sort(list):
    if len(list) == 1:
        return list
    else:
        list1, list2 = split(list)
        return merge(sort(list1), sort(list2))

inv = 0
sort([3, 2, 2, 4, 9, 8, 7])
print("Number of conter inversion = ", inv)