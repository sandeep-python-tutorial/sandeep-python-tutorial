# from multiprocessing import Process, Queue
# import random
#
# def rand_num():
#     num = random.random()
#     print(num)
#
# if __name__ == "__main__":
#     queue = Queue()
#
#     processes = [Process(target=rand_num, args=()) for x in range(4)]
#
#     for p in processes:
#         p.start()
#
#     for p in processes:
#         p.join()

# import multiprocessing as mp
#
# def my_func(x):
#   print(mp.current_process())
#   return x**x
#
# def main():
#   pool = mp.Pool(mp.cpu_count())
#   result = pool.map(my_func, [4,2,3,5,3,2,1,2])
#   result_set_2 = pool.map(my_func, [4,6,5,4,6,3,23,4,6])
#
#   print(result)
#   print(result_set_2)
#
# if __name__ == "__main__":
#   main()

# from multiprocessing import Process, Queue
# import random
#
# def rand_num(queue):
#     num = random.random()
#     queue.put(num)
#
# if __name__ == "__main__":
#     queue = Queue()
#
#     processes = [Process(target=rand_num, args=(queue,)) for x in range(4)]
#
#     for p in processes:
#         p.start()
#
#     for p in processes:
#         p.join()
#
#     results = [queue.get() for p in processes]
#
#     print(results)

#
# from multiprocessing import Process, Pipe
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv()) # prints "[42, None, 'hello']"
#     p.join()


# from multiprocessing import Process, Lock
# def dispmay_name(l, i):
#     l.acquire()
#     print ('Hi', i)
#     l.release()
# if __name__ == '__main__':
#     my_lock = Lock()
#     my_name = ['Aadrika', 'Adwaita', 'Sakya', 'Sanj']
#     for name in my_name:
#         Process(target=dispmay_name, args=(my_lock,name)).start()

# import multiprocessing, logging
# logger = multiprocessing.log_to_stderr()
# logger.setLevel(logging.INFO)
# logger.warning('Error has occurred')