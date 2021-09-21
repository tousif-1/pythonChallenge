# Finding all items in multi dimensional list


def index_all (search_list, item):
    indices = list()
    for i in range(len(search_list)):
        if search_list[i] == item:
            indices.append([i])
        elif isinstance(search_list[i], list):
            for index in index_all(search_list[i], item):
                indices.append([i]+index)
    return indices

list1 = [[[1,2,3], 2 , [1,3]], [1,2,3]]

item = int(input("Item to find: "))
result = index_all(list1, item)

print (result)
