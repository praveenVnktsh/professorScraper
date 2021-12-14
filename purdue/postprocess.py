with open('purdueResearch.csv', 'w') as f1:
    with open('purdueResearch1.csv', 'r') as f:
        for line in f.readlines():
            if len(line) < 5:
                continue    

            line = line.replace(',', ';').replace('&&', ',')
            f1.write(line)