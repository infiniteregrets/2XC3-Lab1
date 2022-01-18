def are_valid_groups(slist, glist):
        attendance = [False] * slist.length

        for sindex in range (0, slist.length - 1):
            present = False
            for group in glist:
                if group.size != 2 and group.size != 3:
                    return False
                    
                if slist[sindex] in group:
                    if attendance[sindex] == False:
                        attendance[sindex] = True
                    else:
                        return False
                    
        return True
