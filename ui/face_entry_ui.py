

import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
from iru import _
from _ui._face_entry import FaceEntry, VideoCapture
from ui.face_entry_person_grid_ui import   iru_person_grid

def face_entry():
    
    window = tkinter.Tk()
    vid = VideoCapture()
    

    vid_canvas = tkinter.Canvas(
        window, width = vid.width, 
        height = vid.height)

    _face_entry = FaceEntry( window, vid, vid_canvas )

    snapshot_btn = tkinter.Button(
            window, text= _("Snapshot"), 
            width=50, command= _face_entry.snapshot )

    select_image_btn = tkinter.Button(
            window, text= _("Select image"), 
            width=50, command= _face_entry.select_image )
    

    window.title ( _('IRU') )

    iru_person_grid( window )

    vid_canvas.grid( 
        column = 0, row = 0 ,
        columnspan = 2 , rowspan = 7, )


    snapshot_btn.grid( column=2, row=6 )
    select_image_btn.grid( column=3, row=6 )

    
    _face_entry.update()
    
    window.mainloop()    
