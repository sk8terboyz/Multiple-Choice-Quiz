# Author: Shane Kennedy
# Github: sk8terboyz

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import json

class Quiz:
    
    def __init__(self):
        # set question number to 0
        self.question_num = 0
        
        # assigns question to the display_question function to update later
        self.display_title()
        self.display_question()
        
        # opt_selected holds the selected option in a question
        self.opt_selected=IntVar()
        
        # display radio buttons
        self.opts = self.radio_buttons()
        
        # display options for the current question
        self.display_options()
        
        # display the button for next and exit
        self.display_buttons()
        
        # display image
        self.display_image()
        
        # number of questions
        self.data_size=len(question)
        
        # count number of correct answers
        self.correct = 0
    
    def display_result(self):
        
        # calculate the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        
        # calculate score percentage
        score = int(self.correct / self.data_size*100)
        result = f"Score: {score}%"
        
        messagebox.showinfo("Result", f"{result}\n{correct}\n{wrong}")
    
    def check_answer(self, question_number):
        # check if selected option is correct
        if self.opt_selected.get() == answer[question_number]:
            return True
    
    def next_btn(self):
        # check answer
        if self.check_answer(self.question_num):
            self.correct += 1
         
        # move to next question
        self.question_num += 1
        
        # check if question_num is equal to the data size
        if self.question_num == self.data_size:
            # display result
            self.display_result()
            # destroy gui
            root.destroy()
        else:
            # show next question
            self.display_question()
            self.display_options()
            self.display_image()
            
    def display_buttons(self):
        # button to move to next question
        Button(root, text="Next", command=self.next_btn, width=10, bg="blue", fg="white", font=("ariel", 16, "bold")).place(x=350, y=380)
    
    def display_options(self):
        val=0
        
        # deselecting options
        self.opt_selected.set(0)
        
        # display text for radio buttons
        for option in options[self.question_num]:
            self.opts[val]['text'] = option
            val += 1
    
    def display_question(self):
        # set question properties
        Label(root, text=question[self.question_num], width=60, font=('ariel', 16, 'bold'), anchor=W).place(x=70, y=100)
    
    def display_title(self):
        # set title properties
        Label(root, text="Pokemon Type Quiz", width=50, bg="green", fg="white", font=("ariel", 20, "bold")).place(x=0, y=2)
        
    def display_image(self):
        # create image object & resize
        base_img = Image.open(images[self.question_num])
        base_img = base_img.resize((260, 200))
        img = ImageTk.PhotoImage(base_img)
        l1 = Label(root, image=img)
        l1.image = img
        l1.place(x=500, y=100)

    def radio_buttons(self):
        # initialize empty list
        question_list = []
        
        # position of first option
        y_pos = 150
        
        # add options to list
        while len(question_list) < 4:
            # set radio button properties
            radio_btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=len(question_list)+1, font=("ariel", 14))
            
            # add button to list
            question_list.append(radio_btn)
            
            # place button
            radio_btn.place(x=100, y=y_pos)
            
            # increment y-axis pos
            y_pos += 40
        
        # return radio buttons
        return question_list
    
root = Tk()
root.geometry("800x650")
root.title("Pokemon Type Quiz")

# get data from json file
with open('data.json') as f:
    data = json.load(f)

# set the question, options, & answer
question = (data['question'])
options = (data['options'])
answer = (data['answer'])
images = (data['images'])

# object of the Quiz class
quiz = Quiz()

root.mainloop()