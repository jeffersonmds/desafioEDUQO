def desafioEduqo(n):
    underline = n - 1
    stars = 1
    for x in range(n):
        print ("_" * underline + "*" * stars + "_" * underline)
        stars += 2
        underline -= 1
        

