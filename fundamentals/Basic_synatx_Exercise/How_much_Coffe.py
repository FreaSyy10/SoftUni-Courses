coffe_you_need = 0
lower_case = 1
upper_case = 2

while True:
    command=input()
    if command == "END":
        break
    if command == "coding":
        coffe_you_need+=lower_case
    elif command == "CODING":
        coffe_you_need+=upper_case
    if command == "dog" or command == "cat":
        coffe_you_need+=lower_case
    elif command == "DOG" or command == "CAT":
        coffe_you_need+=upper_case
    if command == "movie":
       coffe_you_need += lower_case
    elif command == "MOVIE":
        coffe_you_need += upper_case

if coffe_you_need <= 5:
    print(coffe_you_need)
else:
    print("You need extra sleep")