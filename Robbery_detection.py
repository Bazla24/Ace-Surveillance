import numpy as np
import cv2
import imutils
import datetime
import time
import matplotlib.pyplot as plt
import os
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import pickle 

filename = 'Robbery.pkl'

def Robbery(root):
    gun_cascade = cv2.CascadeClassifier('FYP/cascade.xml')
    camera = cv2.VideoCapture('FYP/g1.mp4')

    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack()

    firstFrame = None
    gun_exist = False
    gun_count = 0
    detected_frames = []
    
    while True:
        ret, frame = camera.read()
    
        if not ret:
            break
   
        frame = imutils.resize(frame, width=500)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       
        gun = gun_cascade.detectMultiScale(gray,
                                       1.3, 5,
                                       minSize=(160, 160))
       
        if len(gun) > 0:
            gun_exist = True
           
        for (x, y, w, h) in gun:
            gun_count += 1
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            total_frames = int(camera.get(cv2.CAP_PROP_FRAME_COUNT))
            gun_percentage = (len(detected_frames) / total_frames) * 100
            cv2.putText(frame, "Gun Detection: {:.2f}%".format(gun_percentage), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        if firstFrame is None:
            firstFrame = gray
            continue
   
        #   Draw the timestamp on the frame
        cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S %p"),
                    (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.35, (0, 0, 255), 1)
        
        key = cv2.waitKey(1) & 0xFF
      
        if key == ord('q'):
            break
        if gun_exist:
            detected_frames.append((datetime.datetime.now(), gun_count))

        # Reset the gun counter and flag
        gun_count = 0
        gun_exist = False

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(frame)
        pil_image = pil_image.resize((800, 600), Image.ANTIALIAS)

        # Convert the PIL Image to a Tkinter PhotoImage object
        tk_image = ImageTk.PhotoImage(pil_image)

        # Draw the image on the canvas
        canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
        
        root.update()
        
    camera.release()
    cv2.destroyAllWindows()
    with open(filename, 'wb') as file:
        pickle.dump(detected_frames, file)    
    return detected_frames

def plot_robbery_graph(detected_frames,root):
    all_results =[]
    with open('Robbery.pkl', 'rb') as file:
        all_results = pickle.load(file)
    # Extract the datetime and gun count from detected_frames
    datetime_list = [dt for dt, count in all_results]
    gun_count_list = [count for dt, count in all_results]
        
    all_results += datetime_list + gun_count_list    
    with open('Robbery.pkl', 'wb') as file:
        pickle.dump(all_results, file)    
 
    fig = Figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).plot(datetime_list)
    fig.suptitle('Gun Detection Over Time')
    fig.axes[0].set_xlabel('Time')
    fig.axes[0].set_ylabel('Gun Count')
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

if __name__ == '__main__':
    root2 = tk.Tk()
    # Set the title of the main window
    root2.title("My")

    detected_frames = Robbery(root2)
    plot_robbery_graph(detected_frames,root2)

    root2.mainloop()                                     