from tkinter import Frame, Text, font, Label, Listbox, END, Spinbox, colorchooser, Button, messagebox
from frames.start_page import text_watermark


class TextWatermark(Frame):

    def __init__(self, parent, function):
        # initializes the super constructor
        Frame.__init__(self, parent)

        self.font_family = "@Arial Unicode MS"
        self.font_size = 10
        self.font_color = ((0, 0, 0), "black")

        # the text area for typing the ext to be watermarked on the image
        self.text = Text(self, height=5, width=30)
        # places the cursor in the tex area once the frame is on top
        self.text.focus()
        # places the text area on the frame
        self.text.grid(row=0, column=1, columnspan=2, pady=10)

        # scrollbar = Scrollbar(self, orient="vertical")
        # scrollbar.config(command=self.font_list.yview)
        # scrollbar.grid(row=1, column=1)

        # self.font_list.config(yscrollcommand=scrollbar.set)

        # a list of all the fonts in tkinter sorted alphabetically
        font_families = sorted(list(font.families()))

        # initializes a  label for the font and sets the position on the frame
        _font = Label(self, text="Font:")
        _font.grid(row=1, column=0)

        # initialized the listbox
        self.font_list = Listbox(self, height=5)
        # fill of the listbox with the fonts
        for f in font_families:
            self.font_list.insert(END, f)
        # add a listner to the listbox to call a function when a font is clicked
        self.font_list.bind("<<ListboxSelect>>", self.listbox_used)
        # initially selects the firtst item in the listbox
        self.font_list.select_set(0)
        # calls the listboxselect event on the selected item
        self.font_list.event_generate("<<ListboxSelect>>")
        # sets the listbox position on the frame
        self.font_list.grid(row=1, column=1)

        # initializes a label for the font size and sets the position on the frame
        _size = Label(self, text="size:")
        _size.grid(row=1, column=2)

        # initializes the spinbox for setting the font size
        # and set it on the frame
        self._font_size = Spinbox(self, from_=10, to=15, width=5, command=self.spinbox_used)
        self._font_size.grid(row=1, column=3)

        color_button = Button(self, text="Select Color", command=self.choose_color)
        color_button.grid(row=1, column=4, padx=10)

        done = Button(self, text="Done", command=lambda: self.text_watermark(function))
        done.grid(row=2, column=2, padx=10)

    def listbox_used(self, event):
        """
        This method is called when an item is clickd in the listbox
        :param event:
        :return: None
        """
        # set a class attributes to the font selected
        self.font_family = self.font_list.get(self.font_list.curselection())
        self.configure_text()

    def spinbox_used(self):
        """
        This method is called when a number is chosen in the spinbox for the dont size
        :return: None
        """
        # set a class attributes to the font size selected
        self.font_size = int(self._font_size.get())
        self.configure_text()

    def choose_color(self):
        """
        This method is called when a color for the text is chosen
        :return:
        """
        # opens up the dialog to choose the color from
        self.font_color = colorchooser.askcolor(title="Choose a Color")
        # if no color was chosen (cancel), sets the font color to the default value
        if self.font_color == (None, None):
            self.font_color = ((0, 0, 0), "black")
        self.configure_text()

    def configure_text(self):
        """
        This method is called to update the text style for the watermar
        :return: None
        """
        self.text.configure(font=(self.font_family, int(self.font_size)), fg=f"{self.font_color[1]}")

    def text_watermark(self, function):
        """
        This method gets the text and its format then passes it to the class responsible
        for adding the watermark to the image
        :param function: a function to change the visible frame
        :return: None
        """

        # if nothing was written don't do anything
        if len(self.text.get("1.0", END)) == 1:
            messagebox.showinfo(title="Info", message="Enter a Text")
            return

        # get the text written
        text = self.text.get("1.0", END)
        # pass the text and its firmat to the function responsible fo editing the image
        text_watermark(text, self.font_family, self.font_size, self.font_color)
        # hide this frame
        function("StartPage")
