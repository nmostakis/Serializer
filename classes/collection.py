from os import error

# Klassen sammlung für die einzelnen nodes aus der .xml datei
class my_movie:
    """[Movie Klasse die als Speicher für Tags und Attributes aus einer XML Datei dient]
    """    
    movie_name: str
    year: int
    rating: float
    favorite: bool
    description: str
    format_text: str
    multiple: str
    

    
    def __init__(self, movie_name:str, year:int, rating:str, favorite:bool, description:str, format_text:str, multiple:str ) -> None:
        """[Initialisiert die Parameter in denen die Daten der einzelnen Nodes aus einer XML gespeichert werden]

        Args:
            movie_name (str): [Name des Films]
            year (int): [Erscheinungsdatum]
            rating (str): [Altersbeschränkung]
            favorite (bool): [Favorit Markierung]
            description (str): [Beschreibung]
            format_text (str): [Formate in denen der Film erhältlich ist]
            multiple (str): [Gibt es mehr als ein Format für den Film]
        """        
        self.movie_name = movie_name
        self.year = year
        self.rating = rating
        self.favorite = favorite
        self.description = description
        self.format_text = format_text
        self.multiple = multiple

class my_decade:
    """[Klasse für Nodes 'decade' in der XML Datei mit einer Liste 'Movie' die Objekte mit der Klasse @my_movie enthält]
    """    
    decade: str
    movie = [my_movie]

    def __init__(self, decade:str, movie:list[my_movie]) -> None:
        """[Initialisiert Parameter für die Daten der Nodes 'decade' aus einer XML Datei]

        Args:
            decade (str): [Jahrzehnt in dem der Film erschienen ist]
            movie (list[my_movie]): [Liste aus my_movie objekten mit daten aus der XML Datei]
        """        
        self.decade = decade
        self.movie = movie


class my_genre:
    """[Klasse für die Nodes 'genre' in der XML Datei mit einer Liste 'decades' die Objekte mit der Klasse @my_decade enthält]
    """    
    category: str
    decades = [my_decade]

    def __init__(self, category:str, decades:list[my_decade]) -> None:
        """[Initialisiert Parameter dür die Daten der Nodes 'genre' aus der XML Datei]

        Args:
            category (str): [Attibut der Node 'genre' in dem die Kategorie der Filme steht]
            decades (list[my_decade]): [Liste aus Ojekten mit Daten aus den Nodes 'decade']
        """        
        self.category = category
        self.decades = decades


class my_collection:
    """[Klasse für das Root objekt aus dem Element Tree mit einer liste 'genre' die Objekte der Klasse @my_genre]
    """    
    genre = [my_genre] 

    def __init__(self, genre:list[my_genre]) -> None:
        """[Initialisiert einen Parameter 'liste' für objekte mit der Klasse @my_genre]

        Args:
            genre (list[my_genre]): [Liste aus Objekten mit Daten aus den Nodes 'genre']
        """        
        self.genre = genre


class my_stats:
    """[Klasse für objekte @my_stats enthält Daten aus allen Nodes der XML Datei für die Konvertierung in eine CSV Datei]
    """    
    genre: str
    decade: str
    movie_name: str
    release: int
    favorite: bool
    rating: str
    description: str
    format_text: str
    multiple:str
    
    def __init__(self, genre:str, decade:str, movie_name:str, release:int, favorite:bool, rating:str, description:str, format_text:str, multiple:str) -> None:
        self.genre = genre
        self.decade = decade
        self.movie_name = movie_name
        self.release = release
        self.favorite = favorite
        self.rating = rating
        self.description = description
        self.format_text = format_text
        self.multiple = multiple
        

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