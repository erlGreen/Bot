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
    global findRazuEvent, screenshot, razu, ax1, ax2, ay1, ay2, method, razuSafeClick, lock, checkRazu, razuLogin, showRazu, razuStartCounting, razuLogout, razuReload

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
        time.sleep(0.25)
        pag.click(rx1 + px + 12, ry1 + py + 12)
        for i in range(0, 6):
            with lock:
                pag.click(razuSafeClick)
                pag.press('e')
            time.sleep(0.25 + random.uniform(0.25, 0.75))
        ruch = bool(random.getrandbits(1))
        if ruch is True:
            time.sleep(2)
            with lock:
                pag.click(razuSafeClick)
                pag.keyDown('up')
                time.sleep(0.3)
                pag.keyUp('up')
        time.sleep(6 + random.randrange(2))
        pag.click(razuLogout)  # logout
        time.sleep(380 + random.randrange(20))
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
    global findAliasEvent, screenshot, alias, ax1, ax2, ay1, ay2, method, aliasSafeClick, lock, checkAlias, aliasLogin, showAlias, aliasStartCounting, aliasReload, aliasLogout

    while True:
        findAliasEvent.wait()
        findAliasEvent.clear()
        if time.time() - aliasStartCounting > 300:
            with lock:
                pag.click(aliasSafeClick)
                pag.keyDown('up')
                time.sleep(0.3)
                pag.click(aliasSafeClick)
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
        
        print("alias " + str(aliasFindValue))

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
        time.sleep(0.25)
        pag.click(ax1 + px + 12, ay1 + py + 12)
        for i in range(0, 6):
            with lock:
                pag.click(aliasSafeClick)
                pag.press('e')
            time.sleep(0.25 + random.uniform(0.25, 0.75))
        ruch = bool(random.getrandbits(1))
        if ruch is True:
            time.sleep(2)
            with lock:
                pag.click(aliasSafeClick)
                pag.keyDown('up')
                time.sleep(0.3)
                pag.keyUp('up')
        time.sleep(6 + random.randrange(2))
        pag.click(aliasLogout)  # logout
        time.sleep(380 + random.randrange(20))
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


def shaethread():
    results = [0]
    shaeFindValue = [0]
    shaeLoc = [0]
    global findShaeEvent, screenshot, shae, sx1, sx2, sy1, sy2, method, shaeSafeClick, lock, checkShae, shaeLogin, showShae, shaeStartCounting, shaeLogout, shaeReload

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
        if shaeFindValue[0] > 0.5:
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
        time.sleep(0.25)
        pag.click(sx1 + px + 12, sy1 + py + 35)
        for i in range(0, 6):
            with lock:
                pag.click(shaeSafeClick)
                pag.press('e')
            time.sleep(0.25 + random.uniform(0.25, 0.75))
        time.sleep(6 + random.randrange(2))
        pag.click(shaeLogout)  # logout
        time.sleep(260 + random.randrange(20))
        try:
            pag.click(shaeLogin)  # login
        except:
            img = pag.screenshot()
            cv2.imwrite('/home/erl/Desktop/error1.png', img)
            print("exception shae")
        checkShae = True
        print("look for shae")
        makeSSEvent.set()
        shaeStartCounting = time.time()


def wladthread():
    results = [0, 0]
    wladFindValue = [0, 0]
    wladLoc = [0, 0]
    global findWladEvent, screenshot, wlad, wx1, wx2, wy1, wy2, method, wladSafeClick, lock, checkWlad, wladLogin, showWlad, wladStartCounting, wladLogout, wladReload

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
        if wladFindValue[0] > 0.6:
            if wladFindValue[0] > bestresult:
                bestresult = wladFindValue[0]
            counter += 1
        if wladFindValue[1] > 0.6:
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
        time.sleep(0.25)
        pag.click(wx1 + px + 8, wy1 + py + 8)
        for i in range(0, 6):
            with lock:
                pag.click(wladSafeClick)
                pag.press('e')
            time.sleep(0.25 + random.uniform(0.25, 0.75))
        ruch = bool(random.getrandbits(1))
        if ruch is True:
            time.sleep(2)
            with lock:
                pag.click(wladSafeClick)
                pag.keyDown('down')
                time.sleep(0.3)
                pag.keyUp('down')
        time.sleep(6 + random.randrange(2))
        pag.click(wladLogout)  # logout
        time.sleep(330 + random.randrange(20))
        try:
            pag.click(wladLogin)  # login
        except:
            img = pag.screenshot()
            cv2.imwrite('/home/erl/Desktop/error3.png', img)  # login
            print("exception wlad")
        checkWlad = True
        print("look for wlad")
        makeSSEvent.set()
        wladStartCounting = time.time()


ax1 = 1510
ax2 = 1960
ay1 = 320
ay2 = 750
aliasLogout = (2175, 768)
aliasLogin = (1985, 450)
aliasSafeClick = (2010, 160)
aliasReload = (1590, 110)

rx1 = 2225
rx2 = 2510
ry1 = 245
ry2 = 660
razuLogout = (2865, 768)
razuLogin = (2666, 450)
razuSafeClick = (2600, 155)
razuReload = (2280, 105)

sx1 = 95
sx2 = 520
sy1 = 330
sy2 = 830
shaeLogout = (740, 845)
shaeLogin = (540, 470)
shaeSafeClick = (490, 240)
shaeReload = (155, 175)

wx1 = 765
wx2 = 1205
wy1 = 325
wy2 = 815
wladLogout = (1430, 830)
wladLogin = (1225, 455)
wladSafeClick = (1100, 215)
wladReload = (840, 145)

razuStartCounting = time.time()
aliasStartCounting = time.time()
shaeStartCounting = time.time()
wladStartCounting = time.time()

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

shae = [cv2.imread('/home/erl/Desktop/Bot/shae.png')]

shae[0] = shae[0][7:37, 35:59]
#cv2.imshow('e', shae[0])
#cv2.waitKey(0)

wlad = [cv2.imread('/home/erl/Desktop/Bot/wlad.png'), cv2.imread('/home/erl/Desktop/Bot/zakuty.png')]

wlad[0] = wlad[0][20:51, 8:20]
wlad[1] = wlad[1][25:58, 0:24]



makeSSEvent = threading.Event()
findAliasEvent = threading.Event()
findRazuEvent = threading.Event()
findShaeEvent = threading.Event()
findWladEvent = threading.Event()

lock = threading.Lock()

showAlias = False
showRazu = False
showShae = False
showWlad = False

checkAlias = True
checkRazu = True
checkShae = False
checkWlad = True

method = cv2.TM_CCOEFF_NORMED
screenshot = 0

aliasThread = threading.Thread(target=aliasthread)
aliasThread.start()

razuThread = threading.Thread(target=razuthread)
razuThread.start()

shaeThread = threading.Thread(target=shaethread)
shaeThread.start()

wladThread = threading.Thread(target=wladthread)
wladThread.start()

while True:
    if checkAlias is False and checkRazu is False and checkShae is False and checkWlad is False:
        makeSSEvent.wait()
        makeSSEvent.clear()
    screenshot = np.array(pag.screenshot())
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    #print("screenshot")
    if checkAlias is True:
        findAliasEvent.set()
    if checkRazu is True:
        findRazuEvent.set()
    if checkShae is True:
        findShaeEvent.set()
    if checkWlad is True:
        findWladEvent.set()
    time.sleep(1.5)
