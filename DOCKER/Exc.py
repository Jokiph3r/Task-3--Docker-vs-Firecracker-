import pandas as pd
import os 
import datetime 
import joblib

print(" ____    ____     ___    ____              ____    _____   _____   _____    ____   _____   ___    ___    _   _ ")
print("|  _ \  |  _ \   / _ \  / ___|            |  _ \  | ____| |_   _| | ____|  / ___| |_   _| |_ _|  / _ \  | \ | |")
print("| | | | | | | | | | | | \___ \   _____    | | | | |  _|     | |   |  _|   | |       | |    | |  | | | | |  \| |")
print("| |_| | | |_| | | |_| |  ___) | |_____|   | |_| | | |___    | |   | |___  | |___    | |    | |  | |_| | | |\  |")
print("|____/  |____/   \___/  |____/            |____/  |_____|   |_|   |_____|  \____|   |_|   |___|  \___/  |_| \_|")
print("\n                                                                                  Developed by: Yasir Hussain")
print("\n A Machine Learning Infrence Model to detect DDOS attack by analysing Network traffic. ")


            
Run = True
while Run:
    print("\n This Model is Designed to work in two modes.")
    print("\n 1: Predict Traffic from Network traffic file ")
    print("\n\n 2: Predict Traffic by Manual input values ")
    option= input("\n Choose the mode of Prediciton: ")
    
    if option=='1':
    
        file_path = input('\n \n Enter the path of file: ')
        if os.path.exists(file_path):
            data = pd.read_csv(file_path)
            X_test= data.iloc[: , 0:12].values
            Y_test= data.iloc[: , 12:13].values
            
            from sklearn.preprocessing import StandardScaler
            sc = StandardScaler()
            X_test = sc.fit_transform(X_test)
            
            
            classifier = joblib.load('ml.pkl')
            
            t1= datetime.datetime.now()
            y_pred= classifier.predict(X_test)
            
            t2= datetime.datetime.now()
            
            counter = 1
            for i in y_pred:
                if i == 0:
                    print("\n The Network packet number " + str(counter) + " is Normal.")
                    counter += 1
                else:                
                    print("\n The Network packet number " + str(counter) +" is Malicious")
                    counter += 1
                
            from sklearn.metrics import accuracy_score,precision_score,recall_score ,f1_score
            print('\n       Accuracy is %f Percent' %(accuracy_score(Y_test,y_pred)*100))
            print('\n       Precision score is %f Percent' %(precision_score(Y_test,y_pred)*100))
            print('\n       Recall Score is %f Percent' %(recall_score(Y_test,y_pred)*100))
            print('\n       F1-score is %f Percent' %(f1_score(Y_test, y_pred)*100))
            delta= t2-t1
            testingtime=int(delta.total_seconds()*1000) 
            print("\n Testimg time of model is ", testingtime, "miliseconds")
        
        else:
            print("\n The file does not exist")

    elif option=='2':
        
        classifier = joblib.load('ml.pkl')
        print("Extract the following feature from network traffic and input values") 
        pktcount=int(input('Total number of packets:'))	
        bytecount=int(input('Total number of bytes:'))	
        dur=int(input('Total duration in seconds:'))	
        flows=int(input('Number of flow Entries in switch:'))
        pktperflow=int(input('Packet count during a single flow:'))	
        byteperflow=int(input('Byte coubt during a single flow:'))	
        port_no=int(input('Port number:'))
        tx_bytes=int(input('Number of bytes transfer from switch port:'))	
        rx_bytes=int(input('Number of bytes received on switch port:'))	
        tx_kbps=int(input('data transfer rate:'))	
        rx_kbps=int(input('data receiving rate:'))	
        tot_kbps=int(input('Total bandwidth:'))	
        
        X_test=[[pktcount,bytecount,dur,flows,pktperflow,byteperflow,port_no,tx_bytes,rx_bytes,tx_kbps,rx_kbps,tot_kbps]]
        
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        X_test = sc.fit_transform(X_test)
        
        t1= datetime.datetime.now()
        y_pred= classifier.predict(X_test)
        t2= datetime.datetime.now()
        
        for i in y_pred:
            if i == 0:
                print("\n The Network packet is Normal.")
                
            else:                
                print("\n The Network packet is Malicious")
        delta= t2-t1
        testingtime=int(delta.total_seconds()*1000) 
        print("\n\nTestimg time of model is ", testingtime, "miliseconds")
                
            
    else:
        print("wrong choice")
    answer= input("\n \n would you like to analyse more Network traffic?(y/n)   ")
    while True:
        
        if answer == 'y' :
            Run = True
            break
        elif answer == 'n' :
            Run = False
            break
        else:
            print("Wrong Option")
            break
print("\n\n                     Good Bye!")
