import sys

from bwt_encoder import Encoder as BwtEncoder
from mtf_encoder import Encoder as MtfEncoder
from huffman_encoder import Encoder as HuffmanEncoder

class Encoder:

    @staticmethod
    def encode(input_file: str, output_file: str):
        
        input_text = Reader.read_file(input_file)

        bwt_encoded_text = BwtEncoder.encode(input_text)
        print("BWT encoding - DONE!")

        mtf_encoded_data = MtfEncoder.encode(bwt_encoded_text)
        print("MTF encoding - DONE!")

        huffman_encoded_data = HuffmanEncoder.encode(mtf_encoded_data)
        print("Huffman encoding - DONE!")

        Writer.write_file(data=huffman_encoded_data, output_file=output_file)

class Reader:

    @staticmethod 
    def read_file(input_file):
        with open(input_file, 'rb') as f:
            input_bytes = f.read()
        input_text = input_bytes.decode('latin1')  # <-- вот здесь
        return input_text


class Writer:

    @staticmethod
    def write_file(data, output_file):
        with open(output_file, 'wb') as f:
            f.write(len(data['alphabet']).to_bytes(2, 'big'))
            for sym in data['alphabet']:
                f.write(sym.to_bytes(1, 'big'))

            f.write(data['padding'].to_bytes(1, 'big'))

            f.write(len(data['codebook']).to_bytes(2, 'big'))
            for sym, code in data['codebook'].items():
                f.write(sym.to_bytes(1, 'big'))
                f.write(len(code).to_bytes(1, 'big'))
                f.write(int(code, 2).to_bytes((len(code) + 7) // 8, 'big'))

            f.write(len(data['data']).to_bytes(4, 'big'))
            f.write(data['data'])

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python encoder.py <infile> <zipfile>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    Encoder.encode(input_file, output_file)
