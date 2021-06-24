"""
                                                programa, criador de cronogramas!
"""

import os

index = -1 # index para a lista
on_titles = True #iniciar o titulo

lisSchedule = [] # lista do cronograma
listHors = [] # lista das horas

#_________________________________________________________________________________________________________#
def titles():# adicionar um titulo para o cronograma
    print("Qual nome quer dá para o cronograma?")
    name = input("> ")
    os.system("clear")

    with open("Schedule",'a') as folder:
            folder.write(f'<-------------------{name}------------------->\n')
    return False

def setList(List,hors,size): # salvar em um arquivo txt
    index = -1 # index para a lista
    with open("Schedule",'a') as folder:
        for values in range(len(List)):

            smaller = len(List[values])
            ideal_size = size - smaller
            Space=space(ideal_size)

            week,index = weekList(index)

            folder.write(week + ': ' + List[values]+ Space + '| ' + hors[values] + " Horas" +'\n')

        #folder.write(week + ':' + List + '|' + hors + '\n') 

def weekList(index): # mostrar dia da semana 
    index = index + 1
    week = ['DOM','SEG','TER','QUA','QUI','SEX','SAB']

    if index >= 7: # verificar se os dias já chegou ao fim
        return 'finish',index
    else:
        return week[index],index

def SizeElements(lisSchedule): # verificar o tamanho dos elementos
    sizeM = len(lisSchedule[0]) #pegar o tamanho do primeiro elemento

    for i in range(len(lisSchedule)): # verificar todos os elemento e ver qual é o maior
        size = len(lisSchedule[i])
        if len(lisSchedule[i]) > sizeM:
            sizeM = size

    return sizeM

def space(space):# adicionar os espaços
    string = ""
    space = space + 3
    for i in range(space):
        string = string + " "
    return string

#_________________________________________________________________________________________________________#
    
while True:

    if on_titles == True:
        on_titles = titles()

    week,index=weekList(index)

    if week == 'finish':
        size=SizeElements(lisSchedule)
        setList(lisSchedule,listHors,size)

        print("\nPrograma finalizado!")
        break

    else:
        lisSchedule.append(input(week+': ')) # guardar dados do input em uma lista
        listHors.append(input("Hors: ")) # guardar as horas em uma lista


    