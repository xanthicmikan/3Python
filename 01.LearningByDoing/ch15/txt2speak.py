import os
from pygame import mixer    
from gtts import gTTS

mixer.init()
if not os.path.isfile('tmp.mp3'):
    tts = gTTS(text = '暫時音檔', lang = 'zh-tw')
    tts.save('tmp.mp3')
    print('tmp.mp3 done')
#-----------------#
def bot_speak(text, lang):
    try: 
        mixer.music.load('tmp.mp3')
        tts = gTTS(text=text, lang=lang)
        tts.save('speak.mp3')
        mixer.music.load('speak.mp3')
        mixer.music.play()
        while(mixer.music.get_busy()):
            continue
    except:
        print('Play file fail')
#-----------------#
bot_speak('我是一本書', 'zh-tw')