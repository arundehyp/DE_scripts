#!/usr/bin/env bash
set -euo pipefail

BASE_NAME="file_5_20250615"

ACCOUNT_BASE=""

SAS_TOKEN=""

SRC_NAME="file_5_20250615_00.zip"

SRC_URL="${Account_BASE}/${SRC_NAME}?${SAS_TOKEN}"

for i in $(seq -w 1 10); do
    DEST_URL="${Account_BASE}/${SRC_NAME}_${i}.zip?${SAS_TOKEN}"
    azcopy copy "$SRC_URL" "$DEST_URL" --overwrite=false
done