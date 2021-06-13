a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def lessThan5(lista: list[int]) -> list[int]:
    newList: lista[int] = []
    for e in lista:
        if e < 5:
            print(e)
            newList.append(e)
    return newList
newList = lessThan5(a)

newList = [x for x in a if x < 5]
print(newList)