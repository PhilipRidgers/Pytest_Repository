
class MusicTracker():
    def __init__(self):
        self.track_list = []
    
    def add_track(self, track):
        self.track_list.append(track)

    def list_track(self):
        return self.track_list

    
"""
tracks = MusicTracker()
tracks.add_track("We are the Champions by Queen")
tracks.add_track("Waterloo by Abba")
tracks.list_track()
"""
