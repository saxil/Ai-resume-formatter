from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

class FormatterAgent:
    def __init__(self, openai_api_key: str, model_name: str = "gpt-4o", openrouter_api_base: str = None):
        if openrouter_api_base:
            self.llm = ChatOpenAI(model=model_name, temperature=0.7, openai_api_key=openai_api_key, base_url=openrouter_api_base)
        else:
            self.llm = ChatOpenAI(model=model_name, temperature=0.7, openai_api_key=openai_api_key)
        self.prompt = PromptTemplate(
            template="""You are an expert resume formatter. Given the following parsed resume data and a target job role, rewrite and format the resume content to be clean, professional, and optimized for the specified role.

            Parsed Resume Data: {parsed_resume_data}
            Target Job Role: {job_role}

            Ensure the output is a well-structured, professional resume in plain text format. Focus on clarity, conciseness, and impact. Highlight relevant skills and experiences for the target role.
            """,
            input_variables=["parsed_resume_data", "job_role"],
        )
        self.chain = self.prompt | self.llm

    def format_resume(self, parsed_resume_data: dict, job_role: str) -> str:
        return self.chain.invoke({"parsed_resume_data": parsed_resume_data, "job_role": job_role})
