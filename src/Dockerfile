FROM alpine:3.7

RUN apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN chmod +x /usr/src/app/requirements.txt

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/

ENTRYPOINT ["python3", "app.py"]
