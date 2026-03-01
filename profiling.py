from services.embedding_service import EmbeddingService
import time
import os
import psutil
import torch

process = psutil.Process(os.getpid())

def warmup(generator: EmbeddingService, content: str, rounds=3):
    print('[SERVER] Running warm-up...')
    for _ in range(rounds):
        generator.generate_embedding(content)
    print('[SERVER] Warm-up finished')

def full_profile(func, *args, runs=5):
    print('\n=== PROFILING ===')
    
    results = []
    min_time = 0
    max_time = 0

    for i in range(runs):
        mem_before = process.memory_info().rss
        cpu_before = process.cpu_percent(interval=None)
        gpu_before = (
            torch.cuda.memory_allocated()
            if torch.cuda.is_available()
            else 0
        )

        start = time.perf_counter()
        func(*args)
        if torch.cuda.is_available():
            torch.cuda.synchronize()
        elapsed = time.perf_counter() - start

        mem_after = process.memory_info().rss
        cpu_after = process.cpu_percent(interval=None)
        gpu_after = (
            torch.cuda.memory_allocated()
            if torch.cuda.is_available()
            else 0
        )

        results.append(elapsed)

        print(f"""
              Run {i+1}
              Tempo: {elapsed:.4f}s
              CPU%: {cpu_after}
              RAM Δ: {(mem_after-mem_before)/1024**2:.2f} MB
              VRAM Δ: {(gpu_after-gpu_before)/1024**2:.2f} MB
        """)

    avg = sum(results) / len(results)
    print(f"\nMenor tempo: {min(results):.4f}s")
    print(f"Maior tempo: {max(results):.4f}s")
    print(f"Tempo médio: {avg:.4f}s")