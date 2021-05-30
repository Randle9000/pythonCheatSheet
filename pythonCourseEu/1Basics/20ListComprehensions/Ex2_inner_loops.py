list = [[1,2], [3,4], [5,7]]
a = [element_of_nested_lists for element_of_list in list for element_of_nested_lists in element_of_list]
print(a)

# however for the sake of readability You should use the traditional for loops if nestes is more thant 2levels deep or the logic is too complex

