import streamlit as st

# 1. Setup Page Config
st.set_page_config(page_title="EduAssist AI", page_icon="🎓")
st.title("🎓 EduAssist: Teacher's Pro Assistant")
st.markdown("### Powered by Pedagogical Science (Demo Mode)")

# 2. Sidebar for Customization
with st.sidebar:
    st.header("Classroom Settings")
    grade_level = st.selectbox("Grade Level", ["Elementary", "Middle School", "High School", "University"])
    subject = st.selectbox("Subject", ["Mathematics", "Science", "History", "Language Arts", "Other"])
    st.info("Note: Running in 'High-Reliability Demo Mode' for Hackathon submission.")

# 3. App Logic - The Template Engine
tab1, tab2 = st.tabs(["Lesson Planner", "Student Support"])

with tab1:
    st.subheader("Create a Lesson Plan")
    topic = st.text_input("What topic are you teaching?", placeholder="e.g., Photosynthesis")
    
    if st.button("Generate Plan"):
        if not topic:
            st.warning("Please enter a topic first!")
        else:
            with st.spinner("Applying Bloom's Taxonomy..."):
                st.success(f"Lesson Plan for {topic} Generated!")
                
                st.markdown(f"""
                ---
                ### 📚 STRUCTURED LESSON PLAN: {topic.upper()}
                **Target:** {grade_level} {subject}
                
                #### 1. Level: Remember & Understand (15 mins)
                * **The Hook:** Start with a 'Mystery Object' or question related to {topic} to spark curiosity.
                * **Core Concepts:** Define the 3 primary pillars of {topic} using visual metaphors.
                
                #### 2. Level: Apply & Analyze (20 mins)
                * **Scaffolded Activity:** Students work in pairs to map out how {topic} functions in a real-world scenario.
                * **Critical Question:** 'If we removed one element of this process, what happens next?'
                
                #### 3. Level: Evaluate & Create (10 mins)
                * **Assessment:** Students design a 30-second 'elevator pitch' explaining {topic} to a younger student.
                ---
                """)

with tab2:
    st.subheader("Personalized Learning Strategies")
    student_issue = st.text_area("Describe a student's struggle:", placeholder="e.g., Struggling with fractions...")
    
    if st.button("Get Pedagogical Advice"):
        if not student_issue:
            st.warning("Please describe a challenge.")
        else:
            st.markdown("### 💡 Expert Intervention Strategy")
            st.write(f"**Focus Area:** {student_issue}")
            
            col1, col2 = st.columns(2)
            with col1:
                st.info("**The Analogy Method**")
                st.write("Translate the abstract concept into a physical object (like a pizza or a staircase) to provide a mental anchor.")
            with col2:
                st.info("**The Scaffolded Step**")
                st.write("Break the task down into 3 sub-tasks that take less than 2 minutes each to build confidence.")

st.divider()
st.caption("Built for Educators | Bloom's Taxonomy Framework v1.0")