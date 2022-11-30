import time
import os
import subprocess
import board
import digitalio

os.system(f"sudo python3 /home/pi/door/led_startup.py &")

os.system('amixer cset numid=1 100%')
os.system("cvlc --play-and-exit /home/pi/portal/portal_start.mp3")
# subprocess.Popen('amixer cset numid=1 100%', shell=True)
# subprocess.Popen("cvlc --play-and-exit /home/pi/portal/portal_start.mp3", shell=True)

s1 = digitalio.DigitalInOut(board.D17)
s1.direction = digitalio.Direction.INPUT
s1.pull = digitalio.Pull.DOWN

isopen = s1.value


while True:
        #if (s1.value) == True:
        #       print("closed")
        #else:
        #        print("open")
        if (s1.value != isopen):
                isopen = s1.value
                if isopen == True:
                        print("closed")
                        os.system(f"sudo python3 /home/pi/door/led_close.py &")
                else:
                        print("open")
                        os.system(f"sudo python3 /home/pi/door/led_open.py &")
                        os.system("cvlc --play-and-exit /home/pi/portal/bbc_comedy-sou_07005034.mp3")

        time.sleep(0.05)