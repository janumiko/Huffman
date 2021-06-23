from src.print_to_file import save_to_file
from src.encode import calculate_frequency, create_tree


def main(content: str) -> None:
    frequencies = calculate_frequency(content)
    huffmantree = create_tree(frequencies)

    for key, _ in frequencies:
        print(key + " | " + huffmantree[key])

    print("Do You want to print out the result to a .txt file?")
    response = 'nochoice'

    while response.lower() not in {"yes", "no", "y", "n"}:
        response = input("Please enter yes or no: ")

    if (response.lower() == "yes" or response.lower() == "y"):
        save_to_file(frequencies, huffmantree)


def get_input() -> None:
    while True:
        text = ""
        while text == "":
            text = input("Input text: ")
            if text == "":
                print("Text shouldn't be empty! Try Again!")
        if text.lower == "exit":
            break

        main(text)
