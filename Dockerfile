FROM alpine:3.13.0

EXPOSE 9090
COPY requirements.txt /
COPY flasktest.db /
COPY flasktest.py /

RUN sed -i -e 's/https/http/' /etc/apk/repositories

RUN apk add --no-cache python3 && python3 -m ensurepip && pip3 install --no-cache --upgrade pip setuptools wheel

RUN /usr/bin/pip3 -v install -r requirements.txt

ENTRYPOINT ["/flasktest.py"]
