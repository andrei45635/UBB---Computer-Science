"""
4. Se dă o listă de numere întregi a1,...an, determinați toate sub-secvențele (ordinea elementelor este menținută)
strict crescătoare.

Solutie candidat:
x = (x0, x1, ..., xk), xi e (0, 1, ..., K - 1), K <= N

Conditie consistent:
x = (x0, x1, ..., xk) e consistent daca xi ≠ xj

Conditie solutie:
x = (x0, x1, ..., xk) e solutie daca e consistent si xi < xj, i < j adica elementele sunt in ordinea care apar strict crescatoare
"""

from termcolor import colored


def valid_recursive(list):
    return not (len(list) > 1 and list[len(list) - 2] >= list[len(list) - 1])


def valid_iterative(lst, list):
    for i in range(0, len(lst) - 1):
        if list[lst[i]] >= list[lst[i + 1]]:
            return False
    return True


def backtracking_recursive(solution, list, start):
    solution.append(0)
    for i in range(start, len(list)):
        solution[-1] = list[i]
        if valid_recursive(solution):
            print(solution)
            backtracking_recursive(solution, list, i + 1)
    solution.pop()


def backtracking_iterative(solution, list):
    solution = [-1]
    while len(solution) > 0:
        is_valid = False
        while not is_valid and solution[-1] < len(list) - 1:
            solution[-1] += 1
            is_valid = valid_recursive(solution)
        if is_valid:
            if valid_iterative(solution, list):
                print([list[i] for i in solution])
            solution.append(-1)
        else:
            solution = solution[:-1]


if __name__ == '__main__':
    list = [int(num) for num in input("Input the list: ").split()]
    solution = []
    print(colored("Recursive", "green"))
    backtracking_recursive(solution, list, 0)
    print(colored("\nIterative", "blue"))
    backtracking_iterative(solution, list)
