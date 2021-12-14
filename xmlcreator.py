from os import error
from types import TracebackType
from xml.etree.ElementTree import Element, ElementTree
import defusedxml.ElementTree as ET
import xml.etree.cElementTree as CT
import sys
import traceback



def create_xml() -> Element:
    """[Erstellt ein XML Element mit vorgaben für die Tags und Attribute der einzelnen Elemente und children der Elemente]

    Returns:
        Element: [Testobjekt für die XML Tester Funktion]
    """    
    root = CT.Element("collections")
    genres = CT.SubElement(root, "genres")
    genres.set("category", "")
    decade = CT.SubElement(genres, "decade")
    decade.set("years","")
    movie=CT.SubElement(decade, "movie")
    movie.set("favorite","")
    movie.set("title","")
    format = CT.SubElement(movie,"format",{"multiple":""})
    year = CT.SubElement(movie,"year")
    rating = CT.SubElement(movie,"rating")
    description = CT.SubElement(movie,"description")

    tree = CT.ElementTree(root)
    return tree


 

def xml_tester(root:Element) -> bool:
    """[Testet ein XML Elemet Tree auf gleichheit der Tags und Attributsbezeichnungen]

    Args:
        root (Element): [XML Element Tree der auf Gleichheut mit dem Testelement und Attribuntsbezeichnungen geprüft wird]

    Returns:
        bool: [Sind Test Element und Vergleichselement gleich gibt die funktion den Wert True zurück, sonst wird der Wert False zurückgegeben]
    """    
    test_tree = create_xml()
    test_root = test_tree.getroot()
    ret = False
    
        
    if type(root) != type(test_root):
        print(str(type(root)) + " Is not a RootElementTree Object.")
    else:            
        for genres, testgenres in zip(root, test_root):
            if root.tag != test_root.tag:
                break
            elif genres.tag != testgenres.tag:
                break
            elif genres.attrib.keys() != testgenres.attrib.keys():
                break
            for decade, testdecade in zip(genres, testgenres):
                if decade.tag != testdecade.tag:
                    break
                elif decade.attrib.keys() != testdecade.attrib.keys():
                    break
                for movies, testmovies in zip(decade,testdecade):
                    if movies.tag != testmovies.tag:
                        break
                    elif movies.attrib.keys() != testmovies.attrib.keys():
                        break
                    for stats, teststats in zip(movies, testmovies):
                        if stats.tag != teststats.tag:
                            break
                        elif stats.attrib.keys() != teststats.attrib.keys():
                            break
                        else: 
                            ret = True
                            break
        
    return ret


