import os, random, shutil
def moveFile(fileDir):
        pathDir = os.listdir(fileDir)
        filenumber=len(pathDir)
        count=0
        rate=0.1
        picknumber=int(filenumber*rate)
        sample = random.sample(pathDir, picknumber)
        print (sample)
        for name in sample:
            if count < 390:
                if name.endswith(".jpg"):
                    try:
                        shutil.move(fileDir + name, tarDir+name)
                        shutil.move(fileDir + name.split('.')[0] + ".xml", tarDir+name.split('.')[0] + ".xml")
                        count = count +1
                    except:
                        count=count
                elif name.endswith(".xml"):
                    try:
                        shutil.move(fileDir + name, tarDir+name)
                        shutil.move(fileDir + name.split('.')[0] + ".jpg", tarDir+name.split('.')[0] + ".jpg")
                        count = count +1
                    except:
                        count=count
                print(count)
                    
        return

if __name__ == '__main__':
	fileDir = "/home/terry/tensorflow/models-master/research/object_detection/image_cut/train"
	tarDir = '/home/terry/tensorflow/models-master/research/object_detection/image_cut/test'
	moveFile(fileDir)
