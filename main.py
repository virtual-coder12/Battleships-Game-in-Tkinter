
from tkinter import *
import random
import time
import numpy as np
"""
[true, true, false]
robot = [2,1,4,3,7]
a1 = np.array(robot)
a3 = np.array([2,1,4,6,7])
x = (a1 == a3)
print(a1 == a3)
"""
win = Tk()
win.geometry("700x600")
win.config(bg="#FBCEB1")

#its a team project
win.title("Team Project: Battleship")
#this is for the grid reference
def username():
  global x1
#makes a heading for a username and allows you to input
  lab = Label(win, text="",font=('Helvatical bold',13), bg = '#FBCEB1')
  lab.place(relx = 0.36, rely=0.3)
  
  x1 = Entry(win, text = "")
  x1.place(relx = 0.36, rely = 0.35)

def call():
  x1.destroy()
  reg.destroy() 
  lab2.place(relx = 0.04)
  game()
    
  

  
def reg():
  global lab2
  Ar = x1.get()
  lab2 = Label(win, text='Player Name: ' + str(Ar),font=('Helvatical bold',13), bg = '#FBCEB1')
  lab2.place(relx = 0.12, rely=0)
  call()
#player name displayed at top
    
  
  
reg = Button(win, text="Enter", command = reg)
reg.place(relx = 0.36, rely = 0.4, width=190)


username()


global array
array = []

num_turns=5
for turn in range(num_turns):
  print("Turn:", turn + 1, "of", num_turns)
  print()



