import glob
import shutil


def rename_mp3():
    files = glob.glob("E:\English\PimsleurNew\Second\mp3\Pimsleur_35_*.mp3")
    for file in files:
        new_name = ((file.split('_')[2]).split('.')[0]).zfill(3)
        new_name = file.split('_')[0] + '_35-' + new_name + '.mp3'
        shutil.move(file, new_name)


rename_mp3()
