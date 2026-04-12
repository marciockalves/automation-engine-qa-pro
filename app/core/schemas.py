from pydantic import BaseModel, Field
from typing import List, Optional

class ActionSchema(BaseModel):
    event: str
    attribute: Optional[str]=None
    values: Optional[str]=None
    index: int = 0
    type:str = "str"

class StepSchema(BaseModel):
    step_description: str
    screenshot: bool = False
    order_shot: Optional[str]= "after"
    executions: List[ActionSchema] = []

class ProjectMetadata(BaseModel):
    app_name: str
    scenario_category: str
    test_title: str
    internal_path: str = "/app/scenarios"

class FullScenariosSchema(BaseModel):
    metadata: ProjectMetadata
    steps: List[StepSchema]