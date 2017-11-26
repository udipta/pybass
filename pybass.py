#!/usr/bin/python3.5
import os

os.system('chmod +x manage.py')
os.system('./manage.py runserver')
os.system('google-chrome templates/index.html')

