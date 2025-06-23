import requests

def run_lisp_code(code, url="http://localhost:8080/execute"):
    """
    Sends Lisp code to the Lisp server and returns the output as text.
    
    Parameters:
        code (str): The Lisp code to evaluate.
        url (str): The URL of the Lisp server endpoint.
        
    Returns:
        str: The result returned by the Lisp server.
    """
    try:
        response = requests.get(url, params={"code": code})
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        return f"Error communicating with Lisp server: {e}"

# Example usage
if __name__ == "__main__":
    lisp_code = "(+ 1 2 3)"
    output = run_lisp_code(lisp_code)
    print(f"Output from Lisp server: {output}")
