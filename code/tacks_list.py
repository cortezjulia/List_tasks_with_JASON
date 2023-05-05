#list of tasks where the user can insert, remove and re-add them, using JSON.

import json
import time
import os


tasks=[]
temporary_remove='0'


while True:    
    
    print('Adicionar [1]     Remover [2]     Desfazer remoção[3]     Sair [4]')
    receive_option=input('Digite o número correspondente: ')
    print('\n')
    if receive_option!='1' and receive_option!='2' and receive_option!='3':
        print('Digite um dos números indicados!')
        print('\n')
        time.sleep(3)
        continue
    
    if receive_option=='1':
        receive_task=input('Insira sua tarefa: ')
        tasks.append(receive_task)


    if receive_option=='2':
        if len(tasks)==0:
            print('Não há nada ainda para ser apagado...')
            time.sleep(3)
            temporary_remove='0'
            os.system('cls')
        else:
            temporary_remove=tasks[len(tasks)-1]
            tasks.pop(len(tasks)-1)
   
    if receive_option=='3':
        if temporary_remove!='0':
            tasks.append(temporary_remove)
    
    if receive_option=='4':
        break
    
    print('\n')  
    print('Lista atualizada:')
    for task in tasks:
        print('->',task)

    print('\n')    

    


with open('official_dict.json', 'w', encoding='utf8') as outfile:
    json.dump(
        tasks,
        outfile,
        #commands for text alignment and validating accents
        ensure_ascii=False,
        indent=2,
    )

with open('official_dict.json', 'r', encoding='utf8') as outfile:
    tasks = json.load(outfile)
    # print(pessoa)
    # print(type(pessoa))


        
