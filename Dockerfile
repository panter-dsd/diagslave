FROM alpine:latest

RUN cd /tmp && wget https://www.modbusdriver.com/downloads/diagslave.tgz \
    && cd / && tar -xvf /tmp/diagslave.tgz && rm /tmp/diagslave.tgz

ENV PROTOCOL=tcp
CMD /diagslave/linux_x86-64/diagslave -m $PROTOCOL
