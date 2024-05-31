def find_extra_element(list1, list2):
    # Tính tổng của tất cả các phần tử trong mỗi list
    sum_list1 = sum(list1)
    sum_list2 = sum(list2)
    
    # Phần tử bất thường sẽ là hiệu giữa hai tổng
    extra_element = abs(sum_list1 - sum_list2)
    return extra_element

# Ví dụ sử dụng
list1 = [1, 4, 5, 7, 9]
list2 = [7, 4, 1, 9]
output = find_extra_element(list1, list2)
print(output)