weather = input("How's the weather? (sunny/rainy) ")

if weather == 'sunny':
    print("It hot ☀️")
elif weather == 'rainy':
    print("Don't forget your umbrella")
    print(weather)
elif weather == "foggy":
     print("Be careful")
else:
   print("Sorry, I didn't understand")

# Exercise Notes:
# Please remember to NEST your if statements, 
# (don't use 'and' if you know about it)
# check if the user has a tafe lecture
# check if the weather is hot

# If the weather is hot
#   and there is no lecture => GO TO THE BEACH
#   and there IS a lecture => DO NOT GO TO THE BEACH
# Otherwise => print nothing