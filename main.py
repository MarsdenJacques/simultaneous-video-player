import keyboard
import os
os.environ["PATH"] = os.path.dirname('.\lib\mpv-1.dll') + os.pathsep + os.environ["PATH"]
import mpv
from time import sleep

def playerLoop(players):
    print('x')

running = True
player = mpv.MPV()
player2 = mpv.MPV()
players = []
vidsList = os.listdir('vids/')
for vids in vidsList:
    player = mpv.MPV()
    player._set_property('loop', True)
    player._set_property('fullscreen', True)
    player._set_property('snap-window', True)
    player._set_property('border', False)
    players.append(player)
index = 0
while index < len(players):
    players[index].play('vids/' + vidsList[index])
    index = index + 1
while(running):
    if(keyboard.is_pressed('Enter')):
        index = 0
        while index < len(players):
            players[index].seek(0)
            if(players[index]._get_property('pause')):
                players[index]._set_property('pause', False)
            index = index + 1
        sleep(.1)
    if(keyboard.is_pressed('f')):
        index = 0
        while index < len(players):
            fullscreen = players[index]._get_property('fullscreen')
            players[index]._set_property('fullscreen', not fullscreen)
            index = index + 1
        sleep(.1)
    if(keyboard.is_pressed('Space')):
        index = 0
        while index < len(players):
            paused = players[index]._get_property('pause')
            players[index]._set_property('pause', not paused)
            index = index + 1
        sleep(.1)
    if(keyboard.is_pressed('Escape')):
        running = False