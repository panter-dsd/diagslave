FROM alpine:latest

RUN cd /tmp && wget https://www.modbusdriver.com/downloads/diagslave.tgz \
    && cd / && tar -xvf /tmp/diagslave.tgz && mv /diagslave/linux_x86-64/diagslave /usr/bin && rm /tmp/diagslave.tgz && rm -rf /diagslave

ENV PROTOCOL=tcp
CMD /usr/bin/diagslave -m $PROTOCOL
