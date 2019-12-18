#!/bin/bash

#write out current crontab
crontab -l > mycron
#echo new cron into cron file
if grep -qF "bot.py" mycron;then
   echo "Entry already exists for ./bot.py. Deleting existing entry...\n"
   sed -i '' '/bot.py/d' ./mycron
else
   echo "Entry not found for bot.py"
fi
echo "Adding entry..."
# Sets crontab at minute 0 past every 2nd hour from 8 through 23
# Sleeps between 0 and 119 minutes
# Calls bot
echo "0 8-23/2 * * * sleep ${RANDOM:0:2%120}m ; cd ~ && /usr/bin/python3 ~/bot.py >> bot.log 2>&1" >> mycron
#install new cron file
crontab mycron
rm mycron