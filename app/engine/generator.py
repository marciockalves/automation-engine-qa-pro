import os
from jinja2 import Environment, FileSystemLoader
from app.core.schemas import FullScenariosSchema

class TestGenerator:
    def __init__(self):
        template_path = os.path.join(os.path.dirname(__file__), "templates")
        self.env = Environment(loader=FileSystemLoader(template_path))
        self.template = self.env.get_template("test_case.jinja")

    def _slugify(self, text: str) -> str:
        return text.lower().replace(" ","_").replace("\"","").replace("'","")

    def generate(self, data: FullScenariosSchema):
        render_data = {
            "feature_path": f"../features/{data.metadata.test_title}.feature",
            "steps": []
        }

        for step in data.steps:
            render_data["steps"].append({
                "type": "when",
                "description": step.step_description,
                "function_name": self._slugify(step.step_description),
                "executions": step.executions,
                "screenshot": step.screenshot
            })

        output_code = self.template.render(render_data)

        target_dir = os.path.join("scenarios", data.metadata.app_name)
        os.makedirs(target_dir, exist_ok=True)

        file_path = os.path.join(target_dir, f"test_{data.metadata.test_title}.py")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(output_code)

        return file_path