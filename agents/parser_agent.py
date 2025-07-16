from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class Resume(BaseModel):
    name: str = Field(description="Name of the applicant")
    email: str = Field(description="Email address of the applicant")
    phone: str = Field(description="Phone number of the applicant")
    linkedin: str = Field(description="LinkedIn profile URL of the applicant")
    experience: list[dict] = Field(description="List of work experiences, each with title, company, years, and description")
    education: list[dict] = Field(description="List of educational qualifications, each with degree, institution, and years")
    skills: list[str] = Field(description="List of skills")

import logging

class ParserAgent:
    def __init__(self, openai_api_key: str, base_url: str):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0, openai_api_key=openai_api_key, base_url=base_url, max_tokens=2000)
        self.parser = JsonOutputParser(pydantic_object=Resume)
        self.prompt = PromptTemplate(
            template="""Extract the following information from the resume text provided:
            {format_instructions}
            {resume_text}
            """,
            input_variables=["resume_text"],
            partial_variables={"format_instructions": self.parser.get_format_instructions()},
        )
        self.chain = self.prompt | self.llm | self.parser

    def parse_resume(self, resume_text: str) -> Resume:
        try:
            # Truncate resume_text to avoid exceeding token limits
            truncated_resume_text = resume_text[:7000]  # Limit to 7000 characters
            return self.chain.invoke({"resume_text": truncated_resume_text})
        except Exception as e:
            logging.error(f"Error in ParserAgent: {e}", exc_info=True)
            raise
