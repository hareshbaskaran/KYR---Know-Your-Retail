from abc import ABC, abstractmethod
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.agents import AgentExecutor
from typing import Any


class BaseAgentExecutor(ABC):
    name: str

    def __init__(self, llm):
        self.llm = llm

    @abstractmethod
    def get_agent_executor(self) -> AgentExecutor:
        """
        This method must be implemented by derived classes to
        create and return the specific AgentExecutor instance.
        """
        pass

    def invoke_agent_executor(self, query: str) -> Any:
        """
        Shared implementation for invoking the agent executor.
        Derived classes don't need to override this unless custom logic is required.
        """
        agent_executor = self.get_agent_executor()
        return agent_executor.run(query)


class CsvAgentExecutor(BaseAgentExecutor):
    name = "CSV"

    def __init__(self, llm, csv_path: str):
        super().__init__(llm)
        self.csv_path = csv_path

    def get_agent_executor(self) -> AgentExecutor:
        """
        Implementation for creating an AgentExecutor for CSV data.
        """
        return create_csv_agent(
            llm=self.llm,
            path=self.csv_path,
            verbose=True,
            allow_dangerous_code=True,
        )
