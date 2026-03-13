"""
AI Commit Agent
Analyzes the Python codebase and adds a small, meaningful feature each day.
Uses Google Gemini (free tier) via google-genai.
"""

import os
import json
from google import genai
from google.genai import types


def get_python_files(root="."):
    """Collect all Python files in the repo, excluding hidden and venv dirs."""
    py_files = {}
    exclude_dirs = {".git", ".github", "__pycache__", "venv", ".venv", "node_modules", "dist", "build"}

    abs_root = os.path.abspath(root)
    print(f"🔍 Scanning for Python files in: {abs_root}")

    for dirpath, dirnames, filenames in os.walk(abs_root):
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        for fname in filenames:
            if fname.endswith(".py"):
                fpath = os.path.join(dirpath, fname)
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        content = f.read()
                    rel_path = os.path.relpath(fpath, abs_root)
                    py_files[rel_path] = content
                    print(f"   Found: {rel_path}")
                except Exception as e:
                    print(f"   Could not read {fpath}: {e}")

    return py_files


def build_codebase_summary(py_files):
    """Build a summary string of the codebase for the prompt."""
    parts = []
    for path, content in list(py_files.items())[:20]:
        snippet = content[:3000]
        parts.append(f"### {path}\n```python\n{snippet}\n```")
    return "\n\n".join(parts)


def run_ai_agent(codebase_summary):
    """Call Gemini to decide on and implement a small feature addition."""
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    prompt = f"""You are a senior Python developer working on a project.
Your job is to add ONE small, useful, self-contained feature to the codebase every day.

Rules:
- Make only ONE focused improvement (a new utility function, input validation, a helper, a small class method, etc.)
- The change must be syntactically correct Python
- Keep the change minimal and coherent with existing code style
- Do NOT rewrite existing logic
- Do NOT change unrelated files

You must respond with ONLY valid JSON (no markdown, no code fences) in this exact format:
{{
  "file": "<relative file path to modify>",
  "new_content": "<complete new content of that file>",
  "commit_message": "<short commit message describing the feature, max 72 chars>",
  "description": "<1-2 sentences explaining what was added and why>"
}}

Here is the current Python codebase:

{codebase_summary}

Analyze the code and add one small, meaningful feature. Return ONLY the JSON."""

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=4096,
            temperature=0.4,
        ),
    )
    return response.text


def apply_changes(result_json):
    """Parse AI response and apply file changes."""
    text = result_json.strip()
    if text.startswith("```"):
        text = text.split("```")[1]
        if text.startswith("json"):
            text = text[4:]
    text = text.strip()

    data = json.loads(text)

    file_path = data["file"]
    new_content = data["new_content"]
    commit_message = data["commit_message"]
    description = data.get("description", "")

    os.makedirs(os.path.dirname(file_path) if os.path.dirname(file_path) else ".", exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ Modified: {file_path}")
    print(f"📝 Description: {description}")
    print(f"💬 Commit message: {commit_message}")

    with open("/tmp/commit_message.txt", "w") as f:
        f.write(commit_message)

    return file_path, commit_message


def main():
    print("🤖 AI Commit Agent starting...")

    py_files = get_python_files()
    if not py_files:
        print("❌ No Python files found. Make sure your repo has at least one .py file.")
        return

    print(f"📂 Found {len(py_files)} Python file(s)")

    codebase_summary = build_codebase_summary(py_files)

    print("🧠 Asking Gemini for a feature suggestion...")
    result = run_ai_agent(codebase_summary)

    print("⚙️  Applying changes...")
    apply_changes(result)

    print("✅ Done! Changes are ready to commit.")


if __name__ == "__main__":
    main()