def classAverage(*args):
    averages= list()
    for items in args:
        avrg=float(sum(items)/len(items))
        averages.append(avrg)
        print("{} Sınıfın Ortalaması: {} ".format(items, round(avrg, 2)))
    print("Sınıfların ortalamaları sırasıyla: ",averages)
    print("En başarılı sınıfın ortalaması: ",max(averages))

A = [100, 85, 70]
B = [80, 70,90]
C = [55, 78, 45]
D = [67,77,59]

classAverage(A,B,C,D)
