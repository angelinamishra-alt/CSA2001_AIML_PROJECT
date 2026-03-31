def give_suggestions(missing_skills, score):

    suggestions = []

    if score == 0:
        suggestions.append("Your resume does not match the job requirements at all. Try adding relevant skills.")

    else:
        for skill in missing_skills:
            suggestions.append("Try to add " + skill + " in your resume")

    if score > 80:
        suggestions.append("Your resume is good!")

    return suggestions