if __name__ == "__main__":

    try:
        f = open("fort.98")

    except IOError: print("file fort.98 does not exist")

    else:
        out = []
        for i in range(4):
            line = f.readline()

        while True:
            line1 = f.readline()
            line2 = f.readline()
            line3 = f.readline()
            line4 = f.readline()

            if not line1:
                break

            list1 = line1.split("-")
            Z = list1[0]

            list2 = line2.split(" ")
            while list2.count("") > 0:
                list2.remove("")
            list2.pop(0)
            list2[len(list2)-1] = list2[len(list2)-1].rsplit("\n")[0]

            list3 = line3.split(" ")
            while list3.count("") > 0:
                list3.remove("")
            list3.pop(0)
            list3[len(list3)-1] = list3[len(list3)-1].rsplit("\n")[0]

            for i in range(0, len(list2)):
                out.append(Z + "\t" + list2[i] + "\t" + list3[i])

            tmp1 = out[-1].split("\t")[0]

        for i in out[::-1]:
            tmp0 = i.split("\t")[0]
            if tmp0 != tmp1: print("")
            print(i)
            tmp1 = tmp0

