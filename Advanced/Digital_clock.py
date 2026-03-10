import tkinter
import time

#Initialise the app with basic config
app_window = tkinter.Tk()
app_window.title("Digital Clock")
app_window.geometry("300x140")
app_window.resizable(0,0)


text_font= ("Boulder", 50, 'bold')
background = "#50f2ea"
foreground= "#070707"
border_width = 25



# Text to be inserted in the window
label = tkinter.Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1) # Same as .pack() this one decide according to rows and column

def clock():
    curr_time = time.strftime("%H:%M:%S")
    label.config(text=curr_time)   # Keeps on updating time 
    label.after(200, clock)  # afterhow much time to update here 200 milliseconds

clock()  #Calling out the function

app_window.mainloop()