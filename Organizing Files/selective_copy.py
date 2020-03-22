# Write a program that walks through a folder tree
# and searches for files with a certain file extension (such as .pdf or .jpg).
# Copy these files from whatever location they are in to a new folder.

import os, shutil


def selectiveCopy(folder, extensions, destFolder):
	folder = os.path.abspath(folder)
	destFolder = os.path.abspath(destFolder)
	print('Looking in', folder, 'for files with extensions of', ', '.join(extensions))
	for foldername, subfolders, filenames in os.walk(folder):
		for filename in filenames:
			name, extension = os.path.splitext(filename)
			if extension in extensions:
				fileAbsPath = foldername + os.path.sep + filename
				print('Coping', fileAbsPath, 'to', destFolder)
				shutil.copy(fileAbsPath, destFolder)

extensions = ['.pdf', '.jpg']
folder = '/home/luke/tmp'
destFolder = '/home/luke/tmp2'
selectiveCopy(folder, extensions, destFolder)