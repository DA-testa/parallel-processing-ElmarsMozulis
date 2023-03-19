def p_works(m, data):
    # Sagatavo sarakstu ar darbiem
    jobs = []
    for i in range(m):
        job = [0, i, data[i]]
        jobs.append(job)
    return jobs

def p_threads(n):
    # Sagatavo sarakstu ar patvaļīgiem pavedieniem
    threads = []
    for i in range(n):
        thread = [0, i]
        threads.append(thread)
    return threads
def prepared_works(m, data): # Tiek sagatavots saraksts ar darbiem, 
# m - darbu skaits, data - saraksts, ar darbu izpildes laikiem, cik nepieciešams, lai apstrādātu katru sarakstu.
    list_of_jobs = [] # Izveidots tukšs saraksts, kur tiks saglabāti darbi.
    for i in range(m): # Apstrādā elementu i masīvā, kas atrodas starp 0 un m-1.
        work = [0, i, data[i]] # 0 - sākuma laiks, i - darba identifikators , data[i] - darba izpildes laiks.
        list_of_jobs.append(work) # Izdarītais darbs tiek pievienots sarakstam.
    return list_of_jobs # Kad visi darbi tika paveikti, funkcija return atgriež sarakstu, ar sagatavotiem darbiem.

def prepared_threads(n): # n - pavedienu skaits.
    list_of_threads = [] # Jauns, tukšs saraksts ar pavedieniem.
    for i in range(n): # Apstrādā elementu i masīvā, kas atrodas starp 0 un n-1.
        thread = [0, i] # Tiek izeidots pavediens sarakstā ar sākuma laiku 0 un i pozīciju.
        list_of_threads.append(thread) # Izveidotais pavediens tiek pievienots sarakstam.
    return list_of_threads # Tiek atgriezts saraksts ar izveidotajiem pavedieniem.

def parallel_processing(n, m, data):
    jobs = p_works(m, data)
    threads = p_threads(n)
    output = []

# Notiek darbu apstrāde
    for job in jobs:
        # Atrod vietu, kur beidzas pavediens
        mini_thread = threads[0]
        min_t_id = 0
        for i in range(len(threads)):
            if threads[i][0] < mini_thread[0]:
                mini_thread = threads[i]
                min_t_id = i
        # Aprēķina sākuma laiku
        start_time = max(mini_thread[0], job[0])
        # Pievieno darba rezultātu sarakstam
        output.append((mini_thread[1], start_time))
        # Atjauno pavediena beigu laiku
        threads[min_t_id][0] = start_time + job[2]

    return output
    list_of_jobs = prepared_works(m, data) # Darbu saraksts, kam tika padota informācija par datu masīvu un darbu skaitu.
    list_of_threads = prepared_threads(n) # Pavedienu saraksts, kam tika padota informācija par pavedienu skaitu.
    output = [] # Izveido tukšu rezultātu sarakstu.

# Notiek darbu apstrāde.
    for work in list_of_jobs: # Iziet caur visiem darbiem sarakstā.
        # Meklē brīvo pavedienu starp visiem.
        first_thread = list_of_threads[0] # Atrod pirmo pavedienu sarakstā.
        first_thread_index = 0 # Pirmā pavediena indeks.
        # Šeit notiek for cikls, kas pārbauda katru pavedienu sarakstā. Ja kāds no pavedieniem beidzas ātrāk,
        # tad pirmais pavediens sarakstā pārņem cita pavediena pozīciju sarakstā.
        for i in range(len(list_of_threads)):
            if list_of_threads[i][0] < first_thread[0]:
                first_thread = list_of_threads[i]
                first_thread_index = i
        # Aprēķina darba sākuma laiku.
        outset = max(first_thread[0], work[0])
        # Pievieno jaunu darba rezultātu sarakstam.
        output.append((first_thread[1], outset))
        # Atjauno pavediena beigu laiku.
        list_of_threads[first_thread_index][0] = outset + work[2]

    return output # Atgriež sarakstu ar visiem veiktajiem darbiem un to laikiem.

def main():
    # n un m ievade
    # Tiek ievadīts pavedienu skaits(n) un darbus skaits(m).
    n, m = map(int, input().split())

    #Otrā ievade
    # Tiek ievadīts saraksts, ar darbu izpildes laikiem.
    data = list(map(int, input().split()))

    result = parallel_processing(n, m, data)

    #Izdrukā rezultātu
    for thread, start_time in result:
        print(thread, start_time)
    #Izdrukā rezultātu, pirmā kolonna apzīmēs pavedienu, otrā - sākuma laiku
    for thread, outset in result:
        print(thread, outset)

if __name__ == "__main__":
    main()
    