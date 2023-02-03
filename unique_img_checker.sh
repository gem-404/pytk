#!/bin/bash

: This checks for files in source folder but not in destination folder

sauce=/home/ephantus/sub_anime  # Of course I mean source, as in source folder
destin=/home/ephantus/new_files # Destination folder

ls $destin | cat | cut -d. -f1 | cut -d "-" -f2 | tail -n5
ls $sauce | cat | cut -d. -f1 | tail -n5

