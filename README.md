# eOSOdinStatus
A simple python script to notify about progress on elementary OS 6.0 Odin Release.

![Screenshot](./screenshot.png)


## Usage
Just run the script with  
`python3 fetchGithubOdin.py` or with  
`python3 fetchGithubOdin.py -n` if you want to get a notification, even if the State of eOS has not changed since last time you checked.

I just run it every 5 minutes with crontab. Dont use the superuser crontab because the pip3 installs deps for your user:  
`chmod +x ./fetchGithubOdin.py`  
`chmod +x ./runner.sh`  
`crontab -u USER -e`  
-- add a new line:  
`*/5 * * * * * cd /PATH/TO/SCRIPT/ && /bin/bash /path/to/script/runner.sh`
## Requirements
`sudo apt install python3-pip`  
`pip3 install pydbus`  
`pip3 install bs4`





### Windows users:
Someone in reddit asked for a windows-version of the script.  
So I added fetchGithubOdinWindows.py  

The requirements for **windows** are  
A Python3 installation,  
`pip install bs4`  
`pip install win10toast-persist`  
then the script gets started with  
`python fetchGithubOdinWindows.py` or  
`python fetchGithubOdinWindows.py -n`

To Automate it, rightclick on windows start-button -> Computer Management -> Task Scheduler.  
There you can add a task, edit the Trigger to 00:00 daily and in advanced you can put it on "Every 10 minutes".  
Under Actions you setup python.exe as program/script, C:/path/to/script/fetchGithubOdinWindows.py as the argument and last but not least C:/path/to/script as the starting location.

As i mainly use linux, I didn't test the windows version much.