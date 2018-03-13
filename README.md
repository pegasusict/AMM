
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d0d4ba2150274a66b9871a7f071fae39)](https://www.codacy.com/app/pegasus.ict/AMM?utm_source=github.com&utm_medium=referral&utm_content=pegasusict/AMM&utm_campaign=badger)

# Pegasus' Audiophiles' Music Manager

I've just started learning git(hub), Python and UML so suggestions and useful critique is grately appreciated!
My aim is to reply to any questions/suggestions etc within a week at most (excluding holidays).
All functionality described on this page is subject to change (usually I will not remove planned functionality unless replaced by something better) and may not be available in the early releases but wil be integrated eventually as this project is basically my lifes' work

***
## Audiophiles' Music Manager V0.0.0 pre-Alpha
(c) 2017-2018 Mattijs Snepvangers - pegasus-ict[at]gmail.com

A Suite that can REALLY manage ALL aspects of a digital Music Collection of ANY size (my collection consists of nearly 500k songs...)
***
### REQUIREMENTS:
* Python 3.x
* Lame codec
* dialog
* MySQL Server (will be required in early releases, later it will be made optional for small collections (maybe use SQLite for collections up to 50.000, still under debate)
### RECCOMENDED (when used on collections over 10k songs
* MySQL Server (preferably local socket connection due to large volume of data)
### Included Python Packages:
Nothing yet...
***
### WORKS:
* N/A
***
### Planned Functionality:
1. Index files, Purge Non-Audiofiles, Parse/Purge Tags, Store File- & Tag-Data in DB
2. Generate Audio-Fingerprint, Calculate Audio Quality, Remove Duplicates Based on Quality
3. Transcode &  Normalize
4. Retrieve Artistnames, Albumtitles, ft. Artists, Composer/writer, Albumart, Lyrics
5. Integrate Tags & Art in DB, Fix (& Opt Merge) Artistnames & Titles
6. Insert Tags in Files, Rename & Move Files to target dir structure
7. GUI, AJAX Interface & Android Client
9. DLNA media server, MPD/Audacious integration(?)
***
### Future ideas (maybe): 
* Acoustic Optimisation
* Automagic searching & downloading of missing songs
