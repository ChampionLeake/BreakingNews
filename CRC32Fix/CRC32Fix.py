#
# New York Times Crossword (NDS) CRC32 Patcher
# scripted by ihaveahax 
# CRC32 Algorithm solved by ChampionLeake 
# sanity-checks added by ChampionLeake 
# https://github.com/ihaveamac
# https://github.com/ChampionLeake
#
#!/usr/bin/env python3
import glob
import os
import zlib
for i in glob.iglob('./**/*.sav', recursive=True):
    if os.path.getsize(i) == 0x2000:	#size of the overall savefile
        with open(i, 'rb+') as f:
            data = f.read(0x63C)		#reads the offset of the CRC-bytes
            if data[0x0:0x4] == b'\x72\x50\x63\x42':	#sanity-check for a specific string to be found in the save
                print('New York Times Crossword (NDS) CRC32 Patcher 1.0\nBy ihaveahax and ChampionLeake\n')   
                print('FAMILIAR BYTES FOUND: ', data[0x0:0x4])				
                print('Fixing', i)
                cc = zlib.crc32(data) & 0xFFFFFFFF
                f.write(cc.to_bytes(4, 'little'))
                print('Successfully correct the CRC32 bytes!\n\n')
            else:
                print('Failed to patch CRC32 bytes\n')