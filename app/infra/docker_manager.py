import subprocess
import os

class DockerManager:
    def __init__(self, container_name: str = "plyawright_engine"):
        self.container_name = container_name

    def run_test(self, test_path: str) -> str:
        command = [
            "docker", "compose", "exec","-T",
            "playwright", "pyetst", test_path,
            "--headed", "-s"
        ]

        try:
            process = subprocess.Popen(
                command, 
                stdout = subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                env=os.environ.copy()
            )

            output_log = []
            if process.stdout:
                for line in process.stdout:
                    print(f"[DOCKER]: {line.strip()}")
                    output_log.append(line)
            
            process.wait()
            return "".join(output_log)
        
        except Exception as e:
            return f"Erro ao executar no Docker: {str(e)}"
        
    def ensure_shost(self):
        try:
            subprocess.run(["xhost", "+local:docker"], capture_output=True)
            return True
        except:  # noqa: E722
            return False
        
    