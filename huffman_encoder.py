import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, symbol=None, freq=0):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq
    
class Encoder:

    @staticmethod
    def __build_huffman_tree(freq_table):
        heap = [HuffmanNode(sym, freq) for sym, freq in freq_table.items()]
        heapq.heapify(heap)
        while len(heap) > 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            merged = HuffmanNode(freq=left.freq + right.freq)
            merged.left = left
            merged.right = right
            heapq.heappush(heap, merged)
        return heap[0]

    @staticmethod
    def __build_codes(node, prefix='', codebook=None):
        if codebook is None:
            codebook = dict()
        if node.symbol is not None:
            codebook[node.symbol] = prefix
        else:
            Encoder.__build_codes(node.left, prefix + '0', codebook)
            Encoder.__build_codes(node.right, prefix + '1', codebook)
        return codebook

    @staticmethod
    def __encode_bits(data, codebook):
        bits = ''.join(codebook[sym] for sym in data)
        padding = (8 - len(bits) % 8) % 8
        bits += '0' * padding
        byte_array = bytearray()
        for i in range(0, len(bits), 8):
            byte_array.append(int(bits[i:i+8], 2))
        return byte_array, padding

    @staticmethod
    def encode(data):
        n = data[0]
        alphabet = data[1:n+1]
        mtf_encoded = data[n+1:]

        freq_table = Counter(mtf_encoded)
        huffman_tree = Encoder.__build_huffman_tree(freq_table)
        codebook = Encoder.__build_codes(huffman_tree)
        encoded_bytes, padding = Encoder.__encode_bits(mtf_encoded, codebook)

        return {
            'alphabet': alphabet,
            'data': encoded_bytes,
            'codebook': codebook,
            'padding': padding
        }
