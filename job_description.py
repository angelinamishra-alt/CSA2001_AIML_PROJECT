def extract_skills_from_jd(jd_text):

    # convert to lowercase
    jd_text = jd_text.lower()

    # list of common skills
    skills_list = [
        "python", "java", "c++", "sql", "machine learning",
        "data analysis", "html", "css", "javascript",
        "react", "node", "git", "github", "excel"
    ]

    found_skills = []

    # check each skill
    for skill in skills_list:
        if skill in jd_text:
            found_skills.append(skill)

    return found_skills