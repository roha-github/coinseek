from hashlib import sha256
from bit import Key

passphrase = "test"
private_key = sha256(passphrase.encode()).hexdigest()
key = Key.from_hex(private_key)

# https://privatekeys.pw/key/9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
print("Entropy Text:", passphrase)      # test                                                               (brainwallet)
print("Entropy Hash:", private_key)     # 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
print("Private Key:", key.to_wif())     # L2ZovMyTxxQVJmMtfQemgVcB5YmiEDapDwsvX6RqvuWibgUNRiHz               (C ~ legacy compressed)
print("Bitcoin Address:", key.address)  # 19eA3hUfKRt7aZymavdQFXg5EZ6KCVKxr8                                 (C ~ legacy compressed)
