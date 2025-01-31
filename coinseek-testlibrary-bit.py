from hashlib import sha256
from bit import Key
from bit.format import bytes_to_wif

passwd = "test"
entropy = sha256(passwd.encode()).hexdigest()
key = Key.from_hex(entropy)
wifu = bytes_to_wif(key.to_bytes(), compressed=False)
wifc = bytes_to_wif(key.to_bytes(), compressed=True)
keyu = Key(wifu)
caddr = key.address
uaddr = keyu.address

# https://privatekeys.pw/key/9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
print("Entropy Text                 :", passwd)  # test                                                 (brainwallet)
print("Entropy Hash                 :", entropy) # 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
print("Private Key compressed       :", wifc)    # L2ZovMyTxxQVJmMtfQemgVcB5YmiEDapDwsvX6RqvuWibgUNRiHz (C ~ WIF compressed)
print("Private Key uncompressed     :", wifu)    # 5K2YUVmWfxbmvsNxCsfvArXdGXm7d5DC9pn4yD75k2UaSYgkXTh  (U ~ WIF uncompressed) 
print("Bitcoin Address compressed   :", caddr)   # 19eA3hUfKRt7aZymavdQFXg5EZ6KCVKxr8                   (C ~ legacy compressed)
print("Bitcoin Address uncompressed :", uaddr)   # 1HKqKTMpBTZZ8H5zcqYEWYBaaWELrDEXeE                   (U ~ legacy uncompressed)
