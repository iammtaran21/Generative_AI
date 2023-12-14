import os
from dotenv import load_dotenv,dotenv_values
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

load_dotenv()

if __name__ == '__main__':
    print("Hey")
    print(os.environ["KEY"])
    