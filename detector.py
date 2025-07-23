import datetime

def detect_email(pipeline, email_text):
    result = pipeline.predict([email_text])[0]
    log_result(email_text, result)
    return result

def log_result(email_text, result):
    with open("logs/alerts.log", "a") as f:
        f.write(f"[{datetime.datetime.now()}] RESULT: {result} | EMAIL: {email_text[:100]}...\n")
