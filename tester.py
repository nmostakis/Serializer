from fromXmlToCsv import xmlcsv
from fromXmlToJson import xmljson
from fromXmlToYaml import xmlyaml


xmljson("cerial.xml", "parsed.json")
xmlyaml("cerial.xml", "parsed.yaml")
xmlcsv("cerial.xml", "parsed.csv")
