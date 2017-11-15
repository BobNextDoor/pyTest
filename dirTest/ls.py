import sys

def list(dirName):
	import os
	for childDir in os.listdir(dirName):
		childDirPath = os.path.join(dirName,childDir)
		if os.path.isdir(childDirPath):
			list(childDirPath)
		else:
			print(childDirPath)
list(sys.argv[1])
