#!/usr/bin/python3
import zlib
import argparse

parser = argparse.ArgumentParser(description="A Lossless Data Compresser, For Decompressing Check 'decompress.py'")

parser.add_argument("filename", type = str, help = "File To Compress")

args = parser.parse_args()

file = args.filename

f = open(file, "rb")
content = f.read()
f.close()

compressed_data = zlib.compress(content)

f = open(file, "wb")
f.write(compressed_data)
f.close()

print("[*] Done!")
