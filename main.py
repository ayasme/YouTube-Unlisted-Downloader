import os
from DownloadUnlisted import YouTubeDownloader

if __name__ == "__main__":
    config = YouTubeDownloader.LoadConfig("config.yaml")

    if config is not None:
        ytd = YouTubeDownloader(config["api-key"], config['cookies'], config["dont-sleep"])

        playlists = config["playlists"]

        root_folder = config["download-folder"]

        output_template = config["output-template"]

        rate_limit = config["rate-limit"]
        if not rate_limit:
            rate_limit = None

        for playlist in playlists:
            videos = ytd.GetPlaylist(playlist)

            filtered_videos = YouTubeDownloader.FilterVideos(videos)

            download_folder = os.path.join(root_folder, playlist)

            if not os.path.exists(download_folder):
                os.mkdir(download_folder)

            ytd.DownloadVideos(download_folder, filtered_videos, output_template, rate_limit)