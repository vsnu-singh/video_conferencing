import numpy as np
import cv2
import socket as soc
import _thread as thread
import _pickle as pickle

number=2
name={}

s=soc.socket()

host=""
port=9876
s.bind((host,port))
s.listen(1)

while(1):
    comm,addr=s.accept()
    def fun(com,adr):
        while(1):
            j=comm.recv(999999)
            frame=pickle.load(j)
            cv2.imshow('server',frame)
            frame.send(j)
        

