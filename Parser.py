with open('example.txt', 'r') as f, open('updatedFile.txt', 'w') as n:
    for line in f:
        data = line.strip()
        n.write('INSERT INTO' + data + ';\r\n')
