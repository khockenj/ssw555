import datetime

def MarriageBeforeDivorce(famListData):
    for i in famListData:
        if(i[4] != 0):
            if(i[3] > i[4]):
                dateList.append(i[0])
                print(i[0] + " have marriage date after the divorce date")
    if(len(dateList) == 0):
        print("There is no one having marriage dates after divorce date :)")
    else:
        print("These people have marriage dates after their divorce dates :( ")
        print(dateList)
