from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image, ImageDraw
import pymysql
import matplotlib.pyplot as plt
import time
from tkVideoPlayer import TkinterVideo
import datetime
import winsound
import cv2
from LogIn import LogIN


class Dashboard():
    def __init__(self, window): 
        #self.username = LoginForm.
        self.window = window
        self.window.title('System Management Dashboard')
        self.window.geometry('1366x768')
        self.window.state('zoomed')
        self.window.resizable(0, 0)
        self.window.config(background='#eff5f6')
        self.people_count_list = []
        self.pred = []
        self.conf = [] 
        self.detected_frames = []
        self.available_spots =[]
        self.bg_frame = Image.open('FYP\\17.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image = photo )
        self.bg_panel.image = photo 
        self.bg_panel.pack(fill='both', expand= 'yes')
        
        # window Icon
        icon = PhotoImage(file='FYP\images\pic-icon.png')
        self.window.iconphoto(True, icon)

        # =====================================================================================
        # ============================ HEADER =================================================
        # =====================================================================================
        self.logout_text = Button(text='Logout', bg='white', font=("", 13, "bold"), bd=0, fg='black',
                                  cursor='hand2', activebackground='#32cf8e', command= self.destroy)
        self.logout_text.place(x=1200, y=15)

        # =====================================================================================
        # ============================ SIDEBAR =================================================
        # =====================================================================================
        self.sidebar = Frame(self.window, bg='black')
        self.sidebar.place(x=0, y=0, width=300, height=850)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================

        # logo
        self.logoImage = Image.open('FYP\\images\\hyy.png')
        photo = ImageTk.PhotoImage(self.logoImage)
        self.logo = Label(self.sidebar, image=photo, bg='black')
        self.logo.image = photo
        self.logo.place(x=70, y=80)
        
        # Name of brand/person
        self.brandName = Label(self.sidebar, text='James Bond', bg='black',fg='white', font=("", 15, "bold"))
        self.brandName.place(x=80, y=200)

        # Dashboard
        self.dashboardImage = Image.open('FYP\\images\\dashboard-icon.png')
        photo = ImageTk.PhotoImage(self.dashboardImage)
        self.dashboard = Label(self.sidebar, image=photo, bg='black')
        self.dashboard.image = photo
        self.dashboard.place(x=35, y=289)

        self.dashboard_text = Button(self.sidebar, text='Dashboard', bg='black',fg='white', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff')
        self.dashboard_text.place(x=80, y=291)
 
        # Manage
        self.manageImage = Image.open('FYP\\images\\manage-icon.png')
        photo = ImageTk.PhotoImage(self.manageImage)
        self.manage = Label(self.sidebar, image=photo, bg='black')
        self.manage.image = photo
        self.manage.place(x=35, y=340)

        self.manage_text = Button(self.sidebar, text='Manage', bg='black',fg='white', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff')
        self.manage_text.place(x=80, y=345)

        # Settings
        self.settingsImage = Image.open('FYP\\images\\settings-icon.png')
        photo = ImageTk.PhotoImage(self.settingsImage)
        self.settings = Label(self.sidebar, image=photo, bg='black')
        self.settings.image = photo
        self.settings.place(x=35, y=402)

        self.settings_text = Button(self.sidebar, text='Settings',bg='black',fg='white', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff')
        self.settings_text.place(x=80, y=402)
        

        self.Monior_Activities = Button(self.sidebar, text='Monior Activities',bg='black',fg='white', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff', command=self.Moniter)
        self.Monior_Activities.place(x=85, y=460)
        
        self.Queue = Button(self.sidebar, text='Queue Management',bg='black',fg='white', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff',command=self.Queue_Management)
        self.Queue.place(x=85, y=516)           
        
        self.parking = Button(self.sidebar, text='Parking Analysis',bg='black',fg='white', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff',command=self.Parking_Windows)
        self.parking.place(x=85, y=573)
        
        self.Heat = Button(self.sidebar, text='Heat Maps',bg='black',fg='white', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff',command=self.HeatMaps)
        self.Heat.place(x=85, y=615) 

        self.anomaly = Button(self.sidebar, text='Anomaly Detection',bg='black',fg='white', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff',command=self.Anomaly)
        self.anomaly.place(x=85, y=650)                

        self.reports = Button(self.sidebar, text='Report Analytics',bg='black',fg='white', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff',command=self.reports_analysis)
        self.reports.place(x=85, y=697)                 

        # Exit
        self.exitImage = Image.open('FYP\\images\\exit-icon.png')
        photo = ImageTk.PhotoImage(self.exitImage)
        self.exit = Label(self.sidebar, image=photo, bg='black')
        self.exit.image = photo
        self.exit.place(x=25, y=730)

        self.exit_text = Button(self.sidebar, text='Exit',bg='black',fg='white', font=("", 13, "bold"), bd=0,
                                cursor='hand2', activebackground='#ffffff', command= self.destroy)
        self.exit_text.place(x=85, y=740)  
    
    def Moniter(self):
        root = self.window
        self.mframe = Frame(root, bg='navy')
        self.mframe.place(x=400, y=90, width=1000, height=700)
        videoplayer = TkinterVideo(master=self.mframe, scaled=True)
        videoplayer.load(r"FYP/v.mp4")
        videoplayer.pack(expand=True, fill="both")
        videoplayer.play() # play the video
        

    def Queue_Management(self):
        root = self.window
        self.qframe = Frame(root, bg='red')  
        self.qframe.pack() 
        self.qframe.place(x=400, y=90, width=1000, height=700)
        from QueueManag import queue
        self.people_count_list = queue(self.qframe)

    def Parking_Windows(self):
        root = self.window
        self.pframe = Frame(root, bg='green')
        self.pframe.place(x=400, y=90, width=1000, height=700)   
        from ParkingAnalysis import Parking
        self.available_spots  = Parking(self.pframe) 
        root.mainloop()  

    def HeatMaps(self):
        root = self.window
        self.hframe = Frame(root, bg='yellow')
        self.hframe.place(x=400, y=90, width=1000, height=700) 
        from newheatmap import Heatmap
        self.heatmap = Heatmap(self.hframe)

    def Anomaly(self):
        root = self.window
        self.Aframe = Frame(root, bg='black')
        self.Aframe.place(x=300, y=80, width=600, height=400) 
        self.Bframe = Frame(root,bg='black')
        self.Bframe.place(x=900, y=400, width=600, height=400) 
        self.Cframe = Frame(root,bg='black')
        self.Cframe.place(x=900, y=80, width=600, height=400) 
        self.Dframe = Frame(root,bg='black')
        self.Dframe.place(x=300, y=480, width=600, height=400)                         
        from Robbery_detection import Robbery
        self.detected_frames = Robbery(self.Aframe)
        from fs import mainFunc
        self.pred, self.conf = mainFunc(self.Bframe)

    def reports_analysis(self):
        root = self.window
        self.rframe = Frame(root, bg='black')
        self.rframe.place(x=300, y=80, width=600, height=400)
        from QueueManag import display_previous_plots    
        display_previous_plots(self.people_count_list,self.rframe) 

        from fs import plot_fire
        self.Fsframe = Frame(root,bg='black')
        self.Fsframe.place(x=900, y=80, width=600, height=400)
        plot_fire(self.pred,self.conf,self.Fsframe)

        from ParkingAnalysis import plot_data
        self.Pkframe = Frame(root, bg='black')
        self.Pkframe.place(x=900, y=475, width=600, height=400)
        plot_data(self.available_spots,self.Pkframe )

        from Robbery_detection import plot_robbery_graph
        self. RBframe = Frame(root, bg='black')
        self.RBframe.place(x=300, y=480, width=600, height=400)
        plot_robbery_graph(self.detected_frames,self.RBframe )

    def destroy(self):
        self.window.destroy()
        LogIN()

def dashboard():
    window = Tk()
    Dashboard(window)
    window.mainloop()

if __name__ =='__main__':
    plt.show()
    
    dashboard()