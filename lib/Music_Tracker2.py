class Track():
    def __init__(self, track_name, artist):
        self.track_name = track_name
        self.artist = artist
        self.update_artist()
    
    def update_artist(self):
        self.full_track = f"{self.track_name} by {self.artist}"
        

class MusicTracker():
    def __init__(self):
        self.track_list = []
    
    def add_track(self, track):
        self.track_list.append(track)

    def list_tracks(self):
        list_of_full_tracks = []
        for track in self.track_list:
            list_of_full_tracks.append(track.full_track)
        return list_of_full_tracks
    
"""
tracks = MusicTracker()
tracks.add_track("We are the Champions by Queen")
tracks.add_track("Waterloo by Abba")
tracks.list_track()
"""