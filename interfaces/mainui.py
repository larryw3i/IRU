

import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
from iru import _
from _interfaces._mainui import VideoCapture, Commands

def main_ui():
    
    window = tkinter.Tk()
    vid = VideoCapture()
    

    vid_canvas = tkinter.Canvas(
        window, width = vid.width, 
        height = vid.height)

    commands = Commands( window, vid, vid_canvas )

    snapshot_btn = tkinter.Button(
            window, text= _("Snapshot"), 
            width=50, command= commands.snapshot )

    select_image_btn = tkinter.Button(
            window, text= _("Select image"), 
            width=50, command= commands.select_image )

    window.title ( _('IRU') )

    vid_canvas.pack()

    snapshot_btn.pack(
        anchor=tkinter.CENTER, 
        expand=True )

    select_image_btn.pack(
        anchor=tkinter.CENTER, 
        expand=True )
    
    commands.update()
    
    window.mainloop()    
