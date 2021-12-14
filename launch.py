from sys import flags, prefix
from fromXmlToCsv import xmlcsv
from fromXmlToJson import xmljson
from fromXmlToYaml import xmlyaml
from classes.collection import ArgumentError
import argparse
import pathlib
import os

parser = argparse.ArgumentParser(description="converts files into different formats (from xml to json, yaml, csv)")
metavar_converter = ["yaml","xml","csv","json"]
parser.add_argument("-in", "--input", help="enter Filepath to convert")
parser.add_argument("-out", "--output", help="Choose path to output converted file to")
parser.add_argument("-type", "--conversiontype", help="Choose the type of conversion you want to apply to the file")

args = parser.parse_args()
    
wrongtype = "Conversiontype and file extension of output path must match"

if pathlib.Path(args.input).suffix != ".xml":
    print("File is not a valid .xml file")
elif os.path.exists(args.input):
    if args.conversiontype == "yaml":
        if pathlib.Path(args.output).suffix == args.conversiontype:
            xmlyaml(args.input, args.output)
        else:
            print(wrongtype)
    elif args.conversiontype == "csv":
        if pathlib.Path(args.output).suffix == args.conversiontype:
            xmlcsv(args.input,args.output)
        else:
            print(wrongtype)
    elif args.conversiontype == "json":
        if pathlib.Path(args.output).suffix == args.conversiontype:
            xmljson(args.input, args.output)
        else:
            print(wrongtype)
        
else:
    print("No such file exists")


