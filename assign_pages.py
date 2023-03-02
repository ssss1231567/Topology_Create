import fitz
import re
from fitz.fitz import FileNotFoundError as FileNotFoundErrorFitz

class FinderPages:   
    @staticmethod 
    def assign_name(path_file : str) -> str:
        with fitz.open(path_file) as doc:
            name_project : str = ""
            page = doc.load_page(0)
            texts : list = page.get_text("words", sort=True)
            check_finded = lambda text: text[4] if len(text) > 0 else ""
            find_part_name = lambda text: "=" in text[4] and len(text[4]) > 4
            find_full_name = lambda text: finded_part in text[4] and len(text[4]) > len(finded_part)
            finded_part_information : list = next(filter(find_part_name, texts), [])
            finded_part : str = check_finded(finded_part_information,).replace("=", "")
            full_name_information : list = next(filter(find_full_name, texts), [])
            full_name_project : str = check_finded(full_name_information)
            name_project_regex : list = re.findall(r"{}[a-zA-Z0-9]*".format(finded_part), full_name_project)
            name_project = name_project_regex[0] if len(name_project_regex) > 0 else ""
        return name_project

    @staticmethod
    def assign_pages_chapter(path_file : str, chapter : str) -> tuple:
        finded_pages = []
        with fitz.open(path_file) as doc:
            tocs = doc.get_toc()
            temp_pages : set = set()
            for toc in tocs:
                if chapter in toc[1]:
                    temp_pages.add(toc[2])
            finded_pages.append(min(temp_pages))
            finded_pages.append(max(temp_pages))
        return tuple(finded_pages)
        