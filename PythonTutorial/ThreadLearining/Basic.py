# Basic Creation of thread
# import threading
#
#
# def f():
#     print('Thread function\n')
#     return
#
#
# for i in range(3):
#     t = threading.Thread(target=f)
#     t.start()


# Basic Custom thread Creation
# import threading
#
#
# class CustomThread(threading.Thread):
#     def run(self):
#         print('Custom thread function.\n')
#
#
# for i in range(3):
#     t = CustomThread()

# Start thread with arguments
# import threading
# import time
#
#
# def f(i):
#     for p in range(3):
#         time.sleep(i+1)
#         print('Thread #',i,"\n")
#         time.sleep(i)
#         return
#
#
# # start threads by passing function to Thread constructor
# for i in range(3):
#     t = threading.Thread(target=f, args=(i,))
#     t.start()


# Play with thread
# import threading
# import time
#
#
# def f(i):
#     for p in range(3):
#         time.sleep(i+1.5)
#         print(threading.current_thread().getName())
#         return
#
#
# # start threads by passing function to Thread constructor
# for i in range(3):
#     t = threading.Thread(target=f, args=(i,))
#     t.setName( 'Thread#'+str(i) )
#     t.start()