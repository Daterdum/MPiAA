from math import inf


def shortest_route(coordinates, obstacles, size=500):
    """
    Function for finding shortest route between 2 points
    :param coordinates: dictionary {'s_x': start_x, 's_y': start_y, 'e_x': end_x, 'e_y': end_y, 'size': size}
    :param obstacles: dictionary with all obstacles {№: {'x': x, 'y': y, 'r': r}, ...}
    :param size: size of canvas
    :return:
    """
    canvas_ar = [[]]
    step = int(coordinates['size'])

    def collides(obstacle, node):
        """
        Function for checking collision for each node in array
        """
        if node.x in range(obstacle['x'] - obstacle['r'], obstacle['x'] + obstacle['r']):
            if node.y in range(obstacle['y'] - obstacle['r'], obstacle['y'] + obstacle['r']):
                return True
        return False

    def canvas_to_arr(obstacles, size=500, step=30):
        """
        Function for creating array of Nodes, and filling them with correct 'is_empty' property
        """
        line = 0
        element = 0
        for y in range(0, size, step):
            canvas_ar.append([])
            for x in range(0, size, step):
                canvas_ar[line].append([])
                check = 0
                for obstacle in obstacles.values():
                    check = 1 if collides(obstacle, Node(x, y)) else check
                canvas_ar[line][element] = Node(x, y, is_empty=True if check == 0 else False)
                element += 1
            element = 0
            line += 1

    def lee_algorithm(array, start, end):
        """
        Main algorithm for finding shortest route
        """
        array[start[0]][start[1]].marker = 0

        def _indication(array):
            """
            Function for marking each Node in array according to its distance from start node.
            Stops when end Node is marked.
            """
            def _filter(variable):
                if variable is None:
                    return False
                else:
                    return True
            mark = 0
            while (array[end[0]][end[1]].marker is None):
                # draw_markers()  # show markers with each iteration
                for line in array:
                    for element in line:
                        if element.marker == mark:
                            for neighbour in filter(_filter, element.neighbours.values()):
                                if neighbour.marker is None and neighbour.is_empty:
                                    neighbour.marker = mark + 1
                # print('\n mark = {}\n'.format(mark)) # separates marking print cycle
                mark += 1

        route_coordinates = []
        route_coordinates.append(array[end[1]][end[0]])

        def route_back(point):
            """
            Function for building route back from end to start according to markers.
            """
            if not point.is_empty:
                pass
            elif point.marker == 0:
                pass
            else:
                closest_neighbour = point.closest_neighbour()
                route_coordinates.append(closest_neighbour)
                route_back(closest_neighbour)

        _indication(array)
        if array[end[1]][end[0]].marker is None:
            return [0]
        else:
            route_back(array[end[1]][end[0]])
            return route_coordinates

    def arr_to_graph(array):
        """
        Function for creating graph system between Nodes in array
        """
        for line_num, line in enumerate(array):
            for element_num, element in enumerate(line):
                if element.is_empty:
                    element.neighbours['top_nbr'] = array[line_num - 1][element_num] if line_num != 0 else None
                    element.neighbours['bot_nbr'] = array[line_num + 1][element_num] if line_num != len(array) - 1 else None
                    element.neighbours['left_nbr'] = array[line_num][element_num - 1] if element_num != 0 else None
                    element.neighbours['right_nbr'] = array[line_num][element_num + 1] if element_num != len(line) - 1 else None

    def draw_markers():
        """
        Support function.
        Used to print markers of each node in array. Isn't used in completing task.
        """
        for line in canvas_ar:
            temp = []
            for element in line:
                if element.marker is None:
                    if not element.is_empty:
                        temp.append('*')
                    else:
                        temp.append('_')
                else:
                    temp.append(str(element.marker))
            print(temp)

    _obstacles = {k: {in_k: int(in_v) for in_k, in_v in v.items()} for k, v in obstacles.items()}
    canvas_to_arr(obstacles=_obstacles, size=size, step=step)
    canvas_ar.pop()
    arr_to_graph(canvas_ar)
    start_node = [int(int(coordinates['s_x']) / step), int(int(coordinates['s_y']) / step)]
    end_node = [int(int(coordinates['e_x']) / step), int(int(coordinates['e_y']) / step)]
    output = lee_algorithm(canvas_ar, start_node, end_node)
    return output


class Node:
    """
    Class of objects used in creating graph for building shortest route.
    Contains information and references about its neighbours.
    is_empty parameter shows if any obstacle collides with node.
    """
    def __init__(self, x, y, side=30, is_empty=False, top_nbr=None, bot_nbr=None, left_nbr=None, right_nbr=None):
        self.x = x
        self.y = y
        self.side = side  # not implemented yet
        self.neighbours = {'top_nbr': top_nbr, 'bot_nbr': bot_nbr, 'left_nbr': left_nbr, 'right_nbr': right_nbr}
        self.is_empty = is_empty
        self.marker = None

    def x_g(self, step=30):
        return int(self.x / step) if self.x != 0 else 0

    def y_g(self, step=30):
        return int(self.y / step) if self.y != 0 else 0

    def marker(self):
        return self.marker

    def closest_neighbour(self):
        lowest_marker = inf
        point = None
        for neighbour in [x for x in self.neighbours.values() if x is not None]:
            if neighbour.marker is None:
                continue
            elif neighbour.marker < lowest_marker:
                lowest_marker = neighbour.marker
                point = neighbour
        return point


def main():
    print(shortest_route(coordinates={"s_x": "120",
                                "s_y": "120",
                                "e_x": "350",
                                "e_y": "450",
                                "size": "30"},
                   obstacles={
                                "1": {
                                    "x": "250",
                                    "y": "120",
                                    "r": "40"
                                },
                                "2": {
                                    "x": "10",
                                    "y": "10",
                                    "r": "20"
                                },
                                "3": {
                                    "x": "10",
                                    "y": "10",
                                    "r": "20"
                                },
                                "4": {
                                    "x": "10",
                                    "y": "10",
                                    "r": "20"
                                }}))


if __name__ == "__main__":
    main()
