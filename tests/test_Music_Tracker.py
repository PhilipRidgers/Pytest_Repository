from lib.Music_Tracker import *


"""
tracks = MusicTracker()
tracks.add_track("We are the Champions by Queen")
tracks.add_track("Waterloo by Abba")
tracks.list_track()
"""

"""
Ensure that an empty list doesn't cause issues.
"""
def test_empty_list():
    tracks = MusicTracker()
    assert tracks.track_list == []

"""
Ensure that adding a track to the list works!
"""
def test_add_track():
    tracks = MusicTracker()
    tracks.add_track("We are the Champions by Queen")
    assert tracks.track_list == ["We are the Champions by Queen"]

"""
Ensure that the correct track list is shown after two tracks have been added.
"""

def test_track_list_is_correct():
    tracks = MusicTracker()
    tracks.add_track("We are the Champions by Queen")
    tracks.add_track("Waterloo by Abba")
    assert tracks.list_track() == ["We are the Champions by Queen", "Waterloo by Abba"]