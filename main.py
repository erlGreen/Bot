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
    global findRazuEvent, screenshot, razu, ax1, ax2, ay1, ay2, method, razuSafeClick, lock, checkRazu, razuLogin, showRazu, razuStartCounting, razuReload

    while True:
        findRazuEvent.wait()
        findRazuEvent.clear()
        if time.time() - razuStartCounting > 300:
            with lock:
                pag.click(razuSafeClick)
                pag.keyDown('up')
                time.sleep(0.3)
                pag.keyUp('up')
                pag.click(razuReload)
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
        if razuFindValue[0] > 0.7:
            if razuFindValue[0] > bestresult:
                bestresult = razuFindValue[0]
            counter += 1
        if razuFindValue[1] > 0.7:
            if razuFindValue[1] > bestresult:
                bestresult = razuFindValue[1]
            counter += 1
        if razuFindValue[2] > 0.7:
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
        time.sleep(0.4)
        with lock:
            pag.click(rx1 + px + 12, ry1 + py + 20)
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
                pag.keyUp('up')
        with lock:
            pag.click(razuLogout1)  # logout
        time.sleep(3 + random.randrange(4))
        with lock:
            pag.click(razuLogout2)  # logout
        time.sleep(410 + random.randrange(10))
        try:
            with lock:
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
    global findAliasEvent, screenshot, alias, ax1, ax2, ay1, ay2, method, aliasSafeClick, lock, checkAlias, aliasLogin, showAlias, aliasStartCounting, aliasReload

    while True:
        findAliasEvent.wait()
        findAliasEvent.clear()
        if time.time() - aliasStartCounting > 300:
            with lock:
                pag.click(aliasSafeClick)
                pag.keyDown('up')
                time.sleep(0.3)
                pag.keyUp('up')
                pag.click(aliasReload)
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
        if aliasFindValue[0] > 0.7:
            if aliasFindValue[0] > bestresult:
                bestresult = aliasFindValue[0]
            counter += 1
        if aliasFindValue[1] > 0.7:
            if aliasFindValue[1] > bestresult:
                bestresult = aliasFindValue[1]
            counter += 1
        if aliasFindValue[2] > 0.7:
            if aliasFindValue[2] > bestresult:
                bestresult = aliasFindValue[2]
            counter += 1
        if aliasFindValue[3] > 0.7:
            if aliasFindValue[3] > bestresult:
                bestresult = aliasFindValue[3]
            counter += 1
        if aliasFindValue[4] > 0.7:
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
        time.sleep(0.4)
        with lock:
            pag.click(ax1 + px + 6, ay1 + py + 20)
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
                pag.keyUp('up')
        with lock:
            pag.click(aliasLogout1)  # logout
        time.sleep(3 + random.randrange(4))
        with lock:
            pag.click(aliasLogout2)  # logout
        time.sleep(410 + random.randrange(10))
        try:
            with lock:
                pag.click(aliasLogin)  # login
        except:
            img = pag.screenshot()
            cv2.imwrite('/home/erl/Desktop/error1.png', img)
            print("exception alias")
        checkAlias = True
        print("look for alias")
        makeSSEvent.set()
        aliasStartCounting = time.time()


