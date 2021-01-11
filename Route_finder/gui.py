import tkinter as tk
from json import load, dump
from algorithm import shortest_route, Node


class Obstacles_GUI:
    def __init__(self, master):
        self.master = master
        self.obstacle_counter = 0
        master.title("Input obstacles")
        with open('obstacles.json', 'w') as f:
            dump({}, f)
        self.input_box()

    def input_box(self):
        title_frame = tk.Frame(self.master, borderwidth=2, relief=tk.FLAT)
        title_frame.pack(pady=10, fill=tk.X)
        title_label = tk.Label(title_frame, text='Enter coordinates of obstacles')
        title_label.pack()

        main_frame = tk.Frame(self.master, borderwidth=2, relief=tk.FLAT)
        main_frame.pack(fill=tk.BOTH, side=tk.TOP, padx=5)
        # start frame
        frame_start = tk.Frame(main_frame, borderwidth=2, relief=tk.RAISED)
        frame_start.pack(fill=tk.X, side=tk.LEFT, padx=5)
        label_s = tk.Label(frame_start, text="Press 'Add' to add more obstacle, press")
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

        frame_r = tk.Frame(frame_start)
        frame_r.pack(fill=tk.X, side=tk.LEFT, padx=10, pady=10)

        label_r = tk.Label(frame_r, text="Enter radius")
        label_r.pack()

        self.entry_r = tk.Entry(frame_r)
        self.entry_r.pack()

        # frame for both buttons
        frame_buttons = tk.Frame(self.master, borderwidth=2, relief=tk.FLAT)
        frame_buttons.pack(side=tk.TOP, pady=30)
        # submit button frame
        frame_submit_btn = tk.Frame(frame_buttons, borderwidth=2, relief=tk.FLAT)
        frame_submit_btn.pack(side=tk.LEFT, pady=30)

        submit_button = tk.Button(frame_submit_btn, text="Enter", command=self.submit_input, height=3, width=10)
        submit_button.pack()

        # add button frame
        frame_add_btn = tk.Frame(frame_buttons, borderwidth=2, relief=tk.FLAT)
        frame_add_btn.pack(side=tk.LEFT, pady=30)

        add_button = tk.Button(frame_add_btn, text="Add", command=self._add_value, height=3, width=10)
        add_button.pack()

    def _add_value(self):  # write code here
        self.obstacle_counter += 1
        temp = load(open('obstacles.json'))
        temp.update({self.obstacle_counter: {'x': self.entry_x.get(), 'y': self.entry_y.get(), 'r': self.entry_r.get()}})
        with open(file='obstacles.json', mode='w') as f:
            dump(temp, f)
        self.entry_y.delete(0, 'end')
        self.entry_x.delete(0, 'end')
        self.entry_r.delete(0, 'end')

    def submit_input(self):  # needs rework
        self.master.destroy()


class Input_GUI:
    def __init__(self, master):
        self.master = master
        master.title("Input")
        self.input_box()

    def input_box(self):
        # size frame
        frame_size = tk.Frame(self.master, borderwidth=2, relief=tk.RAISED)
        frame_size.pack(pady=5)

        label_size = tk.Label(frame_size, text="Enter size")
        label_size.pack()

        self.entry_size = tk.Entry(frame_size)
        self.entry_size.pack()

        frame_coordinates = tk.Frame(self.master, borderwidth=2, relief=tk.FLAT)
        frame_coordinates.pack(fill=tk.X, side=tk.TOP, padx=5)
        # start frame
        frame_start = tk.Frame(frame_coordinates, borderwidth=2, relief=tk.RAISED)
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

        # end frame
        frame_end = tk.Frame(frame_coordinates, borderwidth=2, relief=tk.RAISED)
        frame_end.pack(fill=tk.X, side=tk.LEFT, padx=5)
        label_e = tk.Label(frame_end, text="End point coordinates")
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

        # submit button frame
        frame_submit_btn = tk.Frame(self.master, borderwidth=2, relief=tk.FLAT)
        frame_submit_btn.pack(fill=tk.X, side=tk.TOP, pady=30)

        submit_button = tk.Button(frame_submit_btn, text="Enter", command=self.submit_input, height=3, width=10)
        submit_button.pack()

    def submit_input(self):
        try:
            with open(file='input.json', mode='w') as f:
                temp = {
                        's_x': self.entry_x.get(),
                        's_y': self.entry_y.get(),
                        'e_x': self.entry_x_e.get(),
                        'e_y': self.entry_y_e.get(),
                        'size': self.entry_size.get()
                }
                dump(temp, f)
            self.master.destroy()
        except AttributeError:  # Add exception workaround
            print("Error")


