[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d0d4ba2150274a66b9871a7f071fae39)](https://www.codacy.com/app/pegasus.ict/AMM?utm_source=github.com&utm_medium=referral&utm_content=pegasusict/AMM&utm_campaign=badger)

# Audiophiles' Music Manager V0.0.0-DEV
Updated: 2021-02-05
Copyleft: 2017-2021 Mattijs Snepvangers
Licence: GPL v3+

## GOAL

My goal is to write a suite that can REALLY _manage_ ALL aspects of a digital Music Collection of ANY size (my
collection consists of a little over 500k songs...)

### Currently, the suite will consist of:
 * core(python3.9+) - this consists of a set of daemons which keep an eye on incoming files, processing them and storing them in the database.
 * server(php8/laravel8) - this will be a web/rpc server providing an interface to search the collection, creating and maintaining playlists and requests, as well as administering the settings for the 'core'; file naming conventions, black/whitelists etc.
 * gui - python based multiplatform graphical admin program
 * gui - python based multiplatform graphical client program


### (planned) REQUIREMENTS:
* Core:
    * Python 3.x
    * MySQL/MariaDB Server
* Server/webUI
    * PHP8/Laravel8

### Planned Functionality (MoSCoW prioritizing):

 -[ ] **_Must_** Index files
 -[ ] **_Must_** Purge Non-Audio files 
 -[ ] **_Must_** Parse & Purge Tags
 -[ ] **_Must_** Store File- & Tag-Data in DB
 -[ ] **_Must_** Generate Audio-Fingerprint
 -[ ] **_Must_** Calculate Audio Quality(bitrate/channels/sampling)
 -[ ] **_Must_** Remove Duplicates Based on Quality
 -[ ] **_Must_** Integrate Tags & Art in database, Fix (& Merge) Artist names & Titles
 -[ ] **_Must_** Insert Tags in Files
 -[ ] **_Must_** Rename & Move Files to target dir structure

 -[ ] **_Should_** Transcode & Normalize
 -[ ] **_Should_** Retrieve Artist names, Album titles, ft. Artists, Composer/writer, Album art, Lyrics
 -[ ] **_Should_** AJAX Interface
  
 -[ ] **_Could_** GUI 

 -[ ] **_Would_** Android Client
 -[ ] **_Would_** DLNA media server, audio player integration(?)

### Future ideas (still under debate):

* Acoustic Optimisation
* Automagic searching & downloading of missing songs
