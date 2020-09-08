def primo(n) :
    divisores = 0
    den = 1
    while den <= n :
        if n % den == 0 :
            divisores += 1
        den += 1
    if divisores == 2 :
        return 'primo'
    else :
        return 'Num é primo'

x = int(input('n : '))
primo(x)
