import csv


def student_param():
    with open('hw.csv') as f:
        weight = 0
        height = 0

        read_f = csv.reader(f)
        for row in read_f:
            try:
                students = int(row[0])
                height += float(row[1])
                weight += float(row[2])
            except:
                pass
    return round(height * 2.54 / students, 3), round(weight * 0.453 / students, 3)
