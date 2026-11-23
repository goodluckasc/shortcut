import sys
import yaml
from pathlib import Path
from clipper import cut_and_crop
from subtitles import make_srt, burn_subtitles

def main(config_path="config.yaml"):
    cfg = yaml.safe_load(open(config_path, encoding="utf-8"))
    out_dir = Path(cfg["output_dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    lang = None if cfg.get("language", "auto") == "auto" else cfg["language"]

    for clip in cfg["clips"]:
        raw = out_dir / f"{clip['name']}_raw.mp4"
        final = out_dir / f"{clip['name']}.mp4"
        cut_and_crop(cfg["input_video"], clip["start"], clip["end"], raw)
        if cfg.get("subtitles", True):
            srt = out_dir / f"{clip['name']}.srt"
            make_srt(raw, srt, cfg.get("whisper_model", "small"), lang)
            burn_subtitles(raw, srt, final)
            raw.unlink()
        else:
            raw.rename(final)
        print(f"Done: {final}")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "config.yaml")
