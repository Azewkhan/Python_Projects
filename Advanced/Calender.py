from tkinter import *
import calendar


def show_calendar():
    window = Tk()  
    window.config(background = 'grey')
    window.title("Christian Calender")
    window.geometry("550x600")
    year = int(year_field.get()) # External function defined in next code
    window_content = calendar.calendar(year) # This function gives you the calendar 
    calYear = Label( window ,text = window_content, font ="Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)
        
    window.mainloop()

if __name__ == '__main__':
    wind = Tk()
    wind.config( background = "grey")
    wind.title("Calendar")
    wind.geometry("250x140")
    cal =  Label(wind, text = "Enter New year",bg = 'grey',font =('times',28,"bold"))
    year = Label(wind, text="Enter year", bg='dark grey')
    year_field = Entry(wind) # This function takes the entry
    button= Button(wind,text= "Show calendar", bg= "blue", fg= "Black",command = show_calendar) # button function and it's command

  #putting widgets in position
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=4, column=1)
    wind.mainloop()
       
    



