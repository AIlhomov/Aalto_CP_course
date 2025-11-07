t = int(input())

def onSegment(p, q, r):
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - \
          (q[0] - p[0]) * (r[1] - q[1])

    if val == 0:
        return 0

    return 1 if val > 0 else 2

def doIntersect(points):
    o1 = orientation(points[0][0], points[0][1], points[1][0])
    o2 = orientation(points[0][0], points[0][1], points[1][1])
    o3 = orientation(points[1][0], points[1][1], points[0][0])
    o4 = orientation(points[1][0], points[1][1], points[0][1])

    if o1 != o2 and o3 != o4:
        return True

    if o1 == 0 and onSegment(points[0][0], points[1][0], points[0][1]):
        return True

    if o2 == 0 and onSegment(points[0][0], points[1][1], points[0][1]):
        return True

    if o3 == 0 and onSegment(points[1][0], points[0][0], points[1][1]):
        return True

    if o4 == 0 and onSegment(points[1][0], points[0][1], points[1][1]):
        return True

    return False

for i in range(t):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    segment1 = [(x1, y1), (x2, y2)]
    segment2 = [(x3, y3), (x4, y4)]

    if doIntersect([segment1, segment2]):
        print('YES')
    else:
        print('NO')