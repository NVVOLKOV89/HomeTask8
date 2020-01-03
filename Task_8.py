import time
import os
import psutil
import sys

My_List = []
def show_time(f):
    next_list = []
    def wrapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        strtproc = proc.memory_info().rss/1000000
        starttime = time.time()
        f(*args, **kwargs)
        stoptime = time.time()
        proc = psutil.Process(os.getpid())
        stopproc = proc.memory_info().rss/1000000
        print('Затраченное время на выполнение:', stoptime - starttime)
        print('Затраченное память на выполнение:', stopproc - strtproc)
    return wrapper

@show_time
def funk_my(numb):
    funk_list = []
    for i in range(numb + 1):
        funk_list.append([i, i**i])
    return print(funk_list)

funk_my(500)

#Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).
nat_list = []
starttime = time.time()
nat_list = [x for x in range (1000000 )]
stoptime = time.time()
list_time = stoptime - starttime
list_proc = sys.getsizeof(nat_list)



starttime_gen = time.time()
nat_list_gen = (x for x in range (1000000 ))
stoptime_gen = time.time()
list_time_gen = stoptime_gen - starttime_gen
list_proc_gen = sys.getsizeof(nat_list_gen)

print('Gen работает быстрее на:', list_time - list_time_gen)
print('Gen занимает меньше памяти на:', list_proc - list_proc_gen)
