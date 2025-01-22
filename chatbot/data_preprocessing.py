from transformers import pipeline
import spacy
from datasets import load_dataset
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load pre-trained model for question answering from Hugging Face
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
nlp = spacy.load("en_core_web_md")

# Load the SQuAD dataset
squad_dataset = load_dataset('squad')

# Extract contexts, questions, and answers
contexts = [data['context'] for data in squad_dataset['train']]
questions = [data['question'] for data in squad_dataset['train']]
answers = [data['answers']['text'][0] for data in squad_dataset['train']]

def get_most_relevant_context(user_query, contexts):
    # Convert user query into a spaCy document
    query_doc = nlp(user_query.lower())
    
    # List to hold the similarity scores
    similarities = []
    
    # Compare the user's query with each context
    for context in contexts:
        context_doc = nlp(context.lower())
        similarity = cosine_similarity([query_doc.vector], [context_doc.vector])
        similarities.append(similarity)
    
    # Get the context with the highest similarity score
    best_match_index = np.argmax(similarities)
    return contexts[best_match_index]

def get_answer_from_context(question, context):
    # Use Hugging Face pipeline to get the answer from the context
    result = qa_pipeline({
        "context": context,
        "question": question
    })
    return result['answer']

def get_chatbot_response(user_query):
    # Get the most relevant context based on user query
    context = get_most_relevant_context(user_query, contexts)
    print(f"Using context: {context}")  # Debugging: Print the selected context
    return get_answer_from_context(user_query, context)
