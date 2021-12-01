from xml.etree.ElementTree import Element, ElementTree
import defusedxml.ElementTree as ET
import xml.etree.cElementTree as CT


# erstellt ein element tree object als vorlage für die xml datei die geparsed werden soll
def create_xml() -> Element:
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


# testet zwei element tree objekte auf gleichheit der tags und attributes 
'''
description: 
param: @test_root - Das ist das root-Element vom Tree
        @root  - ist irgendein anderes root
return: bool - gibt zurück ob Tag ooder nacht ist
'''
def xml_tester(test_root:Element, root:Element) -> bool:
    ret = False
    for a1, a2 in zip(test_root, root):
        if a1.tag == a2.tag:
            for b1, b2 in zip(a1, a2):
                if b1.tag == b2.tag:
                    if b1.attrib.keys() == b2.attrib.keys():
                        for c1, c2 in zip(b1, b2):
                            if c1.tag == c2.tag:
                                if c1.attrib.keys() == c2.attrib.keys():
                                    for d1, d2 in zip(c1, c2):
                                        if d1.tag == d2.tag:
                                            ret = True
    return ret
