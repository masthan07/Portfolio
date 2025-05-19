import streamlit as st
import json
from streamlit_lottie import st_lottie
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import streamlit.components.v1 as components

# Set page configuration
st.set_page_config(page_title="Masthan Basha | Portfolio", layout="wide")

# Sidebar
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("", ["🏠 Home", "🎓 Education", "🛠 Skills", "💼 Projects", "📜 Certifications", "📫 Contact"])

# Custom CSS styling
st.markdown("""
    <style>
    @keyframes slideIn {
        from { transform: translateX(-40px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    .slide-in {
        animation: slideIn 0.7s cubic-bezier(0.23, 1, 0.32, 1) both;
    }
    .main-title {
        font-size: 3em;
        font-weight: bold;
        color: #fff;
        background: linear-gradient(90deg, #ff512f 0%, #dd2476 50%, #1abc9c 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-fill-color: transparent;
    }
    .subtitle {
        font-size: 1.5em;
        font-weight: 600;
        color: #fff;
        background: linear-gradient(90deg, #36d1c4 0%, #5b86e5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        text-fill-color: transparent;
    }
    .section-title {
        font-size: 2em;
        margin-top: 20px;
        font-weight: bold;
        color: #222;
        border-bottom: 2px solid #1abc9c;
        padding-bottom: 5px;
        background: none !important;
        -webkit-background-clip: initial !important;
        -webkit-text-fill-color: initial !important;
        background-clip: initial !important;
        text-fill-color: initial !important;
    }
    .section-title .emoji, .section-title span, .section-title svg {
        background: none !important;
        color: inherit !important;
        -webkit-background-clip: initial !important;
        -webkit-text-fill-color: initial !important;
        background-clip: initial !important;
        text-fill-color: initial !important;
    }
    .project-box {
        border: 1px solid #ddd;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        background-color: #ffffff;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    form {
        display: flex;
        flex-direction: column;
        gap: 10px;
        max-width: 500px;
        margin: 0 auto;
        padding: 20px;
        background-color: #f8f9fa;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    input, textarea {
        padding: 12px;
        border: 1px solid #ddd;
        border-radius: 5px;
        font-size: 16px;
        background-color: white;
    }
    textarea {
        min-height: 150px;
        resize: vertical;
    }
    button {
        background-color: #1abc9c;
        color: white;
        padding: 12px 24px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }
    button:hover {
        background-color: #16a085;
    }
    a {
        color: #1abc9c;
        text-decoration: none;
        transition: color 0.3s ease;
    }
    a:hover {
        color: #16a085;
    }
    </style>
""", unsafe_allow_html=True)

# Load projects from JSON
def load_projects():
    with open("projects.json", "r") as f:
        return json.load(f)

# Lottie animation URLs for each section
LOTTIE_URLS = {
    "home": "https://assets10.lottiefiles.com/packages/lf20_0yfsb3a1.json",  # Developer
    "skills": "https://assets2.lottiefiles.com/packages/lf20_kkflmtur.json",  # Coding
    "projects": "https://assets2.lottiefiles.com/packages/lf20_49rdyysj.json",  # Project management
    "certifications": "https://assets2.lottiefiles.com/packages/lf20_ysas1vcp.json",  # Certificate
    "contact": "https://assets2.lottiefiles.com/packages/lf20_tno6cg2w.json",  # Messaging
}

