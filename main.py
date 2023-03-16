# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    
    """ processor = [(0, i) for i in range(n)]
    finish = [0] * n
    for i in range(m):
        task = data[i]
        next = min(processor)[1]
        output.append((next, processor[next][0]))
        processor[next]= (processor[next][0] + task, next)
         """
    return output
        
""" for i in processor:
        next = finish.index(min(finish))
        output.append((next, finish[next]))
        finish[next] = finish[next] + i[0]
    return output """
"""     for i in range(n):
        processor = (0, i) """
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
    for i, j in result:
        print(i, j)


if __name__ == "__main__":
    main()
