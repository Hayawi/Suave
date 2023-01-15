import youtube_dl

class download_song:
    
    def download(self,url):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': './downloads/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
