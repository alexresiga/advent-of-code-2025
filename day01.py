data = [x.strip() for x in open("data.in").readlines()]
part1, part2, op = 50, 50, {"L": -1, "R": 1}
print(sum(1 for d in data if (part1 := (part1 + op[d[0]] * int(d[1:]))) % 100 == 0))
print(sum(1 for d in data for _ in range(int(d[1:])) if (part2 := (part2 + op[d[0]])) % 100 == 0))