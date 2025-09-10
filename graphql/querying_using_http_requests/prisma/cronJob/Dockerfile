FROM alpine:3.7

# update pkg manger to find curl
RUN apk update

# # now we can install curl
RUN apk --no-cache add curl


ADD crontab.txt /crontab.txt
ADD script.sh /script.sh
COPY entry.sh /entry.sh
RUN chmod 755 /script.sh /entry.sh
RUN /usr/bin/crontab /crontab.txt

CMD ["/entry.sh"]