from math import sqrt, inf


def sort_points(points, func):
    return sorted(points, key=lambda point: func(point))


def dist(a, b):
    return sqrt(((b.x - a.x) ** 2) + ((b.y - a.y) ** 2))


def closest_from_three(points):
    min_dist = dist(points[0], points[1])
    min_pair = [points[0], points[1]]
    for index, point in enumerate(points):
        for id_other_point in range(index + 1, len(points)):
            if dist(point, points[id_other_point]) < min_dist:
                min_dist = dist(point, points[id_other_point])
                min_pair = [point, points[id_other_point]]
    return min_pair


def closest_pair_between(pleft, pright, d):
    xm = (pleft[-1].x + pright[0].x)/2
    pstripe = sort_points([point for point in pleft+pright if abs(point.x - xm) < d], Point.y)

    min_dist = inf
    min_pair = []
    for index, point in enumerate(pstripe):
        for compare_id in range(index + 1, len(pstripe)):
            if point.y - pstripe[compare_id].y < d:
                if dist(point, pstripe[compare_id]) < min_dist:
                    min_dist = dist(point, pstripe[compare_id])
                    min_pair = [point, pstripe[compare_id]]
            else:
                break
    return min_pair


def closest_pair(points):
    if len(points) < 2:
        return "Exception"  # "unittest.assertWarns" works weird with "raise Exception"
    pair = sort_points(_closest_pair(sort_points(points, Point.x)), Point.x)
    return make_pair(pair[0], pair[1])


def _closest_pair(points):
    if len(points) == 2:
        return points
    if len(points) <= 3:
        return closest_from_three(points)
    p_l = _closest_pair(points[: int(len(points)/2)])
    p_r = _closest_pair(points[int(len(points)/2): ])
    d = min(dist(p_l[0], p_l[1]), dist(p_r[0], p_r[1]))
    p_b = closest_pair_between(points[: int(len(points)/2)], points[int(len(points)/2): ], d)
    return sorted([p_l, p_r, p_b], key=lambda point: dist(point[0], point[1]))[0]


def make_pair(point_1, point_2):
    return "Point 1 = ({}, {}), point 2 = ({}, {})".format(point_1.x, point_1.y, point_2.x, point_2.y)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def x(self):
        return self.x

    def y(self):
        return self.y


def main():
    alist = [Point(-1, 20), Point(-1.5, 10), Point(-2, -10), Point(-2.7, -20),
            Point(-10, 20), Point(-10.5, 10), Point(-11.7, -10), Point(-12.2, -20),
            Point(1, 21), Point(1.5, 11), Point(2, -9), Point(2.7, -19),
            Point(10, 21), Point(10.5, 11), Point(11.7, -9), Point(12.2, -19)]
    print(closest_pair(alist))


if __name__ == "__main__":
    main()
