# this one is easy
# we can do two ways to remove a list:
# 1. Using sets
# 2. Using a loop and construct a list

#easiest way
example_a = [1,2,4,6,32,32,1,45,68,7,8,9,0]
new_a = set(example_a)
newer_a = list(new_a)
print(newer_a)

# a bit harder:

def pruneDuplicates(doubles: list[int]) -> list[int]:
    for i in doubles:
        if doubles.count(i) != 1:
            doubles.remove(i)
    return doubles

print(pruneDuplicates(example_a))
