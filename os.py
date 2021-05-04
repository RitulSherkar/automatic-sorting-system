import os 
import shutil
import time 
filesmoved = 0
# This is the path that the code searches the files for
path = 'C:/Users/admin/Downloads'
path1 = path + '/'


l = os.listdir(path)
#STEP-1
# this is ths list of all the directorys you want to sort the item to 
# if you want to add more sorting folder then make a new variable containg the directory of the folder
dir = 'D:\Organiser'
direxe = 'D:/Organiser/exe'
dirpdf = 'D:/Organiser/pdf'
dirtorrent = 'D:/Organiser/torrent'
dirzip = 'D:/Organiser/zip'
dirmp3 = 'D:/Organiser/music'
dirphotos = 'D:/Organiser/photos'
dirmiscellaneous = 'D:/Organiser/miscellaneous '
#STEP-2
#then to make the directory need just copy past this if statement and change the "dir" to the new variable you created in the first step
if not os.path.exists(dir):
    os.mkdir(dir)
    print('organiser created')
if not os.path.exists(direxe):
    os.mkdir(direxe)
    print('exe path created')
if not os.path.exists(dirpdf):
    os.mkdir(dirpdf)
    print('pdf path created')
if not os.path.exists(dirtorrent):
    os.mkdir(dirtorrent)
    print('torrent path created')
if not os.path.exists(dirzip):
    os.mkdir(dirzip)
    print('zip path created')
if not os.path.exists(dirmp3):
    os.mkdir(dirmp3)
    print('music path created')
if not os.path.exists(dirphotos):
    os.mkdir(dirphotos)
    print('photos path created')
if not os.path.exists(dirmiscellaneous):
    os.mkdir(dirmiscellaneous)
    print('miscellaneous path created')
else:
    print ('all directorys are already created')

 

for i in l:
    ext = i.split('.')[1]
    currfile = path1 + i
    if ext == 'pdf':
        shutil.move(currfile ,dirpdf)
        print ('moved pdf')
        filesmoved = filesmoved + 1
    if ext == 'exe':
        shutil.move(currfile ,direxe)
        print ('moved exe')
        filesmoved = filesmoved + 1
    if ext == 'torrent':
        shutil.move(currfile , dirtorrent)
        print('moved torrent')
        filesmoved = filesmoved + 1
    if ext == 'zip':
        shutil.move(currfile , dirzip)
        print('moved zip')
        filesmoved = filesmoved + 1
    if ext == 'mp3':
        shutil.move(currfile , dirmp3)
        print('moved mp3')
        filesmoved = filesmoved + 1
    if ext == 'rar':
        shutil.move(currfile , dirzip)
        print('moved zip')
        filesmoved = filesmoved + 1
    if ext == 'jpg':
        shutil.move(currfile , dirphotos)
        print('moved photos')
        filesmoved = filesmoved + 1
    if ext == 'PNG':
        shutil.move(currfile , dirphotos)
        print('moved photo')
        filesmoved = filesmoved + 1
#STEP-3 
#Copy past this if statement changing "ext == 'extention name'" and the secound variable in the shutil.move statement to the variable you created in step 1
    else:
         shutil.move(currfile , dirmiscellaneous)
         print('moved miscellaneous')
         filesmoved = filesmoved + 1
    

print ('Total files moved :' ,filesmoved)

