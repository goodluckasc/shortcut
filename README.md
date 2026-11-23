# ShortCut

A free, open source tool that turns a long video into vertical short clips with automatic subtitles. It runs fully on your own computer, so there is no cost and no upload to any server.

## What it does

- Cuts clips from a long video using start and end times you choose.
- Crops each clip to 9:16 vertical format (1080x1920), ready for Shorts, Reels and TikTok.
- Generates subtitles automatically with Whisper and burns them into the video.
- Everything is controlled by one config file, so you never need to edit the code.

## Requirements

- Python 3.10 or newer
- FFmpeg installed and available in your terminal

To check FFmpeg, run `ffmpeg -version`. If it is missing, install it from https://ffmpeg.org/download.html

## Installation

    git clone https://github.com/goodluckasc/shortcut.git
    cd shortcut
    pip install -r requirements.txt

## Usage

1. Put your video inside the `input` folder.
2. Copy `config.example.yaml` to `config.yaml`.
3. Open `config.yaml` and set your video name and the clips you want.
4. Run from the main folder:

       python shortcut/main.py config.yaml

5. Your finished shorts appear in the `output` folder.

## Example config

    input_video: input/my_video.mp4
    output_dir: output
    whisper_model: small
    language: auto
    subtitles: true
    clips:
      - start: "00:01:10"
        end: "00:01:55"
        name: clip1

## Roadmap

- [ ] Background music
- [ ] Auto detection of the best moments
- [ ] Batch mode for many videos
- [ ] Simple graphical interface

## Contributing

Ideas and fixes are welcome. Open an issue to discuss a change, or send a pull request.

## Credits

Built with FFmpeg and faster-whisper.

## License

MIT License. Free to use, modify and share.
