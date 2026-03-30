def match_skills(resume_text, job_skills):

    matched = []
    missing = []

    for skill in job_skills:
        if skill in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    return matched, missing