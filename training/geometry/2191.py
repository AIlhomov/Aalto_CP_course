n = int(input())
vertices = [tuple(map(int, input().split())) for _ in range(n)]

vertices.append(vertices[0])

# Shoelace formula
area = 0
for i in range(n):
    x1, y1 = vertices[i]
    x2, y2 = vertices[i + 1]
    area += x1 * y2 - x2 * y1

print(abs(area))
