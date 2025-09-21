from sqlalchemy import create_engine
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits.sql.base import SQLDatabaseToolkit
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain_community.utilities import SQLDatabase
from langchain_community.llms import Ollama
import os
import urllib.parse
from langchain_experimental.tools.python.tool import PythonREPLTool
from langchain.agents import initialize_agent, AgentType

def get_engine():
    # Config
    user = os.getenv("DB_USER", "root")
    raw_password = os.getenv("DB_PASSWORD", "XXXXXXXX")
    encoded_password = urllib.parse.quote_plus(raw_password)
    host = os.getenv("DB_HOST", "localhost")
    db = os.getenv("DB_NAME", "ai_tdv_finacle")
    db_uri = f"mysql+pymysql://{user}:{encoded_password}@{host}/{db}"
    return create_engine(db_uri)


def get_llm_agent():
    engine = get_engine()
    db = SQLDatabase(engine)

    llm = Ollama(model="llama3:8b")  # Make sure Ollama is running
    tools = [
        QuerySQLDataBaseTool(db=db),
        PythonREPLTool()  
    ]
    
    agent_executor = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent_executor


def query_llm(question: str):
    agent = get_llm_agent()
    return agent.run(question)


# For testing
if __name__ == "__main__":
    print(query_llm("What is the total number of transactions?"))
