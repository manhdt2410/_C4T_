items = ['Sport', 'LOL', 'Bts', 'Games', 'Death note', 'Netflix']
i = int(0)

while i < len(items) :
    print(*list(items[i]))
    i = i + 1
    if str(list(items[i])) == 'e' or 'E' :
       print(items[i])
       i = i + 1
       break

