#!/bin/sh

# start cron
/usr/sbin/crond -f -l 8 -L /var/log/log.txt