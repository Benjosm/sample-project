# src/plan_reader.py

def parse_plan(plan_text):
    tasks = []
    for line in plan_text.splitlines():
        line = line.strip()
        if line.startswith("-"):
            task = line[1:].strip()
            tasks.append(task)
        elif line.startswith("- "):
           task = line[2:].strip()
           tasks.append(task)
        elif line.startswith("  -"):
            task = line[3:].strip()
            tasks.append(task)
        elif line.startswith("-  "):
            task = line[3:].strip()
            tasks.append(task)
        elif line.startswith("1. "):
            task = line[3:].strip()
            tasks.append(task)
            
    return tasks