from sys import flags, prefix
from fromXmlToCsv import xmlcsv
from fromXmlToJson import xmljson
from fromXmlToYaml import xmlyaml
from classes.collection import ArgumentError
import argparse


parser = argparse.ArgumentParser(description="converts files into different formats (xml, json, yaml, csv)")
metavar_converter = ["yaml","xml","csv","json"]
parser.add_argument("input_filepath", metavar="input", type=str, help="filepath of file that you want to convert")
parser.add_argument("output_filepath", metavar="output", type=str, help="Path of where the converted file should be placed")
parser.add_argument_group(metavar_converter)




parser.parse_args()
print(parser)