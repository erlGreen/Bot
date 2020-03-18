import pyautogui as pag
import numpy as np
import threading
import time
import cv2
import random


def razuthread():
    results = [0, 0, 0]
    razuFindValue = [0, 0, 0]
    razuLoc = [0, 0, 0]
    razupx = [0, 0, 0]
    razupy = [0, 0, 0]
    global findRazuEvent, screenshot, razu, ax1, ax2, ay1, ay2, method, razuSafeClick, lock, checkRazu, razuLogin, showRazu, razuStartCounting

    while True:
        findRazuEvent.wait()
        findRazuEvent.clear()
        if razuStartCounting != 0 and time.time() - razuStartCounting > 300:
            with lock:
                pag.click(razuSafeClick)
                pag.keyDown('up')
            time.sleep(0.3)
            with lock:
                pag.click(razuSafeClick)
                pag.keyUp('up')
            razuStartCounting = time.time()
        crop = screenshot[ry1:ry2, rx1:rx2]
        #print("checking razu")
        results[0] = cv2.matchTemplate(razu[0], crop, method)
        results[1] = cv2.matchTemplate(razu[1], crop, method)
        results[2] = cv2.matchTemplate(razu[2], crop, method)

        _, razuFindValue[0], _, razuLoc[0] = cv2.minMaxLoc(results[0])
        _, razuFindValue[1], _, razuLoc[1] = cv2.minMaxLoc(results[1])
        _, razuFindValue[2], _, razuLoc[2] = cv2.minMaxLoc(results[2])
        #print("razu " + str(razuFindValue))

        razupx[0], razupy[0] = razuLoc[0]
        razupx[1], razupy[1] = razuLoc[1]
        razupx[2], razupy[2] = razuLoc[2]

        counter = 0
        bestresult = 0
        if razuFindValue[0] > 0.34:
            if razuFindValue[0] > bestresult:
                bestresult = razuFindValue[0]
            counter += 1
        if razuFindValue[1] > 0.34:
            if razuFindValue[1] > bestresult:
                bestresult = razuFindValue[1]
            counter += 1
        if razuFindValue[2] > 0.34:
            if razuFindValue[2] > bestresult:
                bestresult = razuFindValue[2]
            counter += 1

        if showRazu is True:
            cv2.imshow('r', crop)
            cv2.waitKey(1)

        if counter == 0:
            continue
        elif bestresult == razuFindValue[0]:
            px, py = razuLoc[0]
        elif bestresult == razuFindValue[1]:
            px, py = razuLoc[1]
        else:
            px, py = razuLoc[2]

        print("razu found")
        checkRazu = False
        time.sleep(0.25)
        pag.click(rx1 + px + 30, ry1 + py + 30)
        time.sleep(8)
        with lock:
            pag.click(razuSafeClick)
            pag.press('f')
        ruch = bool(random.getrandbits(1))
        if ruch is True:
            time.sleep(2)
            with lock:
                pag.click(razuSafeClick)
                pag.keyDown('up')
            time.sleep(0.3)
            with lock:
                pag.click(razuSafeClick)
                pag.keyUp('up')
        pag.click(razuLogout1)  # logout
        time.sleep(3 + random.randrange(11))
        pag.click(razuLogout2)  # logout
        time.sleep(360 + random.randrange(20))
        try:
            pag.click(razuLogin)  # login
        except:
            img = pag.screenshot()
            cv2.imwrite('/home/erl/Desktop/error2.png', img)  # login
            print("exception razu")
        checkRazu = True
        print("look for razu")
        makeSSEvent.set()
        razuStartCounting = time.time()