def wladthread():
    results = [0, 0]
    wladFindValue = [0, 0]
    wladLoc = [0, 0]
    global findWladEvent, screenshot, wlad, wx1, wx2, wy1, wy2, method, wladSafeClick, lock, checkWlad, wladLogin, showWlad, wladStartCounting, wladLogout1, wladLogout2, wladReload

    while True:
        findWladEvent.wait()
        findWladEvent.clear()
        if time.time() - wladStartCounting > 300:
            with lock:
                pag.click(wladSafeClick)
                pag.keyDown('down')
                time.sleep(0.3)
                pag.keyUp('down')
                pag.click(wladReload)
            wladStartCounting = time.time()
        crop = screenshot[wy1:wy2, wx1:wx2]
        #print("checking wlad")
        results[0] = cv2.matchTemplate(wlad[0], crop, method)
        results[1] = cv2.matchTemplate(wlad[1], crop, method)

        _, wladFindValue[0], _, wladLoc[0] = cv2.minMaxLoc(results[0])
        _, wladFindValue[1], _, wladLoc[1] = cv2.minMaxLoc(results[1])
        #print("wlad " + str(wladFindValue))

        counter = 0
        bestresult = 0
        if wladFindValue[0] > 0.5:
            if wladFindValue[0] > bestresult:
                bestresult = wladFindValue[0]
            counter += 1
        if wladFindValue[1] > 0.5:
            if wladFindValue[1] > bestresult:
                bestresult = wladFindValue[1]
            counter += 1

        if showWlad is True:
            cv2.imshow('w', crop)
            cv2.waitKey(1)

        if counter == 0:
            continue
        elif bestresult == wladFindValue[0]:
            px, py = wladLoc[0]
        else:
            px, py = wladLoc[1]

        print("wlad found")
        checkWlad = False
        time.sleep(0.4)
        with lock:
            pag.click(wx1 + px + 8, wy1 + py + 15)
        time.sleep(8)
        with lock:
            pag.click(wladSafeClick)
            pag.press('f')
        ruch = bool(random.getrandbits(1))
        if ruch is True:
            time.sleep(2)
            with lock:
                pag.click(wladSafeClick)
                pag.keyDown('down')
                time.sleep(0.3)
                pag.keyUp('down')
        with lock:
            pag.click(wladLogout1)  # logout
        time.sleep(3 + random.randrange(4))
        with lock:
            pag.click(wladLogout2)  # logout
        time.sleep(335 + random.randrange(10))
        try:
            with lock:
                pag.click(wladLogin)  # login
        except:
            img = pag.screenshot()
            cv2.imwrite('/home/erl/Desktop/error1.png', img)
            print("exception wlad")
        checkWlad = True
        print("look for wlad")
        makeSSEvent.set()
        wladStartCounting = time.time()


def shaethread():
    results = [0]
    shaeFindValue = [0]
    shaeLoc = [0]
    global findShaeEvent, screenshot, shae, sx1, sx2, sy1, sy2, method, shaeSafeClick, lock, checkShae, shaeLogin, showShae, shaeStartCounting, shaeLogout1, shaeLogout2, shaeReload

    while True:
        findShaeEvent.wait()
        findShaeEvent.clear()
        if time.time() - shaeStartCounting > 300:
            with lock:
                pag.click(shaeSafeClick)
                pag.keyDown('up')
                time.sleep(0.3)
                pag.click(shaeSafeClick)
                pag.keyUp('up')
                pag.click(shaeReload)
            shaeStartCounting = time.time()
        crop = screenshot[sy1:sy2, sx1:sx2]

        results[0] = cv2.matchTemplate(shae[0], crop, method)

        _, shaeFindValue[0], _, shaeLoc[0] = cv2.minMaxLoc(results[0])

        #print("shae " + str(shaeFindValue))

        counter = 0
        if shaeFindValue[0] > 0.7:
            counter += 1

        if showShae is True:
            cv2.imshow('s', crop)
            cv2.waitKey(1)

        if counter == 0:
            continue
        else:
            px, py = shaeLoc[0]

        print("shae found")

        checkShae = False
        time.sleep(0.4)
        with lock:
            pag.click(sx1 + px + 12, sy1 + py + 35)
        time.sleep(8)
        with lock:
            pag.click(shaeSafeClick)
            pag.press('f')
        ruch = bool(random.getrandbits(1))
        if ruch is True:
            time.sleep(2)
            with lock:
                pag.click(shaeSafeClick)
                pag.keyDown('up')
                time.sleep(0.2)
                pag.keyUp('up')
        with lock:
            pag.click(shaeLogout1)  # logout
        time.sleep(3 + random.randrange(4))
        with lock:
            pag.click(shaeLogout2)  # logout
        time.sleep(265 + random.randrange(10))
        try:
            with lock:
                pag.click(shaeLogin)  # login
        except:
            img = pag.screenshot()
            cv2.imwrite('/home/erl/Desktop/error4.png', img)
            print("exception shae")
        checkShae = True
        print("look for shae")
        makeSSEvent.set()
        shaeStartCounting = time.time()


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

