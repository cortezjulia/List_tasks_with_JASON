#list of tasks where the user can insert, remove and re-add them, using JSON.

import json


tasks=[]
flag=0
receive_option='1'

while receive_option=='1':    

    receive_task=input('Insira sua tarefa: ')
    
    tasks.append(receive_task)
    flag+=1
    print('Adicionar [1]     Remover [2]     Sair [3]')
    receive_option=input('Digite o número correspondente: ')
    
if receive_option=='2':
    
    tasks.pop(len(tasks)-1)

with open('official_dict.json', 'w', encoding='utf8') as outfile:
    json.dump(
        tasks,
        outfile,
        #commands for text alignment and validating accents
        ensure_ascii=False,
        indent=2,
    )
