with open('example.txt', 'r') as f, open('updatedFile.txt', 'w') as n:
    for line in f:
        data = line.strip()
        if(data.substring[0,2] == '--')
            currTable = data.substring[2:]
        else
            n.write('INSERT INTO '+currTable+' VALUES (' + data + ');\r\n')
