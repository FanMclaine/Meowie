from flask import Flask
from threading import Thread
from animalpy import animals

app = Flask('')

@app.route('/')
def home(): 
    return f"""
    <html>
        <body style=font-family:Verdana;text-align:center;background:#696969;>
            <h1>fun fac!</h1>
            <p style='font-size:23'>{animals.fact("cat")}</p>
            <iframe width=45% height=45% src='https://www.youtube.com/embed/UIp6_0kct_U?autoplay=1' frameborder='1' allow=autoplay;encrypted-media>a</iframe>
            <h1>hav kat pic!!!!!</h1>
            <img src={animals.picture("cat")} alt='Cat pic' width=300px height=300px>
            <footer>
                <hr style='background-color:black'>
                <p><a href='https://speaklolcat.com' style='color:black'>lolspeak</a><br><a href='https://github.com/FanMclaine' style='color:black'>Mclnoot_</a><br><a href='https://vortex2571.neocities.org/cesiyi.html' style='color:black'>CascadingStyleSheets / Cesiyi</a></p>
            </footer>
        </body>
    </html>
    """

def run():
  app.run(host='0.0.0.0', port=8080)

def alive():  
    server = Thread(target=run)
    server.start()