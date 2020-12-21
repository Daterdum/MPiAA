import tkinter as tk


class Input_GUI:
    def __init__(self, master):
        self.master = master
        master.title("Input")
        self.input_box()

    def input_box(self):
        frame_size = tk.Frame(self.master, borderwidth=2, relief=tk.RAISED)
        frame_size.pack(pady=10)

        label_size = tk.Label(frame_size, text="Enter size")
        label_size.pack()

        self.entry_size = tk.Entry(frame_size)
        self.entry_size.pack()

        frame_start = tk.Frame(self.master, borderwidth=2, relief=tk.RAISED)
        frame_start.pack(fill=tk.X, side=tk.LEFT, padx=5)
        label_s = tk.Label(frame_start, text="Start point cooridnates")
        label_s.pack()

        frame_x = tk.Frame(frame_start)
        frame_x.pack(fill=tk.X, side=tk.LEFT, padx=10, pady=10)

        label_x = tk.Label(frame_x, text="Enter X coordinate", padx=5, pady=5)
        label_x.pack()

        self.entry_x = tk.Entry(frame_x)
        self.entry_x.pack()


        frame_y = tk.Frame(frame_start)
        frame_y.pack(fill=tk.X, side=tk.LEFT, padx=10, pady=10)

        label_y = tk.Label(frame_y, text="Enter Y coordinate")
        label_y.pack()

        self.entry_y = tk.Entry(frame_y)
        self.entry_y.pack()



        frame_end = tk.Frame(self.master, borderwidth=2, relief=tk.RAISED)
        frame_end.pack(fill=tk.X, side=tk.LEFT, padx=5)
        label_e = tk.Label(frame_end, text="End point cooridnates")
        label_e.pack()

        frame_x_e = tk.Frame(frame_end)
        frame_x_e.pack(fill=tk.X, side=tk.LEFT, padx=10, pady=10)

        label_x_e = tk.Label(frame_x_e, text="Enter X coordinate", padx=5, pady=5)
        label_x_e.pack()

        self.entry_x_e = tk.Entry(frame_x_e)
        self.entry_x_e.pack()


        frame_y_e = tk.Frame(frame_end)
        frame_y_e.pack(fill=tk.X, side=tk.LEFT, padx=10, pady=10)

        label_y_e = tk.Label(frame_y_e, text="Enter Y coordinate")
        label_y_e.pack()

        self.entry_y_e = tk.Entry(frame_y_e)
        self.entry_y_e.pack()



        frame_submit_btn = tk.Frame(self.master, borderwidth=2, relief=tk.RAISED)
        frame_submit_btn.pack(pady=10)

        submit_button = tk.Button(self.master, command=self.submit)
        submit_button.pack()

    def submit(self):
        self.start_x = self.entry_x.get()
        self.start_y = self.entry_y.get()
        self.end_x = self.entry_x_e.get()
        self.end_y = self.entry_y_e.get()
        self.size = self.entry_size.get()






class GUI:
    def __init__(self, master):
        self.master = master
        master.title("mpiaa_rgz_v6")
        self.frame = tk.Frame(self.master, relief=tk.RAISED, borderwidth=1)
        self.frame.pack()
        self.additional_frame = tk.Frame(self.master)
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self.master, text="hello there")
        label.pack()
        self.build_menu()

    def build_menu(self):
        mainmenu = tk.Menu(self.master)
        mainmenu.add_command(label="Enter input", command=self.input)  # add commands
        mainmenu.add_command(label="Exit", command=self.master.quit)
        self.master.config(menu=mainmenu)

    def input(self):
        input_root = tk.Tk()
        input_root.geometry("600x300")
        gui = Input_GUI(input_root)
        input_root.mainloop()
        print(gui.start_x)


def build():
    root = tk.Tk()
    root.geometry("600x400")
    gui = GUI(root)
    root.mainloop()
