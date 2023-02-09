
from string import ascii_lowercase


def decrypt(text: str, key: int) -> str:
    """Applies a shift cipher (also known as Caesar cipher) to the input text,
    by rotating it RIGHT of key number of positions.
    Returns the rotated text.
    """
    if type(key) is not int or key < 0:
        raise ValueError("key must be >= 0")

    rotated = ascii_lowercase[-key:] + ascii_lowercase[:-key]
    table = str.maketrans(ascii_lowercase, rotated)

    return text.translate(table)


def _main():
    # read your secret encryption key from the .env file
    # read from decrypt_input.txt ---> encrypted with key 3
    # call decrypt on each line with your key
    # write the decrypted lines to decrypt_output.txt
    pass


if __name__ == "__main__":
    _main()
