from resume_reader import extract_text_from_pdf, clean_text
from job_description import extract_skills_from_jd
from skill_matcher import match_skills
from score_calculator import calculate_score

file = "sample_resume.pdf"

# Step 1: resume
resume_text = extract_text_from_pdf(file)
resume_text = clean_text(resume_text)

# Step 2: job description
jd = """
We are looking for a candidate with Python, SQL and Machine Learning skills.
Knowledge of Git and GitHub is required.
"""

job_skills = extract_skills_from_jd(jd)

# Step 3: matching
matched, missing = match_skills(resume_text, job_skills)

# Step 4: scoring
score = calculate_score(matched, len(job_skills))

print("Matched Skills:", matched)
print("Missing Skills:", missing)
print("Resume Score:", score)