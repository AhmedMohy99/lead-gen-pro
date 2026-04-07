logger.pyfrom datetime import datetime

def log(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs/app.log", "a") as f:
        f.write(f"[{time}] {message}\n")
    print(message)
