num1 = int(input())
num2 = int(input())
num3 = int(input())
positive_number= 0


if num1 >= num2 and num1 >= num3:
    positive_number = num1
elif num2 >= num1 and num2>=num3:
    positive_number = num2
else:
    positive_number = num3


print(positive_number)