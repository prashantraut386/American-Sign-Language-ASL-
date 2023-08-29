from all_lib import *
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
    #print(voices[1].id)
engine.setProperty('voice', voices[0].id) # you can change to female voice just by replacing 0 by 1 in voices[0].
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
temp=np.zeros((512,512,3),np.uint8)
temp=cv.rectangle(temp,(110,150),(350,220),(255,255,255),-1)
cv.putText(temp,'ASL',(184,204),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
temp=cv.rectangle(temp,(110,250),(350,320),(255,255,255),-1)
cv.putText(temp,'AI ASL',(164,304),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
temp=cv.rectangle(temp,(110,350),(350,420),(255,255,255),-1)
cv.putText(temp,'EXIT',(164,404),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
cv.imshow('j9 project',temp)
button=10
k=0
def click(event,xdir,ydir,flags,param):
    if event==cv.EVENT_LBUTTONDOWN:
      #print("xcor = ",xdir," ycor = ",ydir)
      if(110<xdir<350 and 150<ydir<220):
          global button
          button=100
          cv.destroyAllWindows()
      if(110<xdir<350 and 250<ydir<320):
          button=20
          cv.destroyAllWindows()
      if(110<xdir<350 and 350<ydir<420):
          button = 40
          cv.destroyAllWindows()
cv.setMouseCallback('j9 project',click)
cv.waitKey(0)
if(button==100):
 cap=cv.VideoCapture(0)
 k=0
 mphands=mp.solutions.hands
 hands=mphands.Hands()
 dra=mp.solutions.drawing_utils
#h=cv.VideoWriter_fourcc(*'GDVC')
#c=cv.VideoWriter('yuyuyuyu.avi',h,30.00,(640,480))
 count=0
 word=[]
 while(True):
    ret,frame=cap.read()
    frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    #cv.imwrite('efrfe.jpg',frame)
    #print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    #c.write(frame)
    #print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    lmlist=[]
    k=0
    results=hands.process(frame)
    if results.multi_hand_landmarks:#lmlist[4][1]
     for j in results.multi_hand_landmarks:
          
         for id,lm in enumerate(j.landmark):
             h,w,c=frame.shape
             cx,cy=int(lm.x*w),int(lm.y*h)
          
            # print("landmark ",id," xcor=",cx," ycor=",cy)
             
             lmlist.append([cx,cy])
             cv.circle(frame,(cx,cy),5,(255,255,0),cv.FILLED)
         dra.draw_landmarks(frame,j,mphands.HAND_CONNECTIONS)
         
    if(len(lmlist)!=0):
     #print(lmlist)
     #if(lmlist[4][1]<lmlist[6][1] and lmlist[20][1]>lmlist[16][1]>lmlist[12][1]):
     
       #cv.putText(frame,'like',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
     if(lmlist[4][1]<lmlist[6][1] and lmlist[4][1]<lmlist[10][1] and lmlist[4][1]<lmlist[14][1] and lmlist[4][1]<lmlist[18][1] and lmlist[12][1]>lmlist[16][1] and lmlist[12][1]>lmlist[20][1] and lmlist[12][1]>lmlist[8][1] and lmlist[20][0]<lmlist[8][0] and lmlist[4][0]>lmlist[6][0]):

         s=count
         string=str(s)
         cv.putText(frame,string+' A',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('a')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('A is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0

         
     elif(lmlist[4][0]<lmlist[5][0]  and lmlist[16][1]>lmlist[12][1] and lmlist[12][1]<lmlist[8][1] and lmlist[12][1]<lmlist[10][1] and lmlist[20][1]<lmlist[18][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' B',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('b')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('B is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(60<lmlist[4][1]-lmlist[12][1]<90 and lmlist[4][1]<lmlist[3][1] and -20<lmlist[16][1]-lmlist[12][1]<20 and lmlist[4][0]>lmlist[20][1] and lmlist[12][1]>lmlist[10][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' C',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('c')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('C is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(-20<lmlist[4][1]-lmlist[12][1]<20 and lmlist[1][1]-lmlist[8][1]>20 and lmlist[4][1]<lmlist[3][1] and -20<lmlist[16][1]-lmlist[12][1]<20 and -20<lmlist[8][1]-lmlist[12][1]<20 and -20<lmlist[20][1]-lmlist[12][1]<20 and lmlist[4][0]-lmlist[12][0]>0):
         s=count
         string=str(s)
         cv.putText(frame,string+' O',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('o')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('O is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(-10<lmlist[4][1]-lmlist[12][1]<20 and -10<lmlist[4][0]-lmlist[12][0]<20 and lmlist[8][1]<lmlist[12][1] and lmlist[8][1]<lmlist[16][1] and lmlist[8][1]<lmlist[20][1] and lmlist[8][1]<lmlist[4][1] and lmlist[4][1]-lmlist[8][1]>40 and lmlist[8][1]<lmlist[7][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' D',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('d')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('D is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(0<lmlist[4][1]-lmlist[20][1]<20 and 0<lmlist[3][1]-lmlist[12][1]>20 and lmlist[20][1]-lmlist[8][1]<15 and lmlist[4][0]-lmlist[12][0]<-25 and lmlist[4][1]>lmlist[7][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' E',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('e')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('E is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(-40<lmlist[4][1]-lmlist[8][1]<40 and lmlist[20][0]<lmlist[5][0] and lmlist[4][1]-lmlist[16][1]>50 and lmlist[10][1]>lmlist[12][1] and lmlist[11][1]>lmlist[12][1] and lmlist[20][1]<lmlist[18][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' F',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('f')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('F is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[8][0]>lmlist[4][0] and lmlist[8][0]>lmlist[12][0] and lmlist[8][0]>lmlist[16][0] and lmlist[8][0]>lmlist[20][0] and lmlist[8][1]<lmlist[12][1] and lmlist[4][1]<lmlist[6][1] and lmlist[12][1]<lmlist[20][1] and lmlist[4][0]-lmlist[12][0]>40):
         s=count
         string=str(s)
         cv.putText(frame,string+' G',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('g')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('G is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[20][1]<lmlist[4][1] and lmlist[20][1]<lmlist[16][1] and lmlist[20][1]<lmlist[12][1] and lmlist[20][1]<lmlist[8][1] and lmlist[4][0]<lmlist[6][0] and lmlist[18][1]>lmlist[20][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' I',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('i')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('I is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[20][1]<lmlist[4][1] and lmlist[20][1]<lmlist[16][1] and lmlist[20][1]<lmlist[12][1] and lmlist[20][1]<lmlist[8][1] and lmlist[12][0]-lmlist[4][0]<40 and lmlist[18][1]>lmlist[20][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' Y',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('y')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('Y is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[20][0]>lmlist[4][0] and lmlist[20][0]>lmlist[16][0] and lmlist[20][0]>lmlist[12][0] and lmlist[20][0]>lmlist[8][0]):
         s=count
         string=str(s)
         cv.putText(frame,string+' J',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('j')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('J is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[8][0]>lmlist[16][0] and lmlist[8][0]>lmlist[20][0] and lmlist[12][0]>lmlist[16][0] and lmlist[12][0]>lmlist[20][0] and lmlist[5][1]<lmlist[4][1] and -25<lmlist[8][0]-lmlist[12][0]<-7 and lmlist[17][1]>lmlist[0][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' H',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('h')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('H is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[8][0]>lmlist[4][0]>lmlist[12][0] and lmlist[16][1]-lmlist[12][1]>120 and lmlist[4][1]<lmlist[5][1] and lmlist[6][1]>lmlist[8][1] and lmlist[10][1]>lmlist[12][1] and lmlist[6][1]>lmlist[8][1] and lmlist[10][1]>lmlist[12][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' K',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('k')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('K is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[4][0]-lmlist[5][0]>20 and lmlist[4][0]-lmlist[12][0]>20 and lmlist[4][0]-lmlist[10][0]>20 and lmlist[4][1]-lmlist[8][1]>40 and  lmlist[12][1]-lmlist[8][1]>40 and lmlist[8][1]<lmlist[7][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' L',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('l')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('L is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[20][1]>lmlist[4][1] and lmlist[4][1]>lmlist[14][1] and lmlist[12][0]>lmlist[4][0] and lmlist[20][1]>lmlist[4][1] and lmlist[20][1]>lmlist[18][1] and lmlist[12][0]<lmlist[8][0] and lmlist[12][1]>lmlist[10][1] and lmlist[20][1]>lmlist[4][1] and lmlist[4][1]>lmlist[15][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' M',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('m')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('M is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[16][1]>lmlist[4][1] and lmlist[16][1]-lmlist[12][1]<150 and lmlist[12][0]>lmlist[4][0] and lmlist[12][0]<lmlist[8][0] and lmlist[4][1]>lmlist[11][1] and lmlist[8][1]>lmlist[6][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' N',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('n')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('N is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[5][0]>lmlist[4][0]>lmlist[9][0] and lmlist[16][1]<lmlist[12][1] and lmlist[12][1]>lmlist[4][1] and lmlist[8][1]>lmlist[4][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' P',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('p')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('P is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[20][1]>lmlist[4][1] and lmlist[20][1]>lmlist[8][1] and lmlist[20][1]>lmlist[12][1] and lmlist[20][1]>lmlist[16][1] and lmlist[10][1]>lmlist[0][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' Q',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('q')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('Q is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[12][0]>lmlist[8][0] and lmlist[4][1]<lmlist[16][1] and lmlist[16][1]>lmlist[20][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' R',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('r')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('R is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[4][1]<lmlist[11][1] and lmlist[4][1]<lmlist[7][1] and lmlist[4][0]<lmlist[6][0] and lmlist[0][1]>lmlist[4][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' S',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('s')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('S is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[4][1]<lmlist[11][1] and lmlist[7][1]<lmlist[4][1] and lmlist[14][1]>lmlist[18][1] and lmlist[18][1]<lmlist[20][1] and lmlist[0][1]>lmlist[4][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' T',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('t')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('T is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[20][1]>lmlist[4][1] and lmlist[4][1]>lmlist[14][1]  and lmlist[12][0]<lmlist[8][0] and lmlist[8][0]-lmlist[12][0]<50 and lmlist[10][1]>lmlist[12][1] and lmlist[20][1]>lmlist[16][1] and lmlist[16][1]>lmlist[14][1] and lmlist[11][1]>lmlist[12][1] and lmlist[6][1]>lmlist[8][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' U',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('u')
         if(count==51):
             engine=pyttsx3.init()
             engine.say('U is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[20][1]>lmlist[4][1] and lmlist[4][1]>lmlist[14][1] and lmlist[16][1]>lmlist[14][1] and lmlist[10][1]>lmlist[12][1] and lmlist[4][0]<lmlist[5][0] and lmlist[20][1]>lmlist[16][1] and lmlist[16][1]>lmlist[14][1] and lmlist[11][1]>lmlist[12][1] and lmlist[6][1]>lmlist[8][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' V',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('v')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('V is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[20][1]>lmlist[4][1] and lmlist[4][1]>lmlist[14][1] and lmlist[16][1]>lmlist[14][1] and lmlist[10][1]>lmlist[12][1] and lmlist[4][0]>lmlist[5][0]):
         s=count
         string=str(s)
         cv.putText(frame,string+' Z',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('z')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('Z is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[4][1]>lmlist[14][1] and lmlist[10][1]>lmlist[12][1] and lmlist[14][1]>lmlist[16][1] and lmlist[18][1]<lmlist[20][1] and lmlist[6][1]>lmlist[8][1] and lmlist[10][1]>lmlist[12][1] and lmlist[14][1]>lmlist[16][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' W',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('w')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('W is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[8][1]<lmlist[4][1] and lmlist[8][1]<lmlist[20][1] and lmlist[8][1]<lmlist[16][1] and lmlist[8][1]<lmlist[12][1] and lmlist[8][1]>lmlist[7][1] and lmlist[4][1]>lmlist[14][1] and lmlist[11][1]>lmlist[8][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' X',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('x')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('X is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(lmlist[4][0]>lmlist[8][0] and lmlist[16][1]>lmlist[14][1] and lmlist[12][1]>lmlist[10][1] and lmlist[4][1]>lmlist[0][1] and lmlist[4][0]>lmlist[5][0]):
         s=count
         string=str(s)
         cv.putText(frame,string+' space',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'          is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append(' ')

         if(count==51):
             engine=pyttsx3.init()
             engine.say('space is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     elif(-40<lmlist[4][1]-lmlist[8][1]<40 and lmlist[20][0]<lmlist[5][0] and lmlist[4][1]-lmlist[16][1]>50 and lmlist[10][1]>lmlist[12][1] and lmlist[11][1]>lmlist[12][1]):
         s=count
         string=str(s)
         cv.putText(frame,string+' delete',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         count=count+1
         if(count==50):
             cv.putText(frame,'           is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.pop()

         if(count==51):
             engine=pyttsx3.init()
             engine.say('deleted previous letter')
             engine.runAndWait()
             cv.waitKey(2000)
             count=0
     #elif():
        # cv.putText(frame,'Z',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
     elif(lmlist[4][1]>lmlist[14][1] and lmlist[10][1]>lmlist[12][1] and lmlist[14][1]>lmlist[16][1] and lmlist[8][1]<lmlist[6][1]):
         count=count+1
         if(count==50):

             tttt=''.join(word)
             import pyttsx3
             engine=pyttsx3.init()
             cv.putText(frame,tttt,(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             engine.say(tttt)
             engine.runAndWait()
             word=[]
         if(count==51):
             count=0
             cv.waitKey(5000)
        
     #elif(lmlist[12][1]<lmlist[4][1] and lmlist[12][1]<lmlist[16][1] and lmlist[12][1]<lmlist[12][1] and lmlist[12][1]<lmlist[8][1] and lmlist[8][0]>lmlist[12][0] and lmlist[8][0]>lmlist[20][0] and lmlist[8][0]>lmlist[12][0] and lmlist[4][0]>lmlist[16][0]):
      #   cv.putText(frame,'Z',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv.imshow('j9 project',frame)
    f=cv.waitKey(1)
    if(f==ord('q')):
        break
 cv.destroyAllWindows()
 cap.release()
if(button==20):
    cv.destroyAllWindows()
if(button==20):
 speak("good morning respected guest.welcome to asl assistant")
 cap=cv.VideoCapture(0)
 mphands=mp.solutions.hands
 hands=mphands.Hands()
 dra=mp.solutions.drawing_utils
#h=cv.VideoWriter_fourcc(*'GDVC')
#c=cv.VideoWriter('yuyuyuyu.avi',h,30.00,(640,480))
 counta=0
 countb=0
 countc=0
 countd=0
 counte=0
 countf=0
 countg=0
 counth=0
 counti=0
 countj=0
 countk=0
 countl=0
 countm=0
 countn=0
 counto=0
 countp=0
 countq=0
 countr=0
 counts=0
 countt=0
 countu=0
 countv=0
 countx=0
 countw=0
 county=0
 countz=0
 countdt=0
 countsp=0
 count=0
 word=[]
 k=0
 while(True):
    ret,frame=cap.read()
    frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    #cv.imwrite('efrfe.jpg',frame)
    #print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    #c.write(frame)
    #print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    lmlist=[]
    
    results=hands.process(frame)
    if results.multi_hand_landmarks:#lmlist[4][1]
     for j in results.multi_hand_landmarks:
          
         for id,lm in enumerate(j.landmark):
             h,w,c=frame.shape
             cx,cy=int(lm.x*w),int(lm.y*h)
          
             #print("landmark ",id," xcor=",cx," ycor=",cy)
             
             lmlist.append([cx,cy])
             cv.circle(frame,(cx,cy),5,(255,255,0),cv.FILLED)
         dra.draw_landmarks(frame,j,mphands.HAND_CONNECTIONS)
         
    if(len(lmlist)!=0):
     #print(lmlist)
     #if(lmlist[4][1]<lmlist[6][1] and lmlist[20][1]>lmlist[16][1]>lmlist[12][1]):
     
       #cv.putText(frame,'like',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
     if(lmlist[4][1]<lmlist[6][1] and lmlist[4][1]<lmlist[10][1] and lmlist[4][1]<lmlist[14][1] and lmlist[4][1]<lmlist[18][1] and lmlist[12][1]>lmlist[16][1] and lmlist[12][1]>lmlist[20][1] and lmlist[12][1]>lmlist[8][1] and lmlist[20][0]<lmlist[8][0] and lmlist[4][0]>lmlist[6][0]):

         s=counta
         string=str(s)
         cv.putText(frame,string+' A',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         counta=counta+1
         if(counta==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('a')

         if(counta==16):
             engine=pyttsx3.init()
             engine.say('A is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             counta=0

         
     elif(lmlist[4][0]<lmlist[5][0]  and lmlist[16][1]>lmlist[12][1] and lmlist[12][1]<lmlist[8][1] and lmlist[12][1]<lmlist[10][1] and lmlist[20][1]<lmlist[18][1]):
         s=countb
         string=str(s)
         cv.putText(frame,string+' B',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countb=countb+1
         if(countb==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('b')

         if(countb==16):
             engine=pyttsx3.init()
             engine.say('B is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countb=0
     elif(60<lmlist[4][1]-lmlist[12][1]<90 and lmlist[4][1]<lmlist[3][1] and -20<lmlist[16][1]-lmlist[12][1]<20 and lmlist[4][0]>lmlist[20][1] and lmlist[12][1]>lmlist[10][1]):
         s=countc
         string=str(s)
         cv.putText(frame,string+' C',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countc=countc+1
         if(countc==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('c')

         if(countc==16):
             engine=pyttsx3.init()
             engine.say('C is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countc=0
     elif(-20<lmlist[4][1]-lmlist[12][1]<20 and lmlist[1][1]-lmlist[8][1]>20 and lmlist[4][1]<lmlist[3][1] and -20<lmlist[16][1]-lmlist[12][1]<20 and -20<lmlist[8][1]-lmlist[12][1]<20 and -20<lmlist[20][1]-lmlist[12][1]<20 and lmlist[4][0]-lmlist[12][0]>0):
         s=counto
         string=str(s)
         cv.putText(frame,string+' O',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         counto=counto+1
         if(counto==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('o')

         if(counto==16):
             engine=pyttsx3.init()
             engine.say('O is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             counto=0
     elif(-10<lmlist[4][1]-lmlist[12][1]<20 and -10<lmlist[4][0]-lmlist[12][0]<20 and lmlist[8][1]<lmlist[12][1] and lmlist[8][1]<lmlist[16][1] and lmlist[8][1]<lmlist[20][1] and lmlist[8][1]<lmlist[4][1] and lmlist[4][1]-lmlist[8][1]>40 and lmlist[8][1]<lmlist[7][1]):
         s=countd
         string=str(s)
         cv.putText(frame,string+' D',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countd=countd+1
         if(countd==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('d')

         if(countd==16):
             engine=pyttsx3.init()
             engine.say('D is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countd=0
     elif(0<lmlist[4][1]-lmlist[20][1]<20 and 0<lmlist[3][1]-lmlist[12][1]>20 and lmlist[20][1]-lmlist[8][1]<15 and lmlist[4][0]-lmlist[12][0]<-25 and lmlist[4][1]>lmlist[7][1]):
         s=counte
         string=str(s)
         cv.putText(frame,string+' E',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         counte=counte+1
         if(counte==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('e')

         if(counte==16):
             engine=pyttsx3.init()
             engine.say('E is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             counte=0
     elif(-40<lmlist[4][1]-lmlist[8][1]<40 and lmlist[20][0]<lmlist[5][0] and lmlist[4][1]-lmlist[16][1]>50 and lmlist[10][1]>lmlist[12][1] and lmlist[11][1]>lmlist[12][1] and lmlist[20][1]<lmlist[18][1]):
         s=countf
         string=str(s)
         cv.putText(frame,string+' F',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countf=countf+1
         if(countf==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('f')

         if(countf==16):
             engine=pyttsx3.init()
             engine.say('F is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countf=0
     elif(lmlist[8][0]>lmlist[4][0] and lmlist[8][0]>lmlist[12][0] and lmlist[8][0]>lmlist[16][0] and lmlist[8][0]>lmlist[20][0] and lmlist[8][1]<lmlist[12][1] and lmlist[4][1]<lmlist[6][1] and lmlist[12][1]<lmlist[20][1] and lmlist[4][0]-lmlist[12][0]>40):
         s=countg
         string=str(s)
         cv.putText(frame,string+' G',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countg=countg+1
         if(countg==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('g')

         if(countg==16):
             engine=pyttsx3.init()
             engine.say('G is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countg=0
     elif(lmlist[20][1]<lmlist[4][1] and lmlist[20][1]<lmlist[16][1] and lmlist[20][1]<lmlist[12][1] and lmlist[20][1]<lmlist[8][1] and lmlist[4][0]<lmlist[6][0] and lmlist[18][1]>lmlist[20][1]):
         s=counti
         string=str(s)
         cv.putText(frame,string+' I',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         counti=counti+1
         if(counti==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('i')

         if(counti==16):
             engine=pyttsx3.init()
             engine.say('I is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             counti=0
     elif(lmlist[20][1]<lmlist[4][1] and lmlist[20][1]<lmlist[16][1] and lmlist[20][1]<lmlist[12][1] and lmlist[20][1]<lmlist[8][1] and lmlist[12][0]-lmlist[4][0]<40 and lmlist[18][1]>lmlist[20][1]):
         s=county
         string=str(s)
         cv.putText(frame,string+' Y',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         county=county+1
         if(county==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('y')

         if(county==16):
             engine=pyttsx3.init()
             engine.say('Y is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             county=0
     elif(lmlist[20][0]>lmlist[4][0] and lmlist[20][0]>lmlist[16][0] and lmlist[20][0]>lmlist[12][0] and lmlist[20][0]>lmlist[8][0]):
         s=countj
         string=str(s)
         cv.putText(frame,string+' J',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countj=countj+1
         if(countj==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('j')

         if(countj==16):
             engine=pyttsx3.init()
             engine.say('J is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countj=0
     elif(lmlist[8][0]>lmlist[16][0] and lmlist[8][0]>lmlist[20][0] and lmlist[12][0]>lmlist[16][0] and lmlist[12][0]>lmlist[20][0] and lmlist[5][1]<lmlist[4][1] and -25<lmlist[8][0]-lmlist[12][0]<-7 and lmlist[17][1]>lmlist[0][1]):
         s=counth
         string=str(s)
         cv.putText(frame,string+' H',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         counth=counth+1
         if(counth==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('h')

         if(counth==16):
             engine=pyttsx3.init()
             engine.say('H is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             counth=0
     elif(lmlist[8][0]>lmlist[4][0]>lmlist[12][0] and lmlist[16][1]-lmlist[12][1]>120 and lmlist[4][1]<lmlist[5][1] and lmlist[6][1]>lmlist[8][1] and lmlist[10][1]>lmlist[12][1] and lmlist[6][1]>lmlist[8][1] and lmlist[10][1]>lmlist[12][1]):
         s=countk
         string=str(s)
         cv.putText(frame,string+' K',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countk=countk+1
         if(countk==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('k')

         if(countk==16):
             engine=pyttsx3.init()
             engine.say('K is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countk=0
     elif(lmlist[4][0]-lmlist[5][0]>20 and lmlist[4][0]-lmlist[12][0]>20 and lmlist[4][0]-lmlist[10][0]>20 and lmlist[4][1]-lmlist[8][1]>40 and  lmlist[12][1]-lmlist[8][1]>40 and lmlist[8][1]<lmlist[7][1]):
         s=countl
         string=str(s)
         cv.putText(frame,string+' L',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countl=countl+1
         if(countl==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('l')

         if(countl==16):
             engine=pyttsx3.init()
             engine.say('L is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countl=0
     elif(lmlist[20][1]>lmlist[4][1] and lmlist[4][1]>lmlist[14][1] and lmlist[12][0]>lmlist[4][0] and lmlist[20][1]>lmlist[4][1] and lmlist[20][1]>lmlist[18][1] and lmlist[12][0]<lmlist[8][0] and lmlist[12][1]>lmlist[10][1] and lmlist[20][1]>lmlist[4][1] and lmlist[4][1]>lmlist[15][1]):
         s=countm
         string=str(s)
         cv.putText(frame,string+' M',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countm=countm+1
         if(countm==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('m')

         if(countm==16):
             engine=pyttsx3.init()
             engine.say('M is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countm=0
     elif(lmlist[16][1]>lmlist[4][1] and lmlist[16][1]-lmlist[12][1]<150 and lmlist[12][0]>lmlist[4][0] and lmlist[12][0]<lmlist[8][0] and lmlist[4][1]>lmlist[11][1] and lmlist[8][1]>lmlist[6][1]):
         s=countn
         string=str(s)
         cv.putText(frame,string+' N',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countn=countn+1
         if(countn==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('n')

         if(countn==16):
             engine=pyttsx3.init()
             engine.say('N is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countn=0
     elif(lmlist[5][0]>lmlist[4][0]>lmlist[9][0] and lmlist[16][1]<lmlist[12][1] and lmlist[12][1]>lmlist[4][1] and lmlist[8][1]>lmlist[4][1]):
         s=countp
         string=str(s)
         cv.putText(frame,string+' P',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countp=countp+1
         if(countp==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('p')

         if(countp==16):
             engine=pyttsx3.init()
             engine.say('P is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countp=0
     elif(lmlist[20][1]>lmlist[4][1] and lmlist[20][1]>lmlist[8][1] and lmlist[20][1]>lmlist[12][1] and lmlist[20][1]>lmlist[16][1] and lmlist[10][1]>lmlist[0][1]):
         s=countq
         string=str(s)
         cv.putText(frame,string+' Q',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countq=countq+1
         if(countq==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('q')

         if(countq==16):
             engine=pyttsx3.init()
             engine.say('Q is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countq=0
     elif(lmlist[12][0]>lmlist[8][0] and lmlist[4][1]<lmlist[16][1] and lmlist[16][1]>lmlist[20][1]):
         s=countr
         string=str(s)
         cv.putText(frame,string+' R',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countr=countr+1
         if(countr==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('r')

         if(countr==16):
             engine=pyttsx3.init()
             engine.say('R is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countr=0
     elif(lmlist[4][1]<lmlist[11][1] and lmlist[4][1]<lmlist[7][1] and lmlist[4][0]<lmlist[6][0] and lmlist[0][1]>lmlist[4][1]):
         s=counts
         string=str(s)
         cv.putText(frame,string+' S',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         counts=counts+1
         if(counts==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('s')

         if(counts==16):
             engine=pyttsx3.init()
             engine.say('S is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             counts=0
     elif(lmlist[4][1]<lmlist[11][1] and lmlist[7][1]<lmlist[4][1] and lmlist[14][1]>lmlist[18][1] and lmlist[18][1]<lmlist[20][1] and lmlist[0][1]>lmlist[4][1]):
         s=countt
         string=str(s)
         cv.putText(frame,string+' T',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countt=countt+1
         if(countt==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('t')

         if(countt==16):
             engine=pyttsx3.init()
             engine.say('T is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countt=0
     elif(lmlist[20][1]>lmlist[4][1] and lmlist[4][1]>lmlist[14][1]  and lmlist[12][0]<lmlist[8][0] and lmlist[8][0]-lmlist[12][0]<50 and lmlist[10][1]>lmlist[12][1] and lmlist[20][1]>lmlist[16][1] and lmlist[16][1]>lmlist[14][1] and lmlist[11][1]>lmlist[12][1] and lmlist[6][1]>lmlist[8][1]):
         s=countu
         string=str(s)
         cv.putText(frame,string+' U',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countu=countu+1
         if(countu==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('u')
         if(countu==16):
             engine=pyttsx3.init()
             engine.say('U is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countu=0
     elif(lmlist[20][1]>lmlist[4][1] and lmlist[4][1]>lmlist[14][1] and lmlist[16][1]>lmlist[14][1] and lmlist[10][1]>lmlist[12][1] and lmlist[4][0]<lmlist[5][0] and lmlist[20][1]>lmlist[16][1] and lmlist[16][1]>lmlist[14][1] and lmlist[11][1]>lmlist[12][1] and lmlist[6][1]>lmlist[8][1]):
         s=countv
         string=str(s)
         cv.putText(frame,string+' V',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countv=countv+1
         if(countv==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('v')

         if(countv==16):
             engine=pyttsx3.init()
             engine.say('V is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countv=0
     elif(lmlist[20][1]>lmlist[4][1] and lmlist[4][1]>lmlist[14][1] and lmlist[16][1]>lmlist[14][1] and lmlist[10][1]>lmlist[12][1] and lmlist[4][0]>lmlist[5][0]):
         s=countz
         string=str(s)
         cv.putText(frame,string+' Z',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countz=countz+1
         if(countz==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('z')

         if(countz==16):
             engine=pyttsx3.init()
             engine.say('Z is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countz=0
     elif(lmlist[4][1]>lmlist[14][1] and lmlist[10][1]>lmlist[12][1] and lmlist[14][1]>lmlist[16][1] and lmlist[18][1]<lmlist[20][1] and lmlist[6][1]>lmlist[8][1] and lmlist[10][1]>lmlist[12][1] and lmlist[14][1]>lmlist[16][1]):
         s=countw
         string=str(s)
         cv.putText(frame,string+' W',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countw=countw+1
         if(countw==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('w')

         if(countw==16):
             engine=pyttsx3.init()
             engine.say('W is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countw=0
     elif(lmlist[8][1]<lmlist[4][1] and lmlist[8][1]<lmlist[20][1] and lmlist[8][1]<lmlist[16][1] and lmlist[8][1]<lmlist[12][1] and lmlist[8][1]>lmlist[7][1] and lmlist[4][1]>lmlist[14][1] and lmlist[11][1]>lmlist[8][1]):
         s=countx
         string=str(s)
         cv.putText(frame,string+' X',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countx=countx+1
         if(countx==15):
             cv.putText(frame,'      is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append('x')

         if(countx==16):
             engine=pyttsx3.init()
             engine.say('X is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countx=0
     elif(lmlist[4][0]>lmlist[8][0] and lmlist[16][1]>lmlist[14][1] and lmlist[12][1]>lmlist[10][1] and lmlist[4][1]>lmlist[0][1] and lmlist[4][0]>lmlist[5][0]):
         s=countsp
         string=str(s)
         cv.putText(frame,string+' space',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countsp=countsp+1
         if(countsp==15):
             cv.putText(frame,'          is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.append(' ')

         if(countsp==16):
             engine=pyttsx3.init()
             engine.say('space is Collected')
             engine.runAndWait()
             cv.waitKey(2000)
             countsp=0
     elif(-40<lmlist[4][1]-lmlist[8][1]<40 and lmlist[20][0]<lmlist[5][0] and lmlist[4][1]-lmlist[16][1]>50 and lmlist[10][1]>lmlist[12][1] and lmlist[11][1]>lmlist[12][1]):
         s=countdt
         string=str(s)
         cv.putText(frame,string+' delete',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
         countdt=countdt+1
         if(countdt==15):
             cv.putText(frame,'           is Collected',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             word.pop()

         if(countdt==16):
             engine=pyttsx3.init()
             engine.say('deleted previous letter')
             engine.runAndWait()
             cv.waitKey(2000)
             countdt=0
     #elif():
        # cv.putText(frame,'Z',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
     elif(lmlist[4][1]>lmlist[14][1] and lmlist[10][1]>lmlist[12][1] and lmlist[14][1]>lmlist[16][1] and lmlist[8][1]<lmlist[6][1]):
         count=count+1
         if(count==30):
             
             
             tttt=''.join(word)
             import pyttsx3
             engine=pyttsx3.init()
        #     webbrows1er.open("https://www.google.com/search?q="+tttt+"&ei=xlCeYsWZNPnWz7sP2sycmA0&oq=flipk&gs_lcp=Cgdnd3Mtd2l6EAEYADILCAAQsQMQgwEQkQIyCwgAELEDEIMBEJECMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEMkDMgUIABCSAzIFCAAQkgMyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIICAAQgAQQsQM6BQgAEJECOgsILhCABBCxAxDUAjoRCC4QgAQQsQMQgwEQxwEQ0QNKBAhBGABKBAhGGABQydvWAViS6dYBYO771gFoAXABeACAAaMCiAHwBpIBBTAuNC4xmAEAoAEBsAEAwAEB&sclient=gws-wiz")
             u=len(word)
             if(tttt=="bus"):
                webbrowser.open('https://www.redbus.in/online-booking/msrtc')
                word=[]
             elif(tttt=="vl"):
                webbrowser.open("https://learner.vierp.in/")
                word=[]
             elif(tttt=="y"):
                k=7
                speak('youtube is openning search what u want')
                word=[]
             elif(tttt=="trn"):
                k=5
                word=[]
                speak("please tell me train number and name ")
             elif(tttt=="temp"):
                webbrowser.open("https://www.google.com/search?q=today+weather&oq=todays+whe&aqs=chrome.5.69i57j0i10j0i10i512l3j0i10i131i433i457j0i402l2j0i10i512l2.7759j0j15&sourceid=chrome&ie=UTF-8")
             elif(tttt=="g" and u==1 and k==0):
              k=1
              word=[]
              print("hgvuygiugvbuyguib")
              speak('google is openning search what u want')
              #cv.putText(frame,"google",(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
              #tttt=""
             elif(tttt=="a" and u==1 and k==0):
              k=2 
              word=[]
              print("kghbuhukjhu")
              speak('enter the website you want to open')
              #cv.putText(frame,"app",(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
              #tttt=""
             elif(tttt=="m" and u==1 and k==0): 
                k=3
                speak('enter the email you to send')
                word=[]
             elif(tttt=="f" and u==1 and k==0):
                k=4
                speak("enter the the movie u wawnt to see")
                word=[]
             elif(tttt=="pnr" and k==0):
                speak("please enter ten digit PNR number")
                k=6
                word=[]
                #cv.putText(frame,"email",(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
                #tttt=""
             if(k==0):
              cv.putText(frame,tttt,(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
              engine.say(tttt)
              engine.runAndWait()
             elif(k==1):
              cv.putText(frame,"google",(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
              #engine.say('google is opening, search what u want')
              #engine.runAndWait()
             elif(k==7):
              cv.putText(frame,"youtube",(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)  
             elif(k==5):
              cv.putText(frame,"train",(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)     
             elif(k==6):
               cv.putText(frame,"pnr",(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)  
             elif(k==3):
                cv.putText(frame,"email",(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
             elif(k==4):
                cv.putText(frame,"movie",(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)     
             u=len(word)
             print(word)   
             if(k==1 and u>0):
                k=0
                
                webbrowser.open("https://www.google.com/search?q="+tttt+"&ei=xlCeYsWZNPnWz7sP2sycmA0&oq=flipk&gs_lcp=Cgdnd3Mtd2l6EAEYADILCAAQsQMQgwEQkQIyCwgAELEDEIMBEJECMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEMkDMgUIABCSAzIFCAAQkgMyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIICAAQgAQQsQM6BQgAEJECOgsILhCABBCxAxDUAjoRCC4QgAQQsQMQgwEQxwEQ0QNKBAhBGABKBAhGGABQydvWAViS6dYBYO771gFoAXABeACAAaMCiAHwBpIBBTAuNC4xmAEAoAEBsAEAwAEB&sclient=gws-wiz")
                
             elif(k==2 and u>0):
                k=0
                webbrowser.open("https://www."+tttt+".com")

             elif(k==3 and u>0):
                k=0
                to=input()
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login('devansh.lathiya21@vit.edu','12111023') # also enable less secure apps setting in security setting of your mail account 
                server.sendmail('devansh.lathiya21@vit.edu', to, tttt)
                server.close()
             elif(k==4 and u>0):
                k=0
                movie_dir = 'D:\\Movies'
                songs = os.listdir(movie_dir)
                print(songs) 
                speak("Which movie you will love to see")   
                os.startfile(os.path.join(movie_dir,tttt+".mkv"))
             elif(k==5 and u>0):
                k=0
                #speak("please tell me train number and name ")
                #train_no=takeCommand()
                speak("here is running status of train")
                webbrowser.open("https://www.railyatri.in/live-train-status/"+tttt+"?utm_source=lts_dweb_Check_status")
             elif(k==6 and u>0):
                
                #pnr_no=input("PNR NO.=")
                speak("here is PNR status of train")
                webbrowser.open("railyatri.in/pnr-status/"+tttt)
                k=0
             elif(k==7 and u>0):
              webbrowser.open("https://www.youtube.com/results?search_query="+tttt)
              k=0
             word=[]
         if(count==31):
             count=0
             cv.waitKey(5000)
        
     #elif(lmlist[12][1]<lmlist[4][1] and lmlist[12][1]<lmlist[16][1] and lmlist[12][1]<lmlist[12][1] and lmlist[12][1]<lmlist[8][1] and lmlist[8][0]>lmlist[12][0] and lmlist[8][0]>lmlist[20][0] and lmlist[8][0]>lmlist[12][0] and lmlist[4][0]>lmlist[16][0]):
      #   cv.putText(frame,'Z',(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv.imshow('j9 project',frame)
    f=cv.waitKey(1)
    if(f==ord('q')):
        break
 cv.destroyAllWindows()
 cap.release()
if(k==40):
 cv.destroyAllWindows()
 cap.release()



























