import base64
import sys
import xml.etree.ElementTree as ET
import re

def convert(doc_text, file_out):
    with open(file_out, 'wb') as o:
        for line in doc_text.split('\r\n'):
            str = base64.b64decode(line)
            o.write(bytes(str))

def extract(file_in):
    tree = ET.parse(file_in)
    root = tree.getroot()
    re_result = re.search('{(.+)}', root.tag)
    ns = re_result.group(1)
    counter = 0
    for doc in root.findall('.//{' + ns + '}internal-file'):
        file_out = file_in + '_' + str(counter) + '.zip'
        convert(doc.text, file_out)
        counter += 1
            
for arg in sys.argv[1:]:
    extract(arg)