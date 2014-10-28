def computegrade(score):
    try:
        if score>=0.0 and score<=1.0 :
            if score>=0.9:
                grade='A'
            elif score>=0.8:
                grade='B'
            elif score>=0.7:
                grade='C'
            elif score>=0.6:
                grade='D'
            elif score<0.6:
                grade='F'
        else :
            grade='Bad score'
           
    except:
        print'Bad score'  
    return grade

G1=computegrade(0.95)
print G1
G2=computegrade('perfect')
print G2
G3=computegrade(10.0)
print G3
G4=computegrade(0.75)
print G4
G5=computegrade(0.5)
print G5