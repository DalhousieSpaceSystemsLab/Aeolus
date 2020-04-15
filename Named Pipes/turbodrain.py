import os
import errno

FIFO = 'pipe'

with open(FIFO) as fifo:
    for line in fifo:
        print('[i] Incoming message', line)
