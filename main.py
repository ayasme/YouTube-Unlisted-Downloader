import os
from DownloadUnlisted import YouTubeDownloader

if __name__ == "__main__":
    config = YouTubeDownloader.LoadConfig("config.yaml")

    if config is not None:
        ytd = YouTubeDownloader(config["api-key"], config["dont-sleep"])

        playlists = config["playlists"]

        root_folder = config["download-folder"]

        output_template = config["output-template"]

        rate_limit = config["rate-limit"]
        if not rate_limit:
            rate_limit = None

        videos = []
        for playlist in playlists:
            videos += ytd.GetPlaylist(playlist)

            filtered_videos = YouTubeDownloader.FilterVideos(videos)

            if not os.path.exists(root_folder):
                os.mkdir(root_folder)

            ytd.DownloadVideos(root_folder, filtered_videos, output_template, rate_limit)