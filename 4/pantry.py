pantry = ["apple", "ham"]

print(pantry)

while True:
    crate = input("Do you have anything else? ")
    if crate.lower() == "no":
        break
    pantry.append(crate)
    print("The pantry has things in it:", pantry)
    
    tub = input("Do you want anything out of the pantry?")



