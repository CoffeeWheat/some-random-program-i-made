# 傳入pickle資料 #重要!!!!! 讀取順序會影響資料存放的地方
    # with open('task.pickle', 'rb') as f:
    #     daily_task_amount = pickle.load(f)
    #     daily_task_list = pickle.load(f)
    #     daily_task_check_list = pickle.load(f)


# window = tk.Tk()
# window.title('GUI')
# window.geometry('380x400')
# window.resizable(False, False)
# window.iconbitmap('icon.ico')
# window.mainloop()





import pickle #引進pickle函式庫
import os
import tkinter as tk
from tkinter import filedialog

#window1 = tk.Tk()

debug_log = False   #開啟執行時print log

#同步功能############################################
# class Syn:

#     def from_pickle():
#         # try:
#         #     foo = pickle.load(open("var.pickle", "rb"))
#         # except (OSError, IOError) as e:
#         #     foo = 3
#         #     pickle.dump(foo, open("var.pickle", "wb"))

#         Others.print_debug_log('@Syn.from_pickle')

#         try:
#             f = open('task.pickle', 'rb')
#             daily_task = pickle.load(f)
#             daily_task_amount = pickle.load(f)
#             daily_task_list = pickle.load(f)
#             daily_task_check_list = pickle.load(f)

#             #if daily_task != None:
                
#             if daily_task_amount == None:
#                 daily_task_amount = 0
#             if daily_task_list == None:
#                 daily_task_list = [100]
#             if daily_task_check_list == None:
#                 daily_task_check_list = [100]

#         except:
#             f = open('task.pickle', 'wb')
#             daily_task = None
#             daily_task_amount = 0
#             daily_task_list = [100]
#             daily_task_check_list = [100]

#             pickle.dump(daily_task, f)
#             pickle.dump(daily_task_amount, f)
#             pickle.dump(daily_task_list, f)
#             pickle.dump(daily_task_check_list, f)

#         f.close()

        


#     def to_pickle():
#         Others.print_debug_log('@Syn.to_pickle')
#         f = open('task.pickle', 'wb+')
#         daily_task = None
#         daily_task_amount = None
#         daily_task_list = None
#         daily_task_check_list = None

#         pickle.dump(daily_task, f)
#         pickle.dump(daily_task_amount, f)
#         pickle.dump(daily_task_list, f)
#         pickle.dump(daily_task_check_list, f)
#         f.close()

        

#####################################################
    


#其他功能#############################################

class Others:

    def clean_cmd():
        os.system("cls")


    def print_debug_log(def_name):
        if debug_log:
            print('@ ' + def_name + '\n\n')



    #詢問是否繼續循環功能
    def continue_loop():
        Others.print_debug_log('Others.continue_loop\n\n')
        want_to_quit_value = str(input('Continue?\n(y/n)\n\n'))
        while True:
            if want_to_quit_value == 'y':
                break
            elif want_to_quit_value == 'n':
                return
            else:
                print('I don\'t understand what you mean\n')

    #重製文檔
    def reset(lugin):   #reset(路徑)
        #Others.clean_cmd()
        Others.print_debug_log('Others.reset\n\n')
        with open(lugin, 'w') as f:
            f.write('')
        print('\'' + lugin + '\' 文件重置\n\n')

#####################################################

class EncodeAndDecode:

    #主程式
    def main():
        while True:
            Others.clean_cmd()
            Others.print_debug_log('EncodeAndDecode.main')
            _ = str(input('1. 加密\n2. 解密\n3. 重置加密&解密紀錄\nq. 退出功能\n\n'))

            if _ == '1':
                EncodeAndDecode.encode()
            elif _ == '2':
                EncodeAndDecode.decode()
            elif _ == '3':
                _ = input('重置所有加密/解密紀錄嗎？\n(y/n)')
                if _ == 'y':
                    Others.reset('encode_decode_result.txt')
            elif _ == 'q':
                break
            

    #加密功能
    def encode():
        Others.clean_cmd()
        while True:
            
            Others.print_debug_log('EncodeAndDecode.encode')

            origin = input("輸入你想加密的訊息\n輸入 'q' 來退出此模式\n\n")  # 輸入原句子

            if origin == 'q':
                break
            else:
                lugin = 'encode_decode_result'


                with open('encode_decode_result.txt', 'a') as f:
                    f.write('加密\t' + origin + ' -->\n\t')

                encode_result = ''  # 重製編碼結果

                if len(origin) % 2 == 1:  # 設定 loop 次數
                    origin_convert_len = (len(origin) + 1) // 2
                    origin += ' '
                else:
                    origin_convert_len = len(origin) // 2

                for i in range(origin_convert_len):  # 編碼
                    encode_result += origin[i] + origin[len(origin) - 1 - i]
                
                Others.clean_cmd()

                print("加密結果: " + encode_result + '\n')
                with open('encode_decode_result.txt', 'a') as f:
                    f.write(encode_result + "\n\n")

            #Others.continue_loop()


    #解密功能
    def decode():
        Others.clean_cmd()
        while True:
            Others.print_debug_log('EncodeAndDecode.decode')
            origin = input("輸入你想解密的訊息\n輸入 'q' 來退出此模式\n\n")  # 輸入原句子

            if origin == 'q':
                break
            else:    
                lugin = 'encode_decode_result'

                with open('encode_decode_result.txt', 'a') as f:
                    f.write('解密\t' + origin + ' -->\n\t')

                decode_result = ''  # 重製編碼結果

                if len(origin) % 2 == 1:
                    Others.clean_cmd()
                    print('解碼失敗\n\n')
                
                else:
                    origin_convert_len = len(origin) // 2

                    for i in range(origin_convert_len):  # 編碼
                        decode_result += origin[(i * 2)]
                    for i in range(origin_convert_len):  
                        decode_result += origin[(origin_convert_len * 2) - (i * 2) - 1]

                    Others.clean_cmd()

                    print("解密結果: " + decode_result)
                    with open('encode_decode_result.txt', 'a') as f:
                        f.write(decode_result + "\n\n")

                #Others.continue_loop()
                

