import xml.etree.ElementTree as ET
import csv
from  classes.collection import my_stats, FileExtensionError, XmlContentError
import pathlib
from xmlcreator import xml_tester, create_xml


##  Nimmmt den xmlpfad als ersten wert und den exportpfad der csv datei als zweiten wert parsed die .xml zu einer .csv datei
def xmlcsv(xml_import_file:str, csv_parsed_file:str) -> None:
    """[Konvertiert XML Datei in CSV Datei mit Tags und Attributbezeichnungen der XML als Feldnamen und Text und Attributsinhalte als Tabelleninhalte]

    Args:
        xml_import_file ([str]): [Pfad und Name der XML Datei]
        csv_parsed_file ([str]): [Pfad und Name der CSV Datei die aus der XML Datei erstellt werden soll]

    Raises:
        XmlContentError: [Fehlermeldung falls der Inhalt der XML Datei Fehlerhaft ist oder nicht nach vorgegebenem Format aufgebaut ist]
    """    
    file_in = False
    file_out = False
    try:
        if pathlib.Path(xml_import_file).suffix == ".xml":
            file_in = True
        if pathlib.Path(csv_parsed_file).suffix == ".csv":
            file_out = True
    except Exception as x:
        print("No valid inputfile found")
        print("No Valid outputfile found")
        pass
        
    
    if file_in == True and file_out == True:
        tree = ET.parse(xml_import_file)
        
        root = tree.getroot()
        
        tested = xml_tester(root)
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
