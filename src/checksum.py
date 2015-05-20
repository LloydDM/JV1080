'''
Created on Feb 18, 2015

@author: david
'''

PREAMBLE = [240, 65, 16, 106, 18]
EOX = [247]

def checksum(message):
    total = sum(message)
    remainder = total % 128
    checksum = 128 - remainder
    return [checksum]
    
sysex = '\x01\x00\x00\x28\x06'
data = sysex[:]
msg = [ord(c) for c in data]
print msg
print PREAMBLE
print PREAMBLE + msg + checksum(msg) + EOX