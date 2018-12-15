FROM python:3-slim

ADD diagslave.tgz /
RUN mv /diagslave/linux_x86-64/diagslave /usr/bin && rm -rf /diagslave

ADD cmd.py /

ENV PROTOCOL=tcp
ENV SERIAL_PORT=/dev/serial_port

EXPOSE 502

CMD python3 /cmd.py
