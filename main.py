from flask import Flask, render_template, request, redirect
from download_song import download_song
from mash_songs import mash_songs
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def landingPage():
    if request.method == 'POST':
        url_a_track = request.form['a_track']
        url_b_track = request.form['b_track']
        file_a_track = download_song().download(url=url_a_track)
        print(file_a_track)
        file_b_track = download_song().download(url=url_b_track)
        return redirect('/mash-up')
    return render_template('form.html')

@app.route('/mash-up')
def mashup():
    tracks = os.listdir('./downloads/')
    mash_songs().mash('./downloads/' + tracks[0],'./downloads/' + tracks[1])
    os.remove('./downloads/' + tracks[0])
    os.remove('./downloads/' + tracks[1])
    return 'done, check' + os.listdir('./mashups/') + 'for result'

if __name__ == '__main__':
    app.run(debug=True)
