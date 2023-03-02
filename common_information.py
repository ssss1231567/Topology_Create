from fitz.fitz import FileNotFoundError as FileNotFoundErrorFitz
from assign_pages import FinderPages

class CommonInformation:
    def __init__(self, path_file : str) -> None:
        self.__path_file : str = path_file
        self.__name_project : str = ""
        self.__topology_pages : tuple = ()
        self.__in_out_pages : tuple = ()
        
    def assign_common_inforamtion(self):
        self.assign_name()
        self.assign_pages_topology()
        self.assign_pages_in_out()    
    
    def assign_name(self) -> None:
        try:
            self.__name_project = FinderPages.assign_name(self.__path_file)
        except FileNotFoundErrorFitz as e:
            print('File does not exist:', str(e))

    def assign_pages_topology(self) -> None:
        try:
            self.__topology_pages = FinderPages.assign_pages_chapter(self.__path_file, "Busübersicht")
        except FileNotFoundErrorFitz as e:
            print('File does not exist:', str(e))
            
    def assign_pages_in_out(self) -> None:
        try:
            self.__in_out_pages = FinderPages.assign_pages_chapter(self.__path_file, "Adressraumübersicht")
        except FileNotFoundErrorFitz as e:
            print('File does not exist:', str(e))        
    
    def get_name_project(self) -> str:
        return self.__name_project
    
    def get_topology_pages(self) -> tuple:
        return tuple(self.__topology_pages)
    
    def get_in_out_pages(self) -> tuple:
        return tuple(self.__in_out_pages)