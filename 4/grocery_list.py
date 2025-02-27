groceries = {}

while True:
    raw_input = input("Item and quantity? ")

    if raw_input == "":
        break
    else:
        split_input = raw_input.split()

        if len(split_input) != 2:
            print("Invalid input!")
            continue
        else:
            try:
                name = split_input[0].lower()
                groceries[name] = groceries.get(name, 0) + int(split_input[1])
            except: 
                print("Invalid input!")
print(groceries)


