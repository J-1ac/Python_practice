#thread_test.py
import time
import threading                                #thread 모듈 import

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" %i)

print("Start")

threads = []

for i in range(5):
    t = threading.Thread(target=long_task)      #thread 생성
    threads.append(t)

for t in threads:
    t.start()                                   #thread 실행

for t in threads:
    t.join()                                    #join함수로 thread가 종료될때까지 기다림

print("End")