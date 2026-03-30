from resume_reader import extract_text_from_pdf, clean_text

file = "sample_resume.pdf"

text = extract_text_from_pdf(file)
cleaned_text = clean_text(text)

print("RAW TEXT:\n")
print(text[:500])

print("\nCLEANED TEXT:\n")
print(cleaned_text[:500])