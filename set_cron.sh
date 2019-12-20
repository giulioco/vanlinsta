#!/bin/bash

#write out current crontab
crontab -l > mycron
#echo new cron into cron file
if grep -qF "bot.py" mycron;then
   echo "Entry already exists for ./bot.py. Deleting existing entry..."
   sed '/bot.py/d' ./mycron > ./mycron_new
else
   echo "Entry not found for bot.py"
fi
echo "Adding entry..."
# Sets crontab at minute 0 past every 2nd hour from 8 through 23
# Sleeps between 0 and 119 minutes
# Calls bot
echo "0 8-23/2 * * * bash ~/vanlinsta/insta_cron.sh" >> ./mycron_new
#install new cron file
echo "Setting the crontab to the following"
cat mycron_new
crontab mycron_new
echo "Crontab set to the following"
crontab -l
rm mycron mycron_new