def parallel_processing(int_n, int_m, data):
    parallel_threads = [(0, i) for i in range(int_n)] 
    results = [] 

    for i in range(int_m):
        job_time = data[i]

    
        start_time, p_thread_id = parallel_threads[0]
        results.append((p_thread_id, start_time)) 

        parallel_threads[0] = (start_time + job_time, p_thread_id)
        parallel_threads.sort()

    return results


def main():
    int_n, int_m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(int_n, int_m, data)
    for thread_id, start_time in result:
        print(thread_id, start_time)


if __name__ == "__main__":
    main()