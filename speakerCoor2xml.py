import xml.etree.ElementTree as ET

def main() :
	file_txt = open("Grove_speaker_locations_final.txt", "r")
	tree = ET.parse('spaceconfig.24.0.xml', OrderedXMLTreeBuilder())
	root = tree.getroot()
	file_txt_data = file_txt.readlines()
	for line in file_txt_data :
		# parse name x y z coor from txt file by line
		split_line = line.split('"')
		# print(split_line[1].replace("Grove-s",""))
		name_txt = str(int(split_line[1].replace("Grove-s","")))
		# print(name_txt)
		x_coor_txt = split_line[3]
		y_coor_txt = split_line[5]
		z_coor_txt = split_line[7]
		# iterate through xml
		for neighbor in root.iter('speaker'):
			if name_txt == neighbor.attrib['name']:
				neighbor.set('x', str(x_coor_txt))
				neighbor.set('y', str(y_coor_txt))
				neighbor.set('z', str(z_coor_txt))
				neighbor.set('name', str(neighbor.attrib['name']))
	print("end parsing")
	print("close txt file")
	file_txt.close()
	print("creating new xml file")
	tree.write('new.xml')


if __name__ == "__main__":
	main()