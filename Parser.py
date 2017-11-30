with open('tableData', 'r') as f, open('updatedFile.txt', 'w') as n:
    for line in f:
        data = line.strip()
        if(data.substring[0,2] == '--')
            currTable = data.substring[2:]
            line += 1 #might do readline instead
            columns = line.strip()
        else
            n.write('INSERT INTO '+currTable+'(' +columns+ ') VALUES (' + data + ');\r\n')
