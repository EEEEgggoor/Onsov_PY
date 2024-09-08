n = int(input())
tickets = [input() for _ in range(n)]

slov = {}

for i in range(len(tickets)):
    ryad, place, money = tickets[i].split()
    key = (ryad, place)
    if key not in slov:
        slov[key] = set()
    slov[key].add(money)

for (ryad, place), count_money in slov.items():
    print(f"{ryad} {place} - {len(count_money)}")