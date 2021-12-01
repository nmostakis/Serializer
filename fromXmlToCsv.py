import xml.etree.ElementTree as ET
import csv
from  classes.collection import my_stats, FileExtensionError, XmlContentError
import pathlib
from xmlcreator import xml_tester, create_xml


##  Nimmmt den xmlpfad als ersten wert und den exportpfad der csv datei als zweiten wert parsed die .xml zu einer .csv datei
def xmlcsv(xml_import_file, csv_parsed_file):
    if pathlib.Path(xml_import_file).suffix != ".xml":
        raise FileExtensionError(xml_import_file)
    elif pathlib.Path(csv_parsed_file).suffix != ".csv":
        raise FileExtensionError(csv_parsed_file)
    else:
        tree = ET.parse(xml_import_file)
        testerxml = create_xml()
        test_root = testerxml.getroot()
        
        root = tree.getroot()
        
        tested = xml_tester(test_root, root)
        if tested != True:
            raise XmlContentError(root)

        movie= []
        with open(csv_parsed_file, mode="a", newline='\n') as parser:
            fieldnames=["genre","decade","title","release","favorite","rating","description","format_text","multiple"]
            parsedWriter = csv.DictWriter(parser, fieldnames=fieldnames, delimiter=";", quoting=csv.QUOTE_ALL)
            parsedWriter.writeheader()
            for genre in root.iter("genres"):
                for decade in genre.iter("decade"):
                    for movie in decade.iter("movie"):
                        mov = my_stats(genre=genre.attrib["category"], decade=decade.attrib["years"], movie_name=movie.attrib["title"], release=None, favorite=movie.attrib["favorite"], rating=None, description=None, format_text=None, multiple=None)
                        if mov.movie_name == "":
                            raise XmlContentError(mov.movie_name)
                        
                        for entry in movie:
                            if entry.tag == 'year':
                                mov.release = int(entry.text)
                        
                            if entry.tag == 'rating':
                                mov.rating = entry.text
                        
                            if entry.tag == 'description':
                                text = entry.text
                                text = text.strip()
                                text = text.replace("\n", " ")
                                text = text.replace("\t", " ")
                                text = text.replace("\"", "'")
                                mov.description = text
                            
                            if entry.tag == "format":
                                mov.multiple = entry.attrib["multiple"]
                                mov.format_text = entry.text
                        if mov.rating == "":
                            raise XmlContentError(mov.rating)
                        parsedWriter.writerow({fieldnames[0]:mov.genre, fieldnames[1]:mov.decade, fieldnames[2]:mov.movie_name, fieldnames[3]:mov.release, fieldnames[4]:mov.favorite, fieldnames[5]:mov.rating, fieldnames[6]:mov.description, fieldnames[7]:mov.format_text,fieldnames[8]:mov.multiple})

#xmlcsv("cerial.xml","parsed.csv")