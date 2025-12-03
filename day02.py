from itertools import batched

data = [d.split('-') for d in open("data.in").readline().split(',')]
numbers = [str(i) for l, r in data for i in range(int(l), int(r) + 1)]
print(sum(int(i) for i in numbers if i[len(i) // 2:] == i[:len(i) // 2]))
print(sum(int(i) for i in numbers if any(len(set(batched(i, n))) == 1 for n in range(1, len(i) // 2 + 1))))
