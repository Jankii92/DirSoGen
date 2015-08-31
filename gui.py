from tkinter import *
from tkinter.ttk import Style
from SoundProcessor import SoundProc
from wave import *
from tkinter import filedialog
from tkinter import messagebox




class App(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent=parent
        self.parent.title("Centered window")
        self.pack(fill=BOTH,expand=1)
        self.centerWindow()
        
    def centerWindow(self):
        w = 500
        h = 300
        self.nameSound = ""
        self.nameHRIR = ""
        
        
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        
        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w,h,x,y))
        
        self.parent.title("Directional Sound Generator")
        self.style = Style()
        self.style.theme_use("classic")
        
        self.photo = PhotoImage(file='HeadCS.png')
        canv = Canvas(self, width=self.photo.width(),height = self.photo.height())
        canv.grid(row = 0, column = 0, rowspan = 7, columnspan = 2)
        canv.create_image(self.photo.width()/2,self.photo.height()/2,image = self.photo)
        
        
        
        playbutton = Button(self, text = "Play", command=self.play)
        playbutton.grid(row = 1,column = 3)
        loadHRTFbutton = Button(self, text = "Load HRTF file", command=self.loadHRIR)
        loadHRTFbutton.grid(row = 2,column = 3)
        loadSoundbutton = Button(self, text = "Load Sound file", command=self.loadSound)
        loadSoundbutton.grid(row = 3, column = 3)
        
        
        lab1 = Label(self, text = "x-axis [m] :")
        lab2 = Label(self, text  = "y-axis [m] :")
        lab3 = Label(self, text  = "z-axis [m] :")
        lab1.grid(row = 4,column = 3,stick = E)
        lab2.grid(row = 5,column = 3,stick = E)
        lab3.grid(row = 6,column = 3,stick = E)
        self.eX = Entry(self)
        self.eY = Entry(self)
        self.eZ = Entry(self)
        self.eX.grid(row = 4,column = 4,stick = W, columnspan = 1)
        self.eY.grid(row = 5,column = 4,stick = W, columnspan = 1)
        self.eZ.grid(row = 6,column = 4,stick = W, columnspan = 1)
        
        self.label4Text = StringVar()
        self.lab4 = Label(self, textvariable = self.label4Text)
        self.lab4.grid(row = 2, column = 4)
        
        self.label5Text = StringVar()
        self.lab5 = Label(self, textvariable = self.label5Text)
        self.lab5.grid(row = 3, column = 4)
        
        self.SoundProcessor = SoundProc.SoundProc()
        
        self.harir = 1
        self.soundFile = 1
        
        
        
        
    def play(self):
        okX = False
        okY = False
        okZ = False
        
        if(self.eX.get().replace('.','',1).isdigit()):
            x = (float)(self.eX.get())
            okX = True
        if(self.eY.get().replace('.','',1).isdigit()):
            y = (float)(self.eY.get())
            okY = True
        if(self.eZ.get().replace('.','',1).isdigit()):
            z = (float)(self.eZ.get())
            okZ = True
        if(self.nameSound!="" and self.nameHRIR!="" and okX and okY and okZ):
            self.SoundProcessor.play(self.hrir, self.nameSound,x,y,z)
            
            return 1
    
        messagebox.showinfo("Error", "Wrong value or file")
        return 0
        
                
    def loadHRIR(self):
        self.label4Text.set("Bussy") 
        
        self.nameHRIR = filedialog.askopenfilename()
        
        print(self.nameHRIR)
        
        
        
        self.label4Text.set("Ready")  
        
        
    def loadSound(self):
        self.label5Text.set("Bussy")        
        self.nameSound = filedialog.askopenfilename()
        
        
        
        
        self.label5Text.set("Ready")
        
        
def main():
    root =Tk()
    root.geometry("250x150+300+300")
    app = App(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()
    