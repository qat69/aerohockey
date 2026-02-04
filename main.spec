# -*- mode: python ; coding: utf-8 -*-

import os

current_dir = os.getcwd()

a = Analysis(
    ['main.py'],
    pathex=[current_dir],
    binaries=[],
    datas=[
        ('assets/sounds', 'assets/sounds'),
        ('view', 'view'),
        ('constants.py', '.'),
        ('controller', 'controller'),
        ('model', 'model'),
    ],
    hiddenimports=[
        'view',
        'view.menu',
        'view.other_module',

        'constants',
        'arcade',
        'pyglet',
        'pyglet.media',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Game',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.ico'] if os.path.exists('icon.ico') else None,
)