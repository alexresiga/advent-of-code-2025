def j(d, needed):
    need_to_remove = len(d) - needed
    while need_to_remove > 0:
        for i in range(len(d) - 1):
            if d[i] < d[i + 1]:
                d = d[:i] + d[i + 1:]
                break
        need_to_remove -= 1
    return int(d[:needed])


data = [x.strip() for x in open("data.in").readlines()]
print(sum(j(d, 2) for d in data))
print(sum(j(d, 12) for d in data))
