#!/bin/bash

# Configuration
CSV_FILE="grades.csv"
ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"

# 1. Archive Directory Check
if [ ! -d "$ARCHIVE_DIR" ]; then
    echo "Archive directory not found. Creating '$ARCHIVE_DIR'..."
    mkdir "$ARCHIVE_DIR"
fi

# 2. Check if the targets grades.csv file exists before running operations
if [ ! -f "$CSV_FILE" ]; then
    echo "Error: Standard file '$CSV_FILE' not found in current workspace."
    exit 1
fi

# 3. Timestamp Generation (Format: YYYYMMDD-HHMMSS)
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# 4. The Archival Process
NEW_FILENAME="grades_${TIMESTAMP}.csv"

# Move and rename original file
mv "$CSV_FILE" "${ARCHIVE_DIR}/${NEW_FILENAME}"

# 5. Workspace Reset (Create a fresh empty grades.csv with headers)
echo "assignment,group,score,weight" > "$CSV_FILE"

# 6. Logging
echo "[${TIMESTAMP}] Archived: ${CSV_FILE} -> ${ARCHIVE_DIR}/${NEW_FILENAME}" >> "$LOG_FILE"

echo "Archiving sequence completed successfully."
echo "Logs preserved in ${LOG_FILE}."
