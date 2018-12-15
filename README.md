# This is docker container for diagslave utility
https://www.modbusdriver.com/diagslave.html docker container

# Run with serial port option

`docker run -ti --rm -e PROTOCOL=ascii -e SERIAL_PORT=/dev/tty0 --device /dev/tty0 panterdsd/diagslave:latest`

# Run with tcp/udp option

`docker run -ti --rm -p 9991:502 -e PROTOCOL=tcp panterdsd/diagslave:latest`
