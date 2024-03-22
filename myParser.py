import PyPDF2
import re
import pathlib
from typing import Dict, Optional

class Parser:
    """
    Takes pdf files of questions from Christos Nikolaidis' website, that I use often for teaching IB students
    Separates the questions by if they require a graphing calculator or not, and then stores by markscheme
    """

    def __init__(self, folder_path: str, topic: Optional[str]) -> None:
        
        if pathlib.Path(folder_path).is_dir():
            self.folder = folder_path 
        else:
            self.folder = None
            self.file = folder_path

        self.questionBank = {"GDC":[], "nonGDC":[]}
        self.topic = topic

    def __add__(self, new_parser) -> None:

        self.questionBank["GDC"].extend(new_parser.questionBank["GDC"])
        self.questionBank["nonGDC"].extend(new_parser.questionBank["nonGDC"]) 
        self.topic += ", " + new_parser.topic   
    
    def __getitem__(self, key):
        # for later implementation
        pass

    def parse_folder(self) -> None:
        if not self.folder:
            self.parse_questions(self.file)
        else:
            for f in pathlib.Path(self.folder_path).iterdir():
                if f.is_file():
                    self.parse_questions(f)

    def parse_questions(self, file_path: str) -> None:
        # Open the PDF file in binary mode
        with open(file_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)
            # Iterate through each page
            for page_number in range(len(pdf_reader.pages)):
                # Extract text from the page
                page = pdf_reader.pages[page_number]
                page_text= page.extract_text()
                lines = page_text.split("\n \n")
                for line in lines:
                    if re.search(r'\[without GDC\]', line): # see if its a nonGDC question
                        qmark = int(re.findall(r'\[Maximum mark: (\d+)\]', line)[0]) # get the markscheme
                        qtext = line[re.search(r'\[without GDC\]', line).span()[-1] :].strip() # get the question text
                        self.questionBank['nonGDC'].append((qmark, qtext)) # add to dict
                    
                    if re.search(r'\[with GDC\]', line): # see if its a GDC question
                        qmark = int(re.findall(r'\[Maximum mark: (\d+)\]', line)[0]) # get the markscheme
                        qtext = line[re.search(r'\[with GDC\]', line).span()[-1] :].strip() # get the question text
                        self.questionBank['GDC'].append((qmark, qtext)) # add to dict

if __name__ == "__main__":
    filepath = "/Users/aaranya/Downloads/ArithmeticSequences.pdf"
    trying = Parser(filepath, "Arithmetic Sequences")
    trying.parse_folder()