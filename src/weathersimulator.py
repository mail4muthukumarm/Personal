from points import Points
'''
    Main program for weather simulator
'''

if __name__ == "__main__":
    points = Points("input.txt")
    points.read()
    for point in points:
        print(point)





