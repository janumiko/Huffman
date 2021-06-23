import os
from typing import Dict


def save_to_file(content: str, huffman_codes: Dict[str, int]) -> None:
    current_directory = os.getcwd()
    output_directory = os.path.dirname(current_directory)

    output_directory = os.path.join(output_directory, r'output')

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    try:
        with open(os.path.join(output_directory, "output.txt"), "w") as file1:
            file1.write("Character" + " | " + "Code" + '\n')
            for key, _ in content:
                file1.write(key + " | " + huffman_codes[key] + '\n')
    except IOError:
        print("File didn't open, results have not been saved.")
        input()
        raise

    print("Results have been saved succesfully.\n")
