import pathlib

FILEWRITTEN = 'writetest.txt'
ROOT = "/Users/aemass.yutsungchiu"
READPATH = ROOT + "/Leo/FubonDecode/part5_queena_anny_unpacked/k2_motion_take1_anny_2020-04-06-14-38-46_unpacked"

#fresh the errorlist
f = open(FILEWRITTEN, 'w')
f.close()
######################
directory_info_dict = {}

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

for keys in directory_info_dict:
    directory_info_dict[keys]['invalid_file'].sort()

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




            


                