import subprocess

def convert_to_pptx(input, output):
    subprocess.check_call(["pandoc", input , "-o", output])