'''
Created on Feb 20, 2015

@author: David
'''
import rtmidi_python as rtmidi
from time import sleep

PREAMBLE = [240, 65, 16, 106, 18]
EOX = [247]

def checksum(message):
    total = sum(message)
    remainder = total % 128
    checksum = 128 - remainder
    return [checksum]

command = '\x11\x00\x10\x3D\x40'
listed_command = command[:]
payload = [ord(c) for c in listed_command]

sysex_message = PREAMBLE + payload + checksum(payload) + EOX

midiport = rtmidi.MidiOut()
 
midiport.open_port(5)

midiport.send_message(sysex_message)
midiport.send_message([0xc0, 0])

sleep(10)

