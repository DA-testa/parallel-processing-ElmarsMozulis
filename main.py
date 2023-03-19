def p_works(m, data):
    jobs = []
    for i in range(m):
        job = [0, i, data[i]]
        jobs.append(job)
    return jobs

def p_threads(n):
    threads = []
    for i in range(n):
        thread = [0, i]
        threads.append(thread)
    return threads

def parallel_processing(n, m, data):
    jobs = p_works(m, data)
    threads = p_threads(n)
    output = []


    for job in jobs:
        mini_thread = threads[0]
        min_t_id = 0
        for i in range(len(threads)):
            if threads[i][0] < mini_thread[0]:
                mini_thread = threads[i]
                min_t_id = i

        start_time = max(mini_thread[0], job[0])
        output.append((mini_thread[1], start_time))
        threads[min_t_id][0] = start_time + job[2]

    return output

def main():
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    for thread, start_time in result:
        print(thread, start_time)

if __name__ == "__main__":
    main()
