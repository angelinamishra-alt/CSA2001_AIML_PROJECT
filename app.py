import streamlit as st

from resume_reader import extract_text_from_pdf, clean_text
from job_description import extract_skills_from_jd
from skill_matcher import match_skills
from score_calculator import calculate_score
from suggestions import give_suggestions
from resume_comparator import compare_resumes

st.title("ATS Resume Analyzer")

# ---------------- SINGLE RESUME ----------------
st.header("Analyze Resume")

resume_file = st.file_uploader("Upload Resume", type=["pdf"])
jd = st.text_area("Enter Job Description")

if st.button("Analyze Resume"):

    if resume_file is not None and jd != "":

        # save uploaded file
        with open("temp.pdf", "wb") as f:
            f.write(resume_file.read())

        # process resume
        resume_text = extract_text_from_pdf("temp.pdf")
        resume_text = clean_text(resume_text)

        # process job description
        job_skills = extract_skills_from_jd(jd)

        # match skills
        matched, missing = match_skills(resume_text, job_skills)

        # calculate score
        score = calculate_score(matched, len(job_skills))

        # suggestions
        suggestions = give_suggestions(missing)

        # output
        st.subheader("Results")
        st.write("Score:", score)
        st.write("Matched Skills:", matched)
        st.write("Missing Skills:", missing)

        st.subheader("Suggestions")
        for s in suggestions:
            st.write("-", s)

# ---------------- COMPARISON ----------------
st.header("Compare Two Resumes")

file1 = st.file_uploader("Upload Resume 1", type=["pdf"], key="1")
file2 = st.file_uploader("Upload Resume 2", type=["pdf"], key="2")

if st.button("Compare Resumes"):

    if file1 and file2 and jd != "":

        # save files
        with open("r1.pdf", "wb") as f:
            f.write(file1.read())

        with open("r2.pdf", "wb") as f:
            f.write(file2.read())

        # process resumes
        r1 = clean_text(extract_text_from_pdf("r1.pdf"))
        r2 = clean_text(extract_text_from_pdf("r2.pdf"))

        job_skills = extract_skills_from_jd(jd)

        # match + score
        m1, _ = match_skills(r1, job_skills)
        m2, _ = match_skills(r2, job_skills)

        s1 = calculate_score(m1, len(job_skills))
        s2 = calculate_score(m2, len(job_skills))

        result = compare_resumes(s1, s2)

        # output
        st.write("Resume 1 Score:", s1)
        st.write("Resume 2 Score:", s2)
        st.write("Result:", result)