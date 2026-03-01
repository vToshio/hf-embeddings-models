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

    print("Embeddings: ", generator.generate_embedding(content))
    

if __name__ == "__main__":
    main()
