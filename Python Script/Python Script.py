import random
from faker import Faker
from datetime import datetime, timedelta
import math

fake = Faker()
random.seed(42)
Faker.seed(42)

# ---------- Configuration (change if needed) ----------
N_BRANCH = 10
N_TRACK = 30
N_DEPT = 10
N_FACULTY = 10
N_COURSE = 100
N_INSTRUCTOR = 300
N_INTAKE = 20
N_STUDENT = 4000
N_COMPANY = 200
N_EXAM = 400
AVG_Q_PER_EXAM = 15
# results approx rows: N_STUDENT * avg_exams_per_student * avg_q_per_exam
AVG_EXAMS_PER_STUDENT = 5
N_CERT = 3000
N_FREELANCE = 2000

OUT_SQL_FILE = "iti_bigdata.sql"
BATCH_INSERT_SIZE = 500  # number of rows per single INSERT VALUES group

# ---------- Useful lists (Egyptian-style names transliterated) ----------
first_names_m = ["Ahmed","Mohamed","Omar","Khaled","Karim","Youssef","Hassan","Mostafa","Amr","Ibrahim",
                 "Tamer","Mahmoud","Walid","Sami","Fady","Ehab","Hany","Adel","Nader","Sherif"]
first_names_f = ["Fatma","Mona","Salma","Sara","Mariam","Nour","Aya","Rania","Dina","Hend",
                 "Nadia","Eman","Heba","Reem","Noha","Laila","Mai","Nermine","Rana","Sawsan"]
last_names = ["Mohamed","Elsayed","Hassan","Abdelrahman","Ibrahim","Ali","Hassan","Sabry","Fahmy","Elshazly",
              "Gaber","Khalifa","Mahmoud","Samir","Salem","Yacoub","Elgohary","Nabil","Kamel","Lotfy",
              "Gamal","Aly","Khodr","Shalaby","Zaki","Mostafa","Farag","Tawfiq","Suleiman","Badawy",
              "Elmasry","Elbeltagy","Abdalla","Elsherif","Hegazy","Elwakil","Elkomy","Barakat","Hammad","Essa"]

governorates = ['Cairo','Giza','Alexandria','Dakahlia','Sharqia','Gharbia','Menoufia','Ismailia','Sohag','Aswan']

company_samples = ["Valeo Egypt","Orange Egypt","ITIDA Labs","Vodafone Egypt","Etisalat Misr",
                   "IBM Egypt","Dell Egypt","Raya Holding","Sutherland Egypt","Mentor Graphics Egypt"]

course_bases = ["Python Programming","Database Systems","Power BI","Cybersecurity Basics","Web Development",
                "Machine Learning","Cloud Fundamentals","DevOps Essentials","UI/UX Design","Data Structures"]

# ---------- Helper functions ----------
def rand_date(start_year=2020, end_year=2025):
    start = datetime(start_year,1,1)
    end = datetime(end_year,12,31)
    delta = (end - start).days
    return (start + timedelta(days=random.randint(0, delta))).date()

def rand_birth(min_age=20, max_age=30):
    today = datetime.today()
    start = today - timedelta(days=365*max_age)
    end = today - timedelta(days=365*min_age)
    delta = (end - start).days
    return (start + timedelta(days=random.randint(0, delta))).date()

def national_id_from_birth(birth_date):
    # Egyptian-like 14 digits: YYMMDD + 8 random digits
    return birth_date.strftime("%y%m%d") + "".join(str(random.randint(0,9)) for _ in range(8))

def phone_number():
    return random.choice(["010","011","012","015"]) + "".join(str(random.randint(0,9)) for _ in range(8))

def email_from_name(fn, ln, domain="student.iti.local"):
    # lower, replace spaces
    return f"{fn.lower()}.{ln.lower()}@{domain}"

def chunked(iterable, n):
    for i in range(0, len(iterable), n):
        yield iterable[i:i+n]

# ---------- Prepare SQL file and write helper ----------
def write_line(f, s=""):
    f.write(s + "\n")

def escape(s):
    if s is None:
        return "NULL"
    return "'" + str(s).replace("'", "''") + "'"

# ---------- Generate basic metadata entities ----------
# Branches
branches = []
for i in range(1, N_BRANCH+1):
    branches.append({
        "Branch_ID": i,
        "Branch_Name": f"{fake.city()} Branch",
        "Branch_Loc": f"{fake.street_address()}, {random.choice(governorates)}"
    })

# Departments
departments = []
for i in range(1, N_DEPT+1):
    departments.append({"Dept_id": i, "Name": f"Department of {fake.word().capitalize()}"})

