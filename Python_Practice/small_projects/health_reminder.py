from pygame import mixer
from  datetime import  datetime
from time import time


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
    with open('recoreds.txt', 'a') as f:
        f.write( f"{msg} {datetime.now()} \n")

if __name__ == '__main__':
    #musicOnloop('Yaar Mere.mp3', 'stop')
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watertime = 7
    eyetime = 15
    exercisetime = 22
    while True:
        if time() - init_water > watertime:
            print("water drink time reminder!  write stop to kill the alarm")
            musicOnloop('Pouring-liquid-into-metal-canister.mp3', 'stop')
            init_water = time()
            logwriter('Drank water at this time : ')

        if time() - init_eyes > eyetime:
            print("eye relax time reminder!  write stop to kill the alarm")
            musicOnloop('Yaar Mere.mp3', 'stop')
            init_eyes = time()
            logwriter('Did eye exercise at this time : ')

        if time() - init_exercise > exercisetime:
            print("exercise time reminder!  write stop to kill the alarm")
            musicOnloop('Photo Remix.mp3', 'stop')
            init_exercise = time()
            logwriter('Did physical exercise at this time : ')





