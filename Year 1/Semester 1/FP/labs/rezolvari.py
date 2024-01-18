def lista_egale(lst1):
    """
       Primeste o lista de numere pentru care returneaza
       cea mai lunga secventa de numere egale
    """
    lmax = -1
    numar = 0
    if len(lst1) < 3:
        return False
    for curent in lst1:
        if lst1.count(curent) > lmax:
            lmax = lst1.count(curent)
            numar = curent
    print(' '.join([str(numar)] * lmax))
    return ' '.join([str(numar)] * lmax)


def test_egale():
    """
    functie test pt lista_egale
    """
    assert lista_egale([1, 2, 2, 2, 4, 5, 6]) == '2 2 2'
    assert lista_egale([2, 1]) == False
    assert lista_egale([1, 1, 1, 1, 1, 2, 2, 2, 2]) == '1 1 1 1 1'
    assert lista_egale([-1, -1, -1, -1, -1, 2, 4, 2, 2, 4, 5, 2]) == '-1 -1 -1 -1 -1'


def P13(arr):
    """
    Metoda ce primeste o lista si returneaza sublista cea mai lunga care are suma elementelor egala cu 5
    :param arr: lista
    :return: cea mai lunga sublista care are suma elementelor egala cu 5
    """
    n = len(arr)
    max_len = 0
    end = -1
    sum_indices = {}
    current_sum = 0

    for i in range(n):
        current_sum += arr[i]
        if current_sum == 5:
            max_len = i + 1
            end = i
        elif current_sum - 5 in sum_indices:
            if i - sum_indices[current_sum - 5] > max_len:
                max_len = i - sum_indices[current_sum - 5]
                end = i
        if current_sum not in sum_indices:
            sum_indices[current_sum] = i

    longest = arr[end - max_len + 1: end + 1]
    print(longest)
    return longest


def test_suma_elem_cinci():
    assert P13([2, 3, 4, 3, 3]) == '[2, 3]'
    assert P13([1, 2, 3, 4, 5]) == '[2, 3]'
    assert P13([1, 1, 1, 1, 1, 1, 6, 18]) == '[1, 1, 1, 1, 1]'
    assert P13([2, 4, 16, 3]) == '[]'


def same_digits(a, b):
    """
    Metoda ce verifica daca doua numere au aceleasi cifre
    :param a: primul numar
    :param b: al doilea numar
    :return: True daca cele doua numere au aceleasi cifre, False altfel
    """
    if sorted(set(str(a))) == sorted(set(str(b))):
        return True
    return False


def P16(arr):
    """
    Metoda ce primeste o lista si returneaza cea mai lunga sublista cu elemente care are elemente cu aceleasi cifre in baza 10
    :param arr: lista
    :return: cea mai lunga sublista cu elemente care are elemente cu aceleasi cifre in baza 10
    """
    longest = []

    for i in range(len(arr)):
        current = [arr[i]]
        for j in range(i + 1, len(arr)):
            if same_digits(arr[i], arr[j]):
                current.append(arr[j])
        if len(current) > len(longest):
            longest = current
    if len(longest) == 0:
        print("Nu exista")
    print(longest)
    return longest


def test_baza_zece():
    assert(P16([1211, 121, 112, 15, 14, 144, 13])) == '[1211, 121, 112]'
    assert(P16([1, 2, 3, 4, 5])) == 'Nu exista'
    assert(P16([1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 2, 2, 2])) == '[2, 2, 2, 2, 2, 2]'


def test_munte():
    """
    functie test pt lista_munte
    """
    assert lista_munte([2, 3, 4, 3, 2]) == True
    assert lista_munte([1, 2]) == False
    assert lista_munte([1, 2, 3, 4, 5, 6, 7, 2, 4, 5, 3]) == False
    assert lista_munte([-4, -3, -2, -1, 0, -1, -2, -3, -4]) == True


def lista_munte(lst1):
    """
    Primeste o lista de numere pentru care returneaza
    cea mai lunga secventa de tip munte
    """
    if len(lst1) < 3:
        return False
    curent = 1
    while curent < len(lst1) and lst1[curent] > lst1[curent - 1]:
        curent += 1
    if curent == 1 or curent == len(lst1):
        return False
    while curent < len(lst1) and lst1[curent] < lst1[curent - 1]:
        curent += 1
    return curent == len(lst1)
