# Asana is exploring a smart-workload feature designed to streamline task assignment between coworkers. Newly created tasks will be automatically assigned to the team member with the lightest
# workload. For the ith person, the following information is known:
#
# names[i] - their name, a string containing only uppercase and lowercase letters; statuses[i] - their vacation indicator status, which is true if the person is on a vacation, or false otherwise;
# projects[i] - the number of projects they are currently involved in; tasks[i] - the number of tasks assigned to them. If a person's vacation indicator value is set to true, this means they are on
# vacation and cannot be assigned new tasks. Conversely, a vacation indicator value of false means they are open to receive task assignments.
#
# Asana sorts team members according to their availability. Person A has a higher availability than person B if they have fewer tasks to do than B, or if these numbers are equal but A has fewer
# assigned projects than B. Put another way, we can say that person A has a higher availability than person B if their (tasks[A], projects[B]) pair is less than the same pair for B.
#
# Your task is to find the name of the person with the highest availability. It is guaranteed that there is exactly one such person.
#
# Example
#
# For names = ["John", "Martin"], statuses = [false, false],
# projects = [2, 1], and tasks = [16, 5],
# the output should be
# solution(names, statuses, projects, tasks) = "Martin".
#
# The arguments represent information about two team members:
#
# "John", with statuses[0] = false, projects[0] = 2 and tasks[0] = 16; "Martin", with statuses[1] = false, projects[1] = 1 and tasks[1] = 5. Here John and Martin's vacation indicators are both
# false, so both of them are open to new assignments. Martin is only assigned 5 tasks while John is assigned 16, so Martin has the highest availability.
#
# For names = ["John", "Martin"], statuses = [false, true],
# projects = [2, 1], and tasks = [6, 5],
# the output should be
# solution(names, statuses, projects, tasks) = "John".
#
# The arguments stand for the following team members:
#
# "John", with statuses[0] = false, projects[0] = 2 and tasks[0] = 1;
# "Martin", with statuses[1] = true, projects[1] = 1 and tasks[1] = 5.
# In this example Martin cannot be assigned any new tasks because his vacation indicator is true. Therefore, "John" has the highest availability.
#
# For names = ["John", "Martin"], statuses = [false, false],
# projects = [1, 2], and tasks = [6, 6],
# the output should be
# solution(names, statuses, projects, tasks) = "John".
#
# In this case:
#
# "John", with statuses[0] = false, projects[0] = 1 and tasks[0] = 6; "Martin", with statuses[1] = false, projects[1] = 2 and tasks[1] = 6. Both John and Martin's vacation indicators are false,
# and the number of tasks each of them is assigned is 6. However, John is only involved in 1 project, while Martin is involved in 2, meaning that John has the highest availability.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.string names
#
# An array of team members' names.
#
# Guaranteed constraints:
# 1 ≤ names.length ≤ 3.
#
# [input] array.boolean statuses
#
# An array of team members' vacation indicators, where statuses[i] corresponds to the ith team member: if statuses[i] = true, the ith member is on a vacation. Otherwise, they're free to take the task.
#
# Guaranteed constraints:
# statuses.length = names.length.
#
# [input] array.integer projects
#
# An array of the number of projects each team member is involved in, where projects[i] corresponds to the ith team member.
#
# Guaranteed constraints:
# projects.length = names.length,
# 0 ≤ projects[i] ≤ 25.
#
# [input] array.integer tasks
#
# An array of the number of tasks each team member is assigned to, where tasks[i] corresponds to the ith team member.
#
# Guaranteed constraints:
# tasks.length = names.length,
# 0 ≤ tasks[i] ≤ 100.
#
# [output] string
#
# The name of the person with the highest availability.


def solution(names, statuses, projects, tasks):

    # Go through list. Keep track of who is currently the most available person.
    # Once you go through everyone the remaining person should be most available.
    # They guaranteed in the brief there IS a most available person so no need for
    # tiebreakers or worrying about bad inputs/outputs.

    most_available_person_index = None

    # Go by index since we're indexing the same person and their data across multiple lists.
    for person_index in range(len(names)):

        # print("Currently checking index: {}. Most available index currently {}."
        # .format(person_index, most_available_person_index))

        # Base disqualifier, if person is on vacation. Just go to next iteration of loop as they can't be the most available.
        # This could be dangerous in data not guaranteed to have a most available person, since we could return a bad value.
        if statuses[person_index] == True:
            # print("Index was skipped because they were on vacation: {}.".format(person_index))
            continue

        # Empty case, if they're not on vacation and the first person we see. They're the most available!
        # Save their index so you can reference them easily later as names[person_index]
        if most_available_person_index is None:
            # print("Base case. Index is {}. Assigning it to most available".format(person_index))
            most_available_person_index = person_index
            continue

        # Special case with people who have equal number of tasks. Check if they have more projects to see if they are most available.
        if tasks[person_index] == tasks[most_available_person_index]:
            # print("Same tasks case case. Index is {}. Tasks are {}. Checking projects".format(person_index,tasks[person_index]))
            if projects[person_index] < projects[most_available_person_index]:
                # print("Same amount of tasks case. New index had more projects at {} and {}"
                # .format(projects[person_index],projects[most_available_person_index]))
                most_available_person_index = person_index

        # print("New index more tasks base case at current: {} and most: {}"
        # .format(tasks[person_index],tasks[most_available_person_index]))
        # Base case. If current person has more tasks than current most available person. Then they are the most available person.
        if tasks[person_index] < tasks[most_available_person_index]:
            most_available_person_index = person_index

    # At the end of the loop we should have the index of the most available. They want the name of this person so return it.
    return names[most_available_person_index]
