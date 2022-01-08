# Snapchat-Memories-Downloader

This script will download each memory in bulk so you don't have to click the download links one by one.
The script downloads only unique photos, and text in photos saved in snapchat won't be present in the downloaded picture (it's an issues from the source).
Some Videos are are merged and may be suffixed as (1), (2), .... and so on

## Requirements

1. Node.js version 10 or higher (https://nodejs.org/)

## How to run

1. Download your Snapchat data: https://support.snapchat.com/en-US/a/download-my-data
2. Extract the zip-file
3. Place all the scripts in this folder OR set the `-f` flag pointing to the `memories_history.json` file
4. Install the required modules with `npm install commander moment utimes`
5. Run the script: `node main.js`

## Optional Arguments

```
Usage: main [options]
A script to download Snapchat Memories
Example:
  node main.js -c 50 -f ./json/memories_history.json -o Downloads
Options:
  -c <number>     Number of concurrent downloads (default: 30)
  -f <path>       Filepath to memories_history.json (default: "./json/memories_history.json")
  -o <directory>  Download directory (default: "Downloads")
  -h, --help      display help for command
```

## Example

![Alt Text](https://i.imgur.com/QVvh3I4.gif)

## Trouble Shooting

1. Make sure you get a fresh zip-file before running the script, links will expire over time
2. `Syntax Compilation Error` -> please have a look at [this](https://github.com/ToTheMax/Snapchat-All-Memories-Downloader/issues/4#issuecomment-664035581) issue
3. Errors with `npm install` or about `utimes`/`moment` module -> please have a look at [this](https://github.com/ToTheMax/Snapchat-All-Memories-Downloader/issues/26#issuecomment-751382700) issue
4. Still problems? please make a new [issue](https://github.com/ToTheiMax/Snapchat-All-Memories-Downloader/issues)
5. Feel free to add me on discord for other questions: ToTheMax#2203
