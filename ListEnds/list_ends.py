
a:  list[int]= [4,3,2,5,6,234,234,32424,64564,64,3,423,342,4]

def both_ends(a: list[int]) -> list[int]:
    b: list[int] = []
    b.append(a[0])
    b.append(a[len(a)-1])
    return b

print(both_ends(a))