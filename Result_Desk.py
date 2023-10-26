import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
alpha = pd.read_csv(r"C:\Users\White Devil\Desktop\12th Class Ip project\marksheet.csv",index_col ="NAME")#adress of the CSV file

while True:#While Loop to repeat the code itself
    print("__________Welcome To Result Desk__________")
    print("1. Result Of Specific Student's")
    print("2. Result Of all Student")
    print("3. Subject wise Anaylises")
    print("4. Quite")
    open = int(input("Choose any One From Above: "))
    if open == 1:#conditional loop  used for  displaying Result Of a Specific Student's
        print("Report")
        print("Please Enter Student's Roll Number:")
        Rollno = int(input())
        Result = alpha.iloc[Rollno-1]#iloc used to take the roll number
        print(Result)
        _Data_ = pd.DataFrame(Result)
        name = list(_Data_.columns)
        name = str(name[0])
        series = pd.Series(Result)# creating Series
        Subject = list(series.index)#list of the subject which will be used for graphs
        Marks = list(series.values)#list of the Marks which will be used for graph 
        Full_Marks = [40,40,40,40,40,25]#full marks obtained which will be used for comparision
        X = np.arange(len(Subject))
            
           


        while True:#while loop used for looping the graph
            Graph = input("Do You want To See The Graph Y/N: ").upper()
            if Graph == "Y":#Conditional statement for wheteher to display the graph or not
                print("1.Line Graph")
                print("2.Bar Graph")
                print("3.Pie Graph")
                type_graph = int(input("Choose Type Of Graph: "))
                if type_graph == 1:#conditional Statement used for displaying type of graph
                    plt.plot(_Data_)
                    plt.plot(Subject,Full_Marks)
                    plt.xlabel("Subject",color='c')
                    plt.ylabel("Marks",color='m')
                    plt.legend(["Marks Obtaines","Full Marks"])
                    plt.title(name+" RESULT",color='g')
                    plt.yticks([0,10,20,30,40])
                    plt.show() 
                elif type_graph == 2:#conditional Statement used for displaying type of graph
                    plt.bar(Subject,Marks,color='b',width=.15)
                    plt.bar(X+0.25,Full_Marks,color='r',width=.15)
                    plt.xlabel("Subject",color='c')
                    plt.ylabel("Marks",color='m')
                    plt.legend(["Marks Obtaines","Full Marks"])
                    plt.title(name+" RESULT",color = 'g')
                    plt.yticks([0,10,20,30,40])
                    plt.show() 

                elif type_graph == 3:#conditional Statement used for displaying type of graph
                    while True:#while loop used for looping to show the coposition and graph 
                        print("Do you want to See The marks composition Y/N")
                        beta = input().capitalize()
                        if beta == "Y":#coondition for displaying mark composition
                            plt.pie(Full_Marks,labels=Subject,autopct="%05.3f%%")
                            plt.title("Marks Composition",color = 'g')
                            plt.show()
                        elif beta == "N":#condition for displaying Graph
                            plt.pie(Marks,labels=Subject,autopct="%05.3f%%")
                            plt.title(name+" RESULT",color = 'g')
                            plt.show()
                            break
                        else:#condition if we get any invalid input
                            print("Invalid Input")
                    else:#condition if we get any invalid input
                        print("InValid Choice")               
            elif Graph == "N":#condition for not Displaying The Graph
                print("Thank's For Using")
                break
            else:#condition if we get any invalid input
                print("Please Ente Correct Input")
                pass
    elif open == 2:#Conditional statement for displaying the all the data in data frame formate 
        print("-------------------------------------------------RESULT OF 2023-24---------------------------------------------------------")
        print(alpha)
        print("---------------------------------------------------------------------------------------------------------------------------")  
    elif open == 3:#Conditional statement for displaying subject wise  anaylises
        Data = pd.DataFrame(alpha)#dataframe
        Subject = Data.columns#selescting Subject form dataframe
        Subject = list(Subject)#Converting to list
        for i in range(len(Subject)):#printing the subject
            print(i+1,Subject[i])
        while True:#looping the code for subject wise anaylises
            print("To Exit press 143")
            analysis = int(input("Choose anyone from Above: "))#to take input 
            for i in range(len(Subject)):#for loop used for giving further condition
                pass
            if analysis <= i+1:#condition for displaying the graph
                marks = pd.Series(Data[Subject[analysis-1]])
                value = marks.values
                plt.hist(value,bins=5,linestyle='dotted',edgecolor='m',hatch='*',fill =  False)
                plt.title(Subject[analysis-1],color='g')
                plt.xlabel("Marks",color='c')
                plt.ylabel("No Of Student",color='m')
                plt.show()
            elif analysis==143:#conditon for existing the loop
                print("Thanks for Using")
                break                  
            else:#condition for getting an invalid input
                print("invalid Input")
                print("Please Enter a valid Input")                    
    elif open == 4:#condation for Quiting
        print("Thanks for Using")
        break
    else:#condition for invalid input
        print("Enter a Valind Input!")