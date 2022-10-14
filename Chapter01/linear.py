def linear_search(input_list, element):
    for index, value in enumerate(input_list):
        print(index, value)
        if value == element:
            return index

    return -1

input_list = [3, 4, 1, 6, 14]
element = 4
print("index position for the element x is:", linear_search(input_list, element))

def squares(n):
    squared = []
    for item in n:
        squared.append(item**2)
    return squared

input_list = [3, 4, 1, 6, 14]
print(squares(input_list))
