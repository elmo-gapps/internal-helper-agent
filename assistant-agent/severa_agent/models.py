from pydantic import BaseModel


class SeveraAgentRequest(BaseModel):
    prompt: str
