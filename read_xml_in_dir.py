import pathlib
import os
import xml.etree.ElementTree as ET
import sys

# To use it, put it under the same directory of target directories

#ROOT = "/Users/aemass.yutsungchiu"
#print (pathlib.Path.absolute('.')
#READPATH = "/~/Leo/FubonDecode/part5_queena_anny_unpacked/k2_motion_take2_queena_2020-04-06-14-40-17_unpacked"
READPATH = sys.argv[1]

#inpt = 1586155243531
inpt = int(sys.argv[2])
Metadata_path_list = []

for path in pathlib.Path(READPATH).iterdir():
    if path.is_file():
        if (str(path.suffix) == '.xml'):
            tree = ET.parse(path)
            root = tree.getroot()
            if (root.tag == 'FrameMetadata0'):
                Metadata_path_list.append(path)

Metadata_path_list.sort()
diff = inpt
index = 0

#print the list of timestamp
# for elem in Metadata_path_list:
#     tree = ET.parse(elem)
#     root = tree.getroot()
#     timestamp = root.attrib['timestamp']
#     print (root.attrib['timestamp'])

# Find the closest element
for elem in Metadata_path_list:
    tree = ET.parse(elem)
    root = tree.getroot()
    timestamp = root.attrib['timestamp']
    if (abs(inpt - int(timestamp)) < diff):
        diff = abs(inpt - int(timestamp))
    else:
        break
    index += 1

#output
tree = ET.parse(Metadata_path_list[index-1])
root = tree.getroot()
timestamp = root.attrib['timestamp']
print ('closest TS : ' + timestamp + '\t\t\tframe ID: ' + Metadata_path_list[index-1].name)
        
    

