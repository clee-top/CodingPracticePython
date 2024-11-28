
# This problem crops up a LOT.

import numpy as np


# Solution for minimum paths in arrays -> https://leetcode.com/problems/minimum-path-sum/solutions/3345656/python-java-c-simple-solution-easy-to-understand/
def solution(first_array, second_array):

    # Shove the problem into a grid, since we have an algorithm for this.
    grid = np.array([first_array, second_array])

    # Initialize the length of your columns and rows so we can loop over them appropriately.
    num_rows, num_columns = len(grid), len(grid[0])

    # For every row, calculate the best route. Dynamic programming style.
    for grid_element in range(1, num_rows):
        grid[grid_element][0] += grid[grid_element-1][0]

    for grid_element in range(1, num_columns):
        grid[0][grid_element] += grid[0][grid_element-1]

    for grid_element in range(1, num_rows):
        for column_entry in range(1, num_columns):
            grid[grid_element][column_entry] += min(grid[grid_element-1][column_entry], grid[grid_element][column_entry-1])

    # Bottom right of the grid, where the problems usually tell you to go. But you could put any entry here depending on the prompt.
    return grid[-1][-1]


# print(solution([3, 4, 6], [6, 5, 4]))
# print(solution([1, 2, 1, 1, 1, 4], [1, 1, 1, 3, 1, 1]))
# print(solution([-5, -1, -3], [-5, 5, -2]))

testcases = [
    {"name": "test1", "input": [[3, 4, 6], [6, 5, 4]], "expected": 16},
    {"name": "test2", "input": [[1, 2, 1, 1, 1, 4], [1, 1, 1, 3, 1, 1]], "expected": 8},
    {"name": "test3", "input": [[-5, -1, -3], [-5, 5, -2]], "expected": -11}
]

for current_case in testcases:
    current_case_result = solution(current_case["input"][0], current_case["input"][1])
    assert current_case_result == current_case["expected"], f"{current_case['name']} failed, actual = {current_case_result}, expected = {current_case['expected']}"