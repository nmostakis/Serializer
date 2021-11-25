import json
from xml.etree.ElementTree import ParseError
from  classes.collection import FileExtensionError, RootNodeError, XmlContentError, my_movie, my_genre, my_collection, my_decade
import pathlib
import defusedxml.cElementTree as ET
from xmlcreator import create_xml, xml_tester



##  Nimmmt den xmlpfad als ersten wert und den exportpfad der csv datei als zweiten wert parsed die .xml zu einer .csv datei
def xmljson(xml_import_file, json_parsed_file):
    if pathlib.Path(xml_import_file).suffix != ".xml":
        raise FileExtensionError(xml_import_file)
    elif pathlib.Path(json_parsed_file).suffix != ".json":
        raise FileExtensionError(json_parsed_file)
    else:
        try:
            tree = ET.parse(xml_import_file)
        except Exception as ex:
            raise ParseError(ex)
        
        testerxml = create_xml()
        test_root = testerxml.getroot()
        
        root = tree.getroot()
        
        
        tested = xml_tester(test_root, root)
        if tested != True:
            raise XmlContentError(root)
        moviestats = {}
        col = my_collection(genre=[])
        for gen in root:
            
            genr = my_genre(category=gen.attrib["category"], decades=[])
            for decade in gen:
                dec = my_decade(decade=decade.attrib["years"],movie=[])
                
                for movie in decade:
                
                    mov = my_movie(movie_name=movie.attrib["title"],format=None,year=None,rating=None,description=None, favorite=movie.attrib["favorite"])
                    if mov.movie_name == "":
                        raise XmlContentError(mov.movie_name)
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
                    if mov.rating=="":
                        raise XmlContentError(mov.rating)
                    dec.movie.append(mov.__dict__)
                    
                    
                genr.decades.append(dec.__dict__)
                
                    
            col.genre.append(genr.__dict__)
            
        col = col.__dict__
            
        with open(json_parsed_file, "w") as moviejs:
            json.dump(col, moviejs, ensure_ascii=False, indent="\t")


        


