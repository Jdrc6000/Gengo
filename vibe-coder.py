from pathlib import Path

main_path = Path("/Users/joshuacarter/Desktop/Coding/Code Vault/projects/gengo")
txt_path = main_path / "vibe-coded.txt"

full = ""
total_loc = 0

for file_path in sorted(main_path.rglob("*.py")):
    if file_path.name == txt_path.name or file_path.name == "vibe-coder.py" or file_path.name == "__init__.py":
        continue
    elif file_path.parent.name == "tests":
        continue

    content_text = file_path.read_text(encoding="utf-8")
    
    filtered_lines = [
        line for line in content_text.splitlines()
        if not line.strip().startswith("#")
    ]
    filtered_content = "\n".join(filtered_lines)
    
    content = f"--- {file_path.relative_to(main_path)} ---\n{filtered_content}\n\n"

    current_loc = filtered_content.count("\n") + 1
    full += content
    total_loc += current_loc

    print(f"({file_path.parent.name}) {file_path.name} LOC: {current_loc}")

print(f"LOC: {total_loc}")

txt_path.write_text(full, encoding="utf-8")