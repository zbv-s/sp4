import os
import multiprocessing as mp

def bigrams(word, q):
    from collections import Counter
    print(f"Proccess {{PID={os.getpid()}, PPID={os.getppid()}}}:count frequency bigram ")
    res=Counter(word[idx : idx + 2] for idx in range(len(word)-1))
    print(f"Proccess PID {os.getpid()}: get ans: {res}")
    q.put(res)

def division_text(test_str):
     print(f"Proccess {{PID={os.getpid()}, PPID={os.getppid()}}}:count frequency bigram ")
     procs = []
     q = mp.Queue()
     words = test_str.split()
     for word in words:
         proc = mp.Process(target=bigrams, args=(word, q))
         procs.append(proc)
         proc.start()
         result = q.get()
     for proc in procs:
         proc.join()
     return result
        
if __name__ == '__main__':
      test_str = input("Enter the string: ")
      res = division_text(test_str)  
#      print(word + " : " + str(dict(res)))
