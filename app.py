import tkinter as tk
from tkinter import filedialog


class TextEditor(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Text Editor")
        self.geometry("1000x700") # sets the initial size of the window
        self.text = tk.Text(self, font=("TkDefaultFont", 16))
        self.text.pack(fill='both', expand=True)
        self.text.bind('<Control-s>', self.save_file)
        self.text.bind('<Command-s>', self.save_file)
        self.text.bind('<Control-o>', self.open_file)
        self.text.bind('<Command-o>', self.open_file)
        self.text.bind('<Control-Key-equal>', self.increase_text_size)
        self.text.bind('<Command-Key-equal>', self.increase_text_size)
        self.text.bind('<Control-minus>', self.decrease_text_size)
        self.text.bind('<Command-minus>', self.decrease_text_size)
        self.menu = tk.Menu(self)
        self.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)

    def open_file(self, event=None):
        file = filedialog.askopenfile(mode='r', defaultextension=".txt",
                                      filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.text.delete(1.0, 'end')
            self.text.insert('end', file.read())
            file.close()

    def save_file(self, event=None):
        file = filedialog.asksaveasfile(mode='w', defaultextension=".txt",
                                        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            file.write(self.text.get(1.0, 'end'))
            file.close()

    def increase_text_size(self, event=None):
        font = self.text.cget("font")
        size = int(font.split(" ")[-1])
        size += 2
        self.text.config(font=font.split(" ")[0] + " " + str(size))

    def decrease_text_size(self, event=None):
        font = self.text.cget("font")
        size = int(font.split(" ")[-1])
        size -= 2
        self.text.config(font=font.split(" ")[0] + " " + str(size))
        
if __name__ == '__main__':
    editor = TextEditor()
    editor.focus_set()
    editor.text.focus_set()
    editor.mainloop()