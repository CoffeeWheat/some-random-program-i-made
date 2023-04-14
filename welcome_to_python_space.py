# 傳入pickle資料 #重要important!!!!! 讀取順序會影響資料存放的地方
    # with open('task.pickle', 'rb') as f:
    #     daily_task_amount = pickle.load(f)
    #     daily_task_list = pickle.load(f)
    #     daily_task_check_list = pickle.load(f)




import pickle #引進pickle函式庫
import os



debug_log = False

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
        print('Document \'' + lugin + '\'reset\n\n')

#####################################################

class EncodeAndDecode:

    #主程式
    def main():
        while True:
            Others.clean_cmd()
            Others.print_debug_log('EncodeAndDecode.main')
            _ = str(input('1. Encode\n2. Decode\n3. Reset Encode and Decode Document\n4. Quit Function\n\n'))

            if _ == '1':
                EncodeAndDecode.encode()
            elif _ == '2':
                EncodeAndDecode.decode()
            elif _ == '3':
                Others.reset('encode_decode_result.txt')
            elif _ == '4':
                break
            

    #加密功能
    def encode():
        Others.clean_cmd()
        while True:
            
            Others.print_debug_log('EncodeAndDecode.encode')

            origin = input("Type the sentence you want to encode\nType 'q' to cancel the progress\n\n")  # 輸入原句子

            if origin == 'q':
                break
            else:
                lugin = 'encode_decode_result'


                with open('encode_decode_result.txt', 'a') as f:
                    f.write('ENCODE\t' + origin + ' -->\n\t')

                encode_result = ''  # 重製編碼結果

                if len(origin) % 2 == 1:  # 設定 loop 次數
                    origin_convert_len = (len(origin) + 1) // 2
                    origin += ' '
                else:
                    origin_convert_len = len(origin) // 2

                for i in range(origin_convert_len):  # 編碼
                    encode_result += origin[i] + origin[len(origin) - 1 - i]
                
                Others.clean_cmd()

                print("Encoded result: " + encode_result)
                with open('encode_decode_result.txt', 'a') as f:
                    f.write(encode_result + "\n\n")

            #Others.continue_loop()


    #解密功能
    def decode():
        Others.clean_cmd()
        while True:
            Others.print_debug_log('EncodeAndDecode.decode')
            origin = input("Type the sentence you want to decode\nType 'q' to cancel the progress\n\n")  # 輸入原句子

            if origin == 'q':
                break
            else:    
                lugin = 'encode_decode_result'

                with open('encode_decode_result.txt', 'a') as f:
                    f.write('DECODE\t' + origin + ' -->\n\t')

                decode_result = ''  # 重製編碼結果

                if len(origin) % 2 == 1:
                    Others.clean_cmd()
                    print('I don\'t think I can decode this\n\n')
                
                else:
                    origin_convert_len = len(origin) // 2

                    for i in range(origin_convert_len):  # 編碼
                        decode_result += origin[(i * 2)]
                    for i in range(origin_convert_len):  
                        decode_result += origin[(origin_convert_len * 2) - (i * 2) - 1]

                    Others.clean_cmd()

                    print("Encoded result: " + decode_result)
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
            _ = input('Welcome to Task system!\n\n1. Daily Task\n2. Special Task\n3. Quit Function\n\n')

            #daily task
            if _ == '1':

                while True:

                    #Syn.from_pickle()
                    Task.daily.print_daily_task()




                    #輸入日常任務動作
                    _ = input('Command List:\n\tadd : add a daily task\n\tcheck : check a task\n\treset : reset all daily task\n\tdelete : delete a daily task\n\tq : quit this progress\n\n')
                                        
                    if _ == 'add':
                        Task.daily.daily_task_add()

                    elif _ == 'check':
                        Task.daily.daily_task_check()
                        
                    elif _ == 'reset':
                        Task.daily.daily_task_check_reset()

                    elif _ == 'delete':                       
                        Task.daily.daily_task_delete()

                    elif _ == 'q':
                        break

                    else:
                        Others.clean_cmd()
                        print('I didn\'t made this function.\n\n')

            #special task (wip)
            elif _ == '2':
                while True:
                    with open('task.pickle', 'rb') as f:
                        special_task_amount = pickle.load(special_task_amount, f)
                        if special_task_amount == 0:
                            input('You don\'t have any daily task, do you want to create some?')

            #退出任務功能
            elif _ == '3':
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
                print('You don\'t have any daily task\n\n')
                            
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
                _ = str(input('What task do you want to add\nType "q" to cancel the progress\n\n') )    

                #退出當前功能                   
                if _ == 'q':
                    break
                
                #輸入
                else:

                    #名字占存
                    task_want_to_add = _
                    Others.clean_cmd()

                    #日常任務編號指定
                    _ = input('Do you want to specify it a number?\nType number\npress enter to cancel specify\n\n')           
                    

                    #編號卡在中間
                    if _ == int and _ < daily_task_amount and 0 < _: 

                        for i in range(daily_task_amount - _ + 1):
                            daily_task_list[daily_task_amount + 1 - i] = daily_task_list[daily_task_amount - i]
                            daily_task_check_list[daily_task_amount + 1 - i] = daily_task_check_list[daily_task_amount - i]
                        daily_task_list[_ - 1] = task_want_to_add
                        daily_task_check_list[_ - 1] = '1'

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
                input("You don't have any daily task\n")
                return


            while True:
                Task.daily.print_daily_task()
                _ = input('Check & Discard check tasks\n\nType task id\nType "q" to quit the function\n\n')

                #測試變數是否可以為數字
                if _.isdigit():

                    if int(_) <= daily_task_amount and int(_) > 0:
                        if daily_task_check_list[int(_)-1] == '1' or None:
                            daily_task_check_list[int(_)-1] = '2'
                        elif daily_task_check_list[int(_)-1] == '2':
                            daily_task_check_list[int(_)-1] = '1'
                    else:
                        Others.clean_cmd()
                        input('Check failed\n')

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
                    input('Check failed\n')

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
                _ = input('Reset all daily check? (y/n)\n')

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
                    with open('task.pickle', 'wb') as f:        #出大問題
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
                    
                            print('\nDaily Task \'' + str(_) + '\' has been delete\n\n')



                            with open('task.pickle', 'wb') as f:
                                pickle.dump(daily_task_amount, f)
                                pickle.dump(daily_task_list, f)
                                pickle.dump(daily_task_check_list, f)

                    elif _ == 'q':
                        break



                    else:
                        input('Delete daily task failed\n')


            




# 主要程式 ################################################################    

while True:
    Others.clean_cmd()
    _ = str(input('1. Encode and Decode\n2. Task\n3. Reset Files\n4. Quit\n\n'))

    if _ == '1':
        EncodeAndDecode.main()
    elif _ == '2':
        Task.main()
    elif _ == '3':
        _ = input('Do you really want to reset?\n(y/n)\n')
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
            


    elif _ == '4':
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