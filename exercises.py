a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def common_elements(a,b):
    elements_list = []
    for element in a:
        if element in b and element not in elements_list:
            elements_list.append(element)

    return elements_list

print("List Overloap")
print(common_elements(a,b))



#remove duplicates
print("\nRemove Duplicates.")

number_list = [1,1,2,2,3,4,5,5,5,5,6,6,6]

#for loop

def remove_loop(a):
    duplicates_removed = []
    for number in a:
        if number not in duplicates_removed:
            duplicates_removed.append(number)
    return duplicates_removed


def remove_set(a):
    return list(set(a))

print(remove_loop(number_list))
print(remove_set(number_list))


