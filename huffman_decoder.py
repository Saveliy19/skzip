class HuffmanNode:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.left = None
        self.right = None

class Decoder:

    @staticmethod
    def __rebuild_huffman_tree(codebook):
        root = HuffmanNode()
        for symbol, code in codebook.items():
            node = root
            for bit in code:
                if bit == '0':
                    if not node.left:
                        node.left = HuffmanNode()
                    node = node.left
                else:
                    if not node.right:
                        node.right = HuffmanNode()
                    node = node.right
            node.symbol = symbol
        return root

    @staticmethod
    def __decode_bits(encoded_bytes, padding, huffman_tree):
        bitstring = ''.join(f'{byte:08b}' for byte in encoded_bytes)
        if padding:
            bitstring = bitstring[:-padding]

        decoded = []
        node = huffman_tree
        for bit in bitstring:
            node = node.left if bit == '0' else node.right
            if node.symbol is not None:
                decoded.append(node.symbol)
                node = huffman_tree
        return decoded

    @staticmethod
    def decode(alphabet, padding, codebook, encoded_bytes):
        
        huffman_tree = Decoder.__rebuild_huffman_tree(codebook)
        mtf_sequence = Decoder.__decode_bits(encoded_bytes, padding, huffman_tree)
        return [len(alphabet), *alphabet, *mtf_sequence]
