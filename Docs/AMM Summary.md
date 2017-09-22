# Audiophiles Music Manager

### *configuration*:
Check for config file
if not present, run configuration wizard

### *Phase 0*:
Scan source dir(s)
=> Add audio file paths to DB (mp3, m4a, mp2, wav, flac, aac, 3gp, ogg, mpc, wv, au, wma, opus, mid, mod, midi)
purge non-audio files

### *Phase 1*:
For each file:
-[ ] Store “wanted” tags in DB
-[ ] Purge all tags
-[ ] Generate audio fingerprint
-[ ] Store file stats in DB (size, type, length, codec, bitrate, etc)
-[ ] Calculate audio quality based on codec, bitrate and channels

### *Phase 2*:
Find duplicate files based on fingerprint and delete files/ records based on quality

### *Phase 3*:
For each file in DB:
-[ ] Retrieve information from MB
-[ ] Retrieve album cover, tabs(opt), lyrics(opt)
-[ ] Normalize audio levels
-[ ] Trim silence from beginning and end

### *Phase 4*:
Transcode audio files using comparable mp3 vbr quality (store vbr quality setting in tags & DB)
For each file:
-[ ] Insert tags (inc “processed by AMM” & audio quality rating) & album cover
-[ ] If {(albumartist == “various”) & (available tracks =< 50%)} then ((artist ~> albumartist) & (album=”compilations “))
-[ ] Move to destination & rename in accordance with the chosen path/file naming scheme

### *Phase 5*:
Generate & show/email/store/upload report

#### *Thinking about doing something with*:
Find higher quality versions of low quality tracks ( torrent, ftp search, usenet, etc)
