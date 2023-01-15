from pydub import AudioSegment

class mash_songs:

    def mash(self, a_track_loc, b_track_loc):
        a_track = AudioSegment.from_file(a_track_loc, format="mp3")
        b_track = AudioSegment.from_file(b_track_loc, format="mp3")
        overlay = a_track.overlay(b_track)

        print(a_track.dBFS)
        print(b_track.dBFS)

        overlay.export("./mash", format="mp3")
