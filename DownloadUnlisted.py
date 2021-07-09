import os
import shutil
import datetime
import subprocess
import ffmpeg
import yaml
import googleapiclient.discovery

class YouTubeDownloader:
    def __init__(self, apiKey, cookies = None, dont_sleep_path = None):
        #YouTube Data API V3 key
        self.ApiKey = apiKey

        #YouTube cookies for logging in
        if not cookies:
            cookies = None
        self.Cookies = cookies

        #path to Don't Sleep exe
        if not dont_sleep_path:
            dont_sleep_path = None
        self.DontSleepPath = dont_sleep_path

        #ask for username and password
        #self.Username = None
        #self.Password = None
        #username = input("Please input a username and password in order to download private/age-restricted videos (leave blank to skip)\nUsername:")
        #if username:
            #self.Username = username
            #password = input("Password:")
            #if password:
                #self.Password = password

    def LoadConfig(yaml_file):
        if yaml_file is None:
            print("Error! Need a config file.")
            return None

        with open(yaml_file, 'r') as yf:
            config = yaml.safe_load(yf)
            return config

    def UpdateYouTubeDL():
        subprocess.call(['pip', 'install', 'youtube-dl', '--upgrade'])

    def LaunchDontSleep(self):
        if self.DontSleepPath is not None:
            #run don't sleep
            #https://www.softwareok.com/?seite=Microsoft/DontSleep
            dont_sleep = subprocess.Popen([self.DontSleepPath, '-bg', 'block_standby=1', 'block_shutdown=1', 'block_logoff=1', 'block_screensaver=0'], stdin=None, stdout=None, stderr=None, close_fds=True)
            return dont_sleep        
        else:
            return None

    def CloseDontSleep(self):
        subprocess.call([self.DontSleepPath, 'exit'])

    def GetPlaylist(self, playlist):
        #get all videos from playlist
        #https://stackoverflow.com/questions/62345198/extract-individual-links-from-a-single-youtube-playlist-link-using-python
        youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=self.ApiKey)
        request = youtube.playlistItems().list(
                part = "snippet,status",
                playlistId = playlist
        )

        videos = []
        response = request.execute()
        while request is not None:
                response = request.execute()
                videos += response["items"]
                request = youtube.playlistItems().list_next(request, response)

        return videos

    def FilterVideos(videos):
        #filter videos:
        #   must be unlisted
        #   must be uploaded before 1/1/2017

        filtered_videos = []
        for v in videos:
            #check date
            publish_date = v["snippet"]["publishedAt"]
            year = publish_date[0:4]

            #check unlisted status
            status = v["status"]["privacyStatus"]

            if status == "unlisted" and int(year) < 2017:
                #keep this video
                filtered_videos.append(v)

        return filtered_videos

    def DownloadVideos(self, folder, videos, output_template, rate_limit = None):
        #make sure youtube-dl is up to date
        YouTubeDownloader.UpdateYouTubeDL()

        self.LaunchDontSleep()

        for v in videos:
            print('\n')

            id = v["snippet"]["resourceId"]["videoId"]

            ytdl_args = ['youtube-dl', '-o', '{}\{}'.format(folder, output_template), 'https://www.youtube.com/watch?v={}'.format(id), '--write-description', '--write-info-json']

            if rate_limit is not None:
                ytdl_args += ['-r', rate_limit]

            if self.Cookies is not None:
                ytdl_args += ['--cookies', self.Cookies]

            #doesn't work:
            #if self.Username is not None and self.Password is not None:
            #    ytdl_args += ['-u', self.Username, '-p', self.Password]

            subprocess.call(ytdl_args)

        self.CloseDontSleep()

