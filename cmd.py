import os
import subprocess

try:
    protocol = os.environ['PROTOCOL']
except KeyError:
    protocol = None
    print('Protocol is not set')
    exit(1)


def serial_port():
    try:
        return os.environ['SERIAL_PORT']
    except KeyError:
        print('Serial port is not set')
        exit(1)


arguments = ['/usr/bin/diagslave', '-m']

if protocol == 'tcp':
    arguments.append('tcp')
elif protocol == 'udp':
    arguments.append('udp')
elif protocol == 'ascii':
    arguments.append('ascii')
    arguments.append(serial_port())
else:
    print(f'Unknown protocol {protocol}')
    exit(1)

print(f'Start process with parameters {arguments}')
subprocess.call(arguments)
