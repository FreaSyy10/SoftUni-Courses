num_companions=int(input())
days=int(input())
coins=0

for currnet_day in range(1, days+1):
    if currnet_day % 10 == 0:
        num_companions -=2
    if currnet_day % 15 == 0:
        num_companions += 5
    if currnet_day % 3 == 0:
        coins -= 3*num_companions
    if currnet_day % 5 == 0:
        coins += 20 * num_companions
        if currnet_day % 3 ==0:
            coins -= 2*num_companions


    coins +=50
    coins -= 2 * num_companions
    coins_per_companion = int(coins / num_companions)
print(f"{num_companions} companions received {coins_per_companion} coins each.")

