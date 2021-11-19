import defusedxml.ElementTree as ET
import xml.etree.cElementTree as CT
import json
from  classes.collection import FileExtensionError, RootNodeError, XmlContentError, my_movie, my_genre, my_collection, my_decade


def create_xml():
    root = CT.Element("collection")
    genres = CT.SubElement(root, "genres")
    genres.set("category", "")
    decade = CT.SubElement(genres, "decade")
    decade.set("years","")
    movie=CT.SubElement(decade, "movie")
    movie.set("favorite","")
    movie.set("title","")
    format = CT.SubElement(movie,"format")
    year = CT.SubElement(movie,"year")
    rating = CT.SubElement(movie,"rating")
    description = CT.SubElement(movie,"description")

    tree = CT.ElementTree(root)
    return tree


def xml_tester(test_root, root):
    for a1, a2 in zip(test_root, root):
        if a1.tag == a2.tag:
            for b1, b2 in zip(a1, a2):
                if b1.tag == b2.tag:
                    if b1.attrib.keys() == b2.attrib.keys():
                        print("!OK")
                
                        for c1, c2 in zip(b1, b2):
                            if c1.tag == c2.tag:
                                if c1.attrib.keys() == c2.attrib.keys():
                                    print("ok")
                                    for d1, d2 in zip(c1, c2):
                                        print(d1.tag, d2.tag)