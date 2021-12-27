# Raw tech screen from Grand Rounds.

# A squad of robotic rovers are to be landed by NASA on a plateau on Mars.
# This plateau, which is curiously rectangular, must be navigated by the rovers so that their on board cameras can get a complete view of the surrounding terrain to send back to Earth.
# A rover's position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.
# In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot.
# 'M' means move forward one grid point, and maintain the same heading.
# Assume that the square directly North from (x, y) is (x, y+1).
# Input:
# The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.
# The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau.
# The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.
# Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.
# Output:
# The output for each rover should be its final co-ordinates and heading.
# Test Input:
# 5 5 (Top right of the grid)
# 1 2 N (Initial Position , (X,Y, Facing))
# LMLMLMLMM (Turn, move, turn move)
# 3 3 E
# MMRMMRMRRM
# Expected Output:
# 1 3 N
# 5 1 E

# N -> Feedback from proctor. Could get rid of ugly conditionals and use globals, hashmaps and dicts to store direction and vectors.
# N -> You initially tried this with numpy but were worried it would take up time. So simple and fast it is.


# Given coords for end of a plateau and instructions to move rover, return end coordinates and facing direction of rover.
def rover_position(plateau_end, initial_position, instructions):
    # Parse initial position and direction from the input.
    initial_pos_list = initial_position.split()
    current_pos_coord = (int(initial_pos_list[0]), int(initial_pos_list[1]))
    current_direction = initial_pos_list[2]

    # print("Raw list is: " + str(initial_pos_list))
    # print("The initial position of the rover is: " + str(initial_pos_list))
    # print("The initial direction of the rover is " + str(current_direction))

    # Test one move
    # test_move = directional_move(current_direction, current_pos_coord)
    # print("My first rover moved north and is now at: " + str(test_move))

    # Test one turn left and one turn right.
    # right_turn = rover_turn(current_direction, "R")
    # print("Testing a right turn, I should be facing east: " + str(right_turn))
    # left_turn = rover_turn(right_turn, "L")
    # print("Testing a left turn, I should be back facing north: " + str(left_turn))

    # Initially you should error check to make sure your rover is on the grid and while moving make sure it doesn't move off the grid.

    # print("Before the for loop")

    # Go through each instruction and keep track of the rover.
    print("Instructions look like this: " + instructions)
    for command in instructions:
        # print("The command is: " + str(command))

        if command == "L":
            current_direction = rover_turn(current_direction, "L")
        if command == "R":
            current_direction = rover_turn(current_direction, "R")
        if command == "M":
            current_pos_coord = directional_move(current_direction, current_pos_coord)

        print("Instruction parsed, the rover is currently facing: " + str(current_direction) + " and is at: " + str(current_pos_coord))


# Given orientation and a turn command passes back new orientation.
def rover_turn(current_direction, turn_command):
    if turn_command == "L":
        if current_direction == "N":
            return "W"
        if current_direction == "S":
            return "E"
        if current_direction == "E":
            return "N"
        if current_direction == "W":
            return "S"
        else:
            return "Bad direction input, must be north, south, east, or west."
    if turn_command == "R":
        if current_direction == "N":
            return "E"
        if current_direction == "S":
            return "W"
        if current_direction == "E":
            return "S"
        if current_direction == "W":
            return "N"
        else:
            return "Bad direction input, must be north, south, east, or west."
    else:
        return "Turn command must be left or right."


# Translate direction to vector coordinate. Pass direction and current coordinate, pass back coordinate after moving.
def directional_move(direction, current_position):
    if direction == "N":
        return current_position[0], current_position[1] + 1
    if direction == "S":
        return current_position[0], current_position[1] - 1
    if direction == "E":
        return current_position[0] + 1, current_position[1]
    if direction == "W":
        return current_position[0] - 1, current_position[1]
    else:
        return "Not a valid direction."


# Example 1
# rover_position("5 5", "1 2 N", "LMLMLMLMM")

# Example 2
rover_position("5 5", "3 3 E", "MMRMMRMRRM")
