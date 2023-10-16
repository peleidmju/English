import re
import os
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
import sqlite3


class Cours:
    BD_PUTH = 'E:\\English\\Python\\tempfor\\sqlite_db.db'

    def __init__(self, cours) -> None:
        self.__cours = cours
        self.__parent_folder = None

    def __str__(self) -> str:
        return self.__cours

    @property
    def cours(self):
        return self.__cours

    @property
    def parent_folder(self):
        return self.__parent_folder

    @parent_folder.setter
    def parent_folder(self, parent_folder):
        self.__parent_folder = parent_folder
        pass

    def row_cours_table(self, lesson=None):
        querty = (f"SELECT * FROM courses WHERE cours = '{self.cours}'")
        if lesson:
            querty += f" AND lesson = '{lesson}'"
        with sqlite3.connect(self.BD_PUTH) as conn:
            cursor = conn.cursor()
            rows = cursor.execute(querty).fetchall()
        if rows:
            if lesson:
                return rows[0]
            else:
                return rows
        else:
            return None


# pimsl = Cours('Pimsler English')
# pimsl.parent_folder = 'E:\English\PimsleurNew'
# a = pimsl.row_cours_table('Lesson_129')


class Lesson:
    def __init__(self, cours, lesson) -> None:
        self.__lesson = lesson
        self.__cours = cours
        self.mp3shorts = []

    def __str__(self) -> str:
        return self.__cours.__str__() + '_' + self.__lesson

    @property
    def cours(self):
        return self.__cours

    @cours.setter
    def cours(self, cours):
        self.__cours = cours

    @property
    def lesson(self):
        return self.__lesson

    @lesson.setter
    def lesson(self, lesson):
        self.__lesson = lesson

    def bd_puth(self):
        return self.__cours.BD_PUTH

    def row_bd(self):
        row = Cours(self.__cours).row_cours_table(self.__lesson)
        return row
        # return next(Cours(self.__cours).row_cours_table(self.__lesson))


class TestOne:
    def __init__(self) -> None:
        pass


class Mp3AskShort:
    """Короткие фрагменты для склейки. Вся информация в тегах mp3(ID).
        title - question.
        artist - cours.
        album - lesson.
        length - размер в миллисекундах
        composer - answer.
        organization - 
        barcode - id в таблице mp3short.
        tracknumber - номер в lessone и файле csv.
        date - дата занесения в базу.
    """

    def __init__(self, path_mp3) -> None:
        if not os.path.exists(path_mp3):
            raise FileExistsError("{} path is not exists".format(path_mp3))
        self._path = path_mp3
        length_str = str(round(self.get_length()*100))
        length_str = {'length': length_str}
        self.mp3tag_save(**length_str)

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
        list_title = self.mp3tag(tag='title')
        return list_title

    @title.setter
    def title(self, new_title):
        dict_title = {}
        dict_title['title'] = new_title
        self.mp3tag_save(**{'title': new_title})

    @property
    def album(self):
        list_album = self.mp3tag(tag='album')
        return list_album

    @album.setter
    def album(self, new_album):
        dict_album = {}
        dict_album['album'] = new_album
        self.mp3tag_save(**{'album': new_album})

    @property
    def artist(self):
        list_artist = self.mp3tag(tag='artist')
        return list_artist

    @artist.setter
    def artist(self, new_artist):
        dict_artist = {}
        dict_artist['artist'] = new_artist
        self.mp3tag_save(**{'artist': new_artist})

    @property
    def isrc(self):
        list_isrc = self.mp3tag(tag='isrc')
        return list_isrc

    @isrc.setter
    def isrc(self, new_isrc):
        dict_isrc = {}
        dict_isrc['isrc'] = new_isrc
        self.mp3tag_save(**{'isrc': new_isrc})

    @property
    def length(self):
        list_length = self.mp3tag(tag='length')
        return list_length

    @length.setter
    def length(self, new_length):
        dict_length = {}
        dict_length['length'] = new_length
        self.mp3tag_save(**{'length': new_length})

    def mp3tag(self, tag=None, value_tag=None):
        if not tag is None:
            list_tag = MP3(self.path, ID3=EasyID3)
            if tag in list_tag:
                if isinstance(list_tag[tag], list):
                    if list_tag[tag]:
                        return list_tag[tag][0]
                    else:
                        return None
                else:
                    return list_tag[tag]
            else:
                return None
        return MP3(self.path, ID3=EasyID3)

    def mp3tag_save(self, **kwargs):
        new_MP3 = self.mp3tag()
        for k, v in kwargs.items():
            new_MP3[k] = v
        new_MP3.save()

    def get_length(self):
        f = MP3(self.path)
        return (f.info.length)
