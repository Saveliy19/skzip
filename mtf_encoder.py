from typing import List

class Encoder:

    @staticmethod
    def move_to_front(curr_index, lst):
        symbol = lst.pop(curr_index)
        lst.insert(0, symbol)

    @staticmethod
    def mtf_encode(input_text, original_lst):
        lst = original_lst.copy()
        output_arr = []

        for ch in input_text:
            index = lst.index(ch)
            output_arr.append(index)
            Encoder.move_to_front(index, lst)

        return output_arr

    @staticmethod     
    def encode(text: str) -> List[int]:
        lst = sorted(list(set(text)))
        output_arr = Encoder.mtf_encode(text, lst.copy())
        return [len(lst)] + [ord(ch) for ch in lst] + output_arr
