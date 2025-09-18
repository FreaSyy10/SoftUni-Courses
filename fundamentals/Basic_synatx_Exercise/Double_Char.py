while True:
    text = input()
    if text == "End":
        break
    if text == "SoftUni":
        continue

    result = ""
    for ch in text:
        result += ch * 2
    print(result)