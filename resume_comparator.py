def compare_resumes(score1, score2):

    if score1 > score2:
        return "Resume 1 is better"
    
    elif score2 > score1:
        return "Resume 2 is better"
    
    else:
        return "Both resumes are equal"