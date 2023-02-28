import pandas as pd
import numpy as np
import random as rnd

def unpack(path:str)-> pd.DataFrame():
    tasks = pd.DataFrame()                            #Тут будет содержимое всех трех файлов. Первый столб - вопрос, второй - варианты ответа, третий - правильный ответ и четвертый - полученный ответ.
    with open(path+'\\tests.txt') as tests:
        tests_output = np.array(tests.readlines())
        for i in range(len(tests_output)):
            tests_output[i] = tests_output[i].replace("\n",'')
        tasks["Questions"] = tests_output

    with open(path+'\\ans.txt') as ans:
        ans_output = np.array(ans.readlines())
        for i in range(len(ans_output)):
            ans_output[i] = ans_output[i].replace("\n",'')
        tasks["Answers"] = ans_output
    
    with open(path+'\\rans.txt') as rans:
        rans_output = rans.readlines()
        for i in range(len(rans_output)):
            rans_output[i] = int(rans_output[i].replace('\n',''))
        tasks["Right_Answers"] = rans_output

    return tasks




print("Приветствую, пользователь! Что ты желаешь сделать?\n1)Пройти тесты.\n2)Посмотреть статы.\n3)Добавить вопрос.")
answer = '1'#input("Введи номер желаемого развития событий: ")

if answer == '1':
    print("Выбери предмет:\n1)Основы питона\n2)Нампай\n3)Пандас\n4)Матплотлиб")
    theme = '1'#input("Введи номер желаемого развития событий: ")
    if theme == '1':
        questions = unpack('python_basics')  
        questions['Your_ans'] = questions["Check"] = 0
        
        for i in questions.index.array:
            print(questions["Questions"][i])
            print(questions["Answers"][i].replace("_","\n"))
            ans = int(input("Введи число (-1 - завершить принудительно): "))
            questions['Your_ans'] = ans if ans != -1 else 0

            if ans == questions["Right_Answers"][i]:
                print("\nПравильно\n")
                questions.loc[i,("Check")] = 1
            elif ans == -1:
                print("\nХорошо, завершаем\n")
                break
            else:
                print("\nНеверно\n") 
        
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Результаты " + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="[::-1]+'\n')
        result = questions[["Questions","Right_Answers","Your_ans"]]
        result.columns = ["Вопросы:","Правильный ответ:","Твой ответ:"]
        result.index = result.index.array + 1
        r_ans = questions["Check"].sum()
        t_ans = result["Твой ответ:"].sum()
        print(result,"\n")
        print("Правильных ответов дано:", r_ans)
        print("Всего ответов:", t_ans)
        print("{0}% решено верно.".format((r_ans / t_ans).round(4) * 100))


                     
