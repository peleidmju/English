import re
import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3


class Mp3AskShort:

    def __init__(self, path_mp3) -> None:
        if not os.path.exists(path_mp3):
            raise FileExistsError("{} path is not exists".format(path_mp3))
        self._path = path_mp3

    def __str__(self) -> str:
        str_temp_1 = self.title
        str_return = (str_temp_1 if str_temp_1 else '?') + '/'
        str_temp_1 = self.artist
        str_return += (str_temp_1 if str_temp_1 else '?') + '/'
        str_temp_1 = self.album
        str_return += (str_temp_1 if str_temp_1 else '?') + '/'
        str_temp_1 = self.path.rpartition('\\')[2]
        str_temp_1 = str_temp_1[:-4]
        str_return += (str_temp_1 if str_temp_1 else '?') + '/'
        return str_return + 'Mp3AskShort'

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path
        pass

    @property
    def title(self):
        list_title = self.mp3tag()['title']
        return list_title[0]

    @title.setter
    def title(self, new_title):
        dict_title = {}
        dict_title['title'] = new_title
        self.mp3tag_save(**{'title': new_title})

    @property
    def album(self):
        list_album = self.mp3tag()['album']
        return list_album[0]

    @album.setter
    def album(self, new_album):
        dict_album = {}
        dict_album['album'] = new_album
        self.mp3tag_save(**{'album': new_album})

    @property
    def artist(self):
        list_artist = self.mp3tag()['artist']
        return list_artist[0]

    @artist.setter
    def artist(self, new_artist):
        dict_artist = {}
        dict_artist['artist'] = new_artist
        self.mp3tag_save(**{'artist': new_artist})

    def mp3tag(self):
        return MP3(self.path, ID3=EasyID3)

    def mp3tag_save(self, **kwargs):
        new_MP3 = self.mp3tag()
        for k, v in kwargs.items():
            new_MP3[k] = v
        new_MP3.save()

    def length(self):
        f = MP3(self.path)
        return (f.info.length)
