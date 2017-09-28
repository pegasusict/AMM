#!/usr/bin/env python3 -tt
"""
************************************************************************
** Audiophiles Music Manager                         VER0.0.0PREALPHA **
** (C)2017 Mattijs Snepvangers                  pegasus.ict@gmail.com **
** inetc.py              internet client             VER0.0.0PREALPHA **
** License: MIT                    Please keep my name in the credits **
************************************************************************
"""

def lookup_fp(fingerprint, duration):
    """Query MusicBrainz with given fingerprint"""
    import acoustid
    mb_json = acoustid.lookup(mb_apikey, fingerprint, duration)
    ### lookup(apikey, fingerprint, duration): Make a request to the
      ### Acoustid API to look up the fingerprint returned by the
      ### previous function. An API key is required, as is the length,
      ### in seconds, of the source audio. Returns a parsed JSON
      ### response.
    result = acoustid.parse_lookup_result(mb_json)
    ### parse_lookup_result(data): Given a parsed JSON response, return
      ### an iterator over tuples containing the match score (a float
      ### between 0 and 1), the MusicBrainz recording ID, title, and
      ### artist name for each match
    return result

def cddb_query(cd_id):
    """Query cddb.org for information regarding cd_id(?)

    """

def get_albumart(albumArtist, albumTitle):
    """Download album art

    search online for album art which goes with the combination of
    albumTitle/albumArtist"""

def get_lyrics(artist, title):
    """Download lyrics

    search online for lyrics which goes with the combination of
    title/artist"""
