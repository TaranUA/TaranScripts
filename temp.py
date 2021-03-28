import sched
from random import randint
from time import sleep, strftime, time

s = sched.scheduler(time, sleep)
temp=0

#in seconds
start_delay = 1
period = 5
samples=10
filename="temp.csv"

def write_temp(temp):
    file = open(filename, "r")
    nonempty_lines = [line.strip("\n") for line in file if line != "\n"]
    line_count = len(nonempty_lines)
    file.close()
    
    if line_count > samples :
        a_file = open(filename, "r")
        lines = a_file.readlines()
        #print(lines)
        last_lines = lines[-samples:]
        #print(last_lines)
        a_file.close()
        new_file = open(filename, "w+")
        for line in last_lines:
            new_file.write(line)
        new_file.close()
            
    with open(filename, "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

        
def get_temp():
    temp=randint(25,50)
    print("Current temp:", temp)
    write_temp(temp)


def do_something(sc): 
    # do your stuff
    get_temp()
    # do your stuff
    s.enter(period, 1, do_something, (sc,))

s.enter(start_delay, 1, do_something, (s,))
s.run()


