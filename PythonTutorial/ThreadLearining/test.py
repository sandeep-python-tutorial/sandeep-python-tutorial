import threading
import time


def f(i):
    for p in range(3):
        time.sleep(i+1.5)
        print(threading.current_thread().getName())
        print(threading.current_thread().is_alive())
        print(threading.current_thread().isDaemon())
        print(threading.current_thread())
        print(threading.get_ident())
        #print(threading.getprofile())
        #print(threading.gettrace())
        print(threading.main_thread())
        return

my_list =[]
# start threads by passing function to Thread constructor
for i in range(3):
    t = threading.Thread(target=f, args=(i,))
    # t.setName( 'Thread#'+str(i) )
    # t.setDaemon(True)
    t.start()
    t.join(30)
    # print (t.getName())
    # print(t.isDaemon())
    # print(t.is_alive())
    # print(t.ident)
    # print(t.native_id)
    # Befor Start the demon

    # print(t.isDaemon())




