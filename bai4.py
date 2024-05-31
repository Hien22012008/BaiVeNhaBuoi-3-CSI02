def diagonal_sums(matrix):
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    n = len(matrix)
    
    for i in range(n):
        primary_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][n-i-1]
    
    return (primary_diagonal_sum, secondary_diagonal_sum)

# Ví dụ sử dụng
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
output = diagonal_sums(input_matrix)
print(output)