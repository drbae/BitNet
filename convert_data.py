import json

def convert_to_llama3_format(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    with open(output_file, 'w', encoding='utf-8') as f:
        for item in data['data_info']:
            question = item['question']
            answer = item['answer']['contents']

            # Llama 3 Instruct 템플릿 적용
            formatted_text = (
                "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\n"
                "You are a helpful assistant.<|eot_id|>"
                f"<|start_header_id|>user<|end_header_id|>\n\n{question}<|eot_id|>"
                f"<|start_header_id|>assistant<|end_header_id|>\n\n{answer}<|eot_id|>\n"
            )
            f.write(formatted_text)

if __name__ == "__main__":
    inFile = 'SFTlabel.json'
    outFile = 'sft_label.txt'

    dir = 'data/korean/training/'
    convert_to_llama3_format(f"{dir}{inFile}", f"{dir}{outFile}")
    print(f"변환 완료: {dir}{outFile}")

    dir = 'data/korean/validation/'
    convert_to_llama3_format(f"{dir}{inFile}", f"{dir}{outFile}")
    print(f"변환 완료: {dir}{outFile}")