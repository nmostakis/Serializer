import csv
import defusedxml.cElementTree as ET
from classes.collection import my_movie, my_collection, my_decade, my_genre

listed_genre = []
listed_decade = []
listed_movie = []


csv.register_dialect("vita", quotechar='"', delimiter=";", quoting=csv.QUOTE_ALL, escapechar="#")
with open("parsed.csv", "r", encoding="UTF8") as importcsv:
    reader = csv.DictReader(importcsv, dialect="vita")
    
    collection_item = my_collection(genre=[])
    
    
    
    for line in reader:
        
        movie_item = my_movie(movie_name=line["title"],year=line["release"],rating=["rating"],favorite=line["favorite"],description=line["description"])
        if len(collection_item.genre) == 0:
            genre_item = my_genre(category=line["genre"],decades=[])
            #listed_genre.append(genre_item)
            found_gen = genre_item
            collection_item.genre.append(genre_item)
        else:
            found = False
            for genre in collection_item.genre:
                if genre.category == line["genre"]:
                    # genre_item.decades.append(decade_item)
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
            decade_item = my_decade(line["decade"], movie=[])
            found_gen.decades.append(decade_item)
            found_dec = decade_item
            
            
                
            
        if len(listed_decade) == 0:
            decade_item = my_decade(decade=line["decade"],movie=[])
            decade_item.movie.append(movie_item)
            listed_decade.append(decade_item)
        else:
            found = False
            for decade in listed_decade:
                if decade.decade == line["decade"]:
                    decade_item.movie.append(movie_item)
                    found = True
            if found == False:
                decade_item = my_decade(decade=line["decade"],movie=[])
                decade_item.movie.append(movie_item)
                listed_decade.append(decade_item)
            
                
            
        
        
        # if len(listed_decade) == 0:
            
        # else:
        #     for item in listed_decade:
        #         if line["decade"] == item.decade:
        #             decade_item.movie.append(movie_item)
        #         else:
        #             decade_item = my_decade(decade=line["decade"],movie=listed_movie)
                    
        #             decade_item.movie.append(movie_item)    
                        
            
x=1
        # genre_item = my_genre(category=line["genre"],decades=listed_decade)
    

    
    


