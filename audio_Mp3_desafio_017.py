from pyglet import media, app

#Esta e a forma de colocar audio no Python no versao mais recente da biblioteca Pyglet, que e a mais atualizada para o Python 3.11.4

music = media.load("nelson.mp3")
music.play()
app.run()