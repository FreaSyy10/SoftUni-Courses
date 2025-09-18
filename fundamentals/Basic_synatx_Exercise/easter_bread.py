budget= float(input())
price_kg_flour=float(input())

price_pack_eggs= 0.75 * price_kg_flour
price_l_milk=1.25*price_kg_flour
one_bread_milk= price_l_milk /4

loaves=0
money_left=budget
colored_eggs=0

bread_cost= price_pack_eggs +price_kg_flour+one_bread_milk

while money_left >= bread_cost:
    loaves += 1
    money_left -= bread_cost
    colored_eggs += 3

    if loaves % 3 == 0:
        colored_eggs -= (loaves - 2)
print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left:.2f}BGN left.")
