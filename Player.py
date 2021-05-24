from pygame import mixer

import os
import json

import threading
import time

class Player:
    root = 'e:/'
    paused = False
    _album = 0
    _song = 0

    @property
    def path(self):
        return self.root+self.albums[self._album]+'/'+self.songs[self._song]

    @property
    def album(self):
        return self._album

    @album.setter
    def album(self, value):
        if value < 0:
            self._album = len(self.albums)-1
        elif value > len(self.albums)-1:
            self._album = 0
        else:
            self._album = value
        print(self.albums[self._album])
        #load songs from album
        self._song = 0
        self.songs = os.listdir(self.root+self.albums[self._album])

    @property
    def song(self):
        return self._song

    @song.setter
    def song(self, value):
        if value < 0:
            self.album -= 1
            self._song = len(self.songs)-1
        elif value > len(self.songs)-1:
            self.album += 1
            self._song = 0
        else:
            self._song = value

    def __init__(self):
        mixer.init()

        # get albums
        if os.path.exists(self.root+'Music'):
            self.root=self.root+'Music/'
        elif os.path.exists(self.root+'Hudba'):
            self.root=self.root+'Hudba/'
        else:
            raise Exception('Error: root directory not found.')

        self.albums = os.listdir(self.root)
        self.albums.sort()
        print(self.albums)

        if len(self.albums) == 0:
            raise Exception('Error: no songs.')

        # get last song
        if os.path.isfile('player.config'):
            f = open("player.config", "r")
            data=json.load(f)
            self.album = data['Album']
            self.song  = data['Song']
            f.close()
        else:
            self.songs = os.listdir(self.root+self.albums[0])

    def play_loop(self):
        while(True):
            if os.path.isfile(self.path):
                self.play()
                # wait while playing
                while(mixer.music.get_busy() or self.paused):
                    time.sleep(2)
                mixer.music.unload()
            
            # next song
            self.song += 1

    def play(self):
        print(self.songs[self.song])
        mixer.music.load(self.path)
        mixer.music.play()

        f = open("player.config", "w")
        json.dump({ 'Album':self.album, 'Song':self.song }, f)
        f.close()

    def stop(self):
        mixer.music.stop()
        mixer.music.unload()

    def pause(self):
        if self.paused:
            mixer.music.unpause()
            self.paused=False
        else:
            mixer.music.pause()
            self.paused=True

    def next(self):
        self.stop()
        self.song += 1
        self.play()

    def prev(self):
        self.stop()
        self.song -= 1
        self.play()

    def next_a(self):
        self.stop()
        self.album += 1
        self.play()

    def prev_a(self):
        self.stop()
        self.album -= 1
        self.play()

    def start(self):
        th = threading.Thread(target=p.play_loop)
        th.start()

        switcher={
                'pause':self.pause,
                'n':self.next,
                'p':self.prev,
                'na':self.next_a,
                'pa':self.prev_a,
                'stop':self.stop
                }

        while(True):
            c = input('')
            func=switcher.get(c,lambda :'Invalid')
            func()


## Test
p = Player()
p.start()
