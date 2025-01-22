responses = {
    "full stack python with ai": {
        "description": "The Full Stack Python with AI course covers Python, web development (Django/Flask), and AI frameworks like TensorFlow and PyTorch.",
        "duration": "6 months",
        "fees": "$1000",
    },
    "full stack java with ai": {
        "description": "The Full Stack Java with AI course includes Java programming, Spring framework, and AI integration with libraries like DL4J.",
        "duration": "6 months",
        "fees": "$1100",
    },
    "sdet": {
        "description": "The SDET course trains you in automation testing, Selenium, and CI/CD pipelines with a focus on quality engineering.",
        "duration": "4 months",
        "fees": "$800",
    },
}

def get_response(user_input):
    user_input = user_input.lower()
    if "python" in user_input:
        return responses["full stack python with ai"]
    elif "java" in user_input:
        return responses["full stack java with ai"]
    elif "sdet" in user_input or "testing" in user_input:
        return responses["sdet"]
    else:
        return {
            "description": "I'm sorry, I didn't understand that. Please ask about 'Full Stack Python with AI', 'Full Stack Java with AI', or 'SDET'.",
            "duration": "",
            "fees": "",
        }
