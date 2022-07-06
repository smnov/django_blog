from functools import reduce


def lists(l1, l2):
    sol = list(zip(l1, l2))
    lst = []
    for i in sol:
        lst.append(sum(i))
    print(lst)


lists([2,4,3], [5,6,4])

data = ['1234', '11', '111']
answer = reduce(lambda x,y: int(x) + int(y), data)
print(answer)