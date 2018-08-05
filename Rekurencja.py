def countdown(number):
    if number >= 0:
        print(number)
        countdown(number - 1)

def countup(curr, max):
    if curr <= max:
        print(curr)
        countup(curr + 1, max)

def sil(n):
    if n == 1:
        return 1
    else:
        return n * sil(n - 1)


#countdown(10)
#countup(1, 2)
numb = 3
print(f"{numb}! = {sil(numb)}")