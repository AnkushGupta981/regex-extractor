import re

#1. Read File
with open("sample_input.txt","r") as file:
  content = file.read()

#2. Define email regex pattern
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

#3. Extract emails
emails = re.findall(pattern,content)

#4. Remove duplicates
unique_emails = list(set(emails))

#5. Save to new file
with open("extracted_emails.txt","w") as output:
  for email in unique_emails:
    output.write(email + "\n")

#6.Print summary
print("Total Emails Found:", len(emails))
print("Unique Emails:", len(unique_emails))