with open('tableData', 'r') as f, open('updatedFile.txt', 'w') as n:
    for line in f:
        data = line.strip()
        if(data[:2] == '--'):
            currTable = data[2:]
            line = f.readline();
            columns = line.strip()
        else:
            n.write('INSERT INTO '+currTable+'(' +columns+ ') VALUES (' + data + ');\r\n')

print('File Parsed');
