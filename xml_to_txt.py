import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

def xml_to_txt(path):
    name = ""
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            detect = member[0].text
            place_xmin = member[4][0].text
            place_ymin = member[4][1].text
            place_xmax = member[4][2].text
            place_ymax = member[4][3].text
            filename = (root.find('filename').text).split('.')
            if filename[0] != name:
                text_file = open('buffer/'+filename[0]+'.txt',"w+")
                text_file.write(detect+' '+place_xmin+' '+place_ymin+' '+place_xmax+' '+place_ymax)
                text_file.write('\n')
                text_file.close()
            else:
                myfile = open('buffer/'+filename[0]+'.txt', 'a+')
                myfile.write(detect+' '+place_xmin+' '+place_ymin+' '+place_xmax+' '+place_ymax)
                myfile.close()
            name = filename[0]
            

def main():
    for folder in ['test']:
        image_path = os.path.join(os.getcwd(), (folder))
        xml_to_txt(image_path)
        print('Successfully converted xml to txt.')
main()
