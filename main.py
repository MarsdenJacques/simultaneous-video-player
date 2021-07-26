import keyboard
import os
os.environ["PATH"] = os.path.dirname('.\lib\mpv-1.dll') + os.pathsep + os.environ["PATH"]
import mpv
from time import sleep

def toggle(players, property):
    index = 0
    while index < len(players):
        toggle = players[index]._get_property(property)
        players[index]._set_property(property, not toggle)
        index = index + 1
    sleep(.1)

running = True
player = mpv.MPV()
player2 = mpv.MPV()
players = []
vidsList = os.listdir('vids/')
for vids in vidsList:
    player = mpv.MPV()
    player._set_property('loop', True)
    player._set_property('fullscreen', False)
    player._set_property('snap-window', True)
    player._set_property('osc', True)
    player._set_property('border', False)
    player._set_property('keep-open', True)
    players.append(player)
index = 0
while index < len(players):
    players[index].play('vids/' + vidsList[index])
    index = index + 1
while(running):
    if(keyboard.is_pressed('Enter')):
        index = 0
        while index < len(players):
            players[index].seek(0,'absolute')
            players[index]._set_property('pause', True)
            index = index + 1
        sleep(.1)
    if(keyboard.is_pressed('l')):
        toggle(players,'loop')
    if(keyboard.is_pressed('f')):
        toggle(players,'fullscreen')
    if(keyboard.is_pressed('Space')):
        toggle(players,'pause')
    if(keyboard.is_pressed('b')):
        toggle(players,'border')
    if(keyboard.is_pressed('s')):
        toggle(players,'snap-window')
    if(keyboard.is_pressed('c')):
        toggle(players,'osc')
    if(keyboard.is_pressed('k')):
        toggle(players,'keep-open')
    if(keyboard.is_pressed('Escape')):
        running = False

        #make toggle, button for osc, snap, and border