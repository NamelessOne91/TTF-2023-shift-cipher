from dotenv import load_dotenv
from string import ascii_lowercase



def encrypt(text: str, key: int) -> str:
    """Applies a shift cipher (also known as Caesar cipher) to the input text,
    by rotating it LEFT of key number of positions.
    Returns the rotated text.
    """
    if type(text) is not str:
        raise ValueError("text must be a string")
    if type(key) is not int or key < 0:
        raise ValueError("key must be an int >= 0")

    rotated = ascii_lowercase[key:] + ascii_lowercase[:key]
    table = str.maketrans(ascii_lowercase, rotated)

    return text.translate(table)



def _main():
    # read your secret encryption key from the .env file
    # read from encrypt_input.txt
    # call encrypt on each line with your key
    # write the encrypted lines to encrypt_output.txtc
   pass
   


if __name__ == "__main__":
    _main()
