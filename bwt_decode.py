from collections import defaultdict

def inverse_bwt(bwt: str) -> str:
    if not isinstance(bwt, str):
        raise TypeError("Input must be a string.")
    if len(bwt) < 1 or len(bwt) > 1000000:
        raise ValueError("Input length must be between 1 and 1000000.")
    if bwt.count("$") != 1:
        raise ValueError("Transformed string must contain exactly one '$'.")
    if any(c not in "ACGT$" for c in bwt):
        raise ValueError("Transformed string may contain only A, C, G, T and '$'.")
    
    n = len(bwt)
    first_col = sorted(bwt)

    def build_rank(column):
        ranks, count = [], defaultdict(int)
        for c in column:
            ranks.append((c, count[c]))
            count[c] += 1
        return ranks

    last_rank = build_rank(bwt)
    first_rank = build_rank(first_col)
    lf_map = {last: i for i, last in enumerate(first_rank)}

    idx = bwt.index('$')
    result = []
    for _ in range(n):
        char, rank = last_rank[idx]
        result.append(char)
        idx = lf_map[(char, rank)]

    return ''.join(reversed(result))

def main():
    with open('input.dat', 'r') as infile:
        bwt_text = infile.read().strip()

    result = inverse_bwt(bwt_text)

    with open('output.dat', 'w') as outfile:
        outfile.write(result)

if __name__ == '__main__':
    main()
