
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
from iru import _


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

    def snapshot(self):

        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv2.imwrite("frame-" + time.strftime(
                "%d-%m-%Y-%H-%M-%S") + ".g",
                cv2.cvtColor(frame, 
                cv2.COLOR_RGB2BGR) )

    def update(self):

        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(
                image = PIL.Image.fromarray( frame ) )
                
            self.canvas.create_image(
                0, 0, image = self.photo, 
                anchor = tkinter.NW )

        self.window.after( self.delay, self.update )