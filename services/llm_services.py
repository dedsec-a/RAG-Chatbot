from langchain_groq import ChatGroq
from config.settings import groq_api_key
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain

# Function to generate the Answer from the Prompt 

def generate_answer(docs,question):
    llm = ChatGroq(api_key=groq_api_key,model="gemma2-9b-it")
    prompt = ChatPromptTemplate.from_template(
        """You are a very good Event Manager and your work is to give details about the aksed event very accurately
        answer the question in given context only
        <context>
        {context}
        <context>
        Question :{input}"""
    )
    chain = create_stuff_documents_chain(llm=llm,prompt=prompt)
    return chain.invoke({"context":docs,"input":question})[::]

