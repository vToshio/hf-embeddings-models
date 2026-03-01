from models import File
from definition import ROOT_PATH
from typing import List
import os

class IOExtractionService:
    @classmethod
    def extract(cls) -> List[File]:
        files_path = os.path.join(ROOT_PATH, 'files')

        files = os.listdir(files_path)
        extracted: List[File] = []
        for f in files:
            file_path = os.path.join(files_path, f)
            if not os.path.isfile(file_path): continue
 
            with open(file_path, 'r+') as opened_file:
                file = File(f, opened_file.read())
                extracted.append(file)
                print(f'[EXTRACTION] Read content from "{f}"')

        print('[EXTRACTION] Extraction finalized')
            
        return extracted
    