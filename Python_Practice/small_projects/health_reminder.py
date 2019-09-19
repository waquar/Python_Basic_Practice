from pygame import mixer
from  datetime import  datetime
from time import time
from stopwatch import  Stopwatch



def musicOnloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def logwriter(msg):
    with open('records.txt', 'a') as f:
        f.write( f"{msg} {datetime.now()} \n")

if __name__ == '__main__':
    #musicOnloop('Yaar Mere.mp3', 'stop')
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watertime = 7
    eyetime = 20
    exercisetime = 26
    stopwatch = Stopwatch()
    stopwatch.start()

    # while True:
    #     time.sleep(1)fdnkjlgojihdf
    #     print(datetime.now())
    while True:
        if time() - init_water > watertime:
            print("water drink time reminder!  write stop to kill the alarm")
            musicOnloop('godfather.mp3', 'stop')
            init_water = time()
            logwriter('Drank water at this time : ')

        if time() - init_eyes > eyetime:
            print("eye relax time reminder!  write stop to kill the alarm")
            musicOnloop('joker1.mp3', 'stop')
            init_eyes = time()
            logwriter('Did eye exercise at this time : ')

        if time() - init_exercise > exercisetime:
            print("exercise time reminder!  write stop to kill the alarm")
            musicOnloop('joker2.mp3', 'stop')
            init_exercise = time()
            logwriter('Did physical exercise at this time : ')





