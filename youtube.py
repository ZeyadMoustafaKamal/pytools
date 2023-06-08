from pytube import YouTube
from pytools import update_arguments
from pytube.exceptions import RegexMatchError

update_arguments('download_youtube',{'-u':'url','-d':'directory','--a':'audio_only','-r':'resolution'})

def download_youtube(*args,**kwargs):
    url = kwargs.get('url')
    if not url:
        raise ValueError('you have to pass a url')
    resolution = kwargs.get('resolution')
    direcory = kwargs.get('directory')
    audio_only = kwargs.get('audio_only')

    try:
        youtube = YouTube(url, on_progress_callback=on_progress_callback, on_complete_callback=on_complete_callback)
    except RegexMatchError:
        print('Not a valid url')
        return
    if audio_only:
        youtube.streams.get_audio_only().download(direcory)
        return
    if not resolution:
        youtube.streams.get_highest_resolution().download(direcory)
        return
    
    itags = {
        '720':22,
        '360':18,
        '1080':137,
        '480':135
    }
    if not resolution in itags:
        print('invalid resolution')
        return
    youtube.streams.get_by_itag(itags[resolution]).download(direcory)



# the two functions is used in download_youtube_As_video

def on_progress_callback(stream, chunk, bytes_remaining):
    # Calculate and display the download progress
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    progress = (bytes_downloaded / total_bytes) * 100
    print(f"Download progress: {progress:.2f}%")

def on_complete_callback(stream, file_path):
    # Handle completion of the download
    print(f"Download completed! File saved at: {file_path}")

