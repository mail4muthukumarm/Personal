from points import Points
'''
    Main program for weather simulator
'''

if __name__ == "__main__":
    points = Points("input.txt")
    try:
        points.read()
        for point in points:
            print(point)
    except Exception as e:
        print(e.message)