class Task:

    #任務主程式
    def main():
        
        #global daily_task, daily_task_amount, daily_task_list, daily_task_check_list
        
        #選擇任務主項目
        while True:

            # print('daily_task_list = ' + str(daily_task_list))
            # print('daily_task_amount = ' + str(daily_task_amount))
            # input('daily_task_check_list = ' + str(daily_task_check_list))

            try:
                with open('task.pickle', 'rb') as f:
                    daily_task_amount = pickle.load(f)
                    daily_task_list = pickle.load(f)
                    daily_task_check_list = pickle.load(f)

            except:
                daily_task_amount = int(0)
                daily_task_list = [' '] * 100
                daily_task_check_list = ['0'] * 100

                with open('task.pickle', 'wb') as f:
                    pickle.dump(daily_task_amount, f)
                    pickle.dump(daily_task_list, f)
                    pickle.dump(daily_task_check_list, f)
                

            Others.clean_cmd()
            Others.print_debug_log('Task.main')
            
            #輸入任務主項目代碼
            _ = input('你正在任務系統\n\n1. 任務系統\nq. 退出功能\n\n')

            #daily task
            if _ == '1':

                while True:

                    #Syn.from_pickle()
                    Task.daily.print_daily_task()




                    #輸入日常任務動作
                    _ = input('指令:\n\t1 : 添加新任務\n\t2 : 勾選/取消勾選任務\n\t3 : 重製勾選\n\t4 : 刪除任務\n\tq : 退出功能\n\n')
                                        
                    if _ == '1':
                        Task.daily.daily_task_add()

                    elif _ == '2':
                        Task.daily.daily_task_check()
                        
                    elif _ == '3':
                        Task.daily.daily_task_check_reset()

                    elif _ == '4':                       
                        Task.daily.daily_task_delete()

                    elif _ == 'q':
                        break



            #special task (wip)
            # elif _ == '2':
            #     while True:
            #         with open('task.pickle', 'rb') as f:
            #             special_task_amount = pickle.load(special_task_amount, f)
            #             if special_task_amount == 0:
            #                 input('You don\'t have any daily task, do you want to create some?')

            #退出任務功能
            elif _ == 'q':
                break



    class daily:

        #列印已有的日常記事 (fin)
        def print_daily_task():
            
            try:
                with open('task.pickle', 'rb') as f:
                    daily_task_amount = pickle.load(f)
                    daily_task_list = pickle.load(f)
                    daily_task_check_list = pickle.load(f)

            except:
                daily_task_amount = int(0)
                daily_task_list = [' '] * 100
                daily_task_check_list = ['0'] * 100

                with open('task.pickle', 'wb') as f:
                    pickle.dump(daily_task_amount, f)
                    pickle.dump(daily_task_list, f)
                    pickle.dump(daily_task_check_list, f)
                

            with open('task.pickle', 'rb') as f:
                daily_task_amount = pickle.load(f)
                daily_task_list = pickle.load(f)
                daily_task_check_list = pickle.load(f)

            if daily_task_amount == int(0):
                #沒有日常任務
                Others.clean_cmd()
                print('你沒有任何任務\n\n')
                            
            else:
                #有日常任務
                Others.clean_cmd()
                print('你共有' + str(daily_task_amount) + '個任務')
                if daily_task_amount == None:
                    #日常任務數量 為 None (錯誤)
                    print('ERROR: daily_task_amount is nonetype\n\n')
                else:
                    #日常任務正常 未完成
                    print('未完成 :\n')
                    for i in range(daily_task_amount):
                        if daily_task_check_list[i] == '1':
                            print(str(int(i)+1) + '. ' + str(daily_task_list[i]))
                    print('\n')

                    #日常任務正常 已完成
                    print('已完成 :\n')
                    for i in range(daily_task_amount):
                        if daily_task_check_list[i] == '2':
                            print(str(int(i)+1) + '. ' + str(daily_task_list[i]))
                    print('\n')



        #日常代辦 增加 (fin)
        def daily_task_add():
            
            #傳入pickle資料
            with open('task.pickle', 'rb') as f:
                daily_task_amount = pickle.load(f)
                daily_task_list = pickle.load(f)
                daily_task_check_list = pickle.load(f)

            #添加任務
            while True:
                Others.clean_cmd()
                Others.print_debug_log('Task.daily_task_add')
                
                #新增日常任務名字
                _ = str(input('輸入新任務的名字\n輸入 \'q\' 來退出此模式\n\n') )    

                #退出當前功能                   
                if _ == 'q':
                    break
                
                #輸入
                else:

                    #名字占存
                    task_want_to_add = _
                    Others.clean_cmd()

                    #日常任務編號指定
                    _ = input('輸入任務的編號\n或者按下 enter 跳過\n\n')           
                    

                    #編號卡在中間
                    if _.isdigit() == True and int(_) < daily_task_amount and 0 < int(_): 

                        for i in range(daily_task_amount - int(_) + 1):
                            daily_task_list[daily_task_amount - i] = daily_task_list[daily_task_amount - i - 1]
                            daily_task_check_list[daily_task_amount - i] = daily_task_check_list[daily_task_amount - i - 1]
                        daily_task_list[int(_) - 1] = task_want_to_add
                        daily_task_check_list[int(_) - 1] = '1'

                    #編號沒卡
                    else:

                        daily_task_list[int(daily_task_amount)] = str(task_want_to_add)
                        daily_task_check_list[int(daily_task_amount)] = '1'

                    daily_task_amount = int(daily_task_amount) + 1

                with open('task.pickle', 'wb') as f:
                    pickle.dump(daily_task_amount, f)
                    pickle.dump(daily_task_list, f)
                    pickle.dump(daily_task_check_list, f)



        #日常代辦 勾選 (fin)
        def daily_task_check():
            Others.print_debug_log('Task.daily_task_check')

            #傳入pickle資料
            with open('task.pickle', 'rb') as f:
                daily_task_amount = pickle.load(f)
                daily_task_list = pickle.load(f)
                daily_task_check_list = pickle.load(f)

            #檢查任務數量
            if daily_task_amount == int(0):
                input("你沒有任何任務\n")
                return


            while True:
                Task.daily.print_daily_task()
                _ = input('勾選/取消勾選任務\n輸入 \'q\' 來退出此模式\n\n')

                #測試變數是否可以為數字
                if _.isdigit():

                    if int(_) <= daily_task_amount and int(_) > 0:
                        if daily_task_check_list[int(_)-1] == '1' or None:
                            daily_task_check_list[int(_)-1] = '2'
                        elif daily_task_check_list[int(_)-1] == '2':
                            daily_task_check_list[int(_)-1] = '1'
                    else:
                        Others.clean_cmd()
                        input('勾選失敗\n')

                elif _ == 'q':
                    break


                # elif type(_) == str:

                #     if int(_) <= daily_task_amount and int(_) > 0:
                #         if daily_task_check_list[int(_)-1] == 0 or None:
                #             daily_task_check_list[int(_)-1] = 1
                #         elif daily_task_check_list[int(_)-1] == 1:
                #             daily_task_check_list[int(_)-1] = 0


                

                else:
                    Others.clean_cmd()
                    input('勾選失敗\n')

                with open('task.pickle', 'wb') as f:
                    pickle.dump(daily_task_amount, f)
                    pickle.dump(daily_task_list, f)
                    pickle.dump(daily_task_check_list, f)



        #日常代辦 重製勾選
        def daily_task_check_reset():
            Others.print_debug_log('Task.daily_task_check_reset')
            

            #傳入pickle資料 #重要important!!!!! 讀取順序會影響資料存放的地方
            with open('task.pickle', 'rb') as f:
                daily_task_amount = pickle.load(f)
                daily_task_list = pickle.load(f)
                daily_task_check_list = pickle.load(f)

            
            while True:
                Others.clean_cmd()
                Task.daily.print_daily_task()
                _ = input('重置所有任務的勾選？ (y/n)\n')

                if _ == 'y':

                    # with open('task.pickle', 'rb') as f:
                    #     daily_task_amount = pickle.load(f)

                    #input(daily_task_check_list)

                    #daily_task_check_list[1] = [1] * daily_task_amount

                    # print('daily_task_list = ' + str(daily_task_list))
                    # print('daily_task_amount = ' + str(daily_task_amount))
                    # input('daily_task_check_list = ' + str(daily_task_check_list))

                    #daily_task_check_list[0:daily_task_amount] = ['1']

                    for i in range(int(daily_task_amount)):  #daily_task_amount被認為是list (fin)       TypeError: ‘list’ object cannot be interpreted as an integer
                        daily_task_check_list[i] = '1'       #                                          'int' object does not support item assignment

                    

                    #daily_task_check_list = ['0'] * 100
                    with open('task.pickle', 'wb') as f:        #出大問題 (好沒事了)
                        pickle.dump(daily_task_amount, f)
                        pickle.dump(daily_task_list, f)
                        pickle.dump(daily_task_check_list, f)
                    break

                elif _ == 'n':
                    break

                else:
                    pass

        #日常代辦 刪除 (fin)
        def daily_task_delete():
            

            #傳入pickle資料
            with open('task.pickle', 'rb') as f:
                daily_task_amount = pickle.load(f)
                daily_task_list = pickle.load(f)
                daily_task_check_list = pickle.load(f)

                while True:
                    Others.clean_cmd()
                    Task.daily.print_daily_task()
                    Others.print_debug_log('Task.daily_task_delete')
                    


                    _ = input('Which daily task do you want to delete\nType \'q\' to quit this function\n\n')

            
                    if _.isdigit():
                        _ = int(_)
                        if _ > 0 and _ <= daily_task_amount:
                            if daily_task_amount != 1:
                                for i in range(daily_task_amount-_):
                                    daily_task_list[_-1+i] = daily_task_list[_+i]
                                    daily_task_check_list[_-1+i] = daily_task_check_list[_+i]
                                
                            else:
                                daily_task_list[0] = ' '
                                daily_task_check_list[0] = '0'
                            
                            daily_task_amount -= 1
                    
                            #print('任務 \'' + str(_) + '\' 刪除成功\n\n')



                            with open('task.pickle', 'wb') as f:
                                pickle.dump(daily_task_amount, f)
                                pickle.dump(daily_task_list, f)
                                pickle.dump(daily_task_check_list, f)

                        else:
                            Others.clean_cmd()
                            input('刪除失敗\n')


                    elif _ == 'q':
                        break



                    else:
                        Others.clean_cmd()
                        input('刪除失敗\n')


            




