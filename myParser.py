import PyPDF2
import re
import pathlib

class Parser:

    def __init__(self, folder_path) -> None:
        
        if pathlib.is_dir(folder_path):
            self.folder = folder_path 
        else:
            self.file = folder_path

        self.questionBank = {"GDC":[], "nonGDC":[]}

    def parse_folder(self) -> None:
        if not self.folder:
            self.parse_questions(self.file)
        else:
            for f in pathlib.Path(self.folder_path).iterdir():
                if f.is_file():
                    self.parse_questions(f)
    
    def concat_banks(self, new_bank) -> None:
        self.questionBank["GDC"].extend(new_bank["GDC"])
        self.questionBank["nonGDC"].extend(new_bank["nonGDC"])

    def parse_questions(self, file_path) -> None:
        # Open the PDF file in binary mode
        with open(file_path, 'rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)

            # Initialize an empty dictionary to store sections
            sections = {}

            # Initialize variables to track current section number and text
            current_section = None
            current_text = ''

            # Iterate through each page
            for page_number in range(len(pdf_reader.pages)):
                # Extract text from the page
                page = pdf_reader.pages[page_number]
                page_text= page.extract_text()
                lines = page_text.split("\n \n")
                for line in lines:
                    if re.search(r'\[without GDC\]', line): # see if its a nonGDC question
                        qmark = int(re.findall(r'\[Maximum mark: (\d+)\]', line)[0]) # get the markscheme
                        qtext = line[re.search(r'\[Maximum mark: (\d+)\] + \[without GDC\]', line).span()[-1] :].strip() # get the question text
                        self.questionBank['nonGDC'].append((qmark, qtext)) # add to dict
                    
                    if re.search(r'\[with GDC\]', line): # see if its a GDC question
                        qmark = int(re.findall(r'\[Maximum mark: (\d+)\]', line)[0]) # get the markscheme
                        qtext = line[re.search(r'\[Maximum mark: (\d+)\] + \[without GDC\]', line).span()[-1] :].strip() # get the question text
                        self.questionBank['GDC'].append((qmark, qtext)) # add to dict

               # if section_match:
                    # If a new section is found, save the previous section (if any)
                    if current_section is not None:
                        sections[current_section] = current_text.strip()
                    
                    # Update current section number and reset current text
                  #  current_section = section_match.group(1)
                    current_text = ''
                
                # Append text from this page to the current section
                current_text += page_text

            # Save the last section
            if current_section is not None:
                sections[current_section] = current_text.strip()