def aliasthread():
    results = [0, 0, 0, 0, 0]
    aliasFindValue = [0, 0, 0, 0, 0]
    aliasLoc = [0, 0, 0, 0, 0]
    aliaspx = [0, 0, 0, 0, 0]
    aliaspy = [0, 0, 0, 0, 0]
    global findAliasEvent, screenshot, alias, ax1, ax2, ay1, ay2, method, aliasSafeClick, lock, checkAlias, aliasLogin, showAlias, aliasStartCounting

    while True:
        findAliasEvent.wait()
        findAliasEvent.clear()
        if aliasStartCounting != 0 and time.time() - aliasStartCounting > 300:
            with lock:
                pag.click(aliasSafeClick)
                pag.keyDown('up')
            time.sleep(0.3)
            with lock:
                pag.click(aliasSafeClick)
                pag.keyUp('up')
            aliasStartCounting = time.time()
        crop = screenshot[ay1:ay2, ax1:ax2]
        #print("checking alias")
        results[0] = cv2.matchTemplate(alias[0], crop, method)
        results[1] = cv2.matchTemplate(alias[1], crop, method)
        results[2] = cv2.matchTemplate(alias[2], crop, method)
        results[3] = cv2.matchTemplate(alias[3], crop, method)
        results[4] = cv2.matchTemplate(alias[4], crop, method)

        _, aliasFindValue[0], _, aliasLoc[0] = cv2.minMaxLoc(results[0])
        _, aliasFindValue[1], _, aliasLoc[1] = cv2.minMaxLoc(results[1])
        _, aliasFindValue[2], _, aliasLoc[2] = cv2.minMaxLoc(results[2])
        _, aliasFindValue[3], _, aliasLoc[3] = cv2.minMaxLoc(results[3])
        _, aliasFindValue[4], _, aliasLoc[4] = cv2.minMaxLoc(results[4])
        #print("alias " + str(aliasFindValue))

        aliaspx[0], aliaspy[0] = aliasLoc[0]
        aliaspx[1], aliaspy[1] = aliasLoc[1]
        aliaspx[2], aliaspy[2] = aliasLoc[2]
        aliaspx[3], aliaspy[3] = aliasLoc[3]
        aliaspx[4], aliaspy[4] = aliasLoc[4]

        counter = 0
        bestresult = 0
        if aliasFindValue[0] > 0.5:
            if aliasFindValue[0] > bestresult:
                bestresult = aliasFindValue[0]
            counter += 1
        if aliasFindValue[1] > 0.5:
            if aliasFindValue[1] > bestresult:
                bestresult = aliasFindValue[1]
            counter += 1
        if aliasFindValue[2] > 0.5:
            if aliasFindValue[2] > bestresult:
                bestresult = aliasFindValue[2]
            counter += 1
        if aliasFindValue[3] > 0.5:
            if aliasFindValue[3] > bestresult:
                bestresult = aliasFindValue[3]
            counter += 1
        if aliasFindValue[4] > 0.5:
            if aliasFindValue[4] > bestresult:
                bestresult = aliasFindValue[4]
            counter += 1

        if showAlias is True:
            cv2.imshow('a', crop)
            cv2.waitKey(1)

        if counter == 0:
            continue
        elif bestresult == aliasFindValue[0]:
            px, py = aliasLoc[0]
        elif bestresult == aliasFindValue[1]:
            px, py = aliasLoc[1]
        elif bestresult == aliasFindValue[2]:
            px, py = aliasLoc[2]
        elif bestresult == aliasFindValue[3]:
            px, py = aliasLoc[3]
        else:
            px, py = aliasLoc[4]
        print("alias found")
        checkAlias = False
        time.sleep(0.5)
        pag.click(ax1 + px + 30, ay1 + py + 30)
        time.sleep(8)
        with lock:
            pag.click(aliasSafeClick)
            pag.press('f')
        ruch = bool(random.getrandbits(1))
        if ruch is True:
            time.sleep(2)
            with lock:
                pag.click(aliasSafeClick)
                pag.keyDown('up')
            time.sleep(0.3)
            with lock:
                pag.click(aliasSafeClick)
                pag.keyUp('up')
        with lock:
            pag.click(aliasLogout1)  # logout
            pag.press('1')
        time.sleep(3 + random.randrange(11))
        pag.click(aliasLogout2)  # logout
        time.sleep(360 + random.randrange(20))
        try:
            pag.click(aliasLogin)  # login
        except:
            img = pag.screenshot()
            cv2.imwrite('/home/erl/Desktop/error1.png', img)
            print("exception alias")
        checkAlias = True
        print("look for alias")
        makeSSEvent.set()
        aliasStartCounting = time.time()


''''# 2560x1440  alias/firefox/lewo
ax1 = 1920 + 250
ax2 = 1920 + 650
ay1 = 600
ay2 = 1000
aliasLogout1 = (1920 + 80, 150)
aliasLogout2 = (1920 + 150, 340)
aliasLogin = (1920 + 85, 110)
aliasSafeClick = (2600, 160)

# 2560x1440  razu/chrome/prawo
rx1 = 3550
rx2 = 3860
ry1 = 320
ry2 = 670
razuLogout1 = (3250, 150)
razuLogout2 = (3350, 430)
razuLogin = (3250, 450)
razuSafeClick = (3850, 160)'''

# 1360x768  alias/firefox/lewo
ax1 = 150
ax2 = 500
ay1 = 300
ay2 = 700
aliasLogout1 = (80, 150)
aliasLogout2 = (150, 340)
aliasLogin = (85, 110)
aliasSafeClick = (400, 160)

# 1360x768  razu/chrome/prawo
rx1 = 750
rx2 = 1200
ry1 = 200
ry2 = 530
razuLogout1 = (730, 150)
razuLogout2 = (830, 430)
razuLogin = (1150, 450)
razuSafeClick = (1050, 155)

showAlias = False
showRazu = False

razuStartCounting = 0
aliasStartCounting = 0

alias = [cv2.imread('/home/erl/Desktop/Bot/1.png'), cv2.imread('/home/erl/Desktop/Bot/2.png'),
         cv2.imread('/home/erl/Desktop/Bot/3.png'), cv2.imread('/home/erl/Desktop/Bot/4.png'),
         cv2.imread('/home/erl/Desktop/Bot/5.png')]

razu = [cv2.imread('/home/erl/Desktop/Bot/r.png'), cv2.imread('/home/erl/Desktop/Bot/e.png'),
        cv2.imread('/home/erl/Desktop/Bot/t.png')]


makeSSEvent = threading.Event()
findAliasEvent = threading.Event()
findRazuEvent = threading.Event()
lock = threading.Lock()

checkAlias = True
checkRazu = True
method = cv2.TM_CCOEFF_NORMED
screenshot = 0

aliasThread = threading.Thread(target=aliasthread)
aliasThread.start()

razuThread = threading.Thread(target=razuthread)
razuThread.start()

while True:
    if checkAlias is False and checkRazu is False:
        makeSSEvent.wait()
        makeSSEvent.clear()
    screenshot = np.array(pag.screenshot())
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    #print("screenshot")
    if checkAlias is True:
        findAliasEvent.set()
    if checkRazu is True:
        findRazuEvent.set()
    time.sleep(1.5)
