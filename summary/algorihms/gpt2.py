

# from transformers import GPT2Tokenizer,GPT2LMHeadModel


# def gpt2_summary(text):
#     tokenizer=GPT2Tokenizer.from_pretrained('gpt2')
#     model=GPT2LMHeadModel.from_pretrained('gpt2')
#     inputs=tokenizer.batch_encode_plus([text],return_tensors='pt',max_length=1024)
#     summary_ids=model.generate(inputs['input_ids'],early_stopping=True)
#     GPT_summary=tokenizer.decode(summary_ids[0],skip_special_tokens=True)
#     return GPT_summary