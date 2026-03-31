NAME- ANGELINA MISHRA
REGISTRATION NO- 25BCE10663


ATS RESUME ANALYZER
LIVE DEMO- https://resume-analyzer-bv3tjwsnnusptdmszrgjq3.streamlit.app/

PROJECT OVERVIEW:
This project is a simple ATS (Applicant Tracking System) 
Resume Analyzer built using Python. It helps users check 
how well their resume matches a given job description.
The application extracts text from a resume, compares it 
with the job requirements, and provides a match score 
along with suggestions for improvement.
It is designed to simulate how real ATS systems filter 
resumes based on skills and keywords.


FEATURES:

1: Upload resume in PDF format

2: Enter job description manually

3: Extracts important skills from job description

4: Matches resume skills with job requirements

5: Generates a match score

6: Highlights matched and missing skills

7: Provides suggestions to improve the resume

8: Compare two resumes for the same job role



HOW IT WORKS:

1: The user uploads a resume (PDF file)

2: The user enters a job description

3: The system extracts text from the resume

4: Skills are identified from the job description

5: The resume is compared with required skills

6: A score is calculated based on matching skills

7: Suggestions are generated for missing skills



TECHNOLOGIES USED:

Python

Streamlit (for UI)

pdfplumber (for extracting text from PDF)



HOW TO RUN LOCALLY:

1: Clone the repository

2: Install required libraries
   pip install -r requirements.txt
   Run the application

3: streamlit run app.py

4: Open the link shown in terminal


EXAMPLE USE CASE:

A student applying for a data analyst role can paste 
the job description and upload their resume. The system 
will show how well the resume matches the role and 
suggest missing skills such as Python, SQL, or data visualization.


LIMITATIONS:

1: Skill extraction is keyword-based and not fully intelligent

2: Does not understand context deeply

3: Works best with clear and structured resumes



FUTURE IMPROVEMENTS:

1: Use NLP for better skill extraction

2: Add support for multiple file formats

3: Improve scoring logic

4: Add resume formatting suggestions



CONCLUSION:

This project demonstrates a basic implementation of 
how resume screening systems work. It is useful for 
understanding text processing, skill matching, and 
building simple web applications using Python.