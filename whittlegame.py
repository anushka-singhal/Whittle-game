def remove_nails(nails, m):
    def calculate_area(nails):
        n = len(nails)
        area = 0
        for i in range(n):
            j = (i + 1) % n
            area += (nails[i][0] * nails[j][1]) - (nails[j][0] * nails[i][1])
        return abs(area) / 2.0

    def is_clockwise(p, q, r):
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]) <= 0

    def remove_bottommost(nails):
        bottommost = min(nails, key=lambda x: (x[1], x[0]))
        return [nail for nail in nails if nail != bottommost]

    def remove_topmost(nails):
        topmost = max(nails, key=lambda x: (x[1], x[0]))
        return [nail for nail in nails if nail != topmost]

    def remove_leftmost(nails):
        leftmost = min(nails, key=lambda x: (x[0], x[1]))
        return [nail for nail in nails if nail != leftmost]

    if m == 1:
        # Remove the bottommost nail
        return remove_bottommost(nails)

    if m == 2:
        # Remove the bottommost and leftmost nails
        nails = remove_bottommost(nails)
        nails = remove_leftmost(nails)
        return nails

    # If m is greater than 2, any nail can be removed to achieve the same area
    return nails

def main():
    n = int(input())
    nails = [list(map(int, input().split())) for _ in range(n)]
    m = int(input())

    result_nails = remove_nails(nails, m)

    for nail in result_nails:
        print(f"{nail[0]} {nail[1]}")

    if calculate_area(result_nails) == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
