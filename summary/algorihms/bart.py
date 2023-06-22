# from transformers import BartForConditionalGeneration, BartTokenizer, BartConfig
# from transformers import pipeline


# def bart(text):
#     tokenizer=BartTokenizer.from_pretrained('facebook/bart-large-cnn')
#     model=BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
#     summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
#     inputs = tokenizer.encode(text,
#     return_tensors='pt',
#     max_length=1024,
#     truncation=True)
#     summary_ids = model.generate(inputs, max_length=1024, min_length=80, length_penalty=5., num_beams=2)
#     bart_summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
#     return bart_summary
