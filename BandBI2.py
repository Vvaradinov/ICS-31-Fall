#BAND STAGE 2

def Anteater_BandB():
    infile = open("AnteaterBandBStage2.txt", "r")
    outfile = open('Result2.txt','w')
    new_list = []
    for line in infile:
        command = line.strip()[:2].upper()
        text = line.strip()[2:].strip()
        if command == 'NB':
            new_list.append(text)
        elif command == "RB":
            del text
        elif command == 'PL':
            outfile.write(text+'\n')
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


        
