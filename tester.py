import json
from fromXmlToCsv import xmlcsv
from fromXmlToJson import xmljson
from fromXmlToYaml import xmlyaml
from classes.collection import ArgumentError
import sys
import pathlib


# nimmt dateipfad für input und outputfile in variablen und übergibt sie den funktionen 
# 'xmlyaml()' 'xmljson()' 'xmlcsv()'
arguments = sys.argv


convertfiles = ["-yaml","-csv","-json"]
infile = ""
outfile = ""
argfile = ""


index = 0
for arg in arguments:
    if arg == "-in":
        infile = arguments[index+1]
    elif arg == "-out":
        outfile = arguments[index+1]
    elif arg in convertfiles:
        argfile = arguments[index]
    elif arg.endswith(".yaml") or arg.endswith(".xml") or arg.endswith(".csv") or arg.endswith(".json"):
        x=1
    elif arg == arguments[0]:
        x=1
    index += 1


        
    
    


if argfile == "-yaml":
    xmlyaml(infile, outfile)
elif argfile == "-json":
    xmljson(infile, outfile)
elif argfile == "-csv":
    xmlcsv(infile, outfile)