# Faculties
faculties = []
unis = ["Cairo University","Ain Shams University","Alexandria University","AUC","Mansoura University"]
for i in range(1, N_FACULTY+1):
    faculties.append({
        "Faculty_ID": i,
        "Faculty_Name": f"Faculty of {fake.word().capitalize()}",
        "University_Name": random.choice(unis),
        "city": random.choice(governorates)
    })

# Tracks
tracks = []
for i in range(1, N_TRACK+1):
    tracks.append({
        "Track_ID": i,
        "Track_Name": f"{random.choice(['FullStack','DataScience','Cloud','Cybersecurity','AI','UIUX'])} Track {i}",
        "Description": fake.sentence(nb_words=8),
        "supervisor_instruct": None,  # assign later
        "Dept_id": random.randint(1,N_DEPT)
    })

# Intake
intakes = []
for i in range(1, N_INTAKE+1):
    s = rand_date(2020,2024)
    e = s + timedelta(days=random.randint(60,240))
    intakes.append({"id": i, "Start_date": s, "End_date": e, "Type": random.choice(["Full-time","Evening","Part-time"])})

# Courses
courses = []
for i in range(1, N_COURSE+1):
    base = random.choice(course_bases)
    courses.append({
        "Crs_ID": i,
        "Crs_Name": f"{base} {i}",
        "Description": fake.sentence(nb_words=10),
        "Hours": random.choice([30,40,50,60,80]),
        "Dept_id": random.randint(1,N_DEPT)
    })

# Companies
companies = []
for i in range(1, N_COMPANY+1):
    name = random.choice(company_samples) + ("" if i<=len(company_samples) else f" {i}")
    companies.append({"company_id": i, "name": name, "city": random.choice(governorates)})

# Instructors
instructors = []
for i in range(1, N_INSTRUCTOR+1):
    gender = random.choice(["M","F"])
    fn = random.choice(first_names_m) if gender=="M" else random.choice(first_names_f)
    ln = random.choice(last_names)
    hire = rand_date(2010,2024)
    instructors.append({
        "Instructor_ID": i,
        "First_Name": fn,
        "Last_Name": ln,
        "Gender": gender,
        "Email": f"{fn.lower()}.{ln.lower()}@iti.edu.eg",
        "Phone": phone_number(),
        "Hire_Date": hire,
        "salary": round(random.uniform(8000,35000),2),
        "Dept_id": random.randint(1,N_DEPT),
        "user_id": f"instr{i}",
        "Password": fake.password(length=10),
        "city": random.choice(governorates),
        "working_status": random.choice(["Full-time","Part-time","Visiting"])
    })

# assign supervisors randomly to tracks
for t in tracks:
    t["supervisor_instruct"] = random.randint(1, N_INSTRUCTOR)

# Instructor_Branch mapping
instr_branch = []
for instr in instructors:
    n = random.randint(1,3)
    brs = random.sample(range(1,N_BRANCH+1), n)
    for b in brs:
        instr_branch.append({"Instructor_ID": instr["Instructor_ID"], "Branch_ID": b})

# Teach & instructor_crs (map courses to instructors)
teach = []
instr_crs = []
for crs in courses:
    n = random.randint(1,4)
    insts = random.sample(range(1,N_INSTRUCTOR+1), n)
    for inst in insts:
        teach.append({"Instructor_id": inst, "Crs_ID": crs["Crs_ID"]})
        instr_crs.append({"Crs_ID": crs["Crs_ID"], "Instructor_ID": inst})

# crs_track mapping
crs_track = []
for c in courses:
    n = random.randint(1,3)
    tks = random.sample(range(1,N_TRACK+1), n)
    for tk in tks:
        crs_track.append({"Track_ID": tk, "Crs_ID": c["Crs_ID"]})

# Track_Branch_Intake
track_branch_intake = []
for t in range(1,N_TRACK+1):
    brs = random.sample(range(1,N_BRANCH+1), random.randint(1,3))
    its = random.sample(range(1,N_INTAKE+1), random.randint(1,3))
    for b in brs:
        for it in its:
            track_branch_intake.append({"Branch_ID": b, "intake_id": it, "Track_ID": t})

