def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse downwards
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse from right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # Traverse upwards
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

def check_spiral_sum(matrix):
    spiral_sum = sum(spiral_order(matrix))
    row_sum = sum(sum(row) for row in matrix)
    return spiral_sum == row_sum

# Example usage
matrix = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]

print("Spiral order:", spiral_order(matrix))
print("Spiral sum equals total sum?", check_spiral_sum(matrix))
