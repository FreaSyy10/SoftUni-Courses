n = int(input())


for i in range(n):
    numbers = int(input())
    result = ""
    if numbers == 88:
        result="Hello"
    elif numbers == 86:
        result="How are you?"
    elif numbers < 88:
        result="GREAT!"
    elif numbers>88:
        result="Bye."
    print(result)