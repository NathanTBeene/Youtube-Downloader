# YouTube Downloader

This program simply uses the [pytube](https://pytube.io/en/latest/) and [pymovie](https://pypi.org/project/pymovie/) packages to download a YouTube video and either save it as a mp4 or convert it into an mp3.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push
- python 3.12.1
- [pytube](https://pytube.io/en/latest/) - `pip install pytube`
- [pymovie](https://pypi.org/project/pymovie/) - `pip install pymovie`

### Installing and Using

A step by step series of examples that tell you how to get a development
environment running

1. Open up the virtual environment for python 3.12.1 with all the modules installed already.

2. Open `app.py` and run the file.

3. A GUI with a textbox and two buttons labeled mp3 and mp4 should appear.

## Running the tests

Explain how to run the automated tests for this system

### Sample Tests

1. Input a video URL

2. Click either mp4 or mp3 to download the respective file.

3. You will get a notification that the download is complete.

4. You can find the download in the `".\downloads\` and either `\MP4` or `\MP3` 
