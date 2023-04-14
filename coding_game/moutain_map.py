# The task here is to print the ASCII representation of n mountains where the height of each mountain is given.

# Input: n list integers for the height of each mountain
# Output: An ASCII representation of the mountain where each rise in the mountain is represented by '/' and fall by '\'
# (Output lines shall not contain trailing spaces)

# Constraints
# 0<n<15
# 0<height<15
# (every mountain's base starts on the bottom-most line)

# Example:
# Input               Output
# [1, 2, 1]              /\
#                     /\/  \/\


def mountain_map(height):
    m, n = max(height), sum(height) * 2
    mountain_matrix = [[" " for _ in range(n)] for _ in range(m)]

    col_start = 0
    for h_id in range(len(height)):
        col_end = col_start + height[h_id] * 2
        peek_id = [col_start + height[h_id] - 1, col_start + height[h_id]]
        i = m - 1
        
        for j in range(col_start, col_end):
            if j <= peek_id[0]:
                mountain_matrix[i][j] = "/"
                if j < peek_id[0]:
                    i -= 1
            if j >= peek_id[1]:
                mountain_matrix[i][j] = "\\"
                i += 1

        col_start = col_end
    
    return mountain_matrix


def draw_mountain(height, mountain):
    res = ""
    # max_height_id = height.index(max(height))
    # limit = 2 * sum(height[:max_height_id]) + height[max_height_id] + 1

    for i in range(len(mountain)):
        for j in range(len(mountain[0])):
            res += mountain[i][j]
            if j == len(mountain[0]) - 1:
                res += "\n"

    return res.rstrip()


if __name__ == "__main__":
    print()
    height = [1, 2, 1, 10, 4]
    mountain = mountain_map(height)
    print(draw_mountain(height, mountain))