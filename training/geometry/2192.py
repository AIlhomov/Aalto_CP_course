def is_on_segment(px, py, ax, ay, bx, by):

    if min(ax, bx) <= px <= max(ax, bx) and min(ay, by) <= py <= max(ay, by):
        
        cross_product = (px - ax) * (by - ay) - (py - ay) * (bx - ax)

        return cross_product == 0
    return False
#point
def is_inside_polygon(px, py, polygon):

    inside = False
    x1, y1 = polygon[-1]

    for x2, y2 in polygon:
        if is_on_segment(px, py, x1, y1, x2, y2):
            return "BOUNDARY"
        if ((y1 > py) != (y2 > py)) and (px < (x2 - x1) * (py - y1) / (y2 - y1) + x1):
            inside = not inside
        x1, y1 = x2, y2

    return "INSIDE" if inside else "OUTSIDE"

n, m = map(int, input().split())
polygon = [tuple(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(m)]

res = []
for px, py in points:
    res.append(is_inside_polygon(px, py, polygon))

print("\n".join(res))