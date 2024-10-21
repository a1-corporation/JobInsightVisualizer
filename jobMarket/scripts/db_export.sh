#!/bin/bash

DB_PATH="db.sqlite3"
FILE_PATH="data/backup/"
TABLE_PREFIX="jobMarket_"
TABLES_TO_EXPORT=('company' 'jobposting' 'jobsubtype' 'jobsupersubassociation' 'jobsupertype' 'location' 'platform' 'rawfile' 'skill' 'requirement' 'skillcategory')

for table in "${TABLES_TO_EXPORT[@]}"
do
  echo "Creating csv file for $table"
  TABLE_NAME="${TABLE_PREFIX}${table}"
  OUTPUT_CSV="${FILE_PATH}/${TABLE_PREFIX}${table}.csv"
  sqlite3 "$DB_PATH" <<EOF
.headers on
.mode csv
.output $OUTPUT_CSV
SELECT * FROM $TABLE_NAME;
.output stdout
EOF
done
