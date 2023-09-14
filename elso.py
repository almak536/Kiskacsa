# print('Üdv \na\nfedélzeten', end=' *_* ')
"""print('\nSzia', 'Jenő\n', sep='_')

print('''Ez 
több
sorba
kerül
''')
"""

nev = input("Hogy hívnak: ")
titulus = "dr."
print('Szia', nev)
print(f'Szia {nev}')
print('Haliho {0}{1}'.format(titulus, nev))

print('jobbra'.rjust(50,'_'))
print('balra'.ljust(50,'*'))
print('center'.center(50))