from collections import defaultdict

def bwt_transform(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    if len(text) < 1 or len(text) > 1000:
        raise ValueError("Input length must be between 1 and 1000.")
    if text.count("$") != 1 or not text.endswith("$"):
        raise ValueError("Input must contain exactly one '$' at the end.")
    if any(c not in "ACGT$" for c in text):
        raise ValueError("Input may contain only A, C, G, T and '$'.")
    
    rotations = [text[i:] + text[:i] for i in range(len(text))]
    rotations.sort()
    return ''.join(rotation[-1] for rotation in rotations)

def preprocess_bwt(bwt):
    if not isinstance(bwt, str):
        raise TypeError("Input must be a string.")
    if len(bwt) < 1 or len(bwt) > 1000000:
        raise ValueError("Input length must be between 1 and 1000000.")
    if bwt.count("$") != 1:
        raise ValueError("BWT string must contain exactly one '$'.")
    if any(c not in "ACGT$" for c in bwt):
        raise ValueError("BWT string may contain only A, C, G, T and '$'.")

    sorted_bwt = sorted(bwt)
    first_occurrence = {}
    for i, c in enumerate(sorted_bwt):
        if c not in first_occurrence:
            first_occurrence[c] = i

    count = defaultdict(lambda: [0] * (len(bwt) + 1))
    for i in range(1, len(bwt) + 1):
        for c in "ACGT$":
            count[c][i] = count[c][i - 1]
        count[bwt[i - 1]][i] += 1

    return first_occurrence, count

def bw_matching(bwt, pattern, first_occurrence, count):
    if not isinstance(bwt, str) or not isinstance(pattern, str):
        raise TypeError("Inputs must be strings.")
    if len(bwt) < 1 or len(bwt) > 1000000:
        raise ValueError("BWT length must be between 1 and 1000000.")
    if len(pattern) < 1 or len(pattern) > 1000:
        raise ValueError("Pattern length must be between 1 and 1000.")
    if bwt.count("$") != 1:
        raise ValueError("BWT string must contain exactly one '$'.")
    if any(c not in "ACGT$" for c in bwt):
        raise ValueError("BWT string may contain only A, C, G, T and '$'.")
    if any(c not in "ACGT" for c in pattern):
        raise ValueError("Pattern may contain only A, C, G, T.")

    top = 0
    bottom = len(bwt) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if count[symbol][bottom + 1] - count[symbol][top] > 0:
                top = first_occurrence[symbol] + count[symbol][top]
                bottom = first_occurrence[symbol] + count[symbol][bottom + 1] - 1
            else:
                return 0
        else:
            return bottom - top + 1
    return 0

def main():
    with open('input.dat', 'r') as infile:
        lines = [line.strip() for line in infile if line.strip()]
        text = lines[0]
        pattern = lines[1]

    text += '$'
    bwt = bwt_transform(text)
    first_occurrence, count = preprocess_bwt(bwt)
    result = bw_matching(bwt, pattern, first_occurrence, count)

    with open('output.dat', 'w') as outfile:
        outfile.write(str(result) + '\n')

if __name__ == '__main__':
    main()
