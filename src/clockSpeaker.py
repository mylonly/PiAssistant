#!/usr/bin/python
import time
import ctypes

so = ctypes.CDLL("../tts/libtts.so")
timestr = time.strftime('%H:%M', time.localtime( time.time() ) )
text = "现在时间:"+timestr
so.text2wav(text)