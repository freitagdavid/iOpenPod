"""Backward-compatible shim — real code lives in ipod_device/vpd_iokit.py."""
# ruff: noqa: F401, F403
import sys
if sys.platform == "darwin":
    from ipod_device.vpd_iokit import *
else:
    raise ImportError("ipod_iokit_query is macOS-only")
