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

def main():
    with open('input.dat', 'r') as infile:
        text = infile.read().strip()

    result = bwt_transform(text)

    with open('output.dat', 'w') as outfile:
        outfile.write(result)

if __name__ == '__main__':
    main()
