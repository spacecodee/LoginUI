import eel
import sys

# python -m eel main.py web --onefile --noconsole --icon=./web/img/login.ico >= hacer ejecutable de windows

sys.path.append('..')
eel.init('web')

eel.start('index.html', port=8080, cmdline_args=['--start-fullscreen'], size=(1500, 1000))