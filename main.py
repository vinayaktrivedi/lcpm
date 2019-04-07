import sys
from pathlib import Path
sys.path.insert(0, 'modules/')
import mmap


import check_signature
import md5_check
import custom_filelock

import download_package

import check_dependencies
import remove_package
import update
import upgrade 
import install_package
import search_package

command = sys.argv[1]
if(command == "update" or command == "upgrade"):

elif command == "install" or command == "search" or command == "remove":
	package = sys.argv[2]
	package_file = Path("packages.lock")

	if not package_file.is_file():
		print("could not acqure locks")
		exit(1)
	else:
		try:
			file = open("Packages")
			mmap_object = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
			search_string = "Package: "+package+"\nArchitecture"
			index = mmap_object.find(bytearray(search_string,'utf-8'))
			if  index != -1:
				

		except:
			print("fatal error in opening packages database")
			exit(1)

else:
	print("Invalid Arguments")
	exit(1)
