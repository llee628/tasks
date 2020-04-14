import pathlib
import xml.etree.ElementTree as ET
import datetime
import time
import sys


FILEWRITTEN = 'directory_info.txt'
CURRENT_PATH = str(pathlib.Path().absolute())
#READPATH = ROOT + "/Leo/FubonDecode/part5_queena_anny_unpacked/k2_motion_take2_anny_2020-04-06-14-40-22_unpacked"
READPATH = CURRENT_PATH + '/' + sys.argv[1]

print('target directory: ' + READPATH + '\n')

#fresh the writtenfile
f = open(FILEWRITTEN, 'w')
f.write('Target directory: ' + READPATH + '\n\n')
f.close()
######################
directory_info_dict = {}
Metadata_path_list = []

#dictionary: use file extension as keys
for path in pathlib.Path(READPATH).iterdir():
    if path.is_file():
        if (str(path.suffix) in directory_info_dict):
            directory_info_dict[str(path.suffix)]['total_num'] += 1
        else:
            directory_info_dict[str(path.suffix)] = {
                'total_num': 1,
                'invalid_num': 0,
                'invalid_file': []
                }
        if (path.stat().st_size == 0):
            directory_info_dict[str(path.suffix)]['invalid_num'] += 1
            directory_info_dict[str(path.suffix)]['invalid_file'].append(str(path.name))

#sort the file list
for keys in directory_info_dict:
    directory_info_dict[keys]['invalid_file'].sort()

#Build matadata list 
for path in pathlib.Path(READPATH).iterdir():
    if path.is_file():
        if (str(path.suffix) == '.xml'):
            tree = ET.parse(path)
            root = tree.getroot()
            if (root.tag == 'FrameMetadata0'):
                Metadata_path_list.append(path)

Metadata_path_list.sort()

#Find start time
tree = ET.parse(Metadata_path_list[0])
root = tree.getroot()
timestamp = root.attrib['timestamp']
start_time = timestamp
start_time_readable = datetime.datetime.fromtimestamp(int(timestamp)/1000).strftime('%Y-%m-%d %H:%M:%S')

#Find end time
tree = ET.parse(Metadata_path_list[-1])
root = tree.getroot()
timestamp = root.attrib['timestamp']
end_time = timestamp
end_time_readable = datetime.datetime.fromtimestamp(int(timestamp)/1000).strftime('%Y-%m-%d %H:%M:%S')

duration = (int(end_time) - int(start_time))/1000 

#Write start time; end time; duration
with open(FILEWRITTEN, 'a') as the_file:
        the_file.write('Start time: ' + start_time_readable + ' (' + start_time + ')\n')
        the_file.write('End time: ' + end_time_readable + ' (' + end_time + ')\n')
        the_file.write('Duration: ' + str(duration) + ' s\n\n')

#Write the header
for keys in directory_info_dict:
    with open(FILEWRITTEN, 'a') as the_file:
        the_file.write(
            'File type : ' + keys + '\t\t\tTotal number : ' + str(directory_info_dict[keys]['total_num']) +
            '\t\t\tInvalid number : ' + str(directory_info_dict[keys]['invalid_num']) +
            '\t\t\tInvalid rate: ' + str(directory_info_dict[keys]['invalid_num']/directory_info_dict[keys]['total_num'])
            + '\n')

with open(FILEWRITTEN, 'a') as the_file:
    the_file.write('\n******************* Lists of invalid file *******************\n')

for keys in directory_info_dict:
    if (len(directory_info_dict[keys]['invalid_file']) == 0):
        continue
    with open(FILEWRITTEN, 'a') as the_file:
        the_file.write('\nType : ' + keys + '\t\t\tNumbers : ' + str(directory_info_dict[keys]['invalid_num']) + '\n')
    for data in directory_info_dict[keys]['invalid_file']:
        with open(FILEWRITTEN, 'a') as the_file:
            the_file.write(data + '\n')




            


                