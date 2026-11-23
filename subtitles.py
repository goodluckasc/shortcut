import subprocess
from pathlib import Path
from faster_whisper import WhisperModel

def _fmt(t):
    h = int(t // 3600)
    m = int((t % 3600) // 60)
    s = t % 60
    return f"{h:02d}:{m:02d}:{s:06.3f}".replace(".", ",")

def make_srt(video_path, srt_path, model_size="small", language=None):
    model = WhisperModel(model_size, compute_type="int8")
    segments, _ = model.transcribe(str(video_path), language=language)
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, seg in enumerate(segments, start=1):
            f.write(f"{i}\n{_fmt(seg.start)} --> {_fmt(seg.end)}\n{seg.text.strip()}\n\n")
    return Path(srt_path)

def burn_subtitles(video_path, srt_path, out_path):
    style = "FontSize=14,Alignment=2,MarginV=120,Outline=2"
    vf = f"subtitles={srt_path}:force_style='{style}'"
    cmd = ["ffmpeg", "-y", "-i", str(video_path), "-vf", vf, "-c:a", "copy", str(out_path)]
    subprocess.run(cmd, check=True)
    return Path(out_path)
