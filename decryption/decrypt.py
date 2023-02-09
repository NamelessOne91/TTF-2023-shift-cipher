from dotenv import load_dotenv
import os

def decrypt(text: str, ) -> str:
    """Applies a shift cipher (also known as Caesar cipher) to the input text,
    by rotating it RIGHT of key number of positions.
    Returns the rotated text.
    """
    pass


def _main():
    # read your secret encryption key from the .env file
    k = os.getenv("CIPHER_KEY")
    # read from decrypt_input.txt ---> encrypted with key 3
    # call decrypt on each line with your key
    # write the decrypted lines to decrypt_output.txt
    pass



if __name__ == "__main__":
    _main()
