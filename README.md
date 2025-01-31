# coinseek

## usage

```
cd %USERPROFILE%
.\coinseek\Scripts\activate
cd coinseek

python coinseek-sha256.py test
# 9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08

python coinseek-testlibrary-bit.py
# Entropy Text                 : testtesttesttest
# Entropy Hash                 : 5e8b64da785f1572e6da780648eaaffa009152d297bde80f852f068b0ec2989f
# Private Key compressed       : KzPVYsYzN4KJLTHjqoD6i9h7UtfWQDUdMhg1f2gBrLxJnjv4Fm7b
# Private Key uncompressed     : 5JXvbQgsc8Yncg2yqDHLRH1w2ngzQqbMUM6DPDALDzY7JCXUVLz
# Bitcoin Address compressed   : 1DByDY2tA2CES5GYXsbsmfFX8VJMqP8frf
# Bitcoin Address uncompressed : 18JJvjw2XgwmTtVSv7HwKAJTEEFn7rT79P
# Bitcoin Address Script       : 3MMpp9XvjDpFEiPhLaZSa4vmJVGmH2kXbG
```

## setup

https://visualstudio.microsoft.com/de/visual-cpp-build-tools/ - install

```
cd %USERPROFILE%
python -m venv ./coinseek
python -m pip install --upgrade pip
pip install bit
```