def load_lottieurl(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except:
        return None

# Pages
if page == "🏠 Home":
    # First row: Name/subtitle (left), (no animation on right)
    row1_col1, row1_col2 = st.columns([2, 1])
    with row1_col1:
        st.markdown('<span style="font-size:2.2em; vertical-align:middle;"></span>'
                    '<div class="main-title slide-in" style="display:inline;">'
                    '<span style="background: linear-gradient(90deg, #ff512f 0%, #dd2476 50%, #1abc9c 100%);'
                    '-webkit-background-clip: text;'
                    '-webkit-text-fill-color: transparent;'
                    'background-clip: text;'
                    'text-fill-color: transparent;'
                    '">I\'m Bellamkonda Masthan Basha</span>'
                    '</div>', unsafe_allow_html=True)
        st.markdown('<div class="subtitle slide-in">Engineering Student | Python Developer | AI Enthusiast</div>', unsafe_allow_html=True)
    # row1_col2 left empty (no animation)
    # Second row: About, resume, and social links
    st.markdown("""
    <div class="slide-in" style="
        font-size: 1.1em;
        line-height: 1.6;
        color: #34495e;
        margin: 20px 0;
        text-align: left;
        max-width: 800px;
        padding: 10px 0;
    ">
        I'm a motivated engineering student with strong analytical and problem-solving skills,
        eager to apply academic knowledge to real-world engineering challenges.
    </div>
    """, unsafe_allow_html=True)
    with open(r"C:\Users\acer\Downloads\mb(r4).pdf", "rb") as pdf_file:
        st.download_button(
            "📄 Download Resume",
            pdf_file,
            file_name="MasthanBasha_Resume.pdf",
            mime="application/pdf"
        )
    st.markdown('<div class="slide-in">📱 Connect with me:</div>', unsafe_allow_html=True)
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin)](https://www.linkedin.com/in/mastan-blk-4a8100253)")
    with col_b:
        st.markdown("[![GitHub](https://img.shields.io/badge/-GitHub-black?logo=github)](https://github.com/masthan07)")
    with col_c:
        st.markdown("[![Instagram](https://img.shields.io/badge/-Instagram-pink?logo=instagram)](https://instagram.com)")

elif page == "🎓 Education":
    st.markdown('<div class="section-title slide-in">🎓 Education</div>', unsafe_allow_html=True)
    
    # Add custom CSS with animations
    st.markdown("""
    <style>
    @keyframes slideIn {
        from {
            transform: translateX(-100px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    .education-container {
        display: flex;
        flex-direction: row;
        gap: 20px;
        max-width: 1000px;
        margin: 0 auto;
        padding: 20px;
        flex-wrap: wrap;
        justify-content: center;
    }
    .education-item {
        background: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-left: 5px solid #1abc9c;
        transition: all 0.3s ease;
        animation: slideIn 0.5s ease-out forwards;
        opacity: 0;
        min-width: 300px;
        max-width: 320px;
        flex: 1 1 300px;
    }
    .education-item:hover {
        transform: translateY(-5px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
    }
    .education-title {
        font-size: 1.2em;
        color: #2c3e50;
        margin-bottom: 10px;
        font-weight: 600;
        transition: color 0.3s ease;
    }
    .education-item:hover .education-title {
        color: #1abc9c;
    }
    .education-institution {
        color: #34495e;
        font-size: 1.05em;
        margin-bottom: 8px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .education-institution::before {
        content: "🏛️";
        font-size: 1.2em;
    }
    .education-details {
        color: #7f8c8d;
        font-size: 1em;
        margin-top: 15px;
        padding-top: 15px;
        border-top: 1px solid #eee;
    }
    .education-year {
        color: #1abc9c;
        font-weight: 500;
        display: inline-block;
        padding: 5px 15px;
        background: rgba(26, 188, 156, 0.1);
        border-radius: 20px;
        margin-bottom: 10px;
    }
    .education-score {
        display: inline-block;
        padding: 5px 15px;
        background: rgba(52, 152, 219, 0.1);
        border-radius: 20px;
        color: #3498db;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

    # Render the education boxes as HTML (not as code)
    st.markdown(
        '<div class="education-container">'
        '  <div class="education-item" style="animation-delay: 0.1s;">'
        '    <div class="education-title">Bachelor of Technology in Computer Science and Engineering (Data Science)</div>'
        '    <div class="education-institution">Rajeev Gandhi Memorial College of Engineering and Technology, Nandyal</div>'
        '    <div class="education-details">'
        '      <div class="education-year">2022 - 2026</div>'
        '      <div class="education-score">Current CGPA: 8.85/10.0</div>'
        '    </div>'
        '  </div>'
        '  <div class="education-item" style="animation-delay: 0.3s;">'
        '    <div class="education-title">Higher Secondary Education (12th Standard)</div>'
        '    <div class="education-institution">Narayana Junior College, Nellore</div>'
        '    <div class="education-details">'
        '      <div class="education-year">2020 - 2022</div>'
        '      <div class="education-score">Percentage: 96.8%</div>'
        '    </div>'
        '  </div>'
        '  <div class="education-item" style="animation-delay: 0.5s;">'
        '    <div class="education-title">Secondary School Education (10th Standard)</div>'
        '    <div class="education-institution">T.V.R. High School, Proddatur</div>'
        '    <div class="education-details">'
        '      <div class="education-year">2019 - 2020</div>'
        '      <div class="education-score">CGPA: 9.46/10.0</div>'
        '    </div>'
        '  </div>'
        '</div>',
        unsafe_allow_html=True
    )

elif page == "🛠 Skills":
    st.markdown('<div class="section-title slide-in">🛠 Technical Skills</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    box_style = """
        text-align: center;
        padding: 30px 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        height: 400px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: flex-start;
    """
    with col1:
        st.markdown(f"""
        <div class="slide-in" style="{box_style}">
            <div style="margin-bottom: 20px;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="80" height="80">
            </div>
            <h3 style="color: #2c3e50; margin-bottom: 20px;">Programming</h3>
            <div style="color: #34495e;">
                <p style="font-size: 1.1em; margin: 10px 0;">• Python</p>
                <p style="font-size: 1.1em; margin: 10px 0;">• C</p>
                <p style="font-size: 1.1em; margin: 10px 0;">• Java</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="slide-in" style="{box_style}">
            <div style="margin-bottom: 20px;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" width="80" height="80">
            </div>
            <h3 style="color: #2c3e50; margin-bottom: 20px;">Data Tools</h3>
            <div style="color: #34495e;">
                <p style="font-size: 1.1em; margin: 10px 0;">• SQL</p>
                <p style="font-size: 1.1em; margin: 10px 0;">• Power BI</p>
                <p style="font-size: 1.1em; margin: 10px 0;">• MS Excel</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="slide-in" style="{box_style}">
            <div style="margin-bottom: 20px;">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg" width="80" height="80">
            </div>
            <h3 style="color: #2c3e50; margin-bottom: 20px;">Core Concepts</h3>
            <div style="color: #34495e;">
                <p style="font-size: 1.1em; margin: 10px 0;">• Data Structures & Algorithms</p>
                <p style="font-size: 1.1em; margin: 10px 0;">• Machine Learning & Deep Learning</p>
                <p style="font-size: 1.1em; margin: 10px 0;">• Natural Language Processing</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    # No animation for Skills page

elif page == "💼 Projects":
    st.markdown('<div class="section-title slide-in">💼 Projects</div>', unsafe_allow_html=True)
    
    # Add Project Section with improved styling
    st.markdown("""
    <style>
    .add-project-btn {
        background-color: #1abc9c;
        color: white;
        padding: 12px 24px;
        border-radius: 8px;
        cursor: pointer;
        margin-bottom: 30px;
        display: inline-block;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
    .add-project-btn:hover {
        background-color: #16a085;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Initialize session state for form visibility
    if 'show_project_form' not in st.session_state:
        st.session_state.show_project_form = False
    
    # Add Project Button
    if st.button("➕ Add New Project", key="add_project_btn"):
        st.session_state.show_project_form = True
    
    # Show password input if button is clicked
    if st.session_state.show_project_form:
        # Add custom CSS for password field and close button
        st.markdown("""
        <style>
        .password-container {
            position: relative;
            width: 100%;
        }
        .password-input {
            width: 100%;
            padding: 8px 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        .close-btn {
            background-color: #ff4444;
            color: white;
            padding: 8px 16px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 10px;
        }
        .close-btn:hover {
            background-color: #cc0000;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Password input without hiding
        passkey = st.text_input(
            "Password",
            key="project_password",
            help="Enter the password to add a new project"
        )
        
        if passkey == "Mm@6305478742":  # Your password
            st.session_state.show_project_form = False
            st.session_state.show_details_form = True
            st.rerun()
        elif passkey:  # Only show error if password was entered
            st.error("❌ Incorrect password!")
    
    # Show project details form in a new page
    if 'show_details_form' in st.session_state and st.session_state.show_details_form:
        st.markdown("## Add New Project")
        
        # Add close button
        if st.button("❌ Close Form"):
            st.session_state.show_details_form = False
            st.rerun()
            
        with st.form("add_project_form"):
            project_name = st.text_input("Project Name", placeholder="Enter the name of your project")
            project_description = st.text_area("Project Description", placeholder="Describe your project in detail")
            repository_link = st.text_input("Repository Link", placeholder="Enter the GitHub/GitLab repository URL")
            technologies = st.text_input("Technologies", placeholder="Enter technologies used (comma-separated)")
            
            col1, col2 = st.columns([1, 4])
            with col1:
                submitted = st.form_submit_button("Submit Project")
            
            if submitted:
                if not project_name or not project_description or not repository_link or not technologies:
                    st.error("Please fill in all fields!")
                else:
                    try:
                        # Load existing projects
                        with open("projects.json", "r") as f:
                            projects = json.load(f)
                        
                        # Add new project
                        new_project = {
                            "title": project_name,
                            "description": project_description,
                            "repository": repository_link,
                            "technologies": [tech.strip() for tech in technologies.split(",")]
                        }
                        
                        projects.append(new_project)
                        
                        # Save updated projects
                        with open("projects.json", "w") as f:
                            json.dump(projects, f, indent=4)
                        
                        st.success("✅ Project added successfully!")
                        st.balloons()
                        
                        # Reset form state
                        st.session_state.show_details_form = False
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error adding project: {str(e)}")
    
    # Display existing projects
    projects = load_projects()
    for project in projects:
        with st.container():
            st.markdown(f"""
            <div class="project-box slide-in">
                <h4>{project["title"]}</h4>
                <strong>Technologies:</strong> {', '.join(project['technologies'])}  
                <p>{project['description']}</p>
                <a href="{project['repository']}" target="_blank" style="
                    display: inline-block;
                    background-color: #1abc9c;
                    color: white;
                    padding: 8px 16px;
                    border-radius: 5px;
                    text-decoration: none;
                    margin-top: 10px;
                    transition: background-color 0.3s ease;
                ">View Repository</a>
            </div>
            """, unsafe_allow_html=True)

elif page == "📜 Certifications":
    st.markdown('<div class="section-title slide-in">📜 Certifications</div>', unsafe_allow_html=True)
    st.markdown("""
    <style>
    .cert-container {
        display: flex;
        flex-wrap: wrap;
        gap: 24px;
        justify-content: flex-start;
        margin-top: 30px;
    }
    .cert-card {
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border-left: 5px solid #1abc9c;
        padding: 24px 28px 20px 28px;
        min-width: 280px;
        max-width: 340px;
        flex: 1 1 300px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        transition: box-shadow 0.2s;
        animation: slideIn 0.7s cubic-bezier(0.23, 1, 0.32, 1) both;
    }
    .cert-card:hover {
        box-shadow: 0 6px 24px rgba(26,188,156,0.15);
    }
    .cert-icon {
        font-size: 2.2em;
        margin-bottom: 10px;
    }
    .cert-title {
        font-size: 1.15em;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 6px;
    }
    .cert-platform {
        font-size: 1em;
        color: #16a085;
        margin-bottom: 8px;
    }
    .cert-year {
        font-size: 0.98em;
        color: #7f8c8d;
        background: #f2fdfa;
        border-radius: 16px;
        padding: 3px 14px;
        margin-top: 8px;
        font-weight: 500;
    }
    </style>
    <div class="cert-container slide-in">
        <div class="cert-card">
            <div class="cert-icon">🏢</div>
            <div class="cert-title">AWS Cloud Practitioner</div>
            <div class="cert-platform">AWS Portal</div>
            <div class="cert-year">2025</div>
        </div>
        <div class="cert-card">
            <div class="cert-icon">🎯</div>
            <div class="cert-title">Deep Learning</div>
            <div class="cert-platform">Infosys Spring Board</div>
            <div class="cert-year">2025</div>
        </div>
        <div class="cert-card">
            <div class="cert-icon">💼</div>
            <div class="cert-title">Generative AI Virtual Internship</div>
            <div class="cert-platform">Google Cloud</div>
            <div class="cert-year">2024</div>
        </div>
        <div class="cert-card">
            <div class="cert-icon">📊</div>
            <div class="cert-title">MS Excel</div>
            <div class="cert-platform">edX</div>
            <div class="cert-year">2024</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "📫 Contact":
    st.markdown('<div class="section-title slide-in">📫 Contact Me</div>', unsafe_allow_html=True)
    st.markdown("""
    <style>
    .contact-flex {
        display: flex;
        flex-wrap: wrap;
        gap: 40px;
        justify-content: center;
        align-items: flex-start;
        margin-top: 30px;
    }
    .contact-card {
        background: #fff;
        border-radius: 14px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.08);
        padding: 32px 32px 24px 32px;
        min-width: 320px;
        max-width: 400px;
        flex: 1 1 350px;
        display: flex;
        flex-direction: column;
        align-items: stretch;
        animation: slideIn 0.7s cubic-bezier(0.23, 1, 0.32, 1) both;
    }
    .contact-info {
        background: #f8f9fa;
        border-radius: 14px;
        box-shadow: 0 2px 8px rgba(26,188,156,0.07);
        padding: 28px 28px 18px 28px;
        min-width: 340px;
        max-width: 440px;
        flex: 1 1 340px;
        display: flex;
        flex-direction: column;
        gap: 18px;
        font-size: 1.08em;
        color: #34495e;
        animation: slideIn 0.7s cubic-bezier(0.23, 1, 0.32, 1) both;
    }
    .contact-info-title {
        font-size: 1.15em;
        font-weight: 600;
        color: #1abc9c;
        margin-bottom: 10px;
    }
    .contact-info-item {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 6px;
        word-break: break-all;
    }
    .contact-info-icon {
        font-size: 1.3em;
        color: #16a085;
    }
    .contact-form-title {
        font-size: 1.15em;
        font-weight: 600;
        color: #2c3e50;
        margin-bottom: 18px;
        text-align: center;
    }
    </style>
    <div class="contact-flex slide-in">
        <div class="contact-card">
            <div class="contact-form-title">Send Me a Message</div>
    <form action="https://formsubmit.co/bellamkondamasthanbasha@gmail.com" method="POST">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <input type="hidden" name="_subject" value="New Portfolio Contact!">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_autoresponse" value="Thank you for your message! I will get back to you soon.">
        <button type="submit">Send Message</button>
    </form>
        </div>
        <div class="contact-info">
            <div class="contact-info-title">Contact Information</div>
            <div class="contact-info-item"><span class="contact-info-icon">📧</span> bellamkondamasthanbasha@gmail.com</div>
            <div class="contact-info-item"><span class="contact-info-icon">📍</span> Andhra Pradesh, India</div>
            <div class="contact-info-item">
                <span class="contact-info-icon">💼</span>
                <a href="https://www.linkedin.com/in/mastan-blk-4a8100253" target="_blank">
                    <img src="https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin" alt="LinkedIn" style="vertical-align: middle;">
                </a>
            </div>
            <div class="contact-info-item">
                <span class="contact-info-icon">🐙</span>
                <a href="https://github.com/masthan07" target="_blank">
                    <img src="https://img.shields.io/badge/-GitHub-black?logo=github" alt="GitHub" style="vertical-align: middle;">
                </a>
            </div>
        </div>
    </div>
    <div style="margin-top: 30px; color: #7f8c8d; text-align: center; font-size: 1em;">I usually respond within 24 hours. Looking forward to connecting with you!</div>
    """, unsafe_allow_html=True)
