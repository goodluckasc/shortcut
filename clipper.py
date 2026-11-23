import subprocess
from pathlib import Path

def cut_and_crop(input_video, start, end, out_path):
    """Cut a segment and crop it to 9:16 vertical (1080x1920)."""
    vf = "crop=ih*9/16:ih,scale=1080:1920"
    cmd = [
        "ffmpeg", "-y",
        "-ss", start, "-to", end,
        "-i", str(input_video),
        "-vf", vf,
        "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-c:a", "aac",
        str(out_path),
    ]
    subprocess.run(cmd, check=True)
    return Path(out_path)
