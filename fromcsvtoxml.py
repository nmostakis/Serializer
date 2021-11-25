import csv
import defusedxml.cElementTree as ET
from classes.collection import my_movie, my_collection, my_decade, my_genre

listed_genre = []
listed_decade = []
listed_movie = []


csv.register_dialect("vita", quotechar='"', delimiter=";", quoting=csv.QUOTE_ALL, escapechar="#")
with open("parsed.csv", "r", encoding="UTF8") as importcsv:
    reader = csv.DictReader(importcsv, dialect="vita")
    
    collectione = my_collection(genre=listed_genre)
    
    
    
    for line in reader:
        movie_item = my_movie(movie_name=line["title"],year=line["release"],rating=["rating"],favorite=line["favorite"],description=line["description"])
        
        
        
        decade_item = my_decade(decade=line["decade"],movie=listed_movie)
        
        genre_item = my_genre(category=line["genre"],decades=listed_decade)
    

        
    


