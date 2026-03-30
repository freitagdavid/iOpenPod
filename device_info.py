"""Backward-compatible shim — real code lives in ipod_device/info.py."""
# ruff: noqa: F401, F403
from ipod_device.info import *
from ipod_device.info import (
    _estimate_capacity_from_disk_size,
    _Store,
    _populate_fields_from_sysinfo,
    _enrich_from_sysinfo_extended,
    _parse_sysinfo_artwork_formats,
    _enrich_from_hardware_probe,
    _enrich_from_usb_vpd,
    _enrich_from_serial_lookup,
    _enrich_from_windows_registry,
    _enrich_from_itunesdb_header,
    _resolve_checksum_type,
    _enrich_artwork_from_artworkdb,
)
