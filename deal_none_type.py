import os
from xml_helper import parse_xml

root_path = './Annotations'
# pic_path = './JPEGImages'

lsit_ = []
for parent, _, files in os.walk(root_path):
  for file in files:
    xml_path = os.path.join(parent, file)
    coords = parse_xml(xml_path)
    if coords is None:
      # img_path = pic_path + file[:-4] + 'jpg'
      if os.path.exists(xml_path):
        lsit_.append(file[:-4])
        print('delete xmlfile :%s' % file)
        os.remove(xml_path)
      # if os.path.exists(img_path):
      #   print('delete imgfile :%s' % img_path)
      #   os.remove(img_path)


with open('./nonetype.txt', 'w') as out:
  for item in list_:
    out.writelines(item + '\n')
