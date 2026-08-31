# lexoffline.spec — PyInstaller build spec for LexOffline CPC.
#
# Build with:  pyinstaller lexoffline.spec
# (not `pyinstaller main.py` directly — that would ignore the `datas` list
# below and ship a broken executable with no database inside it.)
#
# Produces a single-file executable containing the Python interpreter,
# PySide6/Qt, and cpc_1908.db bundled together. db.py's _resource_dir()
# knows how to find the bundled database at runtime via sys._MEIPASS.

import sys

block_cipher = None

a = Analysis(
    ["main.py"],
    pathex=[],
    binaries=[],
    # (source_path, destination_folder_within_bundle) — '.' means the
    # bundle's root, matching where db.py's _resource_dir() looks for it.
    datas=[
        ("cpc_1908.db", "."),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="LexOfflineCPC",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,          # no terminal window on Windows/macOS
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    # icon="assets/icon.ico",  # uncomment once an app icon exists
)

# On macOS, a onefile EXE alone is a bare Unix executable — not something a
# non-technical user can double-click in Finder without first using
# Terminal (chmod +x, then run it there). Wrapping it in a proper .app
# bundle makes it launchable the normal macOS way, matching what Windows
# users get with a plain .exe.
if sys.platform == "darwin":
    app = BUNDLE(
        exe,
        name="LexOfflineCPC.app",
        icon=None,  # add a .icns path here once an app icon exists
        bundle_identifier="com.advadil.lexofflinecpc",
    )
