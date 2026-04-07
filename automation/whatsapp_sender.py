import webbrowser

def send_whatsapp(phone):
    msg = "Hello I can help you build a website to grow your business"
    url = f"https://wa.me/{phone}?text={msg}"
    webbrowser.open(url)
