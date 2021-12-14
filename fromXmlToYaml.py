import ruamel.yaml
import xml.etree.ElementTree as ET
from  classes.collection import my_movie, my_genre, my_collection, my_decade, FileExtensionError, XmlContentError
import pathlib
import sys
import os
sys.path.append(os.path.abspath("C:/git/serializer/"))
sys.path.append(os.path.abspath("C:/git/serializer/input/"))
sys.path.append(os.path.abspath("C:/git/serializer/test/"))
from xmlcreator import create_xml, xml_tester



##  Nimmmt den xmlpfad als ersten wert und den exportpfad der csv datei als zweiten wert parsed die .xml zu einer .yaml datei
def xmlyaml(xml_import_file:str, yaml_parsed_file:str) -> None:
    """[Konvertiert eine XML Datei in ein Objekt woraus eine YAML Datei erstellt wird]

    Args:
        xml_import_file (str): [Dateipfad und Name der XML Datei die in eine Objekt konvertiert werden soll]
        yaml_parsed_file (str): [Dateipfad und Name der YAML Datei die aus dem Objekt erstellt werden soll]

    Raises:
        XmlContentError: [Fehlermeldung wenn die XML Datei nicht korrekt Formatiert ist oder nicht der vorgegebenen Form entspricht]
    """    
    file_in = False
    file_out = False
    try:
        if pathlib.Path(xml_import_file).suffix == ".xml":
            print("No valid inputfile found")
            file_in = True
        if pathlib.Path(yaml_parsed_file).suffix == ".yaml":
            print("No Valid outputfile found")
            file_out = True
    except Exception as x:
        pass
        
    
    if file_in == True and file_out == True:
        tree = ET.parse(xml_import_file)

        testerxml = create_xml()
        test_root = testerxml.getroot()
        
        root = tree.getroot()
        
        tested = xml_tester(root)
        if tested != True:
            print("Test for xml failed")
        else:    
            moviestats = {}
            col = my_collection(genre=[])
            for gen in root:
        
                genr = my_genre(category=gen.attrib["category"], decades=[])
                for decade in gen:
                    dec = my_decade(decade=decade.attrib["years"],movie=[])
                    
                    for movie in decade:
                        mov = my_movie(movie_name=movie.attrib["title"],format_text=None,multiple=None,year=None,rating=None,description=None, favorite=movie.attrib["favorite"])
                        for entry in movie:
                            
                            if entry.tag == "format":
                                mov.format = entry.text
                                moviestats[entry.tag] = entry.text
                            elif entry.tag == "year":
                                mov.year = int(entry.text)
                                moviestats[entry.tag]=entry.text
                            elif entry.tag == "rating":
                                mov.rating = entry.text
                                moviestats[entry.tag]= entry.text
                            elif entry.tag == "description":
                                mov.description = entry.text
                                moviestats[entry.tag] = entry.text  
                            elif entry.tag == "format":
                                mov.format_text = entry.text
                                mov.multiple = entry.attrib
                        if mov.rating=="":
                            raise XmlContentError(mov.rating)
                        dec.movie.append(mov.__dict__)
                        
                        
                    genr.decades.append(dec.__dict__)
                    
                        
                col.genre.append(genr.__dict__)
                
            col = col.__dict__
            
            with open(yaml_parsed_file, "w") as parsed:
                
                ruamel.yaml.dump(col, parsed, default_flow_style=False, indent=4)
        
