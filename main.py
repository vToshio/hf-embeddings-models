from dotenv import load_dotenv

from services import EmbeddingService, IOExtractionService
from profiling import warmup, full_profile

load_dotenv()

def main():
    files = sorted(IOExtractionService.extract(), key=lambda file: file.name)
    generator = EmbeddingService()
    warmup(generator, files[0].content, 5)

    content = [f.content for f in files]
    full_profile(
        generator.generate_embedding,
        content,
        runs=5
    )

    for file_i in files:
        print(f'\nTesting content #{file_i.name}:')
        for file_j in files:
            print(f'Similarity with "{file_j.name}":\t', generator.compare(file_i.content, file_j.content))

    

if __name__ == "__main__":
    main()
