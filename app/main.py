import argparse
import os
import sys
import json
import subprocess
from openai import OpenAI

API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("OPENROUTER_BASE_URL", default="https://openrouter.ai/api/v1")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("-p", required=True)
    args = p.parse_args()

    if not API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY is not set")

    client = OpenAI(api_key=API_KEY, base_url=BASE_URL)
    messages = [{"role": "user", "content": args.p}]
    while True:
        chat = client.chat.completions.create(
            model="anthropic/claude-haiku-4.5",
            messages=messages,
            tools=[{
                "type": "function",
                "function": {
                    "name": "Read",
                    "description": "Read and return the contents of a file",
                    "parameters": {
                        "type": "object",
                        "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "The path to the file to read"
                        }
                    },
                    "required": ["file_path"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "Write",
                    "description": "Write content to a file",
                    "parameters": {
                    "type": "object",
                    "required": ["file_path", "content"],
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "The path of the file to write to"
                        },
                        "content": {
                            "type": "string",
                            "description": "The content to write to the file"
                        }
                    }
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "Bash",
                    "description": "Execute a shell command",
                    "parameters": {
                    "type": "object",
                    "required": ["command"],
                    "properties": {
                        "command": {
                        "type": "string",
                        "description": "The command to execute"
                        }
                    }
                    }
                }
                }]
        )
        response_message = chat.choices[0].message
        response = chat.choices[0].message

        message_dirct = {"role": response.role, "content": response.content}

        if hasattr(response, "tool_calls") and response.tool_calls is not None:
            message_dirct["tool_calls"] =[
                {"id": tool_call.id, "type": tool_call.type, "function": {
                    "name": tool_call.function.name,
                    "arguments": tool_call.function.arguments
                }} for tool_call in response_message.tool_calls
            ]
        messages.append(message_dirct)
        if not message_dirct.get("tool_calls"):
            print(response.content)
            break

        if not chat.choices or len(chat.choices) == 0:
            raise RuntimeError("no choices in response")

        # You can use print statements as follows for debugging, they'll be visible when running tests.
       # print("Logs from your program will appear here!", file=sys.stderr)

        for tool_call in chat.choices[0].message.tool_calls or []:
            args = json.loads(tool_call.function.arguments)
            file_path = args["file_path"]
            if tool_call.type == "function" and tool_call.function.name == "Read":
                with open(file_path, "r") as f:
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "content": f.read()
                    })
            if tool_call.type == "function" and tool_call.function.name == "Write":
                content = args["content"]
                with open(file_path, "w") as f:
                    f.write(content)
                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "content": f"Wrote to {file_path}"
                })
            if tool_call.type == "function" and tool_call.function.name == "Bash":
                command = args["command"]
                output = subprocess.check_output(command, shell=True, text=True)
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                output = result.stdout + "\n" + result.stderr
                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "content": output
                })
        # TODO: Uncomment the following line to pass the first stage
       # if len(chat.choices[0].message.tool_calls or []) == 0:
           # print(chat.choices[0].message.content)
    # print(chat.choices[0].message.content)


if __name__ == "__main__":
    main()
