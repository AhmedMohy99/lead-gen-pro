def log(message):
    with open("logs/app.log", "a") as f:
        f.write(message + "\n")
    print(message)
