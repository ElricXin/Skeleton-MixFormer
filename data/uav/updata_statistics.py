def updata_statistics():

    #updata label.txt
    f = open('./statistics/label.txt', "a")
    f.truncate(0)

    with open('./statistics/skes_available_name.txt', 'r') as fr:
        str_data = fr.read()
    str_data=str_data.split('\n')
    for i in range(len(str_data)):
        if i < len(str_data) - 1:
            f.write(str(int(str_data[i][-14:-11]))+'\n')
        else:
            f.write(str(int(str_data[i][-14:-11])))
    f.close()

    # updata performer.txt
    f = open('./statistics/performer.txt', "a")
    f.truncate(0)

    with open('./statistics/skes_available_name.txt', 'r') as fr:
        str_data = fr.read()
    str_data=str_data.split('\n')
    for i in range(len(str_data)):
        if i < len(str_data) - 1:
            f.write(str(int(str_data[i][1:4]))+'\n')
        else:
            f.write(str(int(str_data[i][1:4])))
    f.close()

    # updata replication.txt
    f = open('./statistics/replication.txt', "a")
    f.truncate(0)

    with open('./statistics/skes_available_name.txt', 'r') as fr:
        str_data = fr.read()
    str_data=str_data.split('\n')
    for i in range(len(str_data)):
        if i < len(str_data) - 1:
            f.write(str(int(str_data[i][-10:-9]))+'\n')
        else:
            f.write(str(int(str_data[i][-10:-9])))
    f.close()

    # updata setup.txt
    f = open('./statistics/setup.txt', "a")
    f.truncate(0)

    with open('./statistics/skes_available_name.txt', 'r') as fr:
        str_data = fr.read()
    str_data=str_data.split('\n')
    for i in range(len(str_data)):
        if i < len(str_data) - 1:
            f.write(str(int(str_data[i][5:7]))+'\n')
        else:
            f.write(str(int(str_data[i][5:7])))
    f.close()


    #updata camera.txt
    f = open('./statistics/camera.txt', "a")
    f.truncate(0)
    with open('./statistics/skes_available_name.txt', 'r') as fr:
        str_data = fr.read()
    str_data=str_data.split('\n')
    for i in range(len(str_data)):
        if i<len(str_data)-1:
            f.write(str(1)+'\n')
        else:
            f.write(str(1))
    f.close()

if __name__ == '__main__':
    updata_statistics()
