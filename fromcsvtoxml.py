import csv

import xml.etree.ElementTree as ET
from classes.collection import my_movie, my_collection, my_decade, my_genre
from xml.dom import minidom


listed_genre = []
listed_decade = []
listed_movie = []

def create_csvobject_tree(parsed_csv:str) -> object:
    csv.register_dialect("vita", quotechar='"', delimiter=";", quoting=csv.QUOTE_ALL, escapechar="#")
    with open(parsed_csv, "r", encoding="UTF8") as importcsv:
        reader = csv.DictReader(importcsv, dialect="vita")
        
        collection_item = my_collection(genre=[])
        
        
        
        for line in reader:
            
            movie_item = my_movie(movie_name=line["title"],year=line["release"],rating=line["rating"],favorite=line["favorite"],description=line["description"],format_text=line["format_text"],multiple=line["multiple"])
            if len(collection_item.genre) == 0:
                genre_item = my_genre(category=line["genre"],decades=[])
                found_gen = genre_item
                collection_item.genre.append(genre_item)
            else:
                found = False
                for genre in collection_item.genre:
                    if genre.category == line["genre"]:
                        found_gen = genre
                        found = True
                if found == False:
                    genre_item = my_genre(category=line["genre"],decades=[])
                    found_gen = genre
                    collection_item.genre.append(genre_item)
                '''
                Hier ist das Genre auf jeden Fall angelegt
                '''
            if len(found_gen.decades) == 0:
                decade_item = my_decade(decade=line["decade"], movie=[])
                found_dec = decade_item
                found_gen.decades.append(decade_item)
                decade_item.movie.append(movie_item)
            else:
                found = False
                for decade in found_gen.decades:
                    if decade.decade == line["decade"]:
                        found_dec = decade
                        found = True
                if found == False:
                    decade_item = my_decade(decade=line["decade"],movie=[])
                    found_dec = decade
                    genre_item.decades.append(decade_item)
                    decade_item.movie.append(movie_item)
                else:
                    decade_item.movie.append(movie_item)

    return collection_item



collection_object = create_csvobject_tree("parsed.csv")

collection = ET.Element("collection")
for genre_item in collection_object.genre:
    genres = ET.SubElement(collection,"genres")
    genres.set("category", genre_item.category)
    for decades_item in genre_item.decades:
        decades = ET.SubElement(genres, "decade")
        decades.set("years", decades_item.decade)
        for movie_items in decades_item.movie:
            movies = ET.SubElement(decades, "movie")
            movies.set("favorite", movie_items.favorite)
            movies.set("title", movie_items.movie_name)
            for movie_stats, movie_text in movie_items.__dict__.items():
                if movie_stats == "favorite" or movie_stats == "movie_name":
                    continue
                elif movie_stats == "format_text":
                    format_text = movie_text
                elif movie_stats == "multiple":
                    multiple = movie_text
                else:
                    movie_stat = ET.SubElement(movies, movie_stats)
                    movie_stat.text = movie_text
            format_node = ET.SubElement(movies,"format",{"multiple":multiple})
            format_node.text = format_text
                
    
tree = ET.ElementTree(collection)
# print(ET.tostringlist(collection))

ET.indent(tree,"\t")

tree.write("backwards_parsed.xml",xml_declaration=True,encoding="UTF8",method="xml", short_empty_elements=False)



