import os

def save_to_file(content, huffman_codes):
    current_directory = os.getcwd()
    output_directory = os.path.dirname(current_directory)

    output_directory = os.path.join(output_directory, r'output')

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(os.path.join(output_directory,"output.txt"), "w") as file1:
        file1.write("Character" + " | " + "Code" + '\n')
        for (key,code) in content:
            file1.write(key + " | " + huffman_codes[key] + '\n')
