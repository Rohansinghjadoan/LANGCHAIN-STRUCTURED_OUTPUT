from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser  # ✅ available in your version

load_dotenv()

# Step 1: Define the LLM
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# Step 2: Define parser (we'll enforce structure via format_instructions)
parser = JsonOutputParser()

# Step 3: Build prompt template with explicit JSON schema
template = PromptTemplate(
    template=(
        "Give 3 facts about {topic}.\n"
        "Return the output strictly as valid JSON in this format:\n"
        "{{\n"
        "  \"fact_1\": \"<first fact>\",\n"
        "  \"fact_2\": \"<second fact>\",\n"
        "  \"fact_3\": \"<third fact>\"\n"
        "}}\n"
        "{format_instructions}"
    ),
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# Step 4: Chain prompt → model → parser
chain = template | model | parser

# Step 5: Run
result = chain.invoke({"topic": "black hole"})
print("✅ Structured Output:\n", result)
