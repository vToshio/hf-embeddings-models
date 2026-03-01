from dotenv import load_dotenv

from services.extraction.io_strategy import IOExtractionStrategy
from services import EmbeddingService
from profiling import warmup, full_profile

load_dotenv()

def main():
    content = IOExtractionStrategy.extract()
    generator = EmbeddingService()
    warmup(generator, content[1], 5)

    full_profile(
        generator.generate_embedding,
        content,
        runs=5
    )

    for index_i, emb1 in enumerate(content):
        print(f'\nTesting content #{index_i}:')
        for index_j, emb2 in enumerate(content):
            print(f'Similarity between {index_i} and {index_j}: ', generator.compare(emb1, emb2))

    

if __name__ == "__main__":
    main()
