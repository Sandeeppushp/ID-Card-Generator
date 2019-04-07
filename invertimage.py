from PIL import Image
import PIL.ImageOps    


from os import listdir
from os.path import isfile, join
mypath="."
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
c=[]
num=range(0,len(onlyfiles))
for i in range(0,len(onlyfiles)):
	c.append(num[i])
	c.append(onlyfiles[i])

for i in range(0,len(onlyfiles),2):
        print(str(c[i])+' '+str(c[i+1])+'\n')



file=input('Enter index Eg. 1: ')

temp=c.index(file)
file=c[temp+1]

image = Image.open(file)
inverted_image = PIL.ImageOps.invert(image)
inverted_image.save('new_name.png')

print('\n\nYour image is inverted Successfully')
