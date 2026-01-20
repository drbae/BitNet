# 모델 및 토크나이저 로드

from unsloth import FastLanguageModel
import torch

max_seq_length = 2048  # 문장길이
dtype = None  # 자동감지
load_in_4bit = True  # 4비트 로드 활성화 ~ 메모리 절약

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="models/llama-3-8b-Instruct-bnb-4bit",
    max_seq_length=max_seq_length,
    dtype=dtype,
    load_in_4bit=load_in_4bit,
)

# LoRA 어댑터 설정
# 모델 전체를 학습시키는 대신 일부 파라미터만 학습시키는 LoRA 설정을 추가합니다.
model = FastLanguageModel.get_peft_model(
    model=model,
    r=16,
    target_modules=[
        "q_proj",
        "k_proj",
        "v_proj",
        "o_proj",
        "gate_proj",
        "up_proj",
        "down_proj",
    ],
    lora_alpha=16,
    lora_dropout=0,
    bias="none",
    use_gradient_checkpointing="unsloth",
)

# 데이터셋 로드 및 학습 (SFTTrainer)
from trl import SFTTrainer
from transformers import TrainingArguments
from datasets import load_dataset
from unsloth import get_chat_template

# 변환
tokenizer = get_chat_template(tokenizer, template_name="llama-3")
def formatting_prompts_func(example):
    instructions = example["instruction"]
    inputs = example["input"]
    outputs = example["output"]
    texts = []
    for instruction, input, output in zip(instructions, inputs, outputs):
        parts = [
          {"role": "user", "content": f"{instruction}\n{input}"},
          {"role": "assistant", "content": output},
        ]
        texts.append(tokenizer.apply_chat_template(parts, tokenize=False, add_generation_prompt=False))
    return {"text": texts}

# 학습할 데이터셋 로드 (예: 고유한 질문-답변 쌍)
dataset = load_dataset("./data/korean", split="train")
dataset = dataset.map(formatting_prompts_func, batched=True)

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    dataset=dataset,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    args=TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        warmup_steps=5,
        max_steps=60,
        learning_rate=2e-4,
        fp16=not torch.cuda.is_bf16_supported(),
        bf16=torch.cuda.is_bf16_supported(),
        logging_steps=1,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=3407,
        output_dir="./models/llama3-8b-Instruct-lora-sft",
        # num_train_epochs= 3,
        # save_total_limit= 3,
        # save_steps= 200,
        # remove_unused_columns= False,
    ),
)

trainer.train()

model.save_pretrained("./models/llama3-8b-Instruct-lora-sft")
model.save_pretrainded_gguf(
    "./models/llama3-8b-Instruct-lora-sft/model.gguf",
    tokenizer=tokenizer,
    quantization_method="q4_k_m",
)
