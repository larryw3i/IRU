

from tkinter import filedialog
import tkinter
import cv2
from PIL import Image, ImageTk
import time
from iru import _
import face_recognition


class VideoCapture:
    def __init__(
        self, 
        video_source = 0):

        # Open the video source
        self.vid = cv2.VideoCapture(video_source)

        if not self.vid.isOpened():
            raise ValueError( \
                _( "Unable to open video source") , 
                video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the 
                # current frame nvertedto BGR
                return (ret, cv2.cvtColor(
                    frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


class Commands:

    def __init__(
        self,
        window: tkinter.Tk,
        vid:VideoCapture,
        canvas: tkinter.Canvas,
        delay = 15
        ):
        self.window = window
        self.vid = vid
        self.canvas = canvas
        self.delay = delay
        self.stop_getting_frame = False

    def make_rect4face(self):
        for top, right, bottom, left in self.face_locations:

            # Draw a box around the face
            cv2.rectangle(self.color_frame, \
                (left, top), (right, bottom), (0, 0, 255), 2)

    def  select_image(self):

        self.stop_getting_frame = True

        path = filedialog.askopenfilename(\
            filetypes=[("Image File",'.jpg')])

        if not path: 
            self.stop_getting_frame = False
            return

        self.color_frame = face_recognition.load_image_file( path )

        self.face_locations = face_recognition.face_locations( 
            self.color_frame )

        self.make_rect4face()

        self.color_frame = ImageTk.PhotoImage(
            image = Image.fromarray( self.color_frame  ) )


        self.canvas.create_image(
            0, 0, image = self.color_frame, 
            anchor = tkinter.NW )

    def snapshot(self):

        ret, frame = self.vid.get_frame()

        if ret:
            self.color_frame = cv2.cvtColor( frame, cv2.COLOR_RGB2BGR )
            self.face_locations = face_recognition.face_locations(
                self.color_frame)

            self.make_rect4face()

            self.stop_getting_frame = True

            self.color_frame = ImageTk.PhotoImage(
                image = Image.fromarray( self.color_frame  ) )

            self.canvas.create_image(
                0, 0, image = self.color_frame, 
                anchor = tkinter.NW )
            

    def update(self):

        if self.stop_getting_frame: return

        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(
                image = Image.fromarray( frame ) )
                
            self.canvas.create_image(
                0, 0, image = self.photo, 
                anchor = tkinter.NW )

        self.window.after( self.delay, self.update )