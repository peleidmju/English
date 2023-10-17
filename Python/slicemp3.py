from pydub import AudioSegment
import librosa
import sys
# # создаём звуковой файл длительностью 5 секунд
# audio = AudioSegment.silent(duration=5000)
# # сохраняем звуковой файл
# audio.export('E:\English\Python\\tempfor\mp3\silence.mp3')
# открываем звуковой файл
audio = AudioSegment.from_file(
    "E:\English\Python\\tempfor\mp3\Pimsleur_I_26.mp3")
# print(sys.path)
# Вырезаем кусок звукового файла от 5 до 10 секунды
audio_slice = audio[78860:86050]

# Сохраняем вырезанный кусок звукового файла
audio_slice.export("sample_slice.mp3", format="mp3")
