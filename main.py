import keyboard
import os
os.environ["PATH"] = os.path.dirname('D:\Creative\Marsden\Coding Adventures\Python\SimultaneousVideoPlayer\lib\mpv-1.dll') + os.pathsep + os.environ["PATH"]
import mpv
from time import sleep

running = True

player = mpv.MPV()
player2 = mpv.MPV()
players = []
vidsList = os.listdir('vids/')
for vids in vidsList:
    player = mpv.MPV()
    @player.on_key_press('q')
    def my_q_binding():
        player.stop()
    @player.on_key_press('p')
    def my_q_binding():
        paused = player._get_property('pause')
        player._set_property('pause', not paused)
    player._set_property('loop', False)
    players.append(player)
index = 0
while index < len(players):
    players[index].play('vids/' + vidsList[index])
    index = index + 1
sleep(5)
print(vidsList)

#sleep(2) # Or however long you expect it to take to open vlc
#while player. & running:
#    if(keyboard.is_pressed('q')):
#        running = False
#Instance = vlc.Instance('--fullscreen')
#player = Instance.media_player_new()
#Media = Instance.media_new('https://www.youtube.com/watch?v=vDZ9dR2HZ1A')
#Media.get_mrl()
#player.set_media(Media)
#player.play()pip