# command_runner.py

import subprocess
import config
from output_summarizer import op_summary

# Define the path to your tool
tool_path = config.TOOL_COMMAND

def run_tool(argument):
    """Runs the specified tool with the provided argument and returns the output."""
    try:
        command = f"{tool_path} {argument}"
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        if len(config.LLM_API) > 1:
        	output = op_summary(output)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error executing command: {e.output}"

