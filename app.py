#### MAKE SURE YOU HAVE GONE THROUGH README.MD   
global skipped


# IMPORTS ---------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pytube.__main__ import YouTube
import mygoogle
import spotify
import scraper
import sys 
import time
import threading 

#------------------------------

#-------------
browser_path = r'C:\Program Files (x86)\Slimjet\slimjet.exe'
#-------------

#------------------------------------------------------------------
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--log-level=3')
options.add_argument("window-size=400,600")
options.add_argument('--disable-logging')

options.binary_location = browser_path

#-------------------------------------------------------------------

print('------------ INITIALISING, PLEASE WAIT ------------')

driver_path = r'.\setup\chromedriver.exe'                                   # go through README.md 
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.set_window_position(-1000, 100)


queue = []

def queueplayer():
    global np
    global skipped
    if threading.active_count() == 2:
        a = input('press b to break and anything else to continue: ')
        if a == 'b':
            return
            
    for song in queue:
        print('sonngname', ' ', song)
        skipped = False
        print('for song in queue')
        print(song[0])
        driver.get(song[0])
        np = song[0]
        while skipped==False:
            time.sleep(0.1)
        print(f'old queue= {queue}')
        for i in queue:
            try:
                if i[1] == song[1]:
                    queue.remove(i)
                    break
            except:
                if i == song:
                    queue.remove(i)
                    break
            finally:
                print('skipped')
        print('new queue: ')
        for song in queue:
            print(song)
        queueplayer()
    print('queue over, playing radio by default . . . .') 

def play(args):
    print('called')
    if args.startswith('https://open.spotify.com/playlist'):
        tracks = spotify.get_playlist_tracks(args)
        print(tracks)
        for i in range(len(tracks)-1):
            link = scraper.get_link_one(tracks[i-1])
            print(link[0])
            queue.append(link[0])
        print(queue)
    elif args.startswith('https://youtube'):
        queue.append(args) 


    elif args == 'q':
        return

    else:
        player = scraper.get_link(args)
        for i in range(len(player)):
            print(player[i][2])
        print('----\nwhich song do you want to play? \n----')
        try:
            answer = int(input('-> '))
        except:
            return
        queue.append(player[answer-1])
        
        if threading.active_count()<2:
            x = threading.Thread(target=queueplayer)
            x.start()                   


def gplay(args):
    print('called')
    if args.startswith('https://open.spotify.com/playlist'):
        tracks = spotify.get_playlist_tracks(args)
        print(tracks)
        for i in range(len(tracks)-1):
            link = mygoogle.get_link_one(tracks[i-1])
            print(link)
            queue.append(link)
        print(queue)
    
    elif args.startswith('https://open.spotify.com/track'):
        songname = spotify.get_name(args)
        try:
            links = mygoogle.get_link_one(songname)
        except:
            links = scraper.get_link_one(songname)
        finally:
            queue.append(links)

    elif args.startswith('https://youtube'):
        queue.append(args) 


    elif args == 'q':
        return

    else:
        player = scraper.get_link(args)
        for i in range(len(player)):
            print(player[i][2])
        print('----\nwhich song do you want to play? \n----')
        try:
            answer = int(input('-> '))
        except:
            return
        queue.append(player[answer-1])
        
        if threading.active_count()<2:
            x = threading.Thread(target=queueplayer)
            x.start()          


while True:
    init = input('$ ')
    args = init.split()

    if init.startswith('q '):
        if init[2:].startswith('https://open.spotify.com/playlist'):
            play(init[2:])
        else:
            links = scraper.get_link(init[2:])
            for link in links:
                print(link[2])
            xd = int(input('which song do you want to play? '))
            queue.append([links[xd-1][0], links[xd-1][1], links[xd-1][2]])

    if init.startswith('queue'):
        for qsong in queue:
            print(qsong)
        if threading.active_count() <2:
            if input('play queue?(y/n) ').lower()=='y':
                x = threading.Thread(target=queueplayer)
                x.start()    

    if init == 'clear':
        queue = []

    if init == 'rskip':
        print('skipping. . . ')
        driver.find_element_by_tag_name('body').send_keys(Keys.SHIFT, 'n')

    if init == 'skip':
        skipped = True

    if init.startswith('quit'):
        driver.quit()
        queueplayer()
        sys.exit()

    if init == 'showvideo':
        driver.set_window_position(0,0)
        driver.set_window_size(1920, 1080)
        driver.find_element_by_tag_name('body').send_keys('f') 

    if init.startswith('restart'):
        driver.quit()
        driver = webdriver.Chrome(executable_path=driver_path, options=options)
        driver.get('https://www.google.com')
        print('restart complete')

    if init =='hidevideo':
        driver.set_window_size(800, 600)
        driver.set_window_position(-1000,100)

    if init == 'p':
        driver.find_element_by_tag_name('body').send_keys('k') 

    if init.startswith('p '):                                                     # FORCE PLAY 
        play(init[2:])

    if init == 'np':
        a = driver.current_url
        yt = YouTube(a)
        print(yt.title)

    if init.startswith('seek'):
        try:
            for i in range(int(args[1])):
                driver.find_element_by_tag_name('body').send_keys('l') 
        except:
            pass

    if init.startswith('voldn'):
        action = ActionChains(driver)
        slider = driver.find_element_by_class_name('ytp-volume-slider')
        for i in range(int(init[6:])):
            action.click_and_hold(slider).move_by_offset(-5, 0).release().perform()

    if init.startswith('volup'):
        action = ActionChains(driver)
        slider = driver.find_element_by_class_name('ytp-volume-slider')
        for i in range(int(init[6:])):
            action.click_and_hold(slider).move_by_offset(5, 0).release().perform()

    if init.startswith('rewind'):
        try:
            for i in range(int(args[1])):
                driver.find_element_by_tag_name('body').send_keys('j') 
        except:
            pass

    if init == 'help':
        print('please read commands.txt for a list of all commands or use link "https://github.com/im-NL/pylayer/blob/master/commands.txt"')

    if init == 'm':
        driver.find_element_by_tag_name('body').send_keys('m') 
        
    else:
        pass