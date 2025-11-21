def verbose_results(results, number):
    best_time = min(results)
    worst_time = max(results)
    avg_time = sum(results) / len(results)

    print(f"Summary for benchmarking {number} loops, {len(results)} times:")
    print(f"Best: {best_time / number :.8f} sec/op")
    print(f"Worst: {worst_time / number :.8f} sec/op")
    print(f"Average: {avg_time / number :.8f} sec/op")
