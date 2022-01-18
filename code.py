def are_valid_groups(slist, glist):
        for student in slist:
            present = False
            for group in glist:
                if student in group:
                    present = True
            if present == False:
                return False
        return True
