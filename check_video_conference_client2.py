import numpy as np
import cv2
import sys
import socket as soc
import pickle

if(1):
    number=2
    name={}

    s=soc.socket()

    host="127.0.0.1"
    port=9876
    cap = cv2.VideoCapture(0)
    s.connect((host,port))
    
    s.send(input(s.recv(4096).decode()).encode())
    response=""
    while(1):
        print(s.recv(8192).decode())
        response=input().encode()
        if(response==b"0"):
            s.send(response)
            name=s.recv(4096)
            response=name
        s.send(response)
        k=s.recv(4096).decode()
        print(k)
        if "connected" in k:
            break

    print("enter_loop")
    def fun(img):
        img = cv2.medianBlur(img,5)
        ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
                    cv2.THRESH_BINARY,11,2)
        th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                    cv2.THRESH_BINARY,11,2)
        cv2.imshow('frame3',th3)
        cv2.imshow('frame4',th2)
    while(1):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        z=pickle.dumps(frame)
        #print(sys.getsizeof(z))
        print(123)
        print(z)
        s.send(z)
        j=s.recv(9999999)
        try:
            frame1=pickle.loads(j)
        except:
            print(j)
            continue
        cv2.imshow("client2",frame1)
        # Display the resulting frame
        if(sys.getsizeof(frame)>921782):
            print(sys.getsizeof(frame))
        #dst = cv2.addWeighted(gray,0.7,frame,0.3,0)
        #cv2.imshow('frame',gray)
        #cv2.imshow('frame2',frame)
        #fun(frame)
        #cv2.imshow('frame3',dst)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        

    # When everything done, release the capture
    s.send(b"$")
    cap.release()
    cv2.destroyAllWindows()
    s.close()

