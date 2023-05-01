# # 1
# def binary_search(arr: list, element: None) -> int:
#     left, right = 0, len(arr) - 1
#     index = -1

#     while (left <= right) and (-1 == index):
#         mid = (left + right) // 2
#         if arr[mid] == element:
#             index = mid
#         else:
#             if element < arr[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1

#     return index

# # 2
# def binary_search(sequence, start_element, key):
#     end_element = len(sequence) - 1

#     while start_element <= end_element:
#         middle_element = start_element + (end_element - start_element) // 2
#         if sequence[middle_element] == key:
#             return middle_element
#         elif sequence[middle_element] < key:
#             start_element = middle_element + 1
#         else:
#             end_element = middle_element - 1

#     return -1

# 3
def binary_search(arr: list, element: None) -> int:
    left, right = 0, len(arr) - 1
    index = -1

    while (left <= right) and (-1 == index):
        # mid = (left + right) // 2 # Error
        mid = left + ((right - left) // 2) # Fix
        if arr[mid] == element:
            index = mid
        else:
            if element < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return index


if __name__ == '__main__':  
    sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    
    # 1
    find_element = 24
    result = binary_search(sequence, find_element)
    # result = binary_search(sequence, 0, find_element)
    print(result)
    
    # 2
    find_element = 240
    result = binary_search(sequence, find_element)
    # result = binary_search(sequence, 0, find_element)
    print(result)