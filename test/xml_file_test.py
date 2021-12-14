import unittest
import sys
import os

from fromcsvtoxml import create_csvobject_tree
sys.path.append(os.path.abspath("C:/git/serializer/"))
sys.path.append(os.path.abspath("C:/git/serializer/input/"))
from fromXmlToYaml import xmlyaml
from xmlcreator import xml_tester
from fromXmlToYaml import xmlyaml
from fromXmlToJson import xmljson
from fromXmlToCsv import xmlcsv
import xml.etree.ElementTree as ET
import uuid
import logging
import datetime



logging.basicConfig(filename="C:/git/serializer/test/debugtest.log", encoding="utf-8", level=logging.DEBUG)

class Test_xmlcreator(unittest.TestCase):
    
    def test_xmlcreator_correct(self) ->  None:
        """
        [Test Funktion für die xml_tester Funktion.
        Überpfüft Funktionalität der Funktion auf Korrekte eingaben.
        Erwartete Rückgabewert der testerfunktion 'True']
        """        
        tree = ET.parse("C:/git/serializer/input/cerial.xml")
        root = tree.getroot()
        
        result = xml_tester(root)
        self.assertTrue(result)
    
    def test_xmlcreator_incorrect(self) ->  None:
        """
        [Testfunktion XML Dateien mit inkorrektem Inhalt.
        Erwarteter Rückgabewert der testerfunktion 'False']
        """        
        tree = ET.parse("C:/git/serializer/test/false_content.xml")
        root = tree.getroot()
       
        result = xml_tester(root)
        self.assertFalse(result)  # should return as False

    def test_xmlcreator_NoneType(self) ->  None:
        """
        [Test Funktion für die xml_tester Funktion mit dem eingabewert None.
        Erwartetes verhalten der Funktion ist eine Konsolenausgaben und der Rückgabewert 'False']
        """        
        result = xml_tester(None)
        self.assertTrue(sys.stdout)
        self.assertFalse(result)
        

class Test_fromXmlToYaml(unittest.TestCase):
    
    def test_xmlYaml_none(self) ->  None:
        """
        [Test für die xmlYaml Funktion. mit ausgabeparameter 'None'
        Erwartetes Verhalten der Funktion: Konsolenausgabe ]
        """        
        xmlyaml("C:/git/serializer/test/cerial.xml",None)
        guid = uuid.uuid4()
        guid = str(guid)
        self.assertTrue(sys.stdout)
        self.assertFalse(os.path.exists("C:/git/serializer/test/YamlOutTest-"+guid+".yaml"))
    
    def test_none_xmlYaml(self) ->  None:
        guid = uuid.uuid4()
        guid = str(guid)
        xmlyaml(None,"YamlOutTest.yaml")
        self.assertTrue(sys.stdout)
        self.assertFalse(os.path.exists("C:/git/serializer/test/YamlOutTest-"+guid+".yaml"))
        
    def test_xml_to_yaml(self) ->  None:
        guid = uuid.uuid4()
        guid = str(guid)
        xmlyaml("C:/git/serializer/test/cerial.xml", "C:/git/serializer/test/YamlOutTest-"+guid+".yaml")
        self.assertTrue(os.path.exists("C:/git/serializer/test/YamlOutTest-"+guid+".yaml")); logging.debug(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" YamlOutTest-"+guid+".yaml was created")
        os.remove("C:/git/serializer/test/YamlOutTest-"+guid+".yaml"); logging.debug(str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))+" YamlOutTest-"+guid+".yaml was deleted")
    
class Test_fromXmlToCsv(unittest.TestCase):
    
    def test_xmlcsv_none(self) ->  None:
        guid = uuid.uuid4()
        guid = str(guid)
        xmlcsv("C:/git/serializer/test/cerial.xml",None)
        self.assertTrue(sys.stdout)
        self.assertFalse(os.path.exists("C:/git/serializer/test/CsvOutTest-"+guid+".csv"))
    
    def test_none_xmlcsv(self) ->  None:
        guid = uuid.uuid4()
        guid = str(guid)
        xmlcsv(None,"CsvOutTest.csv")
        self.assertTrue(sys.stdout)
        self.assertFalse(os.path.exists("C:/git/serializer/test/CsvOutTest-"+guid+".csv"))
        
    def test_xml_to_csv(self) ->  None:
        guid = uuid.uuid4()
        guid = str(guid)
        xmlcsv("C:/git/serializer/test/cerial.xml", "C:/git/serializer/test/CsvOutTest-"+guid+".csv")
        self.assertTrue(os.path.exists("C:/git/serializer/test/CsvOutTest-"+guid+".csv"))
    
    
class Test_fromXmlTojson(unittest.TestCase):
    
    def test_xmljson_none(self) ->  None:
        guid = uuid.uuid4()
        guid = str(guid)
        xmljson("C:/git/serializer/test/cerial.xml",None)
        self.assertTrue(sys.stdout)
        self.assertFalse(os.path.exists("C:/git/serializer/test/JsonOutTest-"+guid+".json"))
    
    def test_none_xmljson(self) ->  None:
        guid = uuid.uuid4()
        guid = str(guid)
        xmljson(None,"C:/git/serializer/test/JsonOutTest.json")
        self.assertTrue(sys.stdout)
        self.assertFalse(os.path.exists("C:/git/serializer/test/JsonOutTest-"+guid+".json"))
        
    def test_xml_to_json(self) ->  None:
        guid = uuid.uuid4()
        guid = str(guid)
        xmljson("C:/git/serializer/test/cerial.xml", "C:/git/serializer/test/JsonOutTest-"+guid+".json")
        self.assertTrue(os.path.exists("C:/git/serializer/test/JsonOutTest-"+guid+".json"))
    

class Test_fromCsvToxml(unittest.TestCase):
    def test_csv_to_xml_none(self) ->    None:
        guid = uuid.uuid4()
        guid = str(guid)
        item = create_csvobject_tree(None)
        self.assertIsNot(type(item), object)
    
    
    
    
if __name__ == '__main__':
    unittest.main()
