from print_to_file import save_to_file

def main():
    text = input("Input text: ")
    
    frequencies = calculate_frequency(text)
    huffmantree = create_tree(frequencies)

    for (key,code) in frequencies:
        print(key + " | " + huffmantree[key])
    
    print("Do You want to print out the result to txt file?")
    response = 'nochoice'

    while response.lower() not in {"yes", "no", "y", "n"}:
        response = input("Please enter yes or no: ")

    if (response.lower() == "yes" or "y"):
        save_to_file(frequencies,huffmantree)

    print("Press Enter to exit the program:")
    input()

class NodeTree(object):

    def __init__(self, left_node=None, right_node=None):
        self.left_node = left_node
        self.right_node = right_node

    def child(self):
        return (self.left_node, self.right_node)

    def __str__(self):
        return '%s_%s' % (self.left_node, self.right_node)

def huffman_coding(node, Isleft=True, binary=''):
    codes = dict()
    
    if type(node) is str:
        return {node: binary}
    (l, r) = node.child()

    codes.update(huffman_coding(l, True, binary + '0'))
    codes.update(huffman_coding(r, False, binary + '1'))

    return codes

def calculate_frequency(sourcetext):
    frequency = {}

    for char in sourcetext:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return frequency

def create_tree(pairs):

    while len(pairs) > 1:
        (key1, char1) = pairs[-1]
        (key2, char2) = pairs[-2]
        pairs = pairs[:-2]
        node = NodeTree(key1, key2)
        pairs.append((node, char1 + char2))

        pairs = sorted(pairs, key=lambda x: x[1], reverse=True)

    huffman = huffman_coding(pairs[0][0])
    return huffman

main()
