"""
XML Parser
XML Parser for Mount and Blade 2: Bannerlord translation
For commando.com.ua
By Annihilator

If it finds simmilar id's in both files, replaces text argument in first file from second file

Usage:
python parser.py --first --second

--first : Path to first XML
--second : Path to second XML


"""
from os import path
from optparse import OptionParser
import xml.etree.ElementTree as ET

def main(options):

    root = ET.parse(options.first_xml).getroot()
    root2 = ET.parse(options.second_xml).getroot()

    for string in root.findall('strings/string'):
        id = string.get('id')
        text2 = string.get('text')
        for string in root2.findall('strings/string'):
            id2 = string.get('id')
            if (id == id2):
                string.set('text', text2)

    ET.dump(root)
    return 0

if __name__ == "__main__":
    parser = OptionParser(usage="Usage: %prog [options]", version="1.0")
    parser.add_option("--first", dest="first_xml", type="string", help="First XML")
    parser.add_option("--second", dest="second_xml", type="string", help="Second XML")

    (options, args) = parser.parse_args()

    if not path.exists(options.first_xml) or not (options.second_xml):
        print("XML files should exists")
        exit(1)

    exit(main(options))
