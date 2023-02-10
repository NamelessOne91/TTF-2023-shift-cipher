from dotenv import load_dotenv
from string import ascii_lowercase
import os


def decrypt(text: str, key: int) -> str:
    """Applies a shift cipher (also known as Caesar cipher) to the input text,
    by rotating it RIGHT of key number of positions.
    Returns the rotated text.
    """
    if type(text) is not str:
        raise ValueError("text must be a string")
    if type(key) is not int or key < 0:
        raise ValueError("key must be >= 0")

    rotated = ascii_lowercase[-key:] + ascii_lowercase[:-key]
    table = str.maketrans(ascii_lowercase, rotated)

    return text.translate(table)


def _main():
    load_dotenv()
    k = int(os.getenv("CIPHER_KEY"))
    # read from decrypt_input.txt ---> encrypted with key 3
    with open("./decryption/decrypt_input.txt") as input:
        with open("./decryption/decrypt_output.txt", "w") as output:
            for line in input.readlines():
                # call decrypt on each line with your key
                decrypted = decrypt(line, k)
                # write the decrypted lines to decrypt_output.txt
                output.write(decrypted)


if __name__ == "__main__":
    _main()
