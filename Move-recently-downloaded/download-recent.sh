#!/bin/bash

DOWNLOAD_DIR=~/Downloads
TIME=30
DEST_DIR=$(pwd)
find "$DOWNLOAD_DIR" -type f -mmin -"$TIME" -exec mv {} "$DEST_DIR" \;

echo "moved files downloaded within $TIME mins have been moved to $DEST_DIR"

