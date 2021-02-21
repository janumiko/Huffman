import src.encode

if __name__ == "__main__":
    text = ""
    while text == "":
        text = input("Input text: ")
        if text == "":
            print("Text shouldn't be empty! Try Again!")

    src.encode.core(text)
    print("Press Enter to exit the program:")
    input()