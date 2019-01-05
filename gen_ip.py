# -*- coding: UTF-8 -*-

import random
import socket
import struct

# gen ipv4 IP
print socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))

# gen ipv6 IP
print ':'.join('{:x}'.format(random.randint(0, 2**16 - 1)) for i in range(8))


