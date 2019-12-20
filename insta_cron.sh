#!/bin/bash
SLEEP_TIME=${RANDOM:0:2%120}
SLEEP_TIME="${SLEEP_TIME}m"
sleep $SLEEP_TIME
/usr/bin/python3 ~/vanlinsta/bot.py >> ~/vanlinsta/bot.log 2>&1