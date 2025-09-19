num_interations=int(input())

for first_symbol in range(97,97+num_interations):
    for second_symbol in range(97, 97 + num_interations):
        for third_symbol in range(97, 97 + num_interations):
            print(chr(first_symbol),chr(second_symbol),chr(third_symbol))
