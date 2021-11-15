#!/bin/bash

# this script saves arguments as src, dst, file_type and moves files from
#    src to dst. Else it displays error
if [ $# -lt 2 ] || [ $# -gt 3 ]; then
	# anything besides two or three arguments is wrong
	echo "Please submit minimum two directories as arguments"
	echo "> source-directory"
	echo "> destination-directory"
	echo "> file-type (txt, py, java .. ):optional"
else
	# find possible missing directories
	missing_dir=""
	if [ ! -d "$1" ]; then
		# source directory does not exist
		missing_dir="$1"; fi
	if [ ! -d "$2" ] && [ "${missing_dir}" == "" ]; then
		# destination directory does not exist
		echo "$2 does not exist"
		echo "Do you wish to create new directory? (y/yes/Yes/Y/n/no/No/N): "
		read make_dir
		make_dir="${make_dir,,}"
		if [ ${make_dir} == "y" ] || [ ${make_dir} == "yes" ]; then
			# create destination directory
			mkdir $2
		else
			if [ ${make_dir} != "n" ] && [ ${make_dir} != "no" ]; then
				echo "Did not recognize ${make_dir}"; fi
			missing_dir+=" $2"; fi; fi
	if [ "${missing_dir}" != "" ]; then
		echo "At least one directory not found:"${missing_dir}
	else
		# source- and destination directory ready for file moving
		src=$1; dst=$2
		if [ $# -gt 2 ]; then
			file_type=$3
			# Reason why I use cd and cd .. :
			# I want to save name of the files-to-be-moved without /source_directory
			# ex: fil.txt fil2.txt instead of src/fil1.txt src/fil2.txt
			# Therefore I manually go in and out with the cd command
			cd ${src}
			files=$(ls *.${file_type})
			cd ..
		else
			files=$(ls ${src}); fi; fi

		# move elements in $files from src to dst
		for file in ${files}; do
		    mv "${src}/"${file} ${dst}
		    echo "Moved ${file} to ${dst}"; done; fi;