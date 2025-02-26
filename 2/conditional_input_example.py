def get_input():
    return input("Enter your input> ")

def test(provided_text):
    print(provided_text or "You didn't provide any text :(")

def main():
    input_string = get_input()
    test(input_string)
    exit(input_string != None)

main()