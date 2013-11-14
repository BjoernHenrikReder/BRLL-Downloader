#!/usr/bin/env python3
from notifyFormat import notifyFormat
import subprocess

noti = notifyFormat('http://animetake.com/rss', 'title')
subprocess.Popen(['notify-send', "10 minute over"])
