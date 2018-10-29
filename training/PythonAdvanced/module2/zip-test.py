import struct

f = open("notes.zip", 'rb')
data = f.read(30)

(lfhs, version, bitflag, compression_method, last_modification_time,
    last_modification_date, crc32, compressed_size, uncompressed_size, n, m)\
        = struct.unpack('<ihhhhhiiihh', data)
print("Local file header signature: ", hex(lfhs))
print("Version needed to extract: ", version)
print("General purpose bit flag: ", bin(bitflag))
print("Compression method: ", compression_method)
print("File last modification time: ", last_modification_time)
print("File last modification date: ", last_modification_date)
print("CRC-32: ", crc32)
print("Compressed size: ", compressed_size, " bytes.")
print("Uncompressed size: ", uncompressed_size, " bytes.")
print("n: ", n)
print("m: ", m)

filename = f.read(n)
print("filename: ", filename)
extra_field = f.read(m)
print("extra field: ", extra_field)

f.close()