#1600x900

ax1 = 1750
ax2 = 2170
ay1 = 300
ay2 = 700
aliasLogout1 = (1680, 120)
aliasLogout2 = (1785, 305)
aliasLogin = (1685, 80)
aliasReload = (1750, 80)
aliasSafeClick = (2055, 125)

rx1 = 2530
rx2 = 2810
ry1 = 255
ry2 = 535
razuLogout1 = (2450, 150)
razuLogout2 = (2550, 430)
razuLogin = (2950, 465)
razuReload = (2520, 110)
razuSafeClick = (2820, 155)

wx1 = 900
wx2 = 1510
wy1 = 270
wy2 = 790
wladLogout1 = (850, 125)
wladLogout2 = (950, 250)
wladLogin = (1350, 440)
wladReload = (920, 85)
wladSafeClick = (1220, 130)

sx1 = 395
sx2 = 725
sy1 = 145
sy2 = 685
shaeLogout1 = (85, 100)
shaeLogout2 = (190, 230)
shaeLogin = (570, 420)
shaeReload = (155, 55)
shaeSafeClick = (510, 125)

razuStartCounting = time.time()
aliasStartCounting = time.time()
wladStartCounting = time.time()
shaeStartCounting = time.time()

alias = [cv2.imread('/home/erl/Desktop/Bot/1.png'), cv2.imread('/home/erl/Desktop/Bot/2.png'),
         cv2.imread('/home/erl/Desktop/Bot/3.png'), cv2.imread('/home/erl/Desktop/Bot/4.png'),
         cv2.imread('/home/erl/Desktop/Bot/5.png')]

alias[0] = alias[0][1:19, 18:32]
alias[1] = alias[1][0:18, 13:28]
alias[2] = alias[2][1:22, 8:27]
alias[3] = alias[3][1:19, 10:24]

razu = [cv2.imread('/home/erl/Desktop/Bot/r.png'), cv2.imread('/home/erl/Desktop/Bot/e.png'),
        cv2.imread('/home/erl/Desktop/Bot/t.png')]

razu[0] = razu[0][7:26, 12:36]
razu[1] = razu[1][5:25, 20:37]
razu[2] = razu[2][3:22, 16:33]

wlad = [cv2.imread('/home/erl/Desktop/Bot/wlad.png'), cv2.imread('/home/erl/Desktop/Bot/zakuty.png')]

wlad[0] = wlad[0][20:51, 8:20]
wlad[1] = wlad[1][25:58, 0:24]

shae = [cv2.imread('/home/erl/Desktop/Bot/shae.png')]

shae[0] = shae[0][7:37, 35:59]

makeSSEvent = threading.Event()
findAliasEvent = threading.Event()
findRazuEvent = threading.Event()
findWladEvent = threading.Event()
findShaeEvent = threading.Event()

lock = threading.Lock()

method = cv2.TM_CCOEFF_NORMED
screenshot = 0

checkAlias = True
checkRazu = True
checkWlad = True
checkShae = True

showAlias = False
showRazu = False
showWlad = False
showShae = False

aliasThread = threading.Thread(target=aliasthread)
aliasThread.start()

razuThread = threading.Thread(target=razuthread)
razuThread.start()

wladThread = threading.Thread(target=wladthread)
wladThread.start()

shaeThread = threading.Thread(target=shaethread)
shaeThread.start()

while True:
    if checkAlias is False and checkRazu is False and checkWlad is False and checkShae is False:
        makeSSEvent.wait()
        makeSSEvent.clear()
    screenshot = np.array(pag.screenshot())
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    #print("screenshot")
    if checkAlias is True:
        findAliasEvent.set()
    if checkRazu is True:
        findRazuEvent.set()
    if checkWlad is True:
        findWladEvent.set()
    if checkShae is True:
        findShaeEvent.set()
    time.sleep(1.5)
