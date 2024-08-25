# I declare that my work contains no examples of misconduct, such as plagiarism, or
#collusion.
# Any code taken from other sources is referenced within my code solu􀆟on.
# Student ID: 
# Date: 




from graphics import *
# data recoarding list
results = []

#check the results using program function
def credit_program(pass_credit,defer_credit,fail_credit,version):
    if pass_credit == 120:
        print("Progress")
        storeResult("progress",pass_credit,defer_credit,fail_credit,version)
    elif pass_credit == 100 and defer_credit == 20:
        print("Progress (module trailer)")
        storeResult("progress",pass_credit,defer_credit,fail_credit,version)
    elif pass_credit == 100 and fail_credit == 20:
        print("Progress (module trailer)")
        storeResult("module_trailer",pass_credit,defer_credit,fail_credit,version)
    elif fail_credit >= 80:
        print("Exclude")
        storeResult("exclude",pass_credit,defer_credit,fail_credit,version) 
    else:
        print("Do not progress (module retriever)")
        storeResult("module_retriver",pass_credit,defer_credit,fail_credit,version)

# store input data
def storeResult(result,pass_credit,defer_credit,fail_credit,version):
   if version:
        temp =[]
        temp.append(result)
        temp.extend([pass_credit,defer_credit,fail_credit])
        results.append(temp)
        return results
    
# Histogram part 
def bars(results):
    total_outcome= len(results)
    total_progress = 0
    total_trailer = 0
    total_exclude = 0
    total_retriever = 0
    for item in results:
         if len(item) > 0 :
            if item[0] == 'progress':
                total_progress += 1
            elif item[0] == 'module_trailer':
                total_trailer += 1
            elif item[0] == 'exclude':
                total_exclude += 1
            elif item[0] == 'module_retriver':
                total_retriever += 1

 
    win = GraphWin("Histogram", 600, 400) # window size

    x_1 = 40  #  vertical axis
    y_1 = 300  # horizontal axis
    bar_width = 100  # width of the bars

    # Create the total progress bar
    bar_1 = Rectangle(Point(x_1, y_1), Point(x_1 + bar_width, y_1 - 10*total_progress))
    bar_1.setFill('green')

    # Create the total trailer bar
    x_2 = x_1 + bar_width + 30  # Adjust for some space between bars
    y_2 = y_1
    bar_2 = Rectangle(Point(x_2, y_2), Point(x_2 + bar_width, y_2 -10*total_trailer))
    bar_2.setFill('blue')

    # Create the total retriever bar
    x_3 = x_2 + bar_width + 30  
    y_3 = y_2
    bar_3 = Rectangle(Point(x_3, y_3), Point(x_3 + bar_width, y_3 -10*total_retriever))
    bar_3.setFill('brown')
    
    #create the total exclude bar
    x_4 = x_3+ bar_width + 30  # Adjust for some space between bars
    y_4 = y_3
    bar_4 = Rectangle(Point(x_4, y_4), Point(x_4 + bar_width, y_4 - 10*total_exclude))
    bar_4.setFill('red')
    
    aLine = Line(Point(20,y_1),Point(550,y_4))
    
    message_1 = Text(Point(250,350), str(total_outcome) +"  Outcome in total")
    message_1.setSize(20)
    message_1.setStyle("bold")
    
    message_2 = Text(Point(150,50),"Histogram Result")
    message_2.setSize(20)
    message_2.setStyle("bold")
    
    # all bar label
    label_1 = Text(Point(x_1+30,y_1+15),"Progress")
    label_2 = Text(Point(x_2+30,y_2+15),"Trailer")
    label_3 = Text(Point(x_3+30,y_3+15),"Retriever")
    label_4 = Text(Point(x_4+30,y_4+15),"Exclude")
    label_1.setStyle("bold")
    label_2.setStyle("bold")
    label_3.setStyle("bold")
    label_4.setStyle("bold")
    
    # each bar size
    hight_1 = Text(Point(x_1+50,y_1-30),total_progress)
    hight_2 = Text(Point(x_2+50,y_2-50),total_trailer)
    hight_3 = Text(Point(x_3+50,y_3-70),total_retriever)
    hight_4 = Text(Point(x_4+50,y_4-90),total_exclude)    
    
    # Draw the in the window
    bar_1.draw(win)
    bar_2.draw(win)
    bar_3.draw(win)
    bar_4.draw(win)
    aLine.draw(win)
    message_1.draw(win)
    message_2.draw(win)
    label_1.draw(win)
    label_2.draw(win)
    label_3.draw(win)
    label_4.draw(win)
    hight_1.draw(win)
    hight_2.draw(win)
    hight_3.draw(win)
    hight_4.draw(win)
    
    
    win.getMouse()
    win.close()

#validation part

def get_valid_credit(prompt):
    while True:
        try:
            credit = int(input(prompt))
            if 0 <= credit <= 120 and credit % 20 == 0:
                return credit
            else:
                print('Out of range')
        except ValueError:
            print('Integer required')


#identify user
while True :
    try :
        print("MENU ")
        version = input("Enter '1' for student version or Enter '2' for staff version :")
        if version == "1" :
    
            pass_credit= get_valid_credit('Please enter your credits at pass: ')
            defer_credit = get_valid_credit('Please enter your credit at defer: ')
            fail_credit = get_valid_credit('Please enter your credit at fail: ')
            total_credits = pass_credit + defer_credit + fail_credit
            if total_credits != 120:
                print("Total incorrect")
        
            else :
                credit_program(pass_credit,defer_credit,fail_credit,False)
                 
        elif version == "2" :

         while True:
            pass_credit= get_valid_credit('Please enter your credits at pass: ')
            defer_credit = get_valid_credit('Please enter your credit at defer: ')
            fail_credit = get_valid_credit('Please enter your credit at fail: ')
            total_credits = pass_credit + defer_credit + fail_credit
            if total_credits != 120:
                 print("Total incorrect")
        
            else :
                 credit_program(pass_credit,defer_credit,fail_credit,True)
                 
                 print("Would you like to enter another set of data?")
                 multi_outcome =input("Enter 'y' for yes or 'q' to quit and view results:")
                 if multi_outcome == "q" :
                    for i in results :     # part 02 list part
                        print(i)
# part 03 file part

                    with open(".student_data.txt","a") as file :  
                        file.write(str(results))
                    print("student_data file is automatically generated in the document folder") 
                    print("click on window for exit")
                    bars(results)
                    break
                 elif multi_outcome != "y":
                        print("invalid input")
                        break 
        else:
         print("invalid input")                                
    except KeyboardInterrupt:
        print("invalid input/ Try Again !!") 