napis = 'Odwazny rudy lis przeskoczyl nad spiacym wilczurem'
slowa = napis.split()
dlugosc_slow = [len(slowo) for slowo in slowa if slowo != 'nad']

print (dlugosc_slow)


'''
napis = 'Odwazny rudy lis przeskoczyl nad spiacym wilczurem'
slowa = napis.split() # tworzymy tablice ze slowami zawartymi w napisie
dlugosc_slow = []
for slowo in slowa:
    if slowo != 'nad':
        dlugosc_slow.append(len(slowo))

print dlugosc_slow
'''