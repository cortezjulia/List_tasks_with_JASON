#list of tasks where the user can insert, remove and re-add them, using JSON.

import json
import time
import os




while True:    
    
    try: 
        
        with open('official_dict.json', 'r', encoding='utf8') as outfile:
            tasks = json.load(outfile)
            # print(pessoa)
            # print(type(pessoa))
    except:
        tasks=[]
        temporary_tasks=[]


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
            os.system('cls')
        else:
            try:
                last_value=len(tasks)-1
                temporary_tasks.append(tasks[last_value])
                tasks.pop(last_value)
            except NameError:
                temporary_tasks=[]
                last_value=len(tasks)-1
                temporary_tasks.append(tasks[last_value])
                tasks.pop(last_value)
   
    if receive_option=='3':
            try:
                if len(temporary_tasks)!=0:
                    
                    last_value=len(temporary_tasks)-1
                    tasks.append(temporary_tasks[last_value])
                    temporary_tasks.pop(last_value)
                    
            except NameError:
                temporary_tasks=[]        
                
            
    
    if receive_option=='4':
        break

    with open('official_dict.json', 'w', encoding='utf8') as outfile:
        json.dump(
            tasks,
            outfile,
            #commands for text alignment and validating accents
            ensure_ascii=False,
            indent=2,
        )
temporary_tasks=[]   

    
    



    


        
