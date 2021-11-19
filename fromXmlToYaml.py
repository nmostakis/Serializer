import ruamel.yaml
import xml.etree.ElementTree as ET
from  classes.collection import my_movie, my_genre, my_collection, my_decade, FileExtensionError
import pathlib




def xmlyaml(xml_import_file, yaml_parsed_file): 
    if pathlib.Path(xml_import_file).suffix != ".xml":
        raise FileExtensionError(xml_import_file)
    elif pathlib.Path(yaml_parsed_file).suffix != ".yaml":
        raise FileExtensionError(yaml_parsed_file)
    else:
        tree = ET.parse(xml_import_file)

        root = tree.getroot()
        moviestats = {}
        col = my_collection([])
        for gen in root:
            genre = my_genre(category=gen.attrib, decade=[])
            for decad in gen:
                dec = my_decade(decade=decad.attrib,movie=[])
                
                for movie in decad:
                    mov = my_movie(movie_name=movie.attrib,format=None,year=None,rating=None,description=None)
                    
                    for entry in movie:
                        
                        if mov.format == None:
                            mov.format = entry.text
                            moviestats[entry.tag] = entry.text
                        elif mov.year == None:
                            mov.year = int(entry.text)
                            moviestats[entry.tag]=entry.text
                        elif mov.rating == None:
                            mov.rating = entry.text
                            moviestats[entry.tag]= entry.text
                        else:
                            mov.description = entry.text
                            moviestats[entry.tag] = entry.text
                                                    
                    dec.movie.append(mov.__dict__)
                    
                genre.decade.append(dec.__dict__)
            
            col.genre.append(genre.__dict__)

        col = col.__dict__
        
        with open(yaml_parsed_file, "w") as parsed:
            ruamel.yaml.dump(col, parsed)

