from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.llms import OpenAI
from secret_key import openapi_key

import os
os.environ['OPENAI_API_KEY'] = openapi_key
llm=OpenAI(temperature=0.7)


def resto_names_items(cuisine):
#Chain 1    
    prompt_temp_names=PromptTemplate(
        input_variables=['cuisine'],
        template="I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.")
    name_chain=LLMChain(llm=llm,prompt=prompt_temp_names,output_key="resto_name")    

#Chain 2
    prompt_temp_items=PromptTemplate(
        input_variables=['resto_name'],
        template="""Suggest 5 top menu items for {resto_name}. 
        Return it as a comma separated string""")
    items_chain=LLMChain(llm=llm,prompt=prompt_temp_items,output_key="resto_items")

    chain=SequentialChain(
        chains=[name_chain,items_chain],
        input_variables=['cuisine'],
        output_variables=['resto_name','resto_items']
    )

    response=chain({'cuisine':cuisine})
    return response

if __name__ == "__main__":
    print(generate_restaurant_name_and_items(cuisine))