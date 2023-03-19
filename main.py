def parallel_processing(n, m, data):
    threads = [(0, i) for i in range(n)]  # initialize threads with zero start time
    results = []  # list to store results for each job

    for i in range(m):
        job_time = data[i]  # get the time required to process the current job

        # get the thread with the earliest start time
        start_time, thread_id = threads[0]
        results.append((thread_id, start_time))  # store the result for this job

        # update the start time for the thread and re-sort the list of threads
        threads[0] = (start_time + job_time, thread_id)
        threads.sort()

    return results


def main():
    # read input from keyboard
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    # run the parallel processing simulation
    result = parallel_processing(n, m, data)

    # print out the results
    for thread_id, start_time in result:
        print(thread_id, start_time)


if __name__ == "__main__":
    main()