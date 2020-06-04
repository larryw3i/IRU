

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
    
    name_label = tkinter.Label(
        window, text = _('name')
    )
    
    name_entry = tkinter.Entry(
        window,
    )

    window.title ( _('IRU') )

    vid_canvas.grid( 
        column = 0, row = 0 ,
        columnspan = 2 , rowspan = 2, )

    name_label.grid( column=2, row=0 )
    name_entry.grid( column=3, row=1 )

    snapshot_btn.grid( column=2, row=2 )
    select_image_btn.grid( column=2, row=2 )

    
    commands.update()
    
    window.mainloop()    
