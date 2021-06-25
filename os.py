import os 
import shutil

dir = '' # This the folder in which the sorting directories will be created. Add the directory in which you want the files to be sorted
sorA = '' # This is the target folder which the code will sort from. For example the downloads folder
sorter = ['pdf', 'txt' ,'exe']# if you need more sorting directorys just add the extention name 
filePath = sorA + '/'
filesmoved = 0

l = os.listdir(sorA)

if not os.path.exists(dir):
	os.mkdir(dir)
	print('Made the main folder')


for i in l:
	ext = i.split('.')
	currfile = filePath + i
	if len(ext) == 2:
		if len(ext) >= 3:
			x = len(ext) - 1
			ext = ext[x]
		else:
			ext = ext[1]
		if ext in sorter:
			if not os.path.exists(dir  + ext):
				os.mkdir((dir + ext))
				print('Path created :' +(dir + ext))

			shutil.move(currfile ,(dir + ext))
			print('moved :'+ i)
			filesmoved = filesmoved + 1


print(filesmoved)
