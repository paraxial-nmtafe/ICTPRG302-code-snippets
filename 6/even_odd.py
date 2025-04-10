try:
    number = int(input("Enter a whole number: "))
except:
    print("Enter a whole number please.")
    exit(1)

answer = "even" if number % 2 == 0 else "odd"

print(answer.upper())
