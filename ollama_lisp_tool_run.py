import argparse
import requests
from ollama import chat, ChatResponse

# Tool definition
eval_common_lisp_tool = {
    'type': 'function',
    'function': {
        'name': 'eval_common_lisp',
        'description': 'Evaluate Common Lisp code on the Lisp server and return the output.',
        'parameters': {
            'type': 'object',
            'required': ['code'],
            'properties': {
                'code': {
                    'type': 'string',
                    'description': 'Common Lisp code to be evaluated',
                },
            },
        },
    },
}

# Function to call Lisp server
def eval_common_lisp(code: str, server_url: str) -> str:
    try:
        response = requests.get(server_url, params={"code": code})
        response.raise_for_status()
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

available_functions = {
    'eval_common_lisp': eval_common_lisp,
}

def main():
    parser = argparse.ArgumentParser(description="Call Ollama LLM with Lisp eval tool.")
    parser.add_argument('prompt', type=str, help="User prompt to send to the LLM")
    parser.add_argument('--model', type=str, default='llama3.1', help="LLM model name")
    parser.add_argument('--lisp-server', type=str, default='http://localhost:8080/execute', help="URL of the Lisp evaluation server")
    parser.add_argument('--context', type=str, default=None, help="Optional system/context instructions for the LLM")

    args = parser.parse_args()

    messages = []

    # Add context if provided
    if args.context:
        messages.append({'role': 'system', 'content': args.context})

    messages.append({'role': 'user', 'content': args.prompt})

    response: ChatResponse = chat(
        args.model,
        messages=messages,
        tools=[eval_common_lisp_tool]
    )

    if response.message.tool_calls:
        for tool_call in response.message.tool_calls:
            fn_name = tool_call.function.name
            fn_args = tool_call.function.arguments
            if fn_name in available_functions:
                print(f"Calling tool function: {fn_name} with args: {fn_args}")
                output = available_functions[fn_name](**fn_args, server_url=args.lisp_server)
                print("Tool output:", output)
            else:
                print(f"Function {fn_name} not found")

        messages.append(response.message)
        messages.append({'role': 'tool', 'name': fn_name, 'content': output})
        final_response = chat(args.model, messages=messages)
        print("Final model response:", final_response.message.content)

    else:
        print("No tool calls from model")
        print("Model response:", response.message.content)

if __name__ == "__main__":
    main()
