def excape_chars(strings_array, text):
    return any(string in text for string in strings_array)

SHELL_ESCAPE_CHARS = [":", "curl", "bash", "bin", "sh", "exec", "eval,", "|", "import", "chr", "subprocess", "pty", "popen", "read", "get_data", "echo", "builtins", "getattr"]
import subprocess
import os
def pyjail(text):
    if excape_chars(SHELL_ESCAPE_CHARS, text):
        return "No shells are allowed"

    text = f"print(eval(\"{text}\"))"
    proc = subprocess.Popen(['python3', '-c', text], stdout=subprocess.PIPE, preexec_fn=os.setsid)
    output = ""
    try:
        out, err = proc.communicate(timeout=1)
        output = out.decode().replace("\r", "")
        print(output)
        print('terminating process now')
        proc.terminate()
    except Exception as e:
        proc.kill()
        print(e)

    if output:
        return f"```{output}```"

while True:
    print(pyjail(input('>>> ')))
