import random
import pandas as np
class advisor:
    preferences = []
    
    def __init__(self,name,slots,time):
        self.name= name
        self.timeslots = timeslots(time,slots)
        self.slots = slots
    
    def generatepreferences(self,startuplist,cutoff):
        random.shuffle(startuplist)
        self.preferences= startuplist[0:cutoff]
        print(startuplist[0:cutoff])
        
    def generatedprefs(self,startuplist):
        random.shuffle(startuplist)
        self.preferences= startuplist
        
    def amanufacturer(no,slots):
        l=[]
        for i in range(0,no):
            l.append(advisor('A'+str(i),slots,10))
        return(l)

class startup:
    def __init__(self,name,slots,time):
        self.name= name
        self.timeslots = timeslots(time,slots)
        self.slots = slots
    def smanufacturer(no,slots):
        l=[]
        for i in range(0,no):
            l.append(startup('S'+str(i),slots,10))
        return(l)
    
class timeslots:

    def __init__(self,length,no):
        self.slots = [False]*no
        self.participants = [[]]*no
        self.length = length
        
    def addlist(self,pars):
        parcount = 0
        for i in range(0,len(self.slots)):
            if (self.slots[i] != True):
                if(i < len(pars)):
                    self.participants[index].append(pars[parcount])
                    self.slots[i]== True
                    parcount+=1
            
    def addparticipant(self,par,slotindex):
        if(len(self.participants[slotindex]) < self.length):
            print(self.participants[slotindex])
            self.participants[slotindex].append(par)
        else:
            raise ValueError('Full!')

