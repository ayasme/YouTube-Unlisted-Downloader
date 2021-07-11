# YouTube-Unlisted-Downloader
Script for downloading unlisted YouTube videos before they are made private on July 23rd, 2021. Requires [Python 3](https://www.python.org/) and [pip](https://pypi.org/project/pip/).

## Usage
Download the latest release and extract it. In the same folder as the script, create a config.yaml file that includes the following information. See [example_config.yaml](example_config.yaml) for an example.

| Key | Value |
| --- | --- |
| api-key | [YouTube Data API V3](https://developers.google.com/youtube/v3/getting-started) key used for getting playlist info. |
| download-folder | Path for downloaded files. |
| playlists | Playlist IDs to download. |
| output-template | youtube-dl [output template](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#output-template) (for naming files). |
| cookies | Path to cookies file (optional). See the youtube-dl [documentation](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#how-do-i-pass-cookies-to-youtube-dl) for details. Use this if you need to download age-restricted videos. |
| rate-limit | [Rate limit](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#download-options) for youtube-dl (optional). |
| dont-sleep | Path to [Don't Sleep](https://www.softwareok.com/?seite=Microsoft/DontSleep) exe (optional). Running this program will prevent your computer from going to sleep while videos are downloading. |


Run main.py to download all pre-2017 unlisted videos from the playlists included in config.yaml. Video descriptions and metadata will be downloaded as well.
[youtube-dl](https://github.com/ytdl-org/youtube-dl) for Python will be installed if it is not already present.
