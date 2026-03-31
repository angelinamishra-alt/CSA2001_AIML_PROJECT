def give_suggestions(missing_skills):

    suggestions = []

    for skill in missing_skills:
        suggestions.append("Try to add " + skill + " in your resume")

    if len(suggestions) == 0:
        suggestions.append("Your resume is good!")

    return suggestions