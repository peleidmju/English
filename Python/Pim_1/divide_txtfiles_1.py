import glob
import shutil


def rename_mp3():
    files = glob.glob("E:\English\PimsleurNew\Second\mp3\Pimsleur_II_05-*.mp3")
    for file in files:
        new_name = ((file.split('-')[1]).split('.')[0]).zfill(3)
        new_name = file.split('_')[0] + '_35_' + new_name + '.mp3'
        shutil.move(file, new_name)


rename_mp3()
