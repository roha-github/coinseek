# coinseek

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
```

## setup

https://visualstudio.microsoft.com/de/visual-cpp-build-tools/ - install

```
cd %USERPROFILE%
python -m venv ./coinseek
python -m pip install --upgrade pip
pip install bit
```

