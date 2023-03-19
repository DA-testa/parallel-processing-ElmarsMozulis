def parallel_processing(n, m, data):
    threads = [(0, i) for i in range(n)] 
    results = [] 

    for i in range(m):
        job_time = data[i]

    
        start_time, thread_id = threads[0]
        results.append((thread_id, start_time)) 

        threads[0] = (start_time + job_time, thread_id)
        threads.sort()

    return results


def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)
    for thread_id, start_time in result:
        print(thread_id, start_time)


if __name__ == "__main__":
    main()