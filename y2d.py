import pafy
import os
import re
import sys


def readUrl(fname):
    with open(fname+".txt", "r") as File:
        names = File.read().split("\n")
    # print(names)
    return names


def createPath(path):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, path)
    if not os.path.exists(final_directory):
        os.mkdir(final_directory)
        print(final_directory + " created")
    else:
        print("Directory already Exist")
    return path


def download(names, path):
    for url in names:
        video = pafy.new(url)
        title = video.title
        title = re.sub('[^A-Za-z0-9]+', ' ', title)
        best = video.getbest()
        size = best.get_filesize()
        ext = best.extension

        print("Downloading----> {}".format(title))
        print("size : {:.2f} MB".format(size / (1024*1024)))

        filePath = path + "/" + title + "." + ext

        if (not os.path.exists(filePath)):
            best.download(filePath, quiet=False)
        elif (not os.path.getsize(filePath) == size):
            best.download(filePath, quiet=False)
        else:
            print("Already downloaded")


arg_count = len(sys.argv)

if arg_count > 3:
    print("""
          #usage
          for individual video 
          y2d.py TxtFileName folderToSave]
          for full playlist
          y2d.py -p playlistURL
          """)
    exit

if sys.argv[1] == "-p":
    playlist_url = sys.argv[2]
    playlist = pafy.get_playlist(playlist_url)
    title = re.sub('[^A-Za-z0-9]+', ' ', playlist['title'])
    path = createPath(title)
    for item in playlist['items']:
        video = item['pafy']
        names = []
        names.append(video.videoid)
        download(names, path)
else:
    names = readUrl(sys.argv[1])
    path = createPath(sys.argv[2])
    download(names, path)
