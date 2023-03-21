import pandas as pd
import numpy as np
import os
import time



def unpack(path:str)-> pd.DataFrame():
    df = pd.read_csv(f"subs\\{path}\\tests.csv")
    for i in range(len(df["ans"])):
        df.loc[i,"ans"] = df.loc[i,"ans"].replace("_","\n")
    return df

def percent(x,y): return (x / y).round(4) * 100 if y>0 else 0


subjects = os.listdir("D:\\Quiz_game\\subs")

print("Приветствую, пользователь! Что ты желаешь сделать?\n1)Пройти тесты.\n2)Статистика.\n3)Добавить вопрос.\n4)ВЫЙТИ")
answer = '1'#input("Введи номер желаемого развития событий: ")
#os.system('cls')



if answer == '1':
    print("Выбери предмет:")
    for i in range(len(subjects)):
        print(f"{i}. {subjects[i]}")
    var = int(input("Введи номер желаемого развития событий: "))

    questions = unpack(subjects[var])  
    questions['p_ans'] = questions["Check"] = 0
    ans_list = []
    stats = pd.DataFrame(pd.read_csv(f"subs\\{subjects[var]}\\stats.csv", index_col=0))
    #print(stats)
    #os.system('cls')

    for i in questions.index.array:
        print(questions["ques"][i])
        print(questions["ans"][i])
        ans = int(input("Введи число (-1 - завершить принудительно): "))
        ans_list.append(ans if ans != -1 else 0)
        os.system('cls')
        

        if ans == questions["rans"][i]:
            print("\n\n\t\tПравильно\n")
            questions.loc[i,("Check")] = 1
            time.sleep(0.8)
            os.system('cls')
        elif ans == -1:
            print("\n\n\t\tХорошо, завершаем\n\n")
            time.sleep(0.8)
            os.system('cls')
            break
        else:
            print(" ____    __    ____ .______        ______   .__   __.   _______ ") 
            print(" \   \  /  \  /   / |   _  \      /  __  \  |  \ |  |  /  _____|") 
            print("  \   \/    \/   /  |  |_)  |    |  |  |  | |   \|  | |  |  __  ") 
            print("   \            /   |      /     |  |  |  | |  . `  | |  | |_ | ") 
            print("    \    /\    /    |  |\  \----.|  `--'  | |  |\   | |  |__| | ") 
            print("     \__/  \__/     |__| `._____| \______/  |__| \__|  \______| ") 
            time.sleep(1.5)
            os.system('cls')
    
    

    questions['p_ans'] = ans_list +[0]*(len(questions.index.array)-len(ans_list))
    
    
    result = questions[["ques","rans","p_ans"]]
    result.columns = ["Вопросы:","Правильный ответ:","Твой ответ:"]
    result.index = result.index.array + 1
    r_ans = questions["Check"].sum()
    t_ans = len(result["Твой ответ:"])
    stats[time.ctime()] = [t_ans,r_ans,percent(r_ans,t_ans)]
    stats.to_csv(f"subs\\{subjects[var]}\\stats.csv")
    
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= Результаты " + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="[::-1]+'\n')
    print(result,"\n")
    print(f"Дано ответов: {t_ans}\nИз них правильные: {r_ans}\nПроцент попаданий: {percent(r_ans,t_ans)}")
    print(stats)


elif answer == '2':
    os.system('cls')

    ans = input("Что желаете сделать?\n1)Посмотреть статистику\n2)Очистить историю\nВведи цифру:")
    print("Выбери предмет:")
    for i in range(len(subjects)):
        print(f"{i}. {subjects[i]}")
    var = int(input("Введи номер желаемого развития событий: "))

    stats = pd.read_csv(f"subs\\{subjects[var]}\\stats.csv", index_col=0)
    stats.index = ["Дано ответов: ","Из них правильно: ","Процент попаданий: "]  
    if ans == '1':
        print(stats.T)

    if ans == '2':
        ans = input("Вы уверены?\n[y\\n]: ")
        if ans == 'y':
            stats = stats.iloc[:,0]
            stats.to_csv(f"subs\\{subjects[var]}\\stats.csv")
            print("История удалена успешно.")
        else:print("Хорошо, что одумались!")
    
    

if answer == '3':
    sub = input("Введи предмет: ")
    theme = input("Введи тему: ")



