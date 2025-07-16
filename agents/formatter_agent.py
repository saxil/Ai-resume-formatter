from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

class FormatterAgent:
    def __init__(self, openai_api_key: str, model_name: str = "gpt-4o", openrouter_api_base: str = None):
        if openrouter_api_base:
            self.llm = ChatOpenAI(model=model_name, temperature=0.7, openai_api_key=openai_api_key, base_url=openrouter_api_base, max_tokens=2000)
        else:
            self.llm = ChatOpenAI(model=model_name, temperature=0.7, openai_api_key=openai_api_key, max_tokens=2000)
        self.prompt = PromptTemplate(
            template="""You are an expert resume writer and formatter. Your task is to create a professional, ATS-friendly resume based on the provided data. The resume should be tailored to the target job role.

            **Parsed Resume Data:**
            {parsed_resume_data}

            **Target Job Role:**
            {job_role}

            **Instructions:**
            1.  **Contact Information:** At the top, list the name, email, phone number, and LinkedIn profile URL.
            2.  **Summary:** Write a brief, impactful summary (2-3 sentences) that highlights the candidate's key qualifications and career goals, tailored to the target job role.
            3.  **Experience:** For each work experience, list the job title, company, and dates. Use bullet points to describe the responsibilities and achievements. Start each bullet point with a strong action verb and quantify achievements whenever possible.
            4.  **Education:** List the degree, institution, and dates for each educational qualification.
            5.  **Skills:** Create a list of relevant skills, ensuring they align with the target job role.

            The final output should be a single block of text, formatted for a professional resume. Do not include any introductory or concluding remarks.
            """,
            input_variables=["parsed_resume_data", "job_role"],
        )
        self.chain = self.prompt | self.llm

    def format_resume(self, parsed_resume_data: dict, job_role: str) -> str:
        return self.chain.invoke({"parsed_resume_data": parsed_resume_data, "job_role": job_role})
