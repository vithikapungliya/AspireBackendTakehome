from .data_aggregation import llm_input
from langchain_core.prompts import PromptTemplate
from .llm_service import model



prompt= """
ASPIRE is an application mapping course contents, tracking student knowledge, and facilitating various educational aids or interventions, the ultimate goal being to improve student outcomes university wide. 
A list of courses and their summaries are provided. Furthermore the pre requistives for the course and its summary has been provided. 
Use this information and generate a summary for this module {module}.
The data is as follows {data}
"""

def get_llm_response(label,collection):
    llm = model()
    context = llm_input(label,collection)
    prompt_template = PromptTemplate.from_template(prompt)
    summary_prompt = prompt_template.format(module=label, data=context)
    response = llm.invoke(summary_prompt)
    print(response)
    return response.content

# output = get_llm_response("Introduction to Functions")
# print(output)