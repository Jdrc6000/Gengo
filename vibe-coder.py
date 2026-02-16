from pathlib import Path
import re

main_path = Path("/Users/joshuacarter/Desktop/Coding/Code Vault/projects/forge")
txt_path = main_path / "vibe-coded.txt"

full = ""
total_loc = 0
total_code_loc = 0 # uses content_text instead of filtered_content

for file_path in sorted(main_path.rglob("*.py")):
    if file_path.name == txt_path.name or file_path.name == "vibe-coder.py" or file_path.name == "__init__.py":
        continue
    elif file_path.parent.name == "tests":
        continue

    content_text = file_path.read_text(encoding="utf-8")

    filtered_lines = []
    for line in content_text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue  # skip empty lines
        if stripped.startswith("#"):
            continue  # skip full-line comments
        
        # remove inline comments
        line_no_comment = re.sub(r'(?<!["\'])#.*$', '', line)
        
        if line_no_comment.strip():  # skip if the line is empty after removing comment
            filtered_lines.append(line_no_comment.rstrip())
    filtered_content = "\n".join(filtered_lines)
    
    content = f"--- {file_path.relative_to(main_path)} ---\n{filtered_content}\n\n"

    current_loc = filtered_content.count("\n") + 1
    full_loc = content_text.count("\n") + 1
    full += content
    total_loc += current_loc
    total_code_loc += full_loc

    print(f"({file_path.parent.name}) {file_path.name} LOC: {current_loc} ({full_loc})")

print(f"LOC: {total_loc}")
print(f"Full code LOC: {total_code_loc}")

txt_path.write_text(full, encoding="utf-8")