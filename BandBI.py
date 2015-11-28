# vvaradin
#Stage I

def Anteater_BandB():
    infile = open("AnteaterBandBStageI.txt", "r")
    outfile = open('Result.txt','w')
    new_list = []
    for line in infile:
        command = line.strip()[:2].upper()
        text = line.strip()[2:].strip()
        if command == 'NB':
            new_list.append(text)
        elif command == 'LB':
            outfile.write('Number of bedrooms in service:  {:3d}\n'.format(len(new_list)))
            outfile.write('------------------------------------\n')
            for obj in new_list:
                outfile.write(obj+'\n')
        elif command == 'PL':
            outfile.write(text+'\n')
    infile.close()
    outfile.close()
Anteater_BandB()
