with open ("events.log","r") as f:
    json = []
    d = {}
    for line in f:
        l = line.strip().split(",")
        has_logout_count = 0
        if l[1] in d:
            d[l[1]]["event_count"]+=1
            if l[2] =="logout":
                has_logout_count +=1
        else:
            d[l[1]]= {"event_count": 1}
            has_logout_count = 1
        if has_logout_count >1:
            d[l[1]]["has_logout"] = True
        else:
            d[l[1]]["has_logout"] = False
        
    print(d)

