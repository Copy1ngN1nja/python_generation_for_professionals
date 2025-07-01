d = {
    'B': 1,
    'KB': 2 ** 10,
    'MB': 2 ** 20,
    'GB': 2 ** 30,
}

with open('files.txt', 'r') as input_file:
    lines = [line.strip() for line in input_file]
    files = []
    for line in lines:
        name, cnt, unit = line.split()
        weight = int(cnt) * d[unit]
        name, expansion = name.split('.')
        files.append((name, expansion, weight))
    groups = {}
    for name, expansion, weight in files:
        if expansion not in groups:
            groups[expansion] = []
        groups[expansion].append((name, weight))
    for expansion, group in sorted(groups.items()):
        group.sort()
        sumi, unit = 0, 'B'
        for name, weight in group:
            print(f'{name}.{expansion}')
            sumi += weight
        print('----------')
        if sumi >= d['GB']:
            unit = 'GB'
            sumi /= d['GB']
        elif sumi >= d['MB']:
            unit = 'MB'
            sumi /= d['MB']
        elif sumi >= d['KB']:
            unit = 'KB'
            sumi /= d['KB']
        sumi = int(round(sumi))
        print(f'Summary: {sumi} {unit}', end='\n\n')
        
