#!/bin/bash

archive_dir="archive"

if [ ! -d "$archive_dir" ]; then
#check if the archive directory exists or not, if not create it."
        echo "Archive directory not found. Creating '$archive_dir' "
        mkdir "$archive_dir"
fi

logs=organizer.log

#loop for csv files.
for file in *.csv; do
#skips is a csv file is not found.
        [ -e "$file" ] || continue
#log action.
        timestamp=$(date '+%Y%m%d-%H%M%S')
        new="${file%.csv}-${timestamp}.csv"

        {
                echo "Archived File: $file"
                echo "New name: $new"
                echo "Time: $timestamp"
        } >> $logs

#move and rename
        mv "$file" "$archive_dir/$new"

        echo " '$file' is archived in $archive_dir/$new' "
done