# coinseek

## usage

```
cd %USERPROFILE%
.\coinseek\Scripts\activate
cd coinseek

python coinseek-sha256.py test
# 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08

python coinseek-testlibrary-bit.py
# Entropy Text: test
# Entropy Hash: 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08
# Private Key: L2ZovMyTxxQVJmMtfQemgVcB5YmiEDapDwsvX6RqvuWibgUNRiHz
# Bitcoin Address: 19eA3hUfKRt7aZymavdQFXg5EZ6KCVKxr8
```

## setup

https://visualstudio.microsoft.com/de/visual-cpp-build-tools/ - install

```
cd %USERPROFILE%
python -m venv ./coinseek
python -m pip install --upgrade pip
pip install bit
```

