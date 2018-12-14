FROM alpine:latest


RUN cd /tmp && wget https://www.modbusdriver.com/downloads/diagslave.tgz
RUN cd / && tar -xvvf /tmp/diagslave.tgz

ENV PROTOCOL=tcp
CMD /diagslave/linux_x86-64/diagslave -m $PROTOCOL
