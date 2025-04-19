import sys

from bwt_decoder import Decoder as BwtDecoder
from mtf_decoder import Decoder as MtfDecoder
from huffman_decoder import Decoder as HuffmanDecoder

class Decoder:

    @staticmethod
    def decode(input_file: str, output_file: str) -> None:

        alphabet, padding, codebook, encoded_bytes = Reader.read_file(input_file)

        arithmetic_decoded_data = HuffmanDecoder.decode(alphabet, padding, codebook, encoded_bytes)
        print("Huffman decoding - DONE!")

        mtf_decoded_data = MtfDecoder.decode(arithmetic_decoded_data)
        print("MTF decoding - DONE!")

        bwt_decoded_text = BwtDecoder.decode(mtf_decoded_data)
        print("BWT decoding - DONE!")

        Writer.write_file(bwt_decoded_text, output_file)

class Reader:
    @staticmethod
    def read_file(filepath):
        with open(filepath, 'rb') as f:

            alphabet_size = int.from_bytes(f.read(2), 'big')
            alphabet = [int.from_bytes(f.read(1), 'big') for _ in range(alphabet_size)]

            padding = int.from_bytes(f.read(1), 'big')

            codebook_size = int.from_bytes(f.read(2), 'big')
            codebook = {}
            for _ in range(codebook_size):
                symbol = int.from_bytes(f.read(1), 'big')
                code_len = int.from_bytes(f.read(1), 'big')
                byte_len = (code_len + 7) // 8
                code_bytes = f.read(byte_len)
                code_bits = bin(int.from_bytes(code_bytes, 'big'))[2:].zfill(code_len)
                codebook[symbol] = code_bits

            data_length = int.from_bytes(f.read(4), 'big')
            encoded_bytes = f.read(data_length)

        return alphabet, padding, codebook, encoded_bytes

class Writer:
    @staticmethod
    def write_file(data, output_file):
        with open(output_file, 'wb') as f:
            f.write(data.encode('latin1'))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python encoder.py <zipfile> <decfile>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    Decoder.decode(input_file, output_file)