from job_description import extract_skills_from_jd

jd = """
We are looking for a candidate with Python, SQL and Machine Learning skills.
Knowledge of Git and GitHub is required.
"""

skills = extract_skills_from_jd(jd)

print("Skills found:")
print(skills)