def game():
  lab2.config
  #l = Label(win, text = "Place your ships: only'print(num of turns)'font=('Helvatical bold',13))
  #pl.place(relx = 0.32, rely = 0)
  shipnumber = 0 
  n = 1
  x=0.1
  gridref = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E"}
   
  gridref2 = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5"}
   
  gridref3 = {1: "A1", 2: "A2", 3: "A3", 4: "A4", 5: "A5"}
  
  gridref4 = {1: "B1", 2: "B2", 3: "B3", 4: "B4", 5: "B5"}
  
  gridref5 = {1: "C1", 2: "C2", 3: "C3", 4: "C4", 5: "C5"}
  
  gridref6 = {1: "D1", 2: "D2", 3: "D3", 4: "D4", 5: "D5"}
  
  gridref7 = {1: "E1", 2: "E2", 3: "E3", 4: "E4", 5: "E5"}
  
  
  #game starts with player 2 but p1 draws their ship

  # this is what makes the green labels
  for i in gridref:
   gridref[n] = Label(win, text=str(gridref[n]), bg = "#FF7518", relief='solid')
   gridref[n].place(relx = x, rely = 0.07, relwidth = 0.06, relheight = 0.06)
   x+=0.1
   n+=1
  
 
  n2 =1
  y=0.14
   
  for i in gridref2:
   gridref2[n2] = Label(win, text=str(gridref2[n2]), bg = "#FF7518", relief = 'solid')
   gridref2[n2].place(relx = 0.03, rely = y,  relwidth = 0.06, relheight = 0.06)
   y+=0.1
   n2+=1
   
  
  #allows player to click on buttons and place ships
  def times(m):

    global array
    global robot
    array.append(gridref3[m].cget('text'))
    print('My ships' , array)
    gridref3[m].config(bg="#FFD580")
    print('length',len(array))
    print("\n")



    if len(array) == 5:
      Label1 = Label(win, text = "Computers turn wait",font=('Helvatical bold',15))
      Label1.place(relx = 0,rely=0, relwidth=1, relheight=1)




      robot = []
      letters = ['A1', 'A2', 'A3', 'A4', 'A5','B1', 'B2', 'B3', 'B4', 'B5','C1', 'C2', 'C3', 'C4', 'C5','D1', 'D2', 'D3', 'D4', 'D5']



      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      print('Computer', robot)

      Label1.config(text='')
      Label1 = Label(win, text = "Time to guess computer ships",font=('Helvatical bold',15)).place(relx = 0.05,rely=0)
      game()

      def clock():
        print('jiiii')
        win.after(100, clock)

      clock()
      
      
      del array[:]



    
      
  


    
  s = 0.14
  v =1
  
  for i in gridref3:
   gridref3[v] = Button(win, text=str(gridref3[v]), command= lambda m = v: times(m), relief='solid')
   gridref3[v].place(relx = 0.1, rely =s, relwidth = 0.06, relheight = 0.06)
   s +=0.1
   v+=1




    
  def timed1(m):
    global array
    global robot
    array.append(gridref4[m].cget('text'))
    print('computer' + robot)
    print("My ships")
    print(array)
    gridref4[m].config(bg="#FFD580")
    print(len(array))
    if len(array) == 5:
      Label1 = Label(win, text = "Computers turn wait",font=('Helvatical bold',15))
      Label1.place(relx = 0,rely=0, relwidth=1, relheight=1)
      def nextt():
        labx.config(text = "Waiting")
      time.sleep(1)


   

      robot = []
      letters = ['A1', 'A2', 'A3', 'A4', 'A5','B1', 'B2', 'B3', 'B4', 'B5','C1', 'C2', 'C3', 'C4', 'C5','D1', 'D2', 'D3', 'D4', 'D5']



      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      print('computer ships '+ str(robot))
      Label1.config(text='')
      Label1 = Label(win, text = "Time to guess computer ships",font=('Helvatical bold',15)).place(relx = 0.05,rely=0)
      game()
      del array[:]

      
        

  
  
  
  v2 = 1
  s1 = 0.14
  for i in gridref4:
    gridref4[v2] = Button(win, text=str(gridref4[v2]), command= lambda m = v2: timed1(m), relief='solid')
    gridref4[v2].place(relx = 0.2, rely =s1, relwidth = 0.06, relheight = 0.06)
    s1 +=0.1
    v2+=1

  def timed(m):
    global array
    global robot
    array.append(gridref5[m].cget('text'))
    print('Computer' + robot)
    print("My ships")
    print(array)
    gridref5[m].config(bg="#FFD580")
    print(len(array))
    if len(array) == 5:
      Label1 = Label(win, text = "Computers turn wait",font=('Helvatical bold',15))
      Label1.place(relx = 0,rely=0, relwidth=1, relheight=1)
      def nextt():
        labx.config(text = "Waiting")
      time.sleep(1)


   

      robot = []
      letters = ['A1', 'A2', 'A3', 'A4', 'A5','B1', 'B2', 'B3', 'B4', 'B5','C1', 'C2', 'C3', 'C4', 'C5','D1', 'D2', 'D3', 'D4', 'D5']



      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      print('computer ships '+ str(robot))
      Label1.config(text='')
      Label1 = Label(win, text = "Time to guess computer ships",font=('Helvatical bold',15)).place(relx = 0.05,rely=0)
      game()
      del array[:]
        




 
  
  v3 = 1
  s3 = 0.14
  for i in gridref5:
    gridref5[v3] = Button(win, text=str(gridref5[v3]), command= lambda m = v3: timed(m), relief = 'solid')
    gridref5[v3].place(relx = 0.3, rely =s3, relwidth = 0.06, relheight = 0.06)
    s3 +=0.1
    v3+=1


  def timed2(m):
    global array
    global robot
    print('computer' + robot)
    array.append(gridref6[m].cget('text'))
    print("My ships")
    print(array)
    gridref6[m].config(bg="#FFD580")
    print(len(array))
    if len(array) == 5:
      Label1 = Label(win, text = "Computers turn wait",font=('Helvatical bold',15))
      Label1.place(relx = 0,rely=0, relwidth=1, relheight=1)
      def nextt():
        labx.config(text = "Waiting")
      time.sleep(1)


   

      robot = []
      letters = ['A1', 'A2', 'A3', 'A4', 'A5','B1', 'B2', 'B3', 'B4', 'B5','C1', 'C2', 'C3', 'C4', 'C5','D1', 'D2', 'D3', 'D4', 'D5']



      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      print('computer ships '+ str(robot))
      Label1.config(text='')
      Label1 = Label(win, text = "Time to guess computer ships",font=('Helvatical bold',15)).place(relx = 0.05,rely=0)
      game()
      del array[:]
        

      
  
  v4 = 1
  s4 = 0.14
  for i in gridref6:
    gridref6[v4] = Button(win, text=str(gridref6[v4]), command= lambda m = v4: timed2(m), relief = 'solid')
    gridref6[v4].place(relx = 0.4, rely =s4, relwidth = 0.06, relheight = 0.06)
    s4 +=0.1
    v4+=1

  def timed3(m):
    global array
    global robot
    print('computer' + robot)
    array.append(gridref7[m].cget('text'))
    print("place ships")
    print(array)
    gridref7[m].config(bg="#FFD580")
    print(len(array))
    if len(array) == 5:
      Label1 = Label(win, text = "Computers turn wait",font=('Helvatical bold',15))
      Label1.place(relx = 0,rely=0, relwidth=1, relheight=1)
      def nextt():
        labx.config(text = "Waiting")
      time.sleep(1)


   

      robot = []
      letters = ['A1', 'A2', 'A3', 'A4', 'A5','B1', 'B2', 'B3', 'B4', 'B5','C1', 'C2', 'C3', 'C4', 'C5','D1', 'D2', 'D3', 'D4', 'D5']



      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      robot.append(random.choice(letters))
      print('computer ships '+ str(robot))
      Label1.config(text='')
      Label1 = Label(win, text = "Time to guess computer ships",font=('Helvatical bold',15)).place(relx = 0.05,rely=0)
      game()
      del array[:]
        

  
  
  v5 = 1
  s5 = 0.14
  for i in gridref7:
    gridref7[v5] = Button(win, text=str(gridref7[v5]),command= lambda m = v5: timed3(m), relief = 'solid')
    gridref7[v5].place(relx = 0.5, rely =s5, relwidth = 0.06, relheight = 0.06)
    s5 +=0.1
    v5+=1


win.mainloop()


