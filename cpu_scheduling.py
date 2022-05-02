def fcfs(n, arrival_time, burst_time):
    tat = list()
    wt = list()
    sequence = list()
    process_start = list()
    process_end = list()
    for i in range(n):
        sequence.append(i)
        if i == 0:
            process_start.append(0)
        else:
            process_start.append(process_end[i-1])
        process_end.append(process_start[i] + burst_time[i])
        tat.append(process_end[i] - arrival_time[i])
        wt.append(process_start[i] - arrival_time[i])
    print('Gantt Chart:')
    print('=============================================================')
    for i in range(n):
        print('   P{}   |'.format(sequence[i]), process_end[i], end = '')
    print('\n=============================================================')
    avg_tat = sum(tat) / n
    print('Average turn arround time: ',avg_tat, 'ms')
    avg_wt = sum(wt) / n
    print('Average waiting time: ', avg_wt, 'ms')



def sjf(n, arrival_time, burst_time):
    temp_burst = burst_time.copy()
    tat = list()
    wt = list()
    sequence = list()
    process_start = list()
    process_end = list()
    for i in range(n):
        val = min(temp_burst)
        pos = burst_time.index(val)
        sequence.append(pos)
        if i == 0:
            process_start.append(0)
        else:
            process_start.append(process_end[i-1])
        process_end.append(process_start[i] + val)
        tat.append(process_end[i] - arrival_time[i])
        wt.append(process_start[i] - arrival_time[i])
        temp_burst.remove(val)
    print('Gantt Chart:')
    print('=============================================================')
    for i in range(n):
        print('   P{}   |'.format(sequence[i]), process_end[i], end='')
    print('\n=============================================================')
    avg_tat = sum(tat) / n
    print('Average turn arround time: ', avg_tat, 'ms')
    avg_wt = sum(wt) / n
    print('Average waiting time: ', avg_wt, 'ms')

def rr(n, arrival_time, burst_time):
    copy_burst = burst_time.copy()
    q = int(input('Enter the time quantum: '))
    tat = [0]*n
    wt = [0]*n
    sequence = list()
    process_start = list()
    process_end = list()
    done = list()
    count = 0
    while len(done) != n:
        for i in range(n):
            if i not in done:
                sequence.append(i)
                if i == 0 and count == 0:
                    process_start.append(0)
                else:
                    process_start.append(process_end[count - 1])

                if burst_time[i] <= q:
                    process_end.append(process_start[count] + burst_time[i])
                    if count != 0:
                        tat[i] = process_end[count] - arrival_time[i]
                        wt[i] = tat[i] - copy_burst[i]
                    done.append(i)

                if burst_time[i] > q:
                    process_end.append(process_start[count] + q)
                    burst_time[i] = burst_time[i] - q
                    print(burst_time)
                count += 1
    print(process_end)
    print(process_start)
    print('Gantt Chart:')
    print('=============================================================')
    for i in range(count):
        print('   P{}   |'.format(sequence[i]), process_end[i], end='')
    print('\n=============================================================')
    print(tat)
    avg_tat = sum(tat) / n
    print('Average turn arround time: ', avg_tat, 'ms')
    print(wt)
    avg_wt = sum(wt) / n
    print('Average waiting time: ', avg_wt, 'ms')


# start here
n = int(input('Enter the number of processes: '))
arrival_time = list()
burst_time = list()
for i in range(n):
    print('Enter arrival time of process %d: '%i, end = '')
    at = int(input())
    arrival_time.append(at)
    print('Enter the burst time process %d: ' %i, end = '')
    bt = int(input())
    burst_time.append(bt)
ch = 0
while ch < 4:
    print('1. FCFS')
    print('2. SJF')
    print('3. Round Robin')
    print('4. Exit')
    ch = int(input('Enter your choice: '))
    if ch == 1:
        fcfs(n, arrival_time, burst_time)
    if ch == 2:
        sjf(n, arrival_time, burst_time)
    if ch == 3:
        rr(n, arrival_time, burst_time)
    if ch == 4:
        break


