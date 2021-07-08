# YouTube-Unlisted-Downloader
Script for downloading unlisted YouTube videos before they are made private on July 23rd, 2021.

## Usage
Create a config.yaml file that includes the following information. See example_config.yaml for an example.

| Key | Value |
| --- | --- |
| api-key | [YouTube Data API V3](https://developers.google.com/youtube/v3/getting-started) key used for getting playlist info. |
| rate-limit | Rate limit for youtube-dl (optional). |
| dont-sleep | Path of the [Don't Sleep](https://www.softwareok.com/?seite=Microsoft/DontSleep) exe (optional). Running this program will prevent your computer from going to sleep while videos are downloading. |
| download-folder | Path for downloaded files. |
| output-template | youtube-dl output template (for naming files). |
| playlists | Playlist IDs to download. |

Run main.py to download all pre-2017 unlisted videos from the playlists included in config.yaml. Video descriptions and metadata will be downloaded as well.
[youtube-dl](https://github.com/ytdl-org/youtube-dl) for Python will be installed if it is not already present.
