import math
from functools import cmp_to_key


def sort_pts_on_x(pts: list) -> list:
    """pts = [(x1, y1), (x2, y2), ... ]"""
    return sorted(pts, key=cmp_to_key(lambda p, q: p[0] - q[0]))


def min_dist_brute(pts):
    """compute the minimum distance between two points in pts = [(x1, y1), (x2, y2), ... ]"""
    return min(math.dist(p, q) for qi, q in enumerate(pts[:-1]) for p in pts[qi + 1 :])


def min_dist_divide_and_conquer(pts: list) -> float:
    """compute the minimum distance between two points in pts = [(x1, y1), (x2, y2), ... ]
    Note that pts must be sorted on x value"""
    if len(pts) <= 3:
        return min_dist_brute(pts)
    half = len(pts) // 2
    x_cutoff = 0.5 * (pts[half - 1][0] + pts[half][0])
    left_half = pts[:half]
    right_half = pts[half:]
    min_dist = min(min_dist_divide_and_conquer(left_half), min_dist_divide_and_conquer(right_half))

    # check all points close to the cutoff
    pts_strip = [p for p in pts if abs(p[0] - x_cutoff) < min_dist]
    if len(pts_strip) == 0:
        return min_dist
    left_right_min = min_dist_brute(pts_strip)
    return min(min_dist, left_right_min)
