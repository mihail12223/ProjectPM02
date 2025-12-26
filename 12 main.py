def fib_tree(h, k):
    
    n_nodes = (1 << h) - 1 
    fib = [0] * (n_nodes + 1)
    fib[1] = 1
    if n_nodes > 1:
        fib[2] = 1
        for i in range(3, n_nodes + 1):
            fib[i] = fib[i-1] + fib[i-2]
    
    node_index = (1 << (h - 1)) - 1 + k
    
    return fib[node_index]




