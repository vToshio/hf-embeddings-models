from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from typing import List
import os

load_dotenv()

class EmbeddingService:
    _model_name = os.getenv('HF_MODEL')
    _model = SentenceTransformer(_model_name)

    @classmethod    
    def generate_embedding(cls, text: List[str]|str) -> List[tuple]:
        return cls._model.encode(text)
