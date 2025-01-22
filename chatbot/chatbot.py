import random
from .models import load_qa_model, get_answer_from_context
from .data_preprocessing import load_and_preprocess_data

def get_chatbot_response(user_query):
    # Load and preprocess data (this could be cached for performance)
    contexts, questions, answers = load_and_preprocess_data()

    # Load the pre-trained QA model
    qa_pipeline = load_qa_model()

    # Select a random context (In practice, you may want to have a more dynamic dataset)
    context = random.choice(contexts)

    # Get the answer based on the current context
    answer = get_answer_from_context(qa_pipeline, user_query, context)
    
    return answer
