#!/usr/bin/python3
import zlib
import argparse

parser = argparse.ArgumentParser(description="A Lossless Data Decompresser, For Compressing Check 'compress.py'")

parser.add_argument("filename", type = str, help = "File To Decompress")

args = parser.parse_args()

file = args.filename

f = open(file, "rb")
compressed_content = f.read()
f.close()

decompressed_content = zlib.decompress(compressed_content)

f = open(file, "wb")
f.write(decompressed_content)
f.close()

print("[*] Done!")
