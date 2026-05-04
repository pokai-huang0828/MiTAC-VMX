"""Batch-fetch every source detail from the current notebook and save to sources/*.txt."""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
CLI = r"c:/Users/pokai.huang/AppData/Local/Programs/Python/Python312/Scripts/notebooklm.exe"
INDEX = HERE / "sources" / "_index.json"
OUT_DIR = HERE / "sources"

def safe(name: str) -> str:
    name = re.sub(r'[\\/:*?"<>|\r\n\t]+', "_", name).strip()
    return name[:120] if len(name) > 120 else name

def main() -> int:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    env = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
    failures = []
    for s in data["sources"]:
        idx = s["index"]
        sid = s["id"]
        title = safe(s["title"])
        fname = f"{idx:02d}_{title}.txt"
        target = OUT_DIR / fname
        if target.exists() and target.stat().st_size > 0:
            print(f"  [skip] {fname}")
            continue
        print(f"  [get ] #{idx} {title[:60]}")
        result = subprocess.run(
            [CLI, "source", "get", sid],
            capture_output=True, env=env, text=True, encoding="utf-8",
        )
        if result.returncode != 0:
            failures.append((idx, sid, title, result.stderr.strip()[:300]))
            target.write_text(
                f"# ERROR fetching source {sid}\n\nstderr:\n{result.stderr}\n",
                encoding="utf-8",
            )
            continue
        target.write_text(result.stdout, encoding="utf-8")
    print(f"\nDone. {len(data['sources'])} sources, {len(failures)} failures.")
    for idx, sid, title, err in failures:
        print(f"  FAIL #{idx} {title}: {err}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
