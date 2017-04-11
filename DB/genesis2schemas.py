schemas = []
with open('build/genesis.sql','r') as f:
    line = f.readline()
    while line:
        if 'CREATE TABLE' in line:
            tablename = line.split()[2]
            newschema = []
            inline = f.readline()
            while ');' not in inline:
                if inline.strip()[0:2] == '/*': #get rid of block comments
                    while inline.strip()[-2:] != '*/':
                        inline = f.readline()
                elif inline.strip()[0] != '(' and all(d not in inline for d in ['PRIMARY','FOREIGN']):
                    newschema.append(inline.split()[0])
                inline = f.readline()
            schemas.append((tablename,newschema))
        line = f.readline()

with open('schemas.txt','w') as w:
    w.write('schemas = { ')
    w.write(',\n\t'.join("'{}': {}".format(schema[0],schema[1]) for schema in schemas))
##    for schema in schemas:
##        w.write("{}_schema = {}\n".format(schema[0],schema[1]))
##        print("{}_schema = {}\n".format(schema[0],schema[1]))
    w.write(' }')
