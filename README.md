### youtube-downloader

You will need python 3.3+ to run this module.

First Install the dependencies using this command:

```
$ pip install -r requirements.txt
```

## Individual videos

If you want to download individual youtube videos 

put the links in a text folder (i.e. url.txt as provided)

Then run this command
```
$ python y2d.py <url> <folderName>
```
or
 ```
$ python3 y2d.py <url> <folderName>
```
Here, folderName is the folder name where you wish to put your downloaded videos.

If the folder doesn't exist a new folder with the provided name (folderName) will be created

And url is the name of the txt file without the extension

## Playlist

To download a whole playlist run this command
```
$ python y2d.py -p <playlistURL>
```  
  or
```  
$ python3 y2d.py -p <playlistURL>
```

```
example: $ python y2d.py -p https://www.youtube.com/playlist?list=PLzH6n4zXuckpfMu_4Ff8E7Z1behQks5ba
```
