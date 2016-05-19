#!/usr/bin/python
import time
import ctypes

so = ctypes.CDLL("../tts/libtts.so")
timestr = time.strftime('%H:%M', time.localtime( time.time() ) )

so.text2wav("现在时间:"+timestr)