# 主要程式 ################################################################    

# window1 = tk.Tk()
# window1.title('IDK WATS THIS')
# window1.configure(background = '#ffffff')
# window1.geometry('600x300')

while True:
    Others.clean_cmd()
    _ = str(input('1. 加密/解密\n2. 任務系統\n3. 重置所有檔案\nq. 退出\n\n'))

    if _ == '1':
        EncodeAndDecode.main()
    elif _ == '2':
        Task.main()
    elif _ == '3':
        Others.clean_cmd()
        _ = input('重置所有檔案嗎？\n(y/n)\n')
        if _ == 'y':
            Others.clean_cmd()
            #Others.reset('encode_decode_result.txt')
            Others.reset('task.pickle')

            input()

            try:
                with open('task.pickle', 'rb') as f:
                    daily_task_amount = pickle.load(f)
                    daily_task_list = pickle.load(f)
                    daily_task_check_list = pickle.load(f)

            except:
                daily_task_amount = int(0)
                daily_task_list = [' '] * 100
                daily_task_check_list = ['0'] * 100

                with open('task.pickle', 'wb') as f:
                    pickle.dump(daily_task_amount, f)
                    pickle.dump(daily_task_list, f)

                    pickle.dump(daily_task_check_list, f)
                
        else:
            pass
            


    elif _ == 'q':
        break
    








"""

foo_list = [2,4,6] #算出的數值

with open('foo_list.pickle', 'wb') as f:    #with open('(pickle檔名)', 'wb') as (pickle檔內變數):      wb代表寫入資料    write
    pickle.dump(foo_list, f)                #   pickle.dump((py檔內變數), (pickle檔內變數))



with open('foo_list.pickle', 'rb') as f:    #with open('(pickle檔名)', 'rb') as (pickle檔內變數):      rb代表讀取資料    read
    foo_list = pickle.load(f)               #   (py檔內變數) = pickle.load((pickle檔內變數))

print(foo_list)
# output: [2, 4, 6]

"""