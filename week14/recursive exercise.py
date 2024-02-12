# 1. Add a list of numbers recursively
def main():
    list1 = [1, 2, 3, 4, 5]
    print("Add_list: " + str(add_list(list1, 0, 0)))
    
    new_list = []
    print("Reverse_list: " + str(reverse_list(list1, new_list)))

    val = 3
    index = 0
    print("linear search: " + str(recursive_linear_search(list1, val, index)))
    print("binary: " + str(recursive_binary_search(list1, val, index)))


def add_list(list, sum, index):
    # Base case
    # !!! you need to handle '[]' case.
    if index == len(list):
        return sum
    else:
        sum += list[index]
        index += 1
        return add_list(list, sum, index)


# 2. Reverse a list recursively
def reverse_list(list1, new_list):
    # Base case
    if list1 == []:
        # Remember base case is not only for 
        # handling special cases, but also
        # for return desired value in the very end!
        return new_list
    # Recursive case
    else:
        new_list.append(list1[-1])
        # Slice function here create a new list each recursion
        return reverse_list(list1[:-1], new_list)

# 2.2 Version that harder to understand: see Notion.


# 3. Recursive linear search
def recursive_linear_search(l, val, index):
    # Base case
    # !!! you need to handle case that val is not in l
    # !!! when index > len(l) - 1
    if index > len(l) - 1:
        return -1
    if l[index] == val:
        return index
    # Recursive case
    if l[index] != val:
        # !!! index += 1 you can do it in parameter!
        return recursive_linear_search(l, val, index+1)

# 4. Recursive binary search
def binary_search(val, lst, start = 0, end = None):
    if end == None:
        end = len(lst) - 1
    if start > end:
        return -1

    mid = (start + end) // 2
    if lst[mid] == val:
        return mid
    elif lst[mid] > val:
        return binary_search(val, lst, start, mid - 1)
    elif lst[mid] < val:
        return binary_search(val, lst, mid + 1, end)

lst = [1, 2, 3, 4, 5]
print(binary_search(4, lst))

# 5. Recursive bubble sort
def bubble_sort(lst, ind = 0):
    if 
