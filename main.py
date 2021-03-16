import eel
import sys

sys.path.append('..')
eel.init('web')

eel.start('index.html', port=8080, cmdline_args=['--start-fullscreen'], size=(1500, 1000))