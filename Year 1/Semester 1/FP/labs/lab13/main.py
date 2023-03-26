from backtracking_recursiv import BackRec
from backtracking_iterativ import back_iter
from backtrack_recursive import back_rec

if __name__ == '__main__':
    #lista = [0,1,-1,1,-1,0,0,1,-1,1,0,1]
    print('-----recursiv----\n')
    back_rec([], int(input("Introduceti dimensiunea dorita: ")))
    #BackRec(lista, 0, [])
    print("-----iterativ-----\n")
    back_iter([], int(input("Introduceti dimensiunea dorita: ")))