class GUI:
    """
    General GUI class, builds main window, canvas for showing elements and gives methods for interacting with them
    """

    def __init__(self, master):
        self.master = master
        self.robot = None
        master.title("mpiaa_rgz_v6")
        self._create_widgets()

    def _create_widgets(self):  # method for initial building widgets
        self._build_menu()
        self.frame = tk.Frame(self.master, relief=tk.RAISED, borderwidth=1)
        self.frame.pack(side=tk.LEFT)
        self._canvas_init()
        self.r_frame = tk.Frame(self.master, relief=tk.RAISED, borderwidth=1, height=500, width=200)
        self.r_frame.pack(side=tk.LEFT)
        self._do()

    def _build_menu(self):  # needs extension on save and upload scenarios
        mainmenu = tk.Menu(self.master)
        mainmenu.add_command(label="Enter input", command=self._input)
        mainmenu.add_command(label="Enter obstacles", command=self._obstacles)
        mainmenu.add_command(label="Exit", command=self.master.quit)
        self.master.config(menu=mainmenu)

    def _input(self):
        """
        Creates new window for entering start/end coordinates and size of robot
        :return:
        """
        input_root = tk.Tk()
        input_root.geometry("600x300")
        gui = Input_GUI(input_root)
        input_root.mainloop()  # from here we can use updated values

    def _obstacles(self):
        """
        Creates new window for entering obstacles coordinates
        :return:
        """
        input_root = tk.Tk()
        input_root.geometry("600x300")
        gui = Obstacles_GUI(input_root)
        input_root.mainloop()

    def _canvas_init(self):
        self.canvas = tk.Canvas(self.frame, bg="white", height=500, width=500)
        self.canvas.pack()

    def _do(self):
        button = tk.Button(self.r_frame, text="Do", command=self.__do, bg='green', height=30, width=50)
        button.config(height=10, width=100)
        button.pack(side=tk.BOTTOM)

        s_button = tk.Button(self.r_frame, text="Save to file", command=self._save, bg='lightgray', height=30, width=50)
        s_button.config(height=10, width=100)
        s_button.pack(side=tk.TOP)

        l_button = tk.Button(self.r_frame, text="Load from file", command=self._load, bg='lightgray', height=30, width=50)
        l_button.config(height=10, width=100)
        l_button.pack(side=tk.TOP)

    def __do(self):
        self.connector(size=500)

    def connector(self, size=500):
        obstacles = load(open('obstacles.json'))
        coordinates = load(open('input.json'))
        self.end_route = shortest_route(coordinates, obstacles, size=size)
        self.draw_scene(self.end_route, coordinates, obstacles)

    def _save(self):
        end_output = {}
        for k in range(len(self.end_route)):
            end_output.update({k: {'x': self.end_route[k].x, 'y': self.end_route[k].y}})
        with open(file='savefile.json', mode='w') as f:
            dump({'obstacles': load(open('obstacles.json')), 'coordinates': load(open('input.json')), 'end_route': end_output}, f)

    def _load(self):
        obstacles = load(open('savefile.json'))['obstacles']
        coordinates = load(open('savefile.json'))['coordinates']
        _route = load(open('savefile.json'))['end_route']
        route = []
        for node in _route.values():
            route.append(Node(x=node['x'], y=node['y']))
        self.draw_scene(route=route, coordinates=coordinates, obstacles=obstacles)

    def draw_circle(self, x, y, r, **kwargs):
        x = int(x)
        y = int(y)
        r = int(r)
        self.canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)

    def draw_line(self, x0, y0, x1, y1, **kwargs):
        self.canvas.create_line(x0, y0, x1, y1, **kwargs)

    def draw_scene(self, route, coordinates, obstacles):
        self.canvas.delete('all')
        for x in range(0, self.canvas.winfo_width(), int(coordinates['size'])):
            self.draw_line(x, 0, x, self.canvas.winfo_height())
        for y in range(0, self.canvas.winfo_height(), int(coordinates['size'])):
            self.draw_line(0, y, self.canvas.winfo_width(), y)

        point = [int(coordinates['s_x']), int(coordinates['s_y'])]
        self.draw_circle(coordinates['s_x'], coordinates['s_y'], coordinates['size'], fill='green')
        self.draw_circle(coordinates['e_x'], coordinates['e_y'], coordinates['size'], fill='red')
        for obstacle in obstacles.values():
            self.draw_circle(obstacle['x'], obstacle['y'], obstacle['r'], fill='black')
        for node in route[::-1]:
            self.draw_line(point[0], point[1], node.x, node.y, fill='green', width=3)
            point[0] = node.x
            point[1] = node.y


def main():
    root = tk.Tk()
    root.geometry("600x400")
    gui = GUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
