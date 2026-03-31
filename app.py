from resume_reader import extract_text_from_pdf, clean_text
from job_description import extract_skills_from_jd
from skill_matcher import match_skills
from score_calculator import calculate_score
from suggestions import give_suggestions

file = "sample_resume.pdf"

# Resume
resume_text = extract_text_from_pdf(file)
resume_text = clean_text(resume_text)

# Job Description
jd = """
We are looking for a candidate with Python, SQL and Machine Learning skills.
Knowledge of Git and GitHub is required.
"""

job_skills = extract_skills_from_jd(jd)

# Matching
matched, missing = match_skills(resume_text, job_skills)

# Score
score = calculate_score(matched, len(job_skills))

# Suggestions
suggestions = give_suggestions(missing)

print("Matched Skills:", matched)
print("Missing Skills:", missing)
print("Resume Score:", score)

print("\nSuggestions:")
for s in suggestions:
    print("-", s)