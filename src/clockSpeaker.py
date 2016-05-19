#!/usr/bin/python
import time
import ctypes

so = ctypes.CDLL("../tts/libtts.so")
timestr = time.strftime('%Y-%m-%d %X', time.localtime( time.time() ) )
so.text2wav(timestr)