# Students
students = []
phone_students = []
for i in range(1, N_STUDENT+1):
    gender = random.choice(["M","F"])
    fn = random.choice(first_names_m) if gender=="M" else random.choice(first_names_f)
    ln = random.choice(last_names)
    bd = rand_birth(20,30)
    nid = national_id_from_birth(bd)
    branch_id = random.randint(1,N_BRANCH)
    track_id = random.randint(1,N_TRACK)
    faculty_id = random.randint(1,N_FACULTY)
    intake_id = random.randint(1,N_INTAKE)
    company_id = random.choice([None] + list(range(1,N_COMPANY+1)))
    gpa = round(random.uniform(2.0,4.0),2)
    grad = random.choice(["Graduated","Studying","Dropped"])
    students.append({
        "Student_ID": i,
        "Student_First_Name": fn,
        "Student_Last_Name": ln,
        "Gender": gender,
        "Birth_date": bd,
        "Email": email_from_name(fn, ln),
        "National_ID": nid,
        "governorate": random.choice(governorates),
        "Gpa": gpa,
        "Graduation_Status": grad,
        "Branch_ID": branch_id,
        "Track_ID": track_id,
        "Faculty_ID": faculty_id,
        "intack_id": intake_id,
        "company_id": company_id,
        "user_id": f"stud{i}",
        "Password": fake.password(length=10),
        "student_url": f"https://iti.example.com/students/{i}"
    })
    # 1-2 phones
    for _ in range(random.choice([1,1,2])):
        phone_students.append({"Student_ID": i, "Phone": phone_number()})

# Exams
exams = []
for i in range(1, N_EXAM+1):
    crs = random.randint(1,N_COURSE)
    # pick instructor who teaches this course if possible
    insts = [t["Instructor_id"] for t in teach if t["Crs_ID"]==crs]
    inst_id = random.choice(insts) if insts else random.randint(1,N_INSTRUCTOR)
    exam_date = rand_date(2020,2025)
    exams.append({
        "Exam_ID": i,
        "Exam_Name": f"{random.choice(['Midterm','Final','Quiz'])} - Course {crs}",
        "Exam_Type": random.choice(["Written","Practical","Online"]),
        "Exam_Date": exam_date,
        "Duration": random.choice([60,90,120]),
        "Total_degree": 100,
        "Crs_ID": crs,
        "No_question": AVG_Q_PER_EXAM,
        "instructor_id": inst_id
    })

# Questions
questions = []
question_id = 1
for ex in exams:
    nq = random.randint(max(5, AVG_Q_PER_EXAM-4), AVG_Q_PER_EXAM+4)
    for _ in range(nq):
        qtype = random.choice(["MCQ","TrueFalse","Short","Essay"])
        difficulty = random.choice(["Easy","Medium","Hard"])
        marks = random.choice([1,2,3,4,5])
        correct = ""
        if qtype=="MCQ":
            correct = random.choice(["A","B","C","D"])
        elif qtype=="TrueFalse":
            correct = random.choice(["True","False"])
        topic = fake.word().capitalize()
        questions.append({
            "Question_ID": question_id,
            "Exam_ID": ex["Exam_ID"],
            "Question_Type": qtype,
            "Question_Difficulty": difficulty,
            "Marks": marks,
            "Correct_Answer": correct,
            "Crs_id": ex["Crs_ID"],
            "question_topic": topic
        })
        question_id += 1

# Question choices for MCQs
question_choices = []
for q in questions:
    if q["Question_Type"]=="MCQ":
        question_choices.append({
            "Question_ID": q["Question_ID"],
            "choices_id": q["Question_ID"],
            "A": fake.sentence(nb_words=5),
            "B": fake.sentence(nb_words=5),
            "C": fake.sentence(nb_words=5),
            "D": fake.sentence(nb_words=5)
        })

# Exam_Question mapping (redundant since Question has Exam_ID)
# Results generation (this can be very large)
results = []
# We'll not keep all in memory as a list to avoid explosion; we'll stream writing results to SQL directly later.

# Certificates
certs = []
for i in range(1, N_CERT+1):
    st = random.randint(1, N_STUDENT)
    certs.append({
        "Certificate_ID": i,
        "Name": f"ITI Diploma - {random.choice([t['Track_Name'] for t in tracks])}",
        "platform": random.choice(["ITI","Coursera","Udemy","LinkedIn"]),
        "duration": random.choice([40,60,80,100]),
        "issued_date": rand_date(2020,2025),
        "level": random.choice(["Beginner","Intermediate","Advanced"]),
        "student_id": st
    })

# Freelance
freelances = []
for i in range(1, N_FREELANCE+1):
    frel_st = random.randint(1, N_STUDENT)
    freelances.append({
        "freelance_id": i,
        "platform": random.choice(["Upwork","Freelancer","Fiverr","Local"]),
        "payment": round(random.uniform(1000,30000),2),
        "revenue": round(random.uniform(500,20000),2),
        "duration": random.choice([7,14,30,60]),
        "client_country": random.choice(["Egypt","UAE","KSA","USA","UK"]),
        "Date": rand_date(2020,2025),
        "Rating": random.randint(1,5),
        "student_id": frel_st
    })

