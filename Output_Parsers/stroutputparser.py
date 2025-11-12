from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model=ChatHuggingFace(llm=llm)
template_1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']
)

template_2=PromptTemplate(
    template='write a five line summary on the following text./n{text}',
    input_variables=['text']

)
parser=StrOutputParser()

chain=template_1| model|parser|template_2|model|parser
result=chain.invoke({'topic':"balck hole"})

print(result)
