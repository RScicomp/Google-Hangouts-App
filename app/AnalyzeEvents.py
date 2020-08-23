import pandas as pd
from difflib import SequenceMatcher

def combined(companies,pros,cons,score,partner,verticals):
    l = []
    for company,pro,con,score,partner,vertical in zip(companies,pros,cons,score,partner,verticals):
        l.append(company + ": "+ vertical + "\nPros: "+pro + "\nCons: "+con+"\nScore: "+score+"\nPartner: "+partner)
    return(l)

def convertstr(l):
    return(list(map(str,l)))

def toExcel(df, name):
    writer = pd.ExcelWriter(name+'.xlsx')
    df.to_excel(writer,'Sheet1')
    
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def compare(correct,incorrect):
    for i in range(0,len(incorrect)):
        for c in correct:
            similarity = similar(str(c),str(incorrect[i]))
            if (similarity >.91 and similarity < 1):
                if(similarity < .95):
                    print(incorrect[i] + str(i)+ "    " +c + str(similarity))
                incorrect[i] = c
                
                
    return(incorrect)

def getallreviews(output19):
    reviewers19 = list(set(output19['What is your e-mail?']))
    allreviews = []
    for reviewer in reviewers19:
        reviewed = output19[output19['What is your e-mail?']==reviewer]
        pros = list(map(str,list(reviewed['Pros'])))
        cons = list(map(str,list(reviewed['Cons'])))
        companies = convertstr(list(reviewed['What company did you review?']))
        score = convertstr(list(reviewed['Would you "Partner" with this company. ']))
        partner = convertstr(list(reviewed['What milestone does this company need to be reach for you to actually partner with them?']))
        verticals = convertstr(list(reviewed['Company Verticals 1']))
        try:
            averageprolen = sum(map(len, pros) ) / len(pros)
        except: 
            averageprolen = 0
        try: 
            averageconlen = sum(map(len, cons) ) / len(cons)
        except: 
            averageconlen = 0 
        try:
            averagepartnerlen = sum(map(len, partner) ) / len(partner)
        except: 
            averagepartnerlen = 0 
        try:
            avgscore = sum(reviewed['Would you "Partner" with this company. '])/len(reviewed['Would you "Partner" with this company. '])
        except:
            avgscore = None
        comb = combined(companies,pros,cons,score,partner,verticals)
        reviewed = len(reviewed)
        allreviews.append((reviewer,"\n\n".join(comb),averageprolen,averageconlen,averagepartnerlen,reviewed,avgscore))
    return(allreviews)

def getallreviews19(output19):
    reviewers19 = list(set(output19['What is your e-mail?']))
    allreviews = []
    for reviewer in reviewers19:
        reviewed = output19[output19['What is your e-mail?']==reviewer]
        pros = list(map(str,list(reviewed['Pros'])))
        cons = list(map(str,list(reviewed['Cons'])))
        companies = convertstr(list(reviewed['What company did you review?']))
        score = convertstr(list(reviewed['Would you "Partner" with this company. ']))
        partner = convertstr(list(reviewed['What milestone does this company need to be reach for you to actually partner with them?']))
        verticals = convertstr(list(reviewed['Company Verticals 1']))
        try:
            averageprolen = sum(map(len, pros) ) / len(pros)
        except: 
            averageprolen = 0
        try: 
            averageconlen = sum(map(len, cons) ) / len(cons)
        except: 
            averageconlen = 0 
        try:
            averagepartnerlen = sum(map(len, partner) ) / len(partner)
        except: 
            averagepartnerlen = 0 
        try:
            avgscore = sum(reviewed['Would you "Partner" with this company. '])/len(reviewed['Would you "Partner" with this company. '])
        except:
            avgscore = None
        comb = combined(companies,pros,cons,score,partner,verticals)
        reviewed = len(reviewed)
        allreviews.append((reviewer,"\n\n".join(comb),averageprolen,averageconlen,averagepartnerlen,reviewed,avgscore))
    sel19= pd.DataFrame(allreviews)
    sel19.columns = ['Email','Reviews S19','Avg Pro length S19', 'Avg Con length S19', 'Avg Partner length S19','# Reviewed S19', 'Avg Score S19']

    return(sel19)

def getallreviews18(output18):
    reviewers18 = list(set(output18['What is your e-mail?']))
    allreviews18 = []
    for reviewer in reviewers18:
        reviewed = output18[output18['What is your e-mail?']==reviewer]
        pros = list(map(str,list(reviewed['Pros'])))
        cons = list(map(str,list(reviewed['Cons'])))
        companies = convertstr(list(reviewed['What company did you review?']))
        score = convertstr(list(reviewed['Would you "Partner" with this company. ']))
        partner = convertstr(list(reviewed['What milestone does this company need to be reach for you to actually partner with them?']))
        verticals = convertstr(list(reviewed['Company Verticals 1']))
        try:
            averageprolen = sum(map(len, pros) ) / len(pros)
        except: 
            averageprolen = 0
        try: 
            averageconlen = sum(map(len, cons) ) / len(cons)
        except: 
            averageconlen = 0 
        try:
            averagepartnerlen = sum(map(len, partner) ) / len(partner)
        except: 
            averagepartnerlen = 0 
        try:
            avgscore = sum(reviewed['Would you "Partner" with this company. '])/len(reviewed['Would you "Partner" with this company. '])
        except:
            avgscore = None
        comb = combined(companies,pros,cons,score,partner,verticals)
        reviewed = len(reviewed)
        comb = "\n\n".join(comb)
        allreviews18.append((reviewer,comb,averageprolen,averageconlen,averagepartnerlen,reviewed,avgscore))
    sel18= pd.DataFrame(allreviews18)
    sel18.columns = ['Email','Reviews S18','Avg Pro length S18', 'Avg Con length S18', 'Avg Partnere length S18','# Reviewed S18', 'Avg Score S18']
    return(sel18)

def getallreviewsdd(dd19):
    reviewers19 = list(set(dd19['What is your e-mail?']))
    allreviewsdd19 = []
    for reviewer in reviewers19:
        reviewed = dd19[dd19['What is your e-mail?']==reviewer]
        pros = list(map(str,list(reviewed['Pros'])))
        cons = list(map(str,list(reviewed['Cons'])))
        companies = convertstr(list(reviewed['What company did you review?']))
        score = convertstr(list(reviewed['Would you "Partner" with this company.']))
        partner = convertstr(list(reviewed['What milestone does this company need to reach for you to actually partner with them?']))
        verticals = convertstr(list(reviewed['Company Verticals 1']))
        try:
            averageprolen = sum(map(len, pros) ) / len(pros)
        except: 
            averageprolen = 0
        try: 
            averageconlen = sum(map(len, cons) ) / len(cons)
        except: 
            averageconlen = 0 
        try:
            averagepartnerlen = sum(map(len, partner) ) / len(partner)
        except: 
            averagepartnerlen = 0 
        try:
            avgscore = sum(reviewed['Would you "Partner" with this company.'])/len(reviewed['Would you "Partner" with this company.'])
        except:
            avgscore = None
        comb = combined(companies,pros,cons,score,partner,verticals)
        reviewed = len(reviewed)
        allreviewsdd19.append((reviewer,"\n\n".join(comb),averageprolen,averageconlen,averagepartnerlen,reviewed,avgscore))

    dd19= pd.DataFrame(allreviewsdd19)
    dd19.columns = ['Email','Reviews DD19','Avg Pro length DD19', 'Avg Con length DD19', 'Avg Partnere length DD19','# Reviewed DD19', 'Avg Score DD19']
    return(dd19)