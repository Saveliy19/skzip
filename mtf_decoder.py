class Decoder:

    @staticmethod
    def decode(arr):
        len_alphabet = arr[0]
        alphabet = [chr(code) for code in arr[1:1+len_alphabet]]
        mtf_data = arr[1+len_alphabet:]

        lst = list(alphabet)
        result = []

        for index in mtf_data:
            symbol = lst[index]
            result.append(symbol)

            lst.pop(index)
            lst.insert(0, symbol)

        return ''.join(result)
