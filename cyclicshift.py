def solution(elements):
    sorted_elements = elements.copy()
    sorted_elements.sort()

    possible_solutions = {}

    if sorted_elements == elements:
        return 0

    for i in range(len(elements)):
        elements.append(elements.pop(0))
        possible_solutions[tuple(elements)] = i + 1

    if possible_solutions.__contains__(tuple(sorted_elements)):
        return possible_solutions.get(tuple(sorted_elements))

    return -1
