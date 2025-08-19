counter = 0

# Count up, using a while loop
while counter < 10:
    print(counter)
    counter = counter + 1

# Count up, using a for loop with a range
for counter in range(-7, 4): 
    print(counter)

# Printing each letter in `apple`
for each_letter in "apple":
    print(each_letter)


# A count-down, with a while loop... but it's infinite
counter = 1
while counter > 0:
    print("blast off!")


# Printing all even numbers from 0 to 16
counter = -1
while counter < 100:
    counter += 1
    if counter % 2 != 0:
        continue # abort loop and go to top
    print(counter)
    if counter == 16:
        print("We found the best number")
        break # abort loop and go to bottom

# The same as above, but we're using a for loop instead
for counter in range(0,100):
    if counter % 2 != 0:
        continue
    print(counter)
    if counter == 16:
        print("We found the best number")
        break
