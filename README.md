[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d0d4ba2150274a66b9871a7f071fae39)](https://www.codacy.com/app/pegasus.ict/AMM?utm_source=github.com&utm_medium=referral&utm_content=pegasusict/AMM&utm_campaign=badger)

# Audiophiles' Music Manager V0.0.0-DRAFT
All functionality described on this page is subject to change (usually I will not remove planned functionality unless replaced by something better) and may not be available in the early releases but wil be integrated eventually as this project is basically my lifes' work

(c) 2017-2020 Mattijs Snepvangers

## GOAL
My goal is to write an application that can REALLY _manage_ ALL aspects of a digital Music Collection of ANY size (my collection consists of a little over 500k songs...)
Eventually it will be written in Python 3.8+ but I've decided to make a draft in bash4+/php7.4+ first to get a feel for what I'm trying to accomplish when 

### (planned) REQUIREMENTS:
Draft Version:
* Bash 4/5
* GNU find
* fdupes
* fpcalc
* apache/nginx/ etc running PHP 7.4+ and PHP-cli 7.4+
* MySQL/MariaDB Server and CLI
Planned Version 1.0:
* Python 3.x
* MySQL/MariaDB Server

### Planned Functionality (MoSCoW prioritizing):
1. *M* Index files, Purge Non-Audiofiles, Parse & Purge Tags, Store File- & Tag-Data in DB
2. *M* Generate Audio-Fingerprint, Calculate Audio Quality(bitrate/channels/sampling), Remove Duplicates Based on Quality
3. *S* Transcode &  Normalize
4. *S* Retrieve Artistnames, Albumtitles, ft. Artists, Composer/writer, Albumart, Lyrics
5. *M* Integrate Tags & Art in DB, Fix (& Merge) Artistnames & Titles
6. *M* Insert Tags in Files, Rename & Move Files to target dir structure
7. *C* GUI, *S* AJAX Interface & *W* Android Client
9. *W* DLNA media server, MPD/Audacious integration(?)

***
### Future ideas (stil under debate):
* Acoustic Optimisation
* Automagic searching & downloading of missing songs
