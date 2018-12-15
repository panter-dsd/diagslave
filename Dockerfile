FROM alpine:latest

RUN apk update && apk add python3

RUN cd /tmp && wget https://www.modbusdriver.com/downloads/diagslave.tgz \
    && cd / && tar -xvf /tmp/diagslave.tgz && mv /diagslave/linux_x86-64/diagslave /usr/bin \
    && rm /tmp/diagslave.tgz && rm -rf /diagslave

ADD cmd.py /

ENV PROTOCOL=tcp
ENV SERIAL_PORT=/dev/serial_port

EXPOSE 502

CMD python3 /cmd.py
