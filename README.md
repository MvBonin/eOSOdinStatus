# eOSOdinStatus
A simple python script to notify about progress on elementary OS 6.0 Odin Release.

##Usage
Just run the script with python3 fetchGithubOdin.py
or with 
python3 fetchGithubOdin.py -n
if you want to get a notification, even if the State of eOS has not changed since last time you checked.

I just run it hourly with cron:
sudo crontab -e
-- add a new line:
0 * * * * /path/to/script/fetchGithubOdin.py
##Requirements
pip3 install urllib
pip3 install notify-send
pip3 install bs4