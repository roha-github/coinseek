from hashlib import sha256
from bit import Key
from bit.format import bytes_to_wif
from bit.format import public_key_to_segwit_address

passwd = "testtesttesttest"
entropy = sha256(passwd.encode()).hexdigest()
key = Key.from_hex(entropy)
wifu = bytes_to_wif(key.to_bytes(), compressed=False)
wifc = bytes_to_wif(key.to_bytes(), compressed=True)
keyu = Key(wifu)
caddr = key.address
uaddr = keyu.address
scadr = public_key_to_segwit_address(key._public_key)

# https://privatekeys.pw/key/5e8b64da785f1572e6da780648eaaffa009152d297bde80f852f068b0ec2989f
print("Entropy Text                 :", passwd)  # testtesttesttest                                     (brainwallet)
print("Entropy Hash                 :", entropy) # 5e8b64da785f1572e6da780648eaaffa009152d297bde80f852f068b0ec2989f
print("Private Key compressed       :", wifc)    # KzPVYsYzN4KJLTHjqoD6i9h7UtfWQDUdMhg1f2gBrLxJnjv4Fm7b (C ~ WIF compressed)
print("Private Key uncompressed     :", wifu)    # 5JXvbQgsc8Yncg2yqDHLRH1w2ngzQqbMUM6DPDALDzY7JCXUVLz  (U ~ WIF uncompressed) 
print("Bitcoin Address compressed   :", caddr)   # 1DByDY2tA2CES5GYXsbsmfFX8VJMqP8frf                   (C ~ legacy compressed)
print("Bitcoin Address uncompressed :", uaddr)   # 18JJvjw2XgwmTtVSv7HwKAJTEEFn7rT79P                   (U ~ legacy uncompressed)
print("Bitcoin Address Script       :", scadr)   # 3MMpp9XvjDpFEiPhLaZSa4vmJVGmH2kXbG                   (S ~ Script / SegWit )