# Topic table derived from questions
topics = []
for q in questions:
    topics.append({"topic_id": q["Question_ID"], "topic_name": q["question_topic"], "crs_id": q["Crs_id"]})

# --------- Write SQL file ----------
print(f"Writing SQL to {OUT_SQL_FILE} ...")
with open(OUT_SQL_FILE, "w", encoding="utf-8") as f:
    # header
    write_line(f, "-- ITI Examination System large dataset SQL (generated)")
    write_line(f, f"-- Generated on: {datetime.now().isoformat()}")
    write_line(f, "SET NOCOUNT ON;")
    write_line(f, "")

    # CREATE TABLE statements (T-SQL)
    write_line(f, "-- CREATE TABLES")
    write_line(f, "CREATE TABLE Branch (Branch_ID INT IDENTITY(1,1) PRIMARY KEY, Branch_Name NVARCHAR(100) NOT NULL, Branch_Loc NVARCHAR(150) NOT NULL);")
    write_line(f, "CREATE TABLE Department (Dept_id INT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(150) NOT NULL);")
    write_line(f, "CREATE TABLE Faculty (Faculty_ID INT IDENTITY(1,1) PRIMARY KEY, Faculty_Name NVARCHAR(150), University_Name NVARCHAR(150), city NVARCHAR(100));")
    write_line(f, "CREATE TABLE Track (Track_ID INT IDENTITY(1,1) PRIMARY KEY, Track_Name NVARCHAR(150) NOT NULL, Description NVARCHAR(250), supervisor_instruct INT NULL, Dept_id INT NULL);")
    write_line(f, "CREATE TABLE Intake (id INT IDENTITY(1,1) PRIMARY KEY, Start_date DATE, End_date DATE, Type NVARCHAR(50));")
    write_line(f, "CREATE TABLE Course (Crs_ID INT IDENTITY(1,1) PRIMARY KEY, Crs_Name NVARCHAR(150) NOT NULL, Description NVARCHAR(250), Hours INT, Dept_id INT);")
    write_line(f, "CREATE TABLE Instructor (Instructor_ID INT IDENTITY(1,1) PRIMARY KEY, First_Name NVARCHAR(50), Last_Name NVARCHAR(50), Gender CHAR(1), Email NVARCHAR(100) UNIQUE, Phone NVARCHAR(20), Hire_Date DATE, salary DECIMAL(12,2), Dept_id INT, user_id NVARCHAR(50), Password NVARCHAR(100), city NVARCHAR(100), working_status NVARCHAR(50));")
    write_line(f, "CREATE TABLE Instructor_Branch (Instructor_ID INT, Branch_ID INT, PRIMARY KEY (Instructor_ID, Branch_ID));")
    write_line(f, "CREATE TABLE Student (Student_ID INT IDENTITY(1,1) PRIMARY KEY, Student_First_Name NVARCHAR(50), Student_Last_Name NVARCHAR(50), Gender CHAR(1), Birth_date DATE, Email NVARCHAR(100), National_ID VARCHAR(14) UNIQUE, governorate NVARCHAR(50), Gpa DECIMAL(3,2), Graduation_Status NVARCHAR(50), Branch_ID INT, Track_ID INT, Faculty_ID INT, intack_id INT, company_id INT NULL, user_id NVARCHAR(50), Password NVARCHAR(100), student_url NVARCHAR(250));")
    write_line(f, "CREATE TABLE Phone_Student (Student_ID INT, Phone NVARCHAR(20), PRIMARY KEY (Student_ID, Phone));")
    write_line(f, "CREATE TABLE Teach (Instructor_id INT, Crs_ID INT, PRIMARY KEY (Instructor_id, Crs_ID));")
    write_line(f, "CREATE TABLE Crs_Track (Track_ID INT, Crs_ID INT, PRIMARY KEY (Track_ID, Crs_ID));")
    write_line(f, "CREATE TABLE Instructor_Crs (Crs_ID INT, Instructor_ID INT, PRIMARY KEY (Crs_ID, Instructor_ID));")
    write_line(f, "CREATE TABLE Company (company_id INT IDENTITY(1,1) PRIMARY KEY, name NVARCHAR(150), city NVARCHAR(100));")
    write_line(f, "CREATE TABLE Exam (Exam_ID INT IDENTITY(1,1) PRIMARY KEY, Exam_Name NVARCHAR(200), Exam_Type NVARCHAR(50), Exam_Date DATE, Duration INT, Total_degree INT, Crs_ID INT, No_question INT, instructor_id INT);")
    write_line(f, "CREATE TABLE Question (Question_ID INT PRIMARY KEY, Exam_ID INT, Question_Type NVARCHAR(50), Question_Difficulty NVARCHAR(20), Marks INT, Correct_Answer NVARCHAR(50), Crs_id INT, question_topic NVARCHAR(100));")
    write_line(f, "CREATE TABLE Question_Choices (Question_ID INT, choices_id INT, A NVARCHAR(500), B NVARCHAR(500), C NVARCHAR(500), D NVARCHAR(500), PRIMARY KEY (Question_ID, choices_id));")
    write_line(f, "CREATE TABLE Exam_Question (Question_ID INT, Exam_ID INT, PRIMARY KEY (Question_ID, Exam_ID));")
    write_line(f, "CREATE TABLE Result (student_id INT, Exam_ID INT, questions_id INT, degree DECIMAL(6,2), student_ans NVARCHAR(500), pass BIT, PRIMARY KEY (student_id, Exam_ID, questions_id));")
    write_line(f, "CREATE TABLE Certificate (Certificate_ID INT IDENTITY(1,1) PRIMARY KEY, Name NVARCHAR(200), platform NVARCHAR(100), duration INT, issued_date DATE, level NVARCHAR(50), student_id INT);")
    write_line(f, "CREATE TABLE Freelance (freelance_id INT IDENTITY(1,1) PRIMARY KEY, platform NVARCHAR(100), payment DECIMAL(12,2), revenue DECIMAL(12,2), duration INT, client_country NVARCHAR(100), Date DATE, Rating INT, student_id INT);")
    write_line(f, "CREATE TABLE Topic (topic_id INT PRIMARY KEY, topic_name NVARCHAR(200), crs_id INT);")
    write_line(f, "CREATE TABLE Track_Branch_Intake (Branch_ID INT, intake_id INT, Track_ID INT, PRIMARY KEY (Branch_ID, intake_id, Track_ID));")
    write_line(f, "")

    # Foreign key constraints (add after tables creation)
    write_line(f, "-- FOREIGN KEYS")
    # simple FK additions
    write_line(f, "ALTER TABLE Track ADD CONSTRAINT FK_Track_Dept FOREIGN KEY (Dept_id) REFERENCES Department(Dept_id);")
    write_line(f, "ALTER TABLE Track ADD CONSTRAINT FK_Track_Supervisor FOREIGN KEY (supervisor_instruct) REFERENCES Instructor(Instructor_ID);")
    write_line(f, "ALTER TABLE Course ADD CONSTRAINT FK_Course_Dept FOREIGN KEY (Dept_id) REFERENCES Department(Dept_id);")
    write_line(f, "ALTER TABLE Instructor ADD CONSTRAINT FK_Instr_Dept FOREIGN KEY (Dept_id) REFERENCES Department(Dept_id);")
    write_line(f, "ALTER TABLE Student ADD CONSTRAINT FK_Student_Branch FOREIGN KEY (Branch_ID) REFERENCES Branch(Branch_ID);")
    write_line(f, "ALTER TABLE Student ADD CONSTRAINT FK_Student_Track FOREIGN KEY (Track_ID) REFERENCES Track(Track_ID);")
    write_line(f, "ALTER TABLE Student ADD CONSTRAINT FK_Student_Faculty FOREIGN KEY (Faculty_ID) REFERENCES Faculty(Faculty_ID);")
    write_line(f, "ALTER TABLE Student ADD CONSTRAINT FK_Student_Intake FOREIGN KEY (intack_id) REFERENCES Intake(id);")
    write_line(f, "ALTER TABLE Student ADD CONSTRAINT FK_Student_Company FOREIGN KEY (company_id) REFERENCES Company(company_id);")
    write_line(f, "ALTER TABLE Teach ADD CONSTRAINT FK_Teach_Instr FOREIGN KEY (Instructor_id) REFERENCES Instructor(Instructor_ID);")
    write_line(f, "ALTER TABLE Teach ADD CONSTRAINT FK_Teach_Crs FOREIGN KEY (Crs_ID) REFERENCES Course(Crs_ID);")
    write_line(f, "ALTER TABLE Crs_Track ADD CONSTRAINT FK_CrsTrack_Track FOREIGN KEY (Track_ID) REFERENCES Track(Track_ID);")
    write_line(f, "ALTER TABLE Crs_Track ADD CONSTRAINT FK_CrsTrack_Crs FOREIGN KEY (Crs_ID) REFERENCES Course(Crs_ID);")
    write_line(f, "ALTER TABLE Instructor_Branch ADD CONSTRAINT FK_InstrBranch_Instr FOREIGN KEY (Instructor_ID) REFERENCES Instructor(Instructor_ID);")
    write_line(f, "ALTER TABLE Instructor_Branch ADD CONSTRAINT FK_InstrBranch_Branch FOREIGN KEY (Branch_ID) REFERENCES Branch(Branch_ID);")
    write_line(f, "ALTER TABLE Instructor_Crs ADD CONSTRAINT FK_InstrCrs_Crs FOREIGN KEY (Crs_ID) REFERENCES Course(Crs_ID);")
    write_line(f, "ALTER TABLE Instructor_Crs ADD CONSTRAINT FK_InstrCrs_Instr FOREIGN KEY (Instructor_ID) REFERENCES Instructor(Instructor_ID);")
    write_line(f, "ALTER TABLE Exam ADD CONSTRAINT FK_Exam_Crs FOREIGN KEY (Crs_ID) REFERENCES Course(Crs_ID);")
    write_line(f, "ALTER TABLE Exam ADD CONSTRAINT FK_Exam_Instr FOREIGN KEY (instructor_id) REFERENCES Instructor(Instructor_ID);")
    write_line(f, "ALTER TABLE Question ADD CONSTRAINT FK_Question_Exam FOREIGN KEY (Exam_ID) REFERENCES Exam(Exam_ID);")
    write_line(f, "ALTER TABLE Question ADD CONSTRAINT FK_Question_Crs FOREIGN KEY (Crs_id) REFERENCES Course(Crs_ID);")
    write_line(f, "ALTER TABLE Question_Choices ADD CONSTRAINT FK_QChoices_Q FOREIGN KEY (Question_ID) REFERENCES Question(Question_ID);")
    write_line(f, "ALTER TABLE Exam_Question ADD CONSTRAINT FK_ExamQuestion_Q FOREIGN KEY (Question_ID) REFERENCES Question(Question_ID);")
    write_line(f, "ALTER TABLE Exam_Question ADD CONSTRAINT FK_ExamQuestion_Exam FOREIGN KEY (Exam_ID) REFERENCES Exam(Exam_ID);")
    write_line(f, "ALTER TABLE Result ADD CONSTRAINT FK_Result_Student FOREIGN KEY (student_id) REFERENCES Student(Student_ID);")
    write_line(f, "ALTER TABLE Result ADD CONSTRAINT FK_Result_Exam FOREIGN KEY (Exam_ID) REFERENCES Exam(Exam_ID);")
    write_line(f, "ALTER TABLE Result ADD CONSTRAINT FK_Result_Q FOREIGN KEY (questions_id) REFERENCES Question(Question_ID);")
    write_line(f, "ALTER TABLE Certificate ADD CONSTRAINT FK_Cert_Student FOREIGN KEY (student_id) REFERENCES Student(Student_ID);")
    write_line(f, "ALTER TABLE Freelance ADD CONSTRAINT FK_Freelance_Student FOREIGN KEY (student_id) REFERENCES Student(Student_ID);")
    write_line(f, "ALTER TABLE Topic ADD CONSTRAINT FK_Topic_Crs FOREIGN KEY (crs_id) REFERENCES Course(Crs_ID);")
    write_line(f, "ALTER TABLE Track_Branch_Intake ADD CONSTRAINT FK_TBI_Track FOREIGN KEY (Track_ID) REFERENCES Track(Track_ID);")
    write_line(f, "ALTER TABLE Track_Branch_Intake ADD CONSTRAINT FK_TBI_Branch FOREIGN KEY (Branch_ID) REFERENCES Branch(Branch_ID);")
    write_line(f, "ALTER TABLE Track_Branch_Intake ADD CONSTRAINT FK_TBI_Intake FOREIGN KEY (intake_id) REFERENCES Intake(id);")
    write_line(f, "")

    # INSERTS (use IDENTITY_INSERT and explicit ids)
    write_line(f, "/* ---------- INSERT DATA ---------- */")
    write_line(f, "BEGIN TRANSACTION;")
    write_line(f, "")

    # Branch
    write_line(f, "SET IDENTITY_INSERT Branch ON;")
    rows = []
    for b in branches:
        rows.append(f"({b['Branch_ID']}, {escape(b['Branch_Name'])}, {escape(b['Branch_Loc'])})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Branch (Branch_ID, Branch_Name, Branch_Loc) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "SET IDENTITY_INSERT Branch OFF;")
    write_line(f, "")

    # Department
    write_line(f, "SET IDENTITY_INSERT Department ON;")
    rows = []
    for d in departments:
        rows.append(f"({d['Dept_id']}, {escape(d['Name'])})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Department (Dept_id, Name) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "SET IDENTITY_INSERT Department OFF;")
    write_line(f, "")

    # Faculty
    write_line(f, "SET IDENTITY_INSERT Faculty ON;")
    rows = []
    for fac in faculties:
        rows.append(f"({fac['Faculty_ID']}, {escape(fac['Faculty_Name'])}, {escape(fac['University_Name'])}, {escape(fac['city'])})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Faculty (Faculty_ID, Faculty_Name, University_Name, city) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "SET IDENTITY_INSERT Faculty OFF;")
    write_line(f, "")

    # Track
    write_line(f, "SET IDENTITY_INSERT Track ON;")
    rows = []
    for t in tracks:
        sup = t['supervisor_instruct'] if t['supervisor_instruct'] is not None else "NULL"
        rows.append(f"({t['Track_ID']}, {escape(t['Track_Name'])}, {escape(t['Description'])}, {sup}, {t['Dept_id']})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Track (Track_ID, Track_Name, Description, supervisor_instruct, Dept_id) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "SET IDENTITY_INSERT Track OFF;")
    write_line(f, "")

    # Intake
    write_line(f, "SET IDENTITY_INSERT Intake ON;")
    rows = []
    for it in intakes:
        rows.append(f"({it['id']}, {escape(it['Start_date'])}, {escape(it['End_date'])}, {escape(it['Type'])})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Intake (id, Start_date, End_date, Type) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "SET IDENTITY_INSERT Intake OFF;")
    write_line(f, "")

    # Course
    write_line(f, "SET IDENTITY_INSERT Course ON;")
    rows = []
    for c in courses:
        rows.append(f"({c['Crs_ID']}, {escape(c['Crs_Name'])}, {escape(c['Description'])}, {c['Hours']}, {c['Dept_id']})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Course (Crs_ID, Crs_Name, Description, Hours, Dept_id) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "SET IDENTITY_INSERT Course OFF;")
    write_line(f, "")

    # Company
    write_line(f, "SET IDENTITY_INSERT Company ON;")
    rows = []
    for c in companies:
        rows.append(f"({c['company_id']}, {escape(c['name'])}, {escape(c['city'])})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Company (company_id, name, city) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "SET IDENTITY_INSERT Company OFF;")
    write_line(f, "")

    # Instructor
    write_line(f, "SET IDENTITY_INSERT Instructor ON;")
    rows = []
    for ins in instructors:
        rows.append(f"({ins['Instructor_ID']}, {escape(ins['First_Name'])}, {escape(ins['Last_Name'])}, {escape(ins['Gender'])}, {escape(ins['Email'])}, {escape(ins['Phone'])}, {escape(ins['Hire_Date'])}, {ins['salary']}, {ins['Dept_id']}, {escape(ins['user_id'])}, {escape(ins['Password'])}, {escape(ins['city'])}, {escape(ins['working_status'])})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Instructor (Instructor_ID, First_Name, Last_Name, Gender, Email, Phone, Hire_Date, salary, Dept_id, user_id, Password, city, working_status) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "SET IDENTITY_INSERT Instructor OFF;")
    write_line(f, "")

    # Instructor_Branch
    rows = []
    for ib in instr_branch:
        rows.append(f"({ib['Instructor_ID']}, {ib['Branch_ID']})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Instructor_Branch (Instructor_ID, Branch_ID) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "")

    # Teach
    rows = []
    for t in teach:
        rows.append(f"({t['Instructor_id']}, {t['Crs_ID']})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Teach (Instructor_id, Crs_ID) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "")

    # Crs_Track
    rows = []
    for ct in crs_track:
        rows.append(f"({ct['Track_ID']}, {ct['Crs_ID']})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Crs_Track (Track_ID, Crs_ID) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "")

    # Instructor_Crs
    rows = []
    for ic in instr_crs:
        rows.append(f"({ic['Crs_ID']}, {ic['Instructor_ID']})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Instructor_Crs (Crs_ID, Instructor_ID) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "")

    # Student
    write_line(f, "SET IDENTITY_INSERT Student ON;")
    rows = []
    for s in students:
        comp = s['company_id'] if s['company_id'] is not None else "NULL"
        rows.append("(" + ",".join([
            str(s['Student_ID']),
            escape(s['Student_First_Name']),
            escape(s['Student_Last_Name']),
            escape(s['Gender']),
            escape(s['Birth_date']),
            escape(s['Email']),
            escape(s['National_ID']),
            escape(s['governorate']),
            str(s['Gpa']),
            escape(s['Graduation_Status']),
            str(s['Branch_ID']),
            str(s['Track_ID']),
            str(s['Faculty_ID']),
            str(s['intack_id']),
            (str(comp) if comp!="NULL" else "NULL"),
            escape(s['user_id']),
            escape(s['Password']),
            escape(s['student_url'])
        ]) + ")")
    # write in batches to avoid extremely long SQL lines
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Student (Student_ID, Student_First_Name, Student_Last_Name, Gender, Birth_date, Email, National_ID, governorate, Gpa, Graduation_Status, Branch_ID, Track_ID, Faculty_ID, intack_id, company_id, user_id, Password, student_url) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "SET IDENTITY_INSERT Student OFF;")
    write_line(f, "")

    # Phone_Student
    rows = []
    for p in phone_students:
        rows.append(f"({p['Student_ID']}, {escape(p['Phone'])})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Phone_Student (Student_ID, Phone) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "")

    # Exam
    write_line(f, "SET IDENTITY_INSERT Exam ON;")
    rows = []
    for e in exams:
        rows.append("(" + ",".join([
            str(e['Exam_ID']),
            escape(e['Exam_Name']),
            escape(e['Exam_Type']),
            escape(e['Exam_Date']),
            str(e['Duration']),
            str(e['Total_degree']),
            str(e['Crs_ID']),
            str(e['No_question']),
            str(e['instructor_id'])
        ]) + ")")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Exam (Exam_ID, Exam_Name, Exam_Type, Exam_Date, Duration, Total_degree, Crs_ID, No_question, instructor_id) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "SET IDENTITY_INSERT Exam OFF;")
    write_line(f, "")

    # Question and Question_Choices
    # Questions: primary keys are explicit (Question_ID)
    rows_q = []
    for q in questions:
        rows_q.append("(" + ",".join([
            str(q['Question_ID']),
            str(q['Exam_ID']),
            escape(q['Question_Type']),
            escape(q['Question_Difficulty']),
            str(q['Marks']),
            escape(q['Correct_Answer']),
            str(q['Crs_id']),
            escape(q['question_topic'])
        ]) + ")")
    for chunk in chunked(rows_q, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Question (Question_ID, Exam_ID, Question_Type, Question_Difficulty, Marks, Correct_Answer, Crs_id, question_topic) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "")

    rows_qc = []
    for qc in question_choices:
        rows_qc.append("(" + ",".join([
            str(qc['Question_ID']),
            str(qc['choices_id']),
            escape(qc['A']),
            escape(qc['B']),
            escape(qc['C']),
            escape(qc['D'])
        ]) + ")")
    for chunk in chunked(rows_qc, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Question_Choices (Question_ID, choices_id, A, B, C, D) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "")

    # Exam_Question
    rows_eq = []
    for q in questions:
        rows_eq.append(f"({q['Question_ID']}, {q['Exam_ID']})")
    for chunk in chunked(rows_eq, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Exam_Question (Question_ID, Exam_ID) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "")

    # Topic
    rows_t = []
    for t in topics:
        rows_t.append(f"({t['topic_id']}, {escape(t['topic_name'])}, {t['crs_id']})")
    for chunk in chunked(rows_t, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Topic (topic_id, topic_name, crs_id) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "")

    # Certificate
    write_line(f, "SET IDENTITY_INSERT Certificate ON;")
    rows = []
    for c in certs:
        rows.append("(" + ",".join([
            str(c['Certificate_ID']),
            escape(c['Name']),
            escape(c['platform']),
            str(c['duration']),
            escape(c['issued_date']),
            escape(c['level']),
            str(c['student_id'])
        ]) + ")")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Certificate (Certificate_ID, Name, platform, duration, issued_date, level, student_id) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "SET IDENTITY_INSERT Certificate OFF;")
    write_line(f, "")

    # Freelance
    write_line(f, "SET IDENTITY_INSERT Freelance ON;")
    rows = []
    for fr in freelances:
        rows.append("(" + ",".join([
            str(fr['freelance_id']),
            escape(fr['platform']),
            str(fr['payment']),
            str(fr['revenue']),
            str(fr['duration']),
            escape(fr['client_country']),
            escape(fr['Date']),
            str(fr['Rating']),
            str(fr['student_id'])
        ]) + ")")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Freelance (freelance_id, platform, payment, revenue, duration, client_country, Date, Rating, student_id) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "SET IDENTITY_INSERT Freelance OFF;")
    write_line(f, "")

    # Track_Branch_Intake
    rows = []
    for tbi in track_branch_intake:
        rows.append(f"({tbi['Branch_ID']}, {tbi['intake_id']}, {tbi['Track_ID']})")
    for chunk in chunked(rows, BATCH_INSERT_SIZE):
        write_line(f, "INSERT INTO Track_Branch_Intake (Branch_ID, intake_id, Track_ID) VALUES")
        write_line(f, ",\n".join(chunk) + ";")
    write_line(f, "")

    # Finalize transaction
    write_line(f, "COMMIT;")
    write_line(f, "-- End of generated data")
print("Done. SQL file generated.")
