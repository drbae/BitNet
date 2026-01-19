from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
from trl import SFTTrainer
from datasets import load_dataset

# 1. 모델 및 토크나이저 로드 (BF16 버전 권장)
model_id = "models/bitnet-b1.58-2B-4T-bf16"
tokenizer = AutoTokenizer.from_pretrained(model_id)
dataset = load_dataset("nlpai-lab/kullm-v2", split="train[:10%]") # 예시 데이터

# 2. 학습 설정
training_args = TrainingArguments(
    output_dir="./bitnet-finetuned",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=8,
    learning_rate=1e-4,  # BitNet은 다소 높은 학습률이 효과적일 수 있음
    bf16=True,           # 가속기 지원 시 BF16 사용
    logging_steps=10,
    num_train_epochs=1,
    weight_decay=0.01
)

# 3. 트레이너 초기화 및 실행
trainer = SFTTrainer(
    model=model_id,
    train_dataset=dataset,
    dataset_text_field="instruction", # 데이터셋 필드명에 맞게 수정
    max_seq_length=512,
    args=training_args,
)

trainer.train()