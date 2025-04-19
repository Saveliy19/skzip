from collections import defaultdict

class Decoder:

    @staticmethod
    def decode(bwt):
        if not bwt:
            return ""

        symbol_ranks = defaultdict(int)
        last_column = [(char, symbol_ranks[char]) for char in bwt for _ in [symbol_ranks[char]] if not symbol_ranks.__setitem__(char, symbol_ranks[char] + 1)]

        sorted_bwt = sorted(bwt)
        symbol_ranks.clear()
        first_column = [(char, symbol_ranks[char]) for char in sorted_bwt for _ in [symbol_ranks[char]] if not symbol_ranks.__setitem__(char, symbol_ranks[char] + 1)]
        lf_map = {}
        for idx, pair in enumerate(first_column):
            lf_map[pair] = idx
        path = [lf_map[p] for p in last_column]

        position = bwt.index('$')
        result = []
        for _ in range(len(bwt)):
            position = path[position]
            result.append(first_column[position][0])

        return ''.join(reversed(result))[:-1]