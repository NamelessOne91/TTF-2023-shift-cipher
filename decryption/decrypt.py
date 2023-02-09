from dotenv import load_dotenv
import os

def decrypt(riga, key) -> str:
    riga = list(riga)
    testoDecrifrato = ""
    for c in riga:
        if c.isalpha():
            sposta_c = chr((ord(c.upper()) - 65 - key) % 26 + 65)
            if c.islower():
                sposta_c = sposta_c.lower()
            testoDecrifrato += sposta_c
        else:
            testoDecrifrato += c
    return testoDecrifrato
    
load_dotenv()
k = int(os.getenv("CIPHER_KEY"))
with open("decrypt_input.txt") as input:
    testoCriptato = input.readlines()
testoDecifrato = [decrypt(linea, k) for linea in testoCriptato]
with open("output.txt", "w") as output:
    output.writelines(testoDecifrato)