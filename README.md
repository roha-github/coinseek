# coinseek

## note

* https://privatekeys.pw - Rainbow Tabelle für Brainwallet - SHA256 - Private Key - Public Key - Coin Adresse
* Wertebereich für SHA256 von 1 bis 2 ^ 256
  * [/key/23d4a09295be678b21a5f1dceae1f634a69c1b41775f680ebf8165266471401b](https://privatekeys.pw/key/23d4a09295be678b21a5f1dceae1f634a69c1b41775f680ebf8165266471401b) ~ Einstieg über Key (vor/weiter, Zufall)
  * [/key/bc2b1c76edc151a61d7c647b1a6e1c15af579ba1c72bdcca028dcfafa91d0231](https://privatekeys.pw/key/bc2b1c76edc151a61d7c647b1a6e1c15af579ba1c72bdcca028dcfafa91d0231) ~ Zufalls Key = zur Laufzeit berechnet
  * [/key/0000000000000000000000000000000000000000000000000000000000000001](https://privatekeys.pw/key/0000000000000000000000000000000000000000000000000000000000000001) ~ Start = minimum SHA-256 (1)
  * [/key/fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140](https://privatekeys.pw/key/fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140) ~ Ende = maximum SHA-256 (2 ^ 256 = 1,15e+77)
* Lookup falls Adresse und/oder Private Key bekannt
  * [/address/bitcoin/18vqVNQi9fobKZcJWCjZNoDzBxronENfZr](https://privatekeys.pw/address/bitcoin/18vqVNQi9fobKZcJWCjZNoDzBxronENfZr) ~ Adresse mit bekannten Private Key
  * [/address/bitcoin/1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF](https://privatekeys.pw/address/bitcoin/1FeexV6bAHb8ybZjqQMjJrcCrHGW9sb6uF) ~ Adresse ohne bekannten Private Key
* Guthaben
  * [https://privatekeys.pw/richest/bitcoin](https://privatekeys.pw/richest/bitcoin)

## usage

```
cd %USERPROFILE%
.\coinseek\Scripts\activate
cd coinseek

python coinseek-sha256.py test
# 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08

python coinseek-testlibrary-bit.py "test"
# Entropy Text                   : test
# Entropy Hash = sha256(Text)    : 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
# Private Key compressed         : L2ZovMyTxxQVJmMtfQemgVcB5YmiEDapDwsvX6RqvuWibgUNRiHz
# Private Key uncompressed       : 5K2YUVmWfxbmvsNxCsfvArXdGXm7d5DC9pn4yD75k2UaSYgkXTh
# Bitcoin Address C compressed   : 19eA3hUfKRt7aZymavdQFXg5EZ6KCVKxr8
# Bitcoin Address U uncompressed : 1HKqKTMpBTZZ8H5zcqYEWYBaaWELrDEXeE
# Bitcoin Address S Script       : 3PEaV1m4nGi3yTKnzzmqjFTkxzrcFpier5
# Bitcoin Address W SegWit       : bc1qtmrl9526rusw4dnavrcfal72tz6ram5lqzutru

python coinseek-testlibrary-bit.py fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140
# Entropy Text                   : ???
# Entropy Hash = sha256(Text)    : fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140
# Private Key compressed         : L5oLkpV3aqBjhki6LmvChTCV6odsp4SXM6FfU2Gppt5kFLaHLuZ9
# Private Key uncompressed       : 5Km2kuu7vtFDPpxywn4u3NLpbr5jKpTB3jsuDU2KYEqetqj84qw
# Bitcoin Address C compressed   : 1GrLCmVQXoyJXaPJQdqssNqwxvha1eUo2E
# Bitcoin Address U uncompressed : 1JPbzbsAx1HyaDQoLMapWGoqf9pD5uha5m
# Bitcoin Address S Script       : 38Kw57SDszoUEikRwJNBpypPSdpbAhToeD
# Bitcoin Address W SegWit       : bc1q4h0ycu78h88wzldxc7e79vhw5xsde0n8jk4wl5
```

## setup

https://visualstudio.microsoft.com/de/visual-cpp-build-tools/ - install

```
cd %USERPROFILE%
python -m venv ./coinseek
python -m pip install --upgrade pip
pip install bit
```

