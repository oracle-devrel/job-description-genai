# jobposting.py

import streamlit as st
from llm.client import OCIGenAIClient

APPNAME = "AI Assisted Job Posting Generation"
DESC = "As a recruiter or hiring manager, you can use AI assistance to create the first draft of a Job Description based on Job title, company, and division. The Gen AI can assist creating a draft job description that includes summary, description, responsibilities, and qualifications."
example1 = {"companyName": "Oracle", "businessTitle": "AI Researcher", "department": "Research", "additional_hints": "Machine Learning, Python, LLMs"}
example2 = {"companyName": "ABC Corp", "businessTitle": "Lead Software Engineer", "department": "Payment Systems", "additional_hints": "Java, Cloud Technologies, IT security"}



def createJD(businessTitle, companyName, department, additional_hints):
    client = OCIGenAIClient()
    prompt = f"""Your task is to write a job posting for the role of {businessTitle} 
            for the company {companyName} in the {department} and {additional_hints}.
            The job posting should include sections: summary, description, responsibilities, and qualifications.
            The summary should be no more than 50 words.
            Limit the responsibilities to no more than 10 items.\nLimit the qualifications to no more than 10 items.
            Generate a completed answer strictly fewer than 500 words."""
    response = client.generate_text(prompt)
    response = response.inference_response.generated_texts[0].text
    return f"Job Title: {businessTitle}\nCompany Name: {companyName}\nDepartment: {department}\nSkills: {additional_hints}\n\n{response}"

# Using callback functions to update the state
def update_input_fields(companyName, businessTitle, department, additional_hints):
    st.session_state['companyName'] = companyName
    st.session_state['businessTitle'] = businessTitle
    st.session_state['department'] = department
    st.session_state['additional_hints'] = additional_hints

def run():
    st.title(APPNAME)
    st.markdown(DESC)
    st.divider()
    with st.sidebar:
        st.header("Input Job Details")
        companyName = st.text_input("Company Name", key='companyName')
        businessTitle = st.text_input("Job Title", key='businessTitle')
        department = st.text_input("Department", key='department')
        additional_hints = st.text_input("Additional Hints", key='additional_hints')

        generate = st.button(label='Generate', type='primary')
        
        # Setting up callback functions
        with st.container(border=True):
            c1, c2 = st.columns(2)
            with c1:
                st.button("Load Example 1", on_click=update_input_fields, 
                          args=(example1['companyName'], example1['businessTitle'], example1['department'], example1['additional_hints']), 
                          use_container_width=True)
            with c2:
                st.button("Load Example 2", on_click=update_input_fields, 
                          args=(example2['companyName'], example2['businessTitle'], example2['department'], example2['additional_hints']),
                          use_container_width=True)
        
    if generate:
        job_description = createJD(st.session_state['businessTitle'], st.session_state['companyName'], st.session_state['department'], st.session_state['additional_hints'])
        st.subheader("Generated Job Description")
        st.write(job_description)


if __name__ == "__main__":
    st.set_page_config(
        page_title=APPNAME,
        layout='wide'
    )
    run()