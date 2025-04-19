from suffix_builder import SuffixArrayBuilder

class Encoder:

	@staticmethod
	def _build_bwt(text, suffixes, length):
		result = []
		for idx in range(length):
			prev_char_idx = suffixes[idx] - 1
			if prev_char_idx < 0:
				prev_char_idx += length
			result.append(text[prev_char_idx])
		return ''.join(result)

	@staticmethod
	def encode(original: str):
		modified = original + "$"
		size = len(modified)

		suffixes = SuffixArrayBuilder.build(modified, size)
		bwt_result = Encoder._build_bwt(modified, suffixes, size)

		return bwt_result
