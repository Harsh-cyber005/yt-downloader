# -*- mode: python ; coding: utf-8 -*-

import os
from PyInstaller.utils.hooks import collect_data_files

# Path to FFmpeg folder relative to the .spec file location
ffmpeg_folder = 'ffmpeg'  # Update this if your FFmpeg folder has a different name or location

a = Analysis(
    ['script.py'],
    pathex=['path_to_your_script'],  # Update this path if needed
    binaries=[
        (os.path.join(ffmpeg_folder, 'ffmpeg.exe'), 'ffmpeg'),  # Ensure this is correct
    ],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='yt-downloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
