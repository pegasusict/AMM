# Audiophiles Music Manager

### *init, configuration*:
[ configargparse, toml, path/pathtools? ]
Check for config file
if not present, run configuration wizard

### *Phase 0*:
[ path/pathtools? ] Scan source dir(s)
[ mysql.connector/mysqldb ] Add audio file paths to DB (mp3, m4a, mp2, wav, flac, aac, 3gp, ogg, mpc, wv, au, wma, opus, mid, mod, midi), set process flag to 0
[ path/pathtools? ] purge non-audio files

### *Phase 1*:
For each file:
[ mediainfodll, mutagen, audioread, soundfile?] Parse & purge tags
[ acoustid ] Generate audio fingerprint
[ mediainfodll, audioread, soundfile? ] Calculate audio quality based on codec, bitrate and channels
[ mysql.connector/mysqldb ] Store file stats in DB (size, type, length, codec, bitrate, tags, fingerprint, etc)


### *Phase 2*:
[ path/pathtools/sh? ] Find duplicate files based on fingerprint and delete files/ records based on quality

### *Phase 3*:
For each file in DB:
[ musicbrainzngs ] Retrieve information from MB
[ ??? ] Retrieve album cover, tabs(opt), lyrics(opt)

### *Phase 4*:
For each file in DB:
[ sh(lame) ] Transcode using comparable mp3 vbr quality, Normalize audio levels, Trim silence from beginning and end
[ mutagen ] Insert tags (inc “processed by AMM” & audio quality rating) & album cover & lyrics
            If {(albumartist == “various”) & (available tracks =< 50%)} then ((artist ~> albumartist) & (album=”compilations “))
[ path/pathtools? ] Move to destination & rename in accordance with the chosen path/file naming scheme

### *Phase 5*:
Generate & show/email/store/upload report (templates?)

### *Dependencies:*
-[] pythondialog
-[] configargparse / toml
-[] path / pathtools
-[] mysql.connector / mysldb
-[] mediainfodll / audioread / soundfile / mutagen
-[] acoustid
-[] musicbrainzngs
-[] sh
-[] 
