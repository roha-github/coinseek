#!/usr/bin/env python3

offset = 0

file_bitcoinaddress_sorted = './data/bitcoin_addresses.txt'
file_passphrase_input      = './data/passphrases.txt.gz'
file_outputfound_log       = './coinseek.txt'

# --- string exists in sorted textfile ---

import sys

def find_line_start(f, pos):
    if pos == 0:
        return 0  # Bereits am Anfang der Datei
    new_pos = pos
    # Suche rückwärts, bis ein '\n' gefunden wird.
    while new_pos > 0:
        f.seek(new_pos - 1)
        c = f.read(1)
        if c == b'\n':
            break
        new_pos -= 1
    return new_pos

def binary_search_in_file(file_path, target_hash, target_isbyte=False):
    if target_isbyte:
        target_bytes = target_hash
    else:
        target_bytes = target_hash.encode('utf-8')
    
    with open(file_path, 'rb') as f:
        # Bestimme die Dateigröße (Endposition in Bytes)
        f.seek(0, 2)
        file_size = f.tell()
        
        low = 0
        high = file_size
        
        while low < high:
            mid = (low + high) // 2
            # Bestimme den Anfang der Zeile, die das Byte an Position mid enthält
            line_start = find_line_start(f, mid)
            f.seek(line_start)
            line = f.readline()
            if not line:
                # Sollte normalerweise nicht passieren – aber zur Sicherheit:
                high = mid
                continue

            # Entferne Zeilenumbrüche (sowohl '\n' als auch '\r\n')
            line_clean = line.rstrip(b'\r\n')
            
            if line_clean == target_bytes:
                return True
            elif line_clean < target_bytes:
                # Suche in den späteren Zeilen:
                low = f.tell()  # Setzt low auf den Anfang der nächsten Zeile
            else:
                # Suche in den früheren Zeilen:
                high = line_start
        
        return False

# --- process string ---

from hashlib import sha256

from bit import Key
from bit.format import bytes_to_wif
from bit.crypto import ripemd160_sha256
from bit.base32 import encode

def process_phrase(phrase,offset=0,mode=0,info=""):
    # --- adresse berechnen ---
    if mode == 0:
        entropy = sha256(phrase).hexdigest()
        keyc = Key.from_hex(entropy)
        wifc = bytes_to_wif(keyc.to_bytes(), compressed=True)
        wifu = bytes_to_wif(keyc.to_bytes(), compressed=False)
        keyu = Key(wifu)
        adrc = keyc.address
        adru = keyu.address
        adrs = keyc.segwit_address
        witp = ripemd160_sha256(keyc._public_key)
        adrw = encode('bc', 0, witp)
        process_phrase(adru,offset,1,"adru/phrase:"+str(phrase)+info)
        process_phrase(adrc,offset,1,"adrc/phrase:"+str(phrase)+info)
        process_phrase(adrs,offset,1,"adrs/phrase:"+str(phrase)+info)
        process_phrase(adrw,offset,1,"adrw/phrase:"+str(phrase)+info)
        if offset % 1000 == 0:
            print("debug: ",phrase," sha256:",entropy," addr_u:",keyu.address," addr_c:",keyc.address)
    # --- adresse suchen ---
    if mode == 1:
        dateipfad = file_bitcoinaddress_sorted
        hashwert = phrase
        if binary_search_in_file(dateipfad, hashwert):
            flog = open(file_outputfound_log,"a")
            flog.write(str(offset)+","+str(phrase)+","+info+","+"\n")
            flog.close() 

# --- read input file ---

import gzip
import time

def read_gz_blocks(file_path, block_size=1024, offset=0, maxblocks=None):
    with gzip.open(file_path, 'rb') as f:
        # --- start from last position ---
        f.seek(offset)  # Setze die Startposition
        block_count = 0
        timer_start = time.time()
        timer_pointer = timer_start
        timer_interval = 2
        # --- read gzfile line by line ---
        for line in f:
            block_count += 1
            file_position = f.tell()
            if maxblocks is not None and block_count > maxblocks:
                break
            # --- debug by time ---
            if time.time()-timer_pointer >= timer_interval:
                timer_pointer = time.time()
                print("debug: ", block_count, " block, ",time.time()-timer_start," sec")
            # --- process input ---
            if len(line) >= 26:
                hashwert = line[:-1]
                process_phrase(hashwert,file_position)

t0 = time.time()
limit = 100000
limit = None
read_gz_blocks(file_passphrase_input, block_size=4096, offset=offset, maxblocks=limit)
print(time.time() - t0, "s ~ ",(time.time() - t0)/limit," 1/s")

