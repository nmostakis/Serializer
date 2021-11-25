from os import error

# Klassen sammlung für die einzelnen nodes aus der .xml datei
class my_movie:
    movie_name: str
    year: int
    rating: float
    favorite: bool
    # formats: str
    description: str
    

    
    def __init__(self, movie_name:str, year:int, rating:str, favorite:bool, description:str ) -> None:
        self.movie_name = movie_name
        self.year = year
        self.rating = rating
        self.favorite = favorite
        # self.format = formats
        self.description = description
    

# classe für die decade node aus der xml
class my_decade:
    decade: str
    movie = [my_movie]

    def __init__(self, decade:str, movie:list[my_movie]) -> None:
        self.decade = decade
        self.movie = movie


class my_genre:
    category: str
    decades = [my_decade]

    def __init__(self, category:str, decades:list[my_decade]) -> None:
        self.category = category
        self.decades = decades


class my_collection:
    genre = [my_genre] 

    def __init__(self, genre:list[my_genre]) -> None:
        self.genre = genre


class my_stats:
    genre: str
    decade: str
    movie_name: str
    release: int
    favorite: bool
    rating: str
    description: str
    
    def __init__(self, genre:str, decade:str, movie_name:str, release:int, favorite:bool, rating:str, description:str) -> None:
        self.genre = genre
        self.decade = decade
        self.movie_name = movie_name
        self.release = release
        self.favorite = favorite
        self.rating = rating
        self.description = description
        

class FileExtensionError(Exception):
    def __init__(self, file, massage="File extension of inputfile must be a .xml file") -> None:
        self.file = file
        self.massage = massage
        super().__init__(self.massage)
        
class XmlContentError(Exception):
    def __init__(self, xml_content, message="XML tags or attribute keys don't match the default form") -> None:
        self.massage = message
        self.xml_content = xml_content
        super().__init__(message)
        
class RootNodeError(BaseException):
    def __init__(self, node, message="Root node in XML file is not named 'collection'") -> None:
        self.node = node
        self.massage = message
        super().__init__(message)
        
class ArgumentError(Exception):
    def __init__(self, args,message="Arguments incorrect. choose between '-in importfile -out outputfile' or '-out outputfile -in importfile") -> None:
        self.args = args
        self.message = message
        super().__init__(message)