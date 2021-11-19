from os import error


class my_movie:
    movie_name: str
    year: int
    rating: float
    favorite: bool
    format: str
    description: str
    

    
    def __init__(self, movie_name:str, year:str, rating:str, favorite:bool, format:str, description:str ) -> None:
        self.movie_name = movie_name
        self.year = year
        self.rating = rating
        self.favorite = favorite
        self.format = format
        self.description = description
    


class my_decade:
    decade: str
    movie = {my_movie}

    def __init__(self, movie, decade) -> None:
        self.decade = decade
        self.movie = movie


class my_genre:
    category: str
    decades = {my_decade}

    def __init__(self, category, decades) -> None:
        self.category = category
        self.decades = decades


class my_collection:
    genre = [my_genre] 

    def __init__(self, genre:str) -> None:
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
    def __init__(self, file, massage="File extension does not match required") -> None:
        self.file = file
        self.massage = massage
        super().__init__(self.massage)
        
class XmlContentError(Exception):
    def __init__(self, xml_content, message="content of the XML don't macht the Expected layout") -> None:
        self.massage = message
        self.xml_content = xml_content
        super().__init__(message)
        
class RootNodeError(BaseException):
    def __init__(self, node, message="Root node in XML file is not named 'collection'") -> None:
        self.node = node
        self.massage = message
        super().__init__(message)
        