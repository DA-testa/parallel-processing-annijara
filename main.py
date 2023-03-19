# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs    
    thread = [(0, t) for t in range(n) ]

    for t in range (m):
        nxt = min(thread)[1]
        tsk = data[t] 
        output.append((next, thread[nxt][0]))
        thread[nxt] = (thread[nxt][0]+ tsk, nxt)    

    return output 


def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n, m = map(int, input().split())
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = (list(map(int, input().split())))
    
    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for index, time in result:
        print(index, time)


if __name__ == "__main__":
    main()

