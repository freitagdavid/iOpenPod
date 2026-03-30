"""Backward-compatible shim — real code lives in ipod_device/scanner.py."""
# ruff: noqa: F401, F403
from ipod_device.scanner import *
from ipod_device.scanner import (
    _extract_guid_from_instance_id,
    _get_drive_letters,
    _has_ipod_control,
    _get_disk_info,
    _find_ipod_volumes,
    _identify_via_usb_for_drive,
    _identify_via_direct_ioctl,
    _walk_device_tree,
    _probe_hardware_macos,
    _probe_hardware_linux,
)
