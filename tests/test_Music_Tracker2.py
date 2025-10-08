from lib.Music_Tracker2 import *

"""
Test that track name and artist are correctly passed in
"""

def test_instantiaton():
    track = Track("Mastermind", "Taylor Swift")
    assert track.full_track == "Mastermind by Taylor Swift"


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
    track1 = Track("We are the Champions", "Queen")
    music_tracker = MusicTracker()
    music_tracker.add_track(track1)
    assert music_tracker.list_tracks() == ["We are the Champions by Queen"]

def test_add_two_tracks():
    track1 = Track("We are the Champions", "Queen")
    track2 = Track("Actually Romantic", "Taylor Swift")
    music_tracker = MusicTracker()
    music_tracker.add_track(track1)
    music_tracker.add_track(track2)
    assert music_tracker.list_tracks() == ["We are the Champions by Queen", \
    "Actually Romantic by Taylor Swift"]

def test_no_tracks():
    noTrack = Track("", "")
    music_tracker = MusicTracker()
    music_tracker.add_track(noTrack)
    assert music_tracker.list_tracks() == [" by "]


"""
>>> track1 = Track("We are the Champions", "Queen")
>>> track2 = Track("Example", "ArtistMcArtist")
>>> track1
<__main__.Track object at 0x100bc5190>
>>> track2[0]
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'Track' object is not subscriptable
>>> track2.artist
'ArtistMcArtist'
>>> music_tracker = MusicTracker()
>>> music_tracker.add_track(track1)
>>> music_tracker.track_list
[<__main__.Track object at 0x100bc5190>]
>>> music_tracker.add_track(track2)
>>> music_tracker.track_list
[<__main__.Track object at 0x100bc5190>, <__main__.Track object at 0x100bc52d0>]
>>> music_tracker.list_tracks()
['We are the Champions by Queen', 'Example by ArtistMcArtist']
>>> music_tracker.list_tracks
<bound method MusicTracker.list_tracks of <__main__.MusicTracker object at 0x100bc5390>>
>>> [track.artist for track in music_tracker.track_list]
['Queen', 'ArtistMcArtist']
>>> [f"{track.artist} {track.track_name}"  for track in music_tracker.track_list]
['Queen We are the Champions', 'ArtistMcArtist Example']
>>> track2.artist = "Artist Mc Artist"
>>> [f"{track.artist} {track.track_name}"  for track in music_tracker.track_list]
['Queen We are the Champions', 'Artist Mc Artist Example']
>>> 
"""