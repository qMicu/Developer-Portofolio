import os
import platform
import time
from pathlib import Path
import shutil
import sys
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from win10toast import ToastNotifier
toast = ToastNotifier()
toast.show_toast("Sorter", "The Sorter Started",duration=10)
os.chdir("C:\\Users\\Mihail\\Downloads")
class Int:
    HOME_DIR = str(Path.home())  
    NEW_DIR = str(Path("D:\Descarcari"))
    DOWNLOADS = HOME_DIR + os.sep + 'Downloads' + os.sep  
    DOCUMENTS = NEW_DIR + os.sep + 'Documente' + os.sep  
    PICTURES = NEW_DIR + os.sep + 'Poze' + os.sep  
    VIDEOS = NEW_DIR + os.sep + 'Clipuri' + os.sep  
    MUSIC = NEW_DIR + os.sep + 'Audio' + os.sep  
    TORRENT = NEW_DIR + os.sep + 'Torente' + os.sep
    EXECUTABLES = NEW_DIR + os.sep + 'Executabile' + os.sep
    ARCHIVES = NEW_DIR + os.sep + 'Arhive' + os.sep
    SKINS = NEW_DIR + os.sep + 'Skinuri' + os.sep
    DOC_EXTENSIONS = ['.txt', '.doc', '.docx', '.odt', '.rtf', '.wpd', '.pages', '.msg', '.log', '.tex', '.wps','.xlr', '.xls', '.xlsx', '.pdf']
    PICTURE_EXTENSIONS = ['.bmp', '.dds', '.gif', '.heic', '.jpg', '.png', '.psd', '.pspimage', '.tga', '.thm', '.tif','.tiff', '.yuv', '.3dm', '.3ds', '.max', '.obj', '.ai', ',esp', '.svg', '.jpeg']
    VIDEO_EXTENSIONS = ['.3g2', '.3gp', '.asf', '.avi', '.flv', '.m4v', '.mov', '.mp4', '.mpg', '.rm', '.srt', '.swf','.vob', '.wmv', '.mkv']
    MUSIC_EXTENSIONS = ['.aif', '.iff', '.m3u', '.m4a', '.mid', '.mp3', '.mpa', '.wav', '.wma']
    TORRENT_EXTENSIONS = ['.torrent']
    EXECUTABLES_EXTENSIONS = ['.exe','.msi','.bat']
    ARCHIVES_EXTENSIONS = ['.zip','.7z','.rar']
    SKINS_EXTENSIONS = ['.rmskin']
    CURRENT_TIME = time.ctime(time.time())
def main():
    print('Sorting Document Files... \n')
    for extension in Int.DOC_EXTENSIONS:
        sort(Int.DOCUMENTS, extension)
        sort(Int.DOCUMENTS, extension.upper())
    print('Sorting Picture Files... \n')
    for extension in Int.PICTURE_EXTENSIONS:
        sort(Int.PICTURES, extension)
        sort(Int.PICTURES, extension.upper())
    print('Sorting Video Files... \n')
    for extension in Int.VIDEO_EXTENSIONS:
        sort(Int.VIDEOS, extension)
        sort(Int.VIDEOS, extension.upper())
    print('Sorting Music Files... \n')
    for extension in Int.MUSIC_EXTENSIONS:
        sort(Int.MUSIC, extension)
        sort(Int.MUSIC, extension.upper())
    print('Sorting Torent Files... \n')
    for extension in Int.TORRENT_EXTENSIONS:
        sort(Int.TORRENT, extension)
        sort(Int.TORRENT, extension.upper())
    print('Sorting Executable Files... \n')
    for extension in Int.EXECUTABLES_EXTENSIONS:
        sort(Int.EXECUTABLES, extension)
        sort(Int.EXECUTABLES, extension.upper())
    print('Sorting Archive Files... \n')
    for extension in Int.ARCHIVES_EXTENSIONS:
        sort(Int.ARCHIVES, extension)
        sort(Int.ARCHIVES, extension.upper())
    print('Sorting Skin Files... \n')
    for extension in Int.SKINS_EXTENSIONS:
        sort(Int.SKINS, extension)
        sort(Int.SKINS, extension.upper())
    print('Sorting Files Completed, See Output Log')
def sort(target, ext):
    try:
        for files in os.listdir(Int.DOWNLOADS):
            if files.endswith(ext)  :
                if os.path.isfile(target + files):
                    pass
                else:
                    shutil.move(Int.DOWNLOADS + files, target + files)
                    pass
    except IOError as error:
        pass
if __name__ == '__main__':
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
def on_created(event):
     time.sleep(5)
     main()
def on_deleted(event):
     pass
def on_modified(event):
     time.sleep(5)
     main()
def on_moved(event):
    time.sleep(5)
    main()
my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted
my_event_handler.on_modified = on_modified
my_event_handler.on_moved = on_moved
path = "C:\\Users\\Mihai\\Downloads"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)
my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()