def identify_year(year):
    if year%4 == 0:
        print "4"
        if year%100 == 0:
            print "100"
            if year%400 == 0:
                print "400"
                print True
            else:
                print False
        else:
            print True
    else:
        print False

year = input()
identify_year(year)
