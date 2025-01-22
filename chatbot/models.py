from transformers import pipeline

def load_qa_model():
    # Load pre-trained question-answering model from Hugging Face
    qa_pipeline = pipeline('question-answering', model='distilbert-base-uncased-distilled-squad', tokenizer='distilbert-base-uncased-distilled-squad')
    return qa_pipeline

def get_answer_from_context(qa_pipeline, question, context):
    result = qa_pipeline({
        'context': context,
        'question': question
    })
    
    return result['answer']
