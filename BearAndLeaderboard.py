
firstQuery=input()
firstQuery=firstQuery.split(" ")
teamsize=int(firstQuery[0])
querysize=int(firstQuery[1])
if querysize <= 500000 and teamsize >= 1:
    teamHashValue=0
    for i in range(querysize):
        query = input()
        query = query.split(" ")
        team = {}
        valIfExist = team.get(query[0])
        if valIfExist:
            team[query[0]] += valIfExist+int(query[1])
        else :
            team[query[0]] = int(query[1])

        for j in team.keys():
            teamHashValue += int(j)*team[j]
        print(str(teamHashValue))


