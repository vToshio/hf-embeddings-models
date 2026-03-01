from services.extraction.base_service import BaseService
from definition import ROOT_PATH
from typing import List
import os

class IOExtractionStrategy:
    @classmethod
    def extract(cls) -> List[str]:
        files_path = os.path.join(ROOT_PATH, 'files')

        files = os.listdir(files_path)
        extracted = []
        for f in files:
            file_path = os.path.join(files_path, f)
            if not os.path.isfile(file_path): continue

            with open(file_path, 'r+') as file:
                print(f'[EXTRACTION] Read content from "{file.name}"')
                extracted.append(file.read())

        print('[EXTRACTION] Extraction finalized')
            
        return extracted
    