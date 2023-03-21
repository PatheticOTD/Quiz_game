def fib(n):
    bib = [0,1,1]
    for i in range(n):
        bib.append(bib[i-2]+bib[i-1])
        print()
    return(bib[n])

