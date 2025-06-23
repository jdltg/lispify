# llm-lispify

**llm-lispify** is an experimental project inspired by the research paper [“Lisp as a Tool for Large Language Models” (arXiv:2506.10021)](https://arxiv.org/abs/2506.10021).  
It explores combining Lisp’s symbolic programming strengths with large language models (LLMs) to create novel AI workflows.

---

## Project Structure

- `server.lisp` — Lisp server implementation for evaluating Lisp expressions  
- `ollama_lisp_tool_run.py` — Python integration script to run Lisp workflows with Ollama LLM  
- `lisp_server_run.sh` — Shell script to start the Lisp server  
- `test_lisp_server.sh` — Script to test Lisp server interaction  
- `test_eval_lisp_code.py` — Python tests for Lisp code evaluation  
- `README.md` — This file  

---

## About

Lisp’s code-as-data philosophy offers a unique way to represent and manipulate LLM outputs.  
This project explores Lisp as a “glue” language to orchestrate LLM-driven tasks.

It’s an early-stage research prototype, evolving rapidly.

---

## Paper Reference

Part of the research presented in:  
**“Lisp as a Tool for Large Language Models”**  
[https://arxiv.org/abs/2506.10021](https://arxiv.org/abs/2506.10021)

---

## Getting Started

```bash
git clone https://github.com/yourusername/llm-lispify.git
cd llm-lispify

# Start the Lisp server
./lisp_server_run.sh

# Run server interaction tests
./test_lisp_server.sh

# Run Python tests for Lisp evaluation
python3 test_eval_lisp_code.py

# Run the Ollama Lisp tool integration
python3 ollama_lisp_tool_run.py "Your prompt here"
```

---

## Usage: ollama_lisp_tool_run.py arguments

```python
parser = argparse.ArgumentParser(description="Call Ollama LLM with Lisp eval tool.")
parser.add_argument('prompt', type=str, help="User prompt to send to the LLM")
parser.add_argument('--model', type=str, default='llama3.1', help="LLM model name")
parser.add_argument('--lisp-server', type=str, default='http://localhost:8080/execute', help="URL of the Lisp evaluation server")
parser.add_argument('--context', type=str, default=None, help="Optional system/context instructions for the LLM")
```

### Example

```bash
python3 ollama_lisp_tool_run.py "Evaluate (+ 1 2 3)" --model llama3.1 --lisp-server http://localhost:8080/execute --context "You are a Lisp interpreter"
```

---

## Contributing

Contributions and feedback are welcome! Please open issues or submit pull requests.

---

## License

MIT License

---

## Contact

Created by [Your Name]. Reach out for questions or collaboration!

Project link: https://github.com/yourusername/llm-lispify
