import re

def clean_output(text: str) -> str:
    return re.sub(r"◁think▷.*?◁/think▷", "", text, flags=re.DOTALL).strip()
