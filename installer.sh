#!/bin/sh
# ==========================================================
# AIO Image RTLFixer - Universal RTL Rendering Engine
# Developed by: KiaKu_1982
# Telegram: @Rayan_Ku | Channel: @Enigma2_Tutorials
# GitHub: https://github.com/zavyka/AIO-Image-RTLFixer
# ==========================================================

echo "=========================================================="
echo "    Installing AIO Image RTLFixer for DreamOS ARM64       "
echo "=========================================================="

URL="https://github.com/zavyka/AIO-Image-RTLFixer/releases/download/v1.0.0-r0/enigma2-plugin-extensions-aio-image-rtlfixer_1.0.0-r0_arm64.deb"
TMP_DEB="/tmp/rtlfixer.deb"

echo "[1/4] Downloading installation package..."
if which wget >/dev/null 2>&1; then
    wget --no-check-certificate "$URL" -O "$TMP_DEB"
elif which curl >/dev/null 2>&1; then
    curl -k -L "$URL" -o "$TMP_DEB"
else
    echo "Error: Neither wget nor curl found on your receiver."
    exit 1
fi

if [ ! -s "$TMP_DEB" ]; then
    echo "Error: Download failed or file is empty."
    rm -f "$TMP_DEB"
    exit 1
fi

echo "[2/4] Installing package via dpkg..."
dpkg -i "$TMP_DEB"
STATUS=$?

if [ $STATUS -ne 0 ]; then
    echo "[!] Fixing dependencies via apt-get..."
    apt-get update && apt-get install -f -y
    dpkg -i "$TMP_DEB"
fi

echo "[3/4] Cleaning up temporary files..."
rm -f "$TMP_DEB"

echo "[4/4] Restarting Enigma2 to apply changes..."
if which systemctl >/dev/null 2>&1; then
    systemctl restart enigma2
else
    init 4 && sleep 2 && init 3
fi

echo "=========================================================="
echo "  AIO Image RTLFixer has been successfully installed!     "
echo "=========================================================="
exit 0
