from tkinter import Tk, Frame
from frames.start_page import StartPage
from frames.watermark import Watermark
from frames.text_watermark import TextWatermark


class Gui:

    def __init__(self):
        # initializes the tk class
        window = Tk()
        # sets the title of the window
        window.title("Image Watermarking")
        # sets the minimum size of the window
        window.minsize(width=500, height=400)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(window)
        # container.place(x=0, y=0, )
        container.grid(column=0, row=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # creates a dictionary with the key being the name of the frame ad the value the frame itself
        for f in (StartPage, Watermark, TextWatermark):
            frame_name = f.__name__
            frame = f(parent=container, function=self.show_frame)
            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

        # keeps the window active and visible
        window.mainloop()

    def show_frame(self, frame_name: str):
        """
        This method takes in the name of a frame as a parameter and then raises the frame above all others
        so as for the frame to become visible
        :param frame_name: (str) the name of the frame to be raised
        :return: None
        """
        frame = self.frames[frame_name]
        frame.tkraise()
