import re
import json

def process_file(file_path):
    all_messages = []
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        qa_pairs = re.findall(r'\d+\..*?問題："(.*?)".*?回答："(.*?)"', content, re.DOTALL)
        for idx, (question, answer) in enumerate(qa_pairs, start=1):
            system_content = "輸入想讓GPT成為的樣子"
            messages = [
                {"role": "system", "content": system_content},
                {"role": "user", "content": question},
                {"role": "assistant", "content": answer}
            ]
            all_messages.append({"messages": messages})
    return all_messages

# 輸入和輸出檔案路徑
input_file_path = "輸入.txt"
output_file_path = "輸出.jsonl"

result = process_file(input_file_path)

# 將結果寫入輸出檔案中
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for message_dict in result:
        json_str = json.dumps(message_dict, ensure_ascii=False)
        output_file.write(json_str + "\n")

print("已將結果輸出至", output_file_path)