class schedule(advisor,startup):
    def __init__(self,advisorno,startupno,timeslotno,cap):
        self.advisorno = advisorno
        self.startupno = startupno
        self.timeslotno = timeslotno
        self.cap = cap
    def intlist(self,minv,maxv):
        l = []
        for i in range(minv,maxv+1):
            l.append(i)
        return(l)

    def Diff(self,li1, li2): 
        new = []

        for l in li1:
            if l not in li2:
                new.append(l)
        return(new)
    
    def buildschdule(self,advisor,startup,pd):
        advisors = advisor.amanufacturer(self.advisorno,self.timeslotno)
        startups = startup.smanufacturer(self.startupno,self.timeslotno)
        prefs = []
        prefs2 = []
        for i in range(0,len(advisors)):
            rand = random.randint(1, self.startupno)
            advisors[i].generatepreferences(startups, rand)
            prefs.extend(advisors[i].preferences)
            for pref in advisors[i].preferences:
                prefs2.append((pref,pref.name,advisors[i].name,advisors[i]))
        advisorpreferences = pd.DataFrame(prefs2)
        advisorpreferences.columns = ['Startup','SName','AName','Advisor']

        from collections import Counter
        import pandas as pd
        #Organize startups
        df = pd.DataFrame.from_dict(Counter(prefs), orient='index').reset_index()
        df.columns = ['Startup','Count']
        df = df.sort_values(ascending=False,by='Count').reset_index(drop=True)
        df['SName'] = [startup.name for startup in df['Startup']]

        alltimeslots = [startup.timeslots for startup in df['Startup']]
        allpars = [slots.participants for slots in alltimeslots]

        aprefs=[]
        for advisor in advisors:
            aprefs.append((advisor,len(advisor.preferences)))

        aprefs = pd.DataFrame(aprefs)
        aprefs.columns=['Advisor','Count']
        aprefs = aprefs.sort_values(ascending=False,by='Count').reset_index(drop=True)

        dcols = self.intlist(0,self.timeslotno)
        length = self.cap
        for advisor in aprefs['Advisor']:
            sortedprefs = pd.DataFrame([(pref.name,pref) for pref in advisor.preferences])
            sortedprefs.columns = ['SName','Startup']
            sortedprefs = pd.merge(sortedprefs,df,on='SName',how='left').sort_values(ascending=False,by='Count')
            advisor.preferences = list(sortedprefs['Startup_x'])
            tables = [int(startup.name[1]) for startup in advisor.preferences]
            print(tables)
            print(advisor.name)
            #Check for available spots and insert advisor into startup time slot
            for table in tables:
                takencolindex = []
                for i in range(0,len(allpars)): 
                    for j in range(0,len(allpars[i])):
                        if (advisor.name in allpars[i][j]):
                            takencolindex.append(j)

                #Get available advisor columns
                advisoravail = self.Diff(dcols,takencolindex)
                #Get the best/earliest one
                advisoravail.sort()
                print(takencolindex)
                print(advisoravail)

                #Put the first table as advisors best
                index = 0
                lengths = []
                #if the current slot we are putting the advisor in is larger than the length, put them in the next smallest
                #available slot
                for i in range(0,len(advisoravail)):
                    if(i == len(advisoravail)-1 or index >= len(advisoravail)-1):
                        index = index-1
                        break
                        print("impossible")
                    print('Index: ' + str(index))
                    print('Table: ' + str(table))
                    tablepars = len(allpars[table][advisoravail[index]])
                    if (tablepars> length):
                        index+=1
                        lengths.append(tablepars)
                    else:
                        break

                        

                allpars[table][advisoravail[index]]=allpars[table][advisoravail[index]]+[advisor.name]
        return(pd.DataFrame(allpars))

    def dbuildschdule(self,advisor,startup,pd):
        advisors = advisor.amanufacturer(self.advisorno,self.timeslotno)
        startups = startup.smanufacturer(self.startupno,self.timeslotno)
        prefs = []
        prefs2 = []
        for i in range(0,len(advisors)):
            rand = random.randint(1, self.startupno)
            advisors[i].generatedprefs(startups)
            prefs.extend(advisors[i].preferences)
            for pref in advisors[i].preferences:
                prefs2.append((pref,pref.name,advisors[i].name,advisors[i]))
        advisorpreferences = pd.DataFrame(prefs2)
        advisorpreferences.columns = ['Startup','SName','AName','Advisor']

        from collections import Counter
        import pandas as pd
        #Organize startups
        df = pd.DataFrame.from_dict(Counter(prefs), orient='index').reset_index()
        df.columns = ['Startup','Count']
        df = df.sort_values(ascending=False,by='Count').reset_index(drop=True)
        df['SName'] = [startup.name for startup in df['Startup']]

        alltimeslots = [startup.timeslots for startup in df['Startup']]
        allpars = [slots.participants for slots in alltimeslots]

        aprefs=[]
        for advisor in advisors:
            aprefs.append((advisor,len(advisor.preferences)))

        aprefs = pd.DataFrame(aprefs)
        aprefs.columns=['Advisor','Count']
        aprefs = aprefs.sort_values(ascending=False,by='Count').reset_index(drop=True)

        dcols = self.intlist(0,self.timeslotno)
        length = self.cap
        for advisor in aprefs['Advisor']:
            sortedprefs = pd.DataFrame([(pref.name,pref) for pref in advisor.preferences])
            sortedprefs.columns = ['SName','Startup']
            sortedprefs = pd.merge(sortedprefs,df,on='SName',how='left').sort_values(ascending=False,by='Count')
            advisor.preferences = list(sortedprefs['Startup_x'])
            tables = [int(startup.name[1]) for startup in advisor.preferences]
            print(tables)
            print(advisor.name)
            #Check for available spots and insert advisor into startup time slot
            for table in tables:
                takencolindex = []
                for i in range(0,len(allpars)): 
                    for j in range(0,len(allpars[i])):
                        if (advisor.name in allpars[i][j]):
                            takencolindex.append(j)

                #Get available advisor columns
                advisoravail = self.Diff(dcols,takencolindex)
                #Get the best/earliest one
                advisoravail.sort()
                print(takencolindex)
                print(advisoravail)

                #Put the first table as advisors best
                index = 0
                lengths = []
                #if the current slot we are putting the advisor in is larger than the length, put them in the next smallest
                #available slot
                for i in range(0,len(advisoravail)):
                    if(i == len(advisoravail)-1 or index >= len(advisoravail)-1):
                        index = index-1
                        break
                        print("impossible")
                    print('Index: ' + str(index))
                    print('Table: ' + str(table))
                    tablepars = len(allpars[table][advisoravail[index]])
                    if (tablepars> length):
                        index+=1
                        lengths.append(tablepars)
                    else:
                        break



                allpars[table][advisoravail[index]]=allpars[table][advisoravail[index]]+[advisor.name]
        return(pd.DataFrame(allpars))


