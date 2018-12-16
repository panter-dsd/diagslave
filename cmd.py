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


def slave_address():
    return os.environ.get('SLAVE_ADDRESS', None)


def parity():
    return os.environ.get('PARITY', "even")


def baudrate():
    return os.environ.get('BAUDRATE', None)


def tcp_port():
    return os.environ.get('TCP_PORT', 502)


def connection_timeout():
    return os.environ.get('CONNECTION_TIMEOUT', 60)


def data_bits():
    return os.environ.get('DATA_BITS', 8)


def stop_bits():
    return os.environ.get('STOP_BITS', 1)


def master_activity_timeout():
    return os.environ.get('MASTER_ACTIVITY_TIMEOUT', 3)


def add_network_arguments(a):
    a.append('-a')
    a.append(tcp_port())
    a.append('-c')
    a.append(connection_timeout())
    a.append('-o')
    a.append(master_activity_timeout())


arguments = ['/usr/bin/diagslave', '-m']

if protocol == 'tcp':
    arguments.append('tcp')
    add_network_arguments(arguments)
elif protocol == 'udp':
    arguments.append('udp')
    add_network_arguments(arguments)
elif protocol in ['ascii', 'rtu']:
    arguments.append(protocol)
    sa = slave_address()
    if sa:
        arguments.append('-a')
        arguments.append(sa)
    b = baudrate()
    if b:
        arguments.append('-b')
        arguments.append(b)
    arguments.append('-p')
    arguments.append(parity())
    arguments.append('-d')
    arguments.append(data_bits())
    arguments.append('-s')
    arguments.append(stop_bits())
    arguments.append('-o')
    arguments.append(master_activity_timeout())
    arguments.append(serial_port())
else:
    print(f'Unknown protocol {protocol}')
    exit(1)

print(f'Start process with parameters {arguments}')
subprocess.call([str(a) for a in arguments])
