import pyttsx3 # pip install pyttsx3==2.71
import datetime
import speech_recognition as sr # pip install speechRecognition
import wikipedia # pip install wikipedia
import time
import chromedriver_binary
from selenium import webdriver # pip install chromedriver-binary selenium
import psutil
import os
import pyautogui as pag # key入力
import pyperclip as ppc # コピペ


engine = pyttsx3.init()

timelist = ["何時"]
daylist = ["何日"]

def speak(audio):
    #voices = engine.getProperty('voices')
    #engine.setProperty('voice','english')
    engine.setProperty('rate',150)
    engine.say(audio)
    engine.runAndWait()

def time_(): # 今何時
    Time=datetime.datetime.now().strftime("%H:%M:%S") # 24 hour clock, %I:%M:%S 12 hour clock
    speak('現在の時刻は')
    speak(Time)

def date_(): #今日の日付
    #year = datetime.datetime.now().year
    #month = datetime.datetime.now().month
    day = datetime.datetime.now().strftime('%Y年%m月%d日')
    speak('今日の日付は')
    #speak(year)
    #speak('ねん')
    #speak(month)
    #speak('がつ')
    speak(day)
    #speak('にちです')

def greeting_():
    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("おはようございます！")
    elif hour>=12 and hour<18:
        speak("こんにちは")
    elif hour>=18 and hour<24:
        speak("こんばんは！")
    else:
        speak("夜遅くまでご苦労様です。")
    
    date_()
    time_()
    speak("何かお手伝いしましょうか。")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("声を聴......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("初期化.......")
        query = r.recognize_google(audio,language='ja')
        print(query)
    
    except Exception as e:
        print(e)
        print("もう一度お願いします。")
        return "None"
    
    return query


def wikipedia_():
    query = TakeCommand()
    wikipedia.set_lang("ja")
    search_result = wikipedia.search(query)
    if not search_result:
        response_string = "no result"
        return response_string
    try:
        wiki_page = wikipedia.page(search_result[0])
    except Exception as e:
        response_string = "エラーが発生しました。もう一度お願いします。\n" + e.message + "\n" + str(e)
        return response_string
    wiki_content = wiki_page.content
    response_string += wiki_content[0:wiki_content.find("。")] + "。\n"
    response_string += "リンクはこちら：" + wiki_page.url
    return response_string


def memo_write():
    speak("ファイル名は何にしますか")
    memoname = TakeCommand()
    """
    os.system("notepad C:\\Users\\mephistpheles\\Desktop\\"+memoname+".txt")
    time.sleep(2)
    pag.press('enter')
    while True:
        query = TakeCommand()

        if "終了" in query:
            break
    
        elif "改行" in query:
            pag.press('enter')

        ppc.copy(query)
        pag.hotkey('ctrl','v')

    pag.hotkey('ctrl','w')
    """
    # テストしてないから上手くいくか分からん
    file = open("C:\\Users\\mephistpheles\\Desktop\\"+memoname+".txt","w")
    while True:
        speak("話したことを記録します。")
        query = TakeCommand()
        if "終了" in query:
            break

        file.write(query)
    speak("メモを終了します。")

def screenshot():
    img = pag.screenshot()
    speak("スクリーンショットを保存する名前はどうしますか")
    picname = TakeCommand()
    img.save("C:\\Users\\mephistpheles\\Pictures\\Camera Roll\\"+picname+".png")

if __name__ == "__main__":
    #greeting_()

    while True:
        query = TakeCommand()

        if "何時" in query: # 何時　という語句があったらtime_()
            time_()
    
        elif "何日" in query: # 
            date_()

        elif "wikipedia" in query.lower(): # wikipedia検索
            #result = wikipedia_()
            speak("wikipediaで検索します。何を検索しますか。")
            query = TakeCommand()
            wikipedia.set_lang("ja")
            result=wikipedia.summary(query,sentences=5)
            print(result)
            print("続きはwebで" + wikipedia.page(query).url)
            speak(result)
            speak("続きはwebで")

        elif "検索" in query: #chrome検索
            speak("何を検索しますか")
            query = TakeCommand()
            driver = webdriver.Chrome('C:\\Users\\mephistpheles\\Downloads\\chdriver\\chromedriver.exe')
            driver.get('http://www.google.com/')
            search_box = driver.find_element_by_name("q")
            search_box.send_keys(query)
            search_box.submit()
            time.sleep(10)
            driver.quit()

        elif "youtube" in query.lower(): # youtube
            speak("youtubeを使います。何を検索しますか。")
            query = TakeCommand()
            driver = webdriver.Chrome('C:\\Users\\mephistpheles\\Downloads\\chdriver\\chromedriver.exe')
            driver.get('http://www.youtube.com/results?search_query='+ query)
            time.sleep(10)
            driver.quit()

        elif "バッテリー" in query: # バッテリー残量
            battery = psutil.sensors_battery()
            speak("バッテリーの残量は")
            speak(battery)

        elif "line" in query.lower(): # open line
            speak("LINEを開きます。")
            line_app = r'C:\Users\mephistpheles\AppData\Local\LINE\bin\current\LINE.exe'
            os.startfile(line_app)
            # 閉じ方分からん

        elif "メモ" in query: # memo
            speak("メモを取ります")
            memo_write()

        elif "スクリーンショット" in query: # screenshot
            speak("スクリーンショットを取ります")
            screenshot()

        elif "音楽を再生" in query: # play music
            speak("音楽を再生します")
            song_dir = r"C:\Users\mephistpheles\Music\anisong\stardriver"
            music = os.listdir(song_dir)
            speak("何を再生しますか")
            ans = TakeCommand()
            play = int(ans.replace('ナンバー',''))
            os.startfile(os.path.join(song_dir,music[play]))

        elif "終了" in query:
            break
            
speak("では、また呼んでください。")





