import requests
import json
import matplotlib.pyplot as plt
import os

# 定义API的URL
url = "http://localhost:5001/api/v1/generate"
# txt path 
txt_path = './asset/常驻人口.txt'
# promt dir
prompt_dir = './prompts/'
model = 'Hermes-3-Llama-3.1-8B.Q4_K_M.gguf'

def get_response_LLM(prompt):
    response = requests.post(url, json=prompt)
    result = response.json()
    # print(result)
    return result.get("results", [{}])[0].get("text", "")

def code_processor(code):
    lines = code.splitlines()
    new_code =[]
    found_import = False

    for line in lines:
        if 'import' in line:
            found_import = True
        if found_import:
            if "end of the code" in line:
                break
            new_code.append(line)
    return new_code

def process_data():
    prompt_1 = 'task1_prompt.json'
    print('[Task 1] Processing data in dir: ./assst with prompt at dir: '+prompt_dir+prompt_1)
    with open(prompt_dir+prompt_1,'r', encoding='utf-8') as file:
        prompt = json.load(file)
    code = get_response_LLM(prompt)
    new_code = code_processor(code)
    code = "\n".join(new_code)
    with open("process_data.py", "w", encoding="utf-8") as file:
        file.write(code)
    print("[Task 1] Data process program saved.")
    os.system('python ./process_data.py')
    print("[Task 1] Successfully processed the data.")
    print('-----------------------------------------')
    return 

def data_analysis():
    prompt_2 = 'task2_prompt.json'
    print('[Task 2]Analysing data in dir: ./assst with prompt at dir: '+ prompt_dir + prompt_2)
    with open(prompt_dir + prompt_2,'r', encoding='utf-8') as file:
        prompt = json.load(file)
    code = get_response_LLM(prompt)
    new_code = code_processor(code)
    code = "\n".join(new_code)
    with open("analysis_data.py", "w", encoding="utf-8") as file:
        file.write(code)
    print("[Task 2] Data analysis program saved.")
    os.system('python ./analysis_data.py')
    print("[Task 2] Successfully analyzed the data.")
    print('-----------------------------------------')
    return 

def draw_piechart():
    prompt_3 = 'task3_prompt.json'
    print('[Task 3] visualising data in dir: ./assst with prompt at dir: '+ prompt_dir + prompt_3)
    with open(prompt_dir + prompt_3,'r', encoding='utf-8') as file:
        prompt = json.load(file)
    code = get_response_LLM(prompt)
    new_code = code_processor(code)
    code = "\n".join(new_code)
    with open("draw_piechart.py", "w", encoding="utf-8") as file:
        file.write(code)
    print("[Task 3] Pie chart drawing program saved.")
    os.system('python ./draw_piechart.py')
    print("[Task 3] Successfully visualized the data.")
    print('-----------------------------------------')
    return 

def draw_linechart():
    prompt_4 = 'task4_prompt.json'
    print('[Task 4] visualising data in dir: ./assst with prompt at dir: '+ prompt_dir + prompt_4)
    with open(prompt_dir + prompt_4,'r', encoding='utf-8') as file:
        prompt = json.load(file)
    code = get_response_LLM(prompt)
    new_code = code_processor(code)
    code = "\n".join(new_code)
    with open("draw_linechart.py", "w", encoding="utf-8") as file:
        file.write(code)
    print("[Task 4] Line chart drawing program saved.")
    os.system('python ./draw_linechart.py')
    print("[Task 4] Successfully visualized the data.")
    print('-----------------------------------------')
    return 

def run_agent():
    process_data()
    data_analysis()
    draw_piechart()
    draw_linechart()

if __name__ == "__main__":
    run_agent()
