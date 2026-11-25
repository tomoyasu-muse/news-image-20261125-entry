#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Entry program for the make.fun news-image-20261125 bounty.

It places one finished picture, entry.png, into the output folder
as /output/entry.png. That picture sums up the world news of
Wednesday 25 November 2026.

The picture is shipped beside this program instead of being drawn
during grading: the grading sandbox has no network access and does
not promise the fonts the page was typeset with. Copying the
rendered file keeps both grading runs identical, byte for byte,
which this bounty requires.

For a local run, set MAKEFUN_OUTPUT_DIR to choose where the file
lands. The picture is 1024 x 1024 and below 1 MiB.
"""

import hashlib
import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
MAX_BYTES = 1_048_576


def locate_image():
    here = Path(__file__).resolve().parent / IMAGE_NAME
    if here.is_file():
        return here
    sandbox_copy = Path("/bot") / IMAGE_NAME
    if sandbox_copy.is_file():
        return sandbox_copy
    raise FileNotFoundError("entry.png not found next to main.py or in /bot")


def output_path():
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(target_dir) / IMAGE_NAME


def main():
    source = locate_image()
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, target)
    payload = target.read_bytes()
    if payload[:8] != b"\x89PNG\r\n\x1a\n" and payload[:2] != b"\xff\xd8":
        raise RuntimeError("entry.png is not a PNG or JPEG image")
    if len(payload) > MAX_BYTES:
        raise RuntimeError("entry.png exceeds the 1 MiB limit")
    digest = hashlib.sha256(payload).hexdigest()
    print(f"wrote {target} ({len(payload)} bytes, sha256 {digest[:16]}...)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
