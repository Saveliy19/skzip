class SuffixNode:
    def __init__(self):
        self.pos = 0
        self.ranks = [0, 0]

class SuffixArrayBuilder:

    @staticmethod
    def build(text, length):
        if not text.endswith('$'):
            text += '$'
            length = len(text)

        suffix_nodes = [SuffixNode() for _ in range(length)]

        for i in range(length):
            suffix_nodes[i].pos = i
            suffix_nodes[i].ranks[0] = ord(text[i])
            suffix_nodes[i].ranks[1] = ord(text[i + 1]) if i + 1 < length else -1

        suffix_nodes.sort(key=lambda node: (node.ranks[0], node.ranks[1]))

        pos_to_idx = [0] * length
        step = 4
        while step < 2 * length:
            current_rank = 0
            prev_first_rank = suffix_nodes[0].ranks[0]
            suffix_nodes[0].ranks[0] = current_rank
            pos_to_idx[suffix_nodes[0].pos] = 0

            for i in range(1, length):
                if (suffix_nodes[i].ranks[0] == prev_first_rank and 
                    suffix_nodes[i].ranks[1] == suffix_nodes[i - 1].ranks[1]):
                    suffix_nodes[i].ranks[0] = current_rank
                else:
                    prev_first_rank = suffix_nodes[i].ranks[0]
                    current_rank += 1
                    suffix_nodes[i].ranks[0] = current_rank
                pos_to_idx[suffix_nodes[i].pos] = i

            for i in range(length):
                next_pos = suffix_nodes[i].pos + step // 2
                suffix_nodes[i].ranks[1] = (
                    suffix_nodes[pos_to_idx[next_pos]].ranks[0] if next_pos < length else -1
                )

            suffix_nodes.sort(key=lambda node: (node.ranks[0], node.ranks[1]))
            step *= 2

        result = [node.pos for node in suffix_nodes]
        return result
