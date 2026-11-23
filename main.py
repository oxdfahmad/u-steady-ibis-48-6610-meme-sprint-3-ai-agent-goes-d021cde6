"""Rogue-agent meme entry for make.fun bounty
u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.

The kit expects exactly one file in the output directory:
    $MAKEFUN_OUTPUT_DIR/entry.png
a whole PNG (or JPEG), at most 1 MiB and at most 1024 x 1024 pixels.

This program copies the finished meme (meme.png, shipped beside this
script) to that location and then verifies the copy against the kit's
gate before reporting success. Standard library only, no network,
no input, deterministic: the same input bytes always produce the
same output bytes.
"""

import hashlib
import os
import shutil
import struct
import sys

SOURCE_NAME = "meme.png"
TARGET_NAME = "entry.png"
MAX_BYTES = 1_048_576
MAX_SIDE = 1024
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def source_path():
    """Absolute path of the meme shipped with this entry."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, SOURCE_NAME)


def output_dir():
    """Output directory from the environment, defaulting to /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def png_dimensions(path):
    """Read width and height out of a PNG's IHDR chunk.

    Returns (width, height), or None when the file is not a PNG
    with a readable IHDR chunk.
    """
    with open(path, "rb") as handle:
        header = handle.read(24)
    if len(header) < 24 or header[:8] != PNG_SIGNATURE:
        return None
    if header[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message):
    print("ERROR: " + message, file=sys.stderr)
    return 1


def verify_entry(dest, src):
    """Check the written file against the kit's gate.

    Returns (ok, detail): ok is True when the file is a readable
    PNG within the size and dimension caps and byte-identical to
    the source meme; detail is a human-readable summary either way.
    """
    size = os.path.getsize(dest)
    if size > MAX_BYTES:
        return False, "entry.png is %d bytes, over the 1 MiB gate" % size

    dimensions = png_dimensions(dest)
    if dimensions is None:
        return False, "entry.png is not a readable PNG file"
    width, height = dimensions
    if width > MAX_SIDE or height > MAX_SIDE:
        return False, (
            "entry.png is %dx%d, over the 1024x1024 gate"
            % (width, height)
        )

    digest = sha256_of(dest)
    if digest != sha256_of(src):
        return False, "entry.png does not match meme.png byte for byte"

    detail = "%dx%d, %d bytes, sha256 %s" % (
        width, height, size, digest[:16],
    )
    return True, detail


def main():
    src = source_path()
    if not os.path.isfile(src):
        return fail("source meme not found: " + src)

    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, TARGET_NAME)

    shutil.copyfile(src, dest)

    ok, detail = verify_entry(dest, src)
    if not ok:
        return fail(detail)

    print("OK: wrote %s (%s)" % (dest, detail))
    return 0


if __name__ == "__main__":
    sys.exit(main())
