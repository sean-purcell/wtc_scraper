FROM alpine:latest

WORKDIR /app

RUN apk --no-cache add bash python3 perl
RUN apk --no-cache add perl-net-ssleay perl-io-socket-ssl

ADD sendemail /usr/bin/

ADD requirements.txt /app/
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

ADD *.py /app/
ADD entry.sh /app/

ADD crontab /app/
RUN /usr/bin/crontab /app/crontab

ADD EMAIL_CREDENTIALS /app/

# self-documentation
ADD Dockerfile /app/

ENTRYPOINT ["/bin/bash", "entry.sh"]
