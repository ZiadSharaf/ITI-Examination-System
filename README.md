<div align="center">
<h1>🚀 ITI Examination System</h1>

<img src="https://github.com/user-attachments/assets/94bb8a9a-da45-47f3-bfa5-a83c4d96348d" 
alt="ITI Examination System Logo" 
width="180px" 
style="border-radius: 10px; margin: 10px 0;" />


<div align="center">

<h2 style="
background: linear-gradient(90deg, #0078D7, #FFB900);
color: white;
padding: 10px 0;
border-radius: 10px;
width: 70%;
margin: auto;
font-family: 'Segoe UI', sans-serif;
">


 <div align="center">
     
🧰 Technologies & Tools     
</h2>

<p>
<img src="https://img.shields.io/badge/Draw.io-F08705?style=for-the-badge&logo=diagrams.net&logoColor=white" alt="Draw.io"/>
<img src="https://img.shields.io/badge/SQL_Server_Management_Studio-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white" alt="SQL Server Management Studio"/>
<img src="https://img.shields.io/badge/SQL-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white" alt="SQL Server"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/SSRS-CC2927?style=for-the-badge&logo=microsoft-sql-server&logoColor=white" alt="SSRS"/>
<img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=power-bi&logoColor=black" alt="Power BI"/>
<img src="https://img.shields.io/badge/Lovable_AI-FF69B4?style=for-the-badge&logo=ai&logoColor=white" alt="Lovable AI"/>
</p>

</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</div>

<div align="center">
    
## 🎯 Project Overview

This project represents a comprehensive end-to-end solution aimed at transforming how the Information Technology Institute (ITI) manages its academic operations. It goes beyond a simple database, creating a complete ecosystem that handles everything from student registration to advanced business intelligence. At its core, the smart examination system evaluates students’ comprehension and mastery of subjects, supporting multiple exam formats, identifying strengths and weaknesses, and promoting continuous learning. By doing so, it helps learners gain certifications and equips them to meet modern industry demands efficiently.

</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</div>

<div align="center">
  
## ⚙️ Project Workflow

<div align="center">

```mermaid
graph TB
    A[🗺️ ERD] --> B[🗺️ Mapping]
    B --> C[🗄️ Database Creation]
    C --> D[🧮 Database Generation]
    D --> E[⚙️ Stored Procedures]
    E --> F[🏢 Data Warehouse]
    F --> G[📋 SSRS Reports]
    G --> H[📊 Dashboard]
    H --> I[🌐 Website]
    
    style A fill:#ff6b6b,stroke:#fff,stroke-width:3px,color:#fff
    style B fill:#4ecdc4,stroke:#fff,stroke-width:3px,color:#fff 
    style C fill:#45b7d1,stroke:#fff,stroke-width:3px,color:#fff 
    style D fill:#96ceb4,stroke:#fff,stroke-width:3px,color:#fff 
    style E fill:#feca57,stroke:#fff,stroke-width:3px,color:#fff 
    style F fill:#ff9ff3,stroke:#fff,stroke-width:3px,color:#fff 
    style G fill:#54a0ff,stroke:#fff,stroke-width:3px,color:#fff 
    style H fill:#5f27cd,stroke:#fff,stroke-width:3px,color:#fff
    style I fill:#222f3e,stroke:#fff,stroke-width:3px,color:#fff
```

</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</div>


## 🗺️ ERD

<p align="justify" style="font-size:16px; line-height:1.6; margin-bottom:15px;">
  In this phase, we designed the <b>Entity-Relationship Diagram (ERD)</b> to define the main entities,
  their attributes, and the relationships between them. This step provided a clear conceptual
  view of how data flows within the system.
</p>

<div align="center">
  <img src="Photos/erd.png" width="100%" style="border-radius:12px;box-shadow:0 6px 20px rgba(0,0,0,.15);"/>
</div>

</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</div>

## 🗺️ Mapping

<p align="justify" style="font-size:16px; line-height:1.6; margin-bottom:15px;">
  After completing the <b>Entity-Relationship Diagram (ERD)</b>, we performed the <b>mapping process</b> 
  to translate the conceptual model into a logical database structure. This included defining 
  primary and foreign keys, establishing relationships between tables, and preparing the foundation 
  for database creation and further data modeling.
</p>

<div align="center">
  <img src="Photos/Mapping.png" width="100%" style="border-radius:12px;box-shadow:0 6px 20px rgba(0,0,0,.15);"/>
</div>

</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</div>


## 🗄️ Database Creation

<p align="justify" style="font-size:16px; line-height:1.6; margin-top:10px;">
  In this stage, we implemented the <b>database schema</b> by writing and executing the required 
  <b>SQL scripts</b>. We began by creating the database using the 
  <code>CREATE DATABASE</code> command, followed by defining tables and specifying 
  appropriate <b>data types</b> for each attribute using <code>CREATE TABLE</code>. 
  Afterward, we applied <b>constraints</b> such as <code>PRIMARY KEY</code>, 
  <code>FOREIGN KEY</code>, and <code>NOT NULL</code> to ensure data integrity and maintain 
  relationships between entities.
  Finally, the system components were integrated into a functional database environment, 
  and testing was conducted to verify that it efficiently handles exam data, student responses, 
  and related operations.
</p>

<div align="center">
  <img src="Photos/Tables.png" width="100%" style="border-radius:12px;box-shadow:0 6px 20px rgba(0,0,0,.15);"/>
</div>

</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</div>

## 🧮 Database Generation

<p align="justify" style="font-size:16px; line-height:1.6;">
  In this phase, we utilized <b>Python</b> along with several <b>AI-powered platforms</b> 
  to generate the required dataset. Using Python libraries such as 
  <code>Faker</code> and <code>Random</code>, we created structured and diverse synthetic data 
  representing students, courses, and exam activities. 
  <br><br>
  To enhance data realism and variability, we also leveraged <b>AI tools</b> like 
  <b>ChatGPT</b> and <b>Gemini</b> to simulate more complex scenarios, such as 
  realistic exam results, student behavior patterns, and course interactions. 
  <br><br>
  This combination of traditional data generation techniques and AI-assisted modeling 
  allowed us to build a <b>high-quality, representative dataset</b> suitable for testing 
  and system evaluation.
</p>

<div align="center">
  <img src="Photos/Python Script.png" width="100%" style="border-radius:12px;box-shadow:0 6px 20px rgba(0,0,0,.15);"/>
</div>

<div align="center">
  <img src="Photos/Generation.png" width="100%" style="border-radius:12px;box-shadow:0 6px 20px rgba(0,0,0,.15);"/>
</div>

</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</div>

## ⚙️ Stored Procedures

<p align="justify" style="font-size:16px; line-height:1.6;">
  In this phase, we created stored procedures for each table in the database to 
  handle the main data operations. These procedures were developed to perform 
  Insert, Update, and Delete actions efficiently and securely. Using stored 
  procedures helped improve performance, maintain data consistency, and 
  simplify interaction between the application and the database by centralizing all 
  SQL logic in one place. 
</p>

<div align="center">
  <img src="Photos/Stored Procedures.png" width="100%" style="border-radius:12px;box-shadow:0 6px 20px rgba(0,0,0,.15);"/>
</div>

</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</div>

## 🏢 DWH

<p align="justify" style="font-size:16px; line-height:1.6;">
In this stage, we built the analytical layer using <b>SQL Views</b> to serve as a 
<b>virtual data warehouse</b>. A semantic layer was designed above the operational 
database to enable analytical querying without duplicating data physically. 
All data is accessed dynamically through views, ensuring efficiency and consistency 
between the transactional and analytical systems. 
<br><br>
The warehouse follows a <b>Fact–Dimensions architecture</b> that separates 
operational details from analytical insights. The central <b>Fact_ExamActivity</b> 
view captures exam responses, marks, and results, while multiple <b>dimension views</b> 
such as <b>Students</b>, <b>Exams</b>, <b>Courses</b>, <b>Questions</b>, <b>Instructors</b>, 
and <b>Dates</b> provide contextual information. 
This design supports advanced <b>analytical queries</b>, <b>trend analysis</b>, and 
<b>KPI reporting</b> — forming a scalable and efficient analytical model for the 
ITI Examination System.
</p>

<br/>

### 🧩 Fact Table – Exam Activity

<div align="center">
  <img src="Photos/Fact Exam Activity.png" 
       width="100%" 
       style="border-radius:12px;
              box-shadow:0 6px 20px rgba(0,0,0,.15);
              margin-bottom:40px;"/>
</div>

### 🧠 SQL Views

<div align="center">
  <img src="Photos/Views.png" 
       width="100%" 
       style="border-radius:12px;
              box-shadow:0 6px 20px rgba(0,0,0,.15);
              margin-bottom:40px;"/>
</div>

### 🏗️ Data Warehouse Schema

<div align="center">
  <img src="Photos/DWH_Schema.png" 
       width="100%" 
       style="border-radius:12px;
              box-shadow:0 6px 20px rgba(0,0,0,.15);
              margin-bottom:40px;"/>
</div>

</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</div>

## 📋 SSRS Reports

<p align="justify" style="font-size:16px; line-height:1.6;">
Leverage raw data to generate actionable insights that drive academic and administrative decision-making. Utilize SQL Server Reporting Services (SSRS) to design, deploy, and manage paginated reports, all powered by optimized stored procedures to ensure high performance, scalability, and reusability.
</p>

<br/>

### 🧑‍🎓 STUDENT DETAILS BY DEPARTMENT
<div align="center">
  <img src="Photos/Report1.png" 
       width="100%" 
       style="border-radius:12px;
              box-shadow:0 6px 20px rgba(0,0,0,.15);
              margin-bottom:40px;"/>
</div>

### 🧾 STUDENT GRADES
<div align="center">
  <img src="Photos/Report2.png" 
       width="100%" 
       style="border-radius:12px;
              box-shadow:0 6px 20px rgba(0,0,0,.15);
              margin-bottom:40px;"/>
</div>

### 👨‍🏫 INSTUCTOR NAME,COURSES AND STUDENTS NUMBER BY INSTRUCTOR ID
<div align="center">
  <img src="Photos/Report3.png" 
       width="100%" 
       style="border-radius:12px;
              box-shadow:0 6px 20px rgba(0,0,0,.15);
              margin-bottom:40px;"/>
</div>

### 📚 TOPICS FOR COURSES
<div align="center">
  <img src="Photos/Report4.png" 
       width="100%" 
       style="border-radius:12px;
              box-shadow:0 6px 20px rgba(0,0,0,.15);
              margin-bottom:40px;"/>
</div>


</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</div>

## 📊 Dashboard

<div align="center">
 
*Wanna see a sample of our 20+ Dashboards 📊?*

</div>

### 📊 STUDENT OVERVIEW DASHBOARD 
<div align="center">
  <img src="Photos/dashboard1.jpg" 
       width="100%" 
       style="border-radius:12px;
              box-shadow:0 6px 20px rgba(0,0,0,.15);
              margin-bottom:40px;"/>
</div>

</div>

### 💡 ITI QUESTIONS DASHBOARD 
<div align="center">
  <img src="Photos/dashboard2.jpg" 
       width="100%" 
       style="border-radius:12px;
              box-shadow:0 6px 20px rgba(0,0,0,.15);
              margin-bottom:40px;"/>
</div>

</div>

### 🧠 ITI INSTRUCTOR DASHBOARD 
<div align="center">
  <img src="Photos/dashboard3.jpg" 
       width="100%" 
       style="border-radius:12px;
              box-shadow:0 6px 20px rgba(0,0,0,.15);
              margin-bottom:40px;"/>
</div>

</div>

### 📝 ITI EXAMS DASHBOARD 
<div align="center">
  <img src="Photos/dashboard4.jpg" 
       width="100%" 
       style="border-radius:12px;
              box-shadow:0 6px 20px rgba(0,0,0,.15);
              margin-bottom:40px;"/>
</div>

</div>

### 📈 PREDICTIVE ANALYSIS DASHBOARD 
<div align="center">
  <img src="Photos/Predictive_Analysis.png" 
       width="100%" 
       style="border-radius:12px;
              box-shadow:0 6px 20px rgba(0,0,0,.15);
              margin-bottom:40px;"/>
</div>

</div>

### 🧑‍🎓 STUDENT FACEBOOK DASHBOARD 
<div align="center">
  <img src="Photos/Student_Facebook.png" 
       width="100%" 
       style="border-radius:12px;
              box-shadow:0 6px 20px rgba(0,0,0,.15);
              margin-bottom:40px;"/>
</div>

<br>

Wanna explore all dashboards 📊?  
Check the full Power BI file inside the **Dashboard** folder, or view it online below 👇

<br>

<div align="center">
  <a href="https://project.novypro.com/bxWYfq" target="_blank">
    <img src="https://img.shields.io/badge/Explore%20on%20NovyPro-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Explore on NovyPro"/>
  </a>
</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</div>

## 🌐 Website Interface

<p align="justify" style="font-size:16px; line-height:1.6;">
The ITI Examination System is a modern and efficient platform designed to simplify online assessments for both students and instructors. It provides an all-in-one environment where students can take exams, access their results instantly, and track their academic progress. Instructors can effortlessly manage courses, create exams, and monitor student performance through an intuitive dashboard. With its clean interface and seamless functionality, the ITI Examination System ensures a smooth and organized examination process, promoting transparency, accuracy, and convenience for all users. The website was developed using Lovable, which helped streamline the design and functionality of the platform.
</p>

<br/>

### 🌐 Student Login Page
<div align="center">
<img src="Photos/Website_Picture 1.png" 
     alt="Website Screenshot 1" 
     width="800"
     style="border-radius:12px;margin:10px 0;box-shadow:0 4px 15px rgba(0,0,0,.15);" />

</div>

### 🌐 Student Home Page
<div align="center">
<img src="Photos/Website_Picture 2.png"  
     alt="Website Screenshot 2" 
     width="800"
     style="border-radius:12px;margin:10px 0;box-shadow:0 4px 15px rgba(0,0,0,.15);" />

 </div>

### 🌐 Student Home Page
<div align="center">
  <img src="Photos/Website_Picture 3.png"  
     alt="Website Screenshot 3" 
     width="800"
     style="border-radius:12px;margin:10px 0;box-shadow:0 4px 15px rgba(0,0,0,.15);" />

 </div>

### 🌐 Example of a selected exam
<div align="center">
<img src="Photos/Website_Picture 4.png"  
     alt="Website Screenshot 4" 
     width="800"
     style="border-radius:12px;margin:10px 0;box-shadow:0 4px 15px rgba(0,0,0,.15);" />

 </div>

### 🌐 Student Result Page
<div align="center">
 <img src="Photos/Website_Picture 5.png"  
     alt="Website Screenshot 5" 
     width="800"
     style="border-radius:12px;margin:10px 0;box-shadow:0 4px 15px rgba(0,0,0,.15);" />

 </div>

### 🌐 Instructor Login Page
<div align="center">
 <img src="Photos/Website_Picture 6.png"  
     alt="Website Screenshot 6" 
     width="800"
     style="border-radius:12px;margin:10px 0;box-shadow:0 4px 15px rgba(0,0,0,.15);" />

 </div>

### 🌐 Instructor Home Page
<div align="center">
<img src="Photos/Website_Picture 7.png"  
     alt="Website Screenshot 7" 
     width="800"
     style="border-radius:12px;margin:10px 0;box-shadow:0 4px 15px rgba(0,0,0,.15);" />

 </div>

### 🌐 Manage Courses Page
<div align="center">
 <img src="Photos/Website_Picture 8.png"  
     alt="Website Screenshot 8" 
     width="800"
     style="border-radius:12px;margin:10px 0;box-shadow:0 4px 15px rgba(0,0,0,.15);" />

 </div>

### 🌐 View Student results by instructor Page
<div align="center">
 <img src="Photos/Website_Picture 9.png"  
     alt="Website Screenshot 9" 
     width="800"
     style="border-radius:12px;margin:10px 0;box-shadow:0 4px 15px rgba(0,0,0,.15);" />

 </div>
     
<div align="center">
  <a href="https://lovable.dev/projects/c04d7cf8-bd7c-4ac8-98dc-8764ded4a74f" target="_blank">
    <img src="https://img.shields.io/badge/🌐_Explore_The_Website-00bfa6?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Explore Website"/>
  </a>
</div>

</div>
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">
</div>

<div align="center">
 
## 💻 Meet The Dream Team

<div align="center">
<h2 style="color:#0078D7; font-family:'Segoe UI', sans-serif;">✨ The Data Dynamos ✨</h2>

<table>
<tr>

<!-- 🧠 Ziad Sharaf -->
<td align="center">
<img src="https://github.com/user-attachments/assets/4d37d0a6-73af-4f34-be3e-f9541ae88ff1" width="115" height="115" style="border-radius:50%; border:3px solid #0078D7; box-shadow:0 0 10px rgba(0,120,215,0.5); object-fit:cover;"/>
<br><b>Ziad Sharaf</b><br>
<sub>Data Analyst • Power BI Specialist</sub><br><br>
<a href="https://github.com/ZiadSharaf"><img src="https://img.shields.io/badge/GitHub-0078D7?style=flat-square&logo=github&logoColor=white"></a>
<a href="https://www.linkedin.com/in/ziad-sharaf-zs/"><img src="https://img.shields.io/badge/LinkedIn-0078D7?style=flat-square&logo=linkedin&logoColor=white"></a>
</td>

<!-- ⚡ Adham Abdelnasser -->
<td align="center">
<img src="https://github.com/user-attachments/assets/11c653a4-acec-47cc-b960-65137a3148a6" width="115" height="115" style="border-radius:50%; border:3px solid #00BFA6; box-shadow:0 0 10px rgba(0,191,166,0.5); object-fit:cover;"/>
<br><b>Adham Abdelnasser</b><br>
<sub>Data Analyst • BI Developer</sub><br><br>
<a href="https://github.com/Adham-111"><img src="https://img.shields.io/badge/GitHub-00BFA6?style=flat-square&logo=github&logoColor=white"></a>
<a href="https://www.linkedin.com/in/adhamabdelnasser/"><img src="https://img.shields.io/badge/LinkedIn-00BFA6?style=flat-square&logo=linkedin&logoColor=white"></a>
</td>

<!-- 💎 Noreen Essam -->
<td align="center">
<img src="https://github.com/user-attachments/assets/1d0fc507-337b-4336-9174-5ba84cd72237b" width="115" height="115" style="border-radius:50%; border:3px solid #ff69b4; box-shadow:0 0 10px rgba(255,105,180,0.5); object-fit:cover;"/>
<br><b>Noreen Essam</b><br>
<sub>Data Analyst • Visualization Expert</sub><br><br>
<a href="https://github.com/noreenessam"><img src="https://img.shields.io/badge/GitHub-ff69b4?style=flat-square&logo=github&logoColor=white"></a>
<a href="https://www.linkedin.com/in/noreen-essam/"><img src="https://img.shields.io/badge/LinkedIn-ff69b4?style=flat-square&logo=linkedin&logoColor=white"></a>
</td>

<!-- 🎯 Ahmed Ibrahim -->
<td align="center">
<img src="https://github.com/user-attachments/assets/fe2190d1-eeaf-4d0e-b0db-6d1dc418034d" width="115" height="115" style="border-radius:50%; border:3px solid #000000; box-shadow:0 0 10px rgba(0,0,0,0.5); object-fit:cover;"/>
<br><b>Ahmed Ibrahim</b><br>
<sub>Data Engineer • BI Developer</sub><br><br>
<a href="https://github.com/Ahmedibrahim175"><img src="https://img.shields.io/badge/GitHub-000000?style=flat-square&logo=github&logoColor=white"></a>
<a href="https://www.linkedin.com/in/ahmed-ibrahim1752/"><img src="https://img.shields.io/badge/LinkedIn-000000?style=flat-square&logo=linkedin&logoColor=white"></a>
</td>

<!-- 🌟 Nader John -->
<td align="center">
<img src="https://github.com/user-attachments/assets/24f91dbf-2370-4953-8bd0-8c5c54686bf5" width="115" height="115" style="border-radius:50%; border:3px solid #F4A261; box-shadow:0 0 10px rgba(244,162,97,0.5); object-fit:cover;"/>
<br><b>Nader John</b><br>
<sub>Data Analyst • Dashboard Creator</sub><br><br>
<a href="https://github.com/NaderJohn"><img src="https://img.shields.io/badge/GitHub-F4A261?style=flat-square&logo=github&logoColor=white"></a>
<a href="https://www.linkedin.com/in/naderjohn/"><img src="https://img.shields.io/badge/LinkedIn-F4A261?style=flat-square&logo=linkedin&logoColor=white"></a>
</td>

</tr>
</table>

<br>

<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=18&pause=1000&color=0078D7&center=true&width=435&lines=Stronger+Together+💪;Turning+Data+into+Decisions+📊" width="300">
</div>

<br />

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

</div>



