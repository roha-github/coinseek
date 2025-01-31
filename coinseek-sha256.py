import hashlib
import sys

def sha256_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Bitte einen Text als Parameter übergeben.")
    else:
        text = " ".join(sys.argv[1:])
        print(sha256_hash(text))
