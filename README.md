# SonicRacingTransformedAndroidUpdate-NewVersion
https://drive.google.com/drive/folders/1I7E6y4MqFBFT2pyQ2cHkTp2CDtdYy9y6

Sonic Racing Transformed GdGohan Edition

•What changed in this version:

--V531960--

-Greater compatibility with newer devices 

and larger screens

(possibility, considering that it loaded normally 

on my cell phone)

-support for new android

(tested on moto g7 play android 13 LineageOS),

It's not a guarantee, but it's a good alternative 

because it's a different version (even if it's old) 

-Forced game to load in 16:9 aspect ratio (Go to settings > display > full screen apps and disable the game's full screen function)

(Bug fixed:Buttons not showing)

-supports different obb, just edit the apk code 

and adapt it to load the obb 

(This is already possible in unmodified/

original apk)

-Custom Audio

check audio type: https://katiefrogs.github.io/vgmstream-web/

Wwise 2013:https://www.nexusmods.com/witcher3/mods/3234

Recommended audio db = 3 to 4.5

Music: loop=0, stream=1 and vorbis encode

(not tested) Audio(sfx): loop=0, stream=0/1 and ADPCM encode

Voice: loop=0, stream=0 and ADPCM encode

(Music) (Recommended) Fusion Tools:https://www.nexusmods.com/mafiadefinitiveedition/mods/98 

or Ringing Bloom:https://github.com/Silvris/RingingBloom/releases/tag/v2.1

(experimental) HxD editor:https://mh-nexus.de/en/downloads.php?product=HxD20

(Voice) Best Choice for editing (backup the .pck file before): https://smacktalks.org/forums/topic/79306-released-sound-editor%C2%A0version-2101/

alternative (Sound Editor 2018):https://smacktalks.org/forums/topic/68040-sound-editor-2018-released-version-141/page/12/

and to listen to the audios + check id: https://www.nexusmods.com/mafiadefinitiveedition/mods/98

Voice:

Possible solutions/Not working: 

1. use Ringing Bloom to open and export the .pck, open the new .pck in FusionTools and export again, and make changes to the file using HxD

2. 	Ravioli Scanner: https://www.scampers.org/steve/sms/other.htm#ravioli_download (working)

    FusionTools: wem id 0 = Ravioli Scanner: File0012

    File size < or = to the original

3.  export all wem and bnk files using FusionTools and create new pck with it

4.  Sound Editor (working) StreamsEng.pck only

(To use the other streams .pck in the Sound Editor):

5.  export all wem and bnk files using FusionTools and create new pck with Sound Editor 2017/18 or Sound Editor 2.1.0.1 (working)

    Voice = wem and Sfx = bnk

    or Voice = wem + bnk

5,1. Modify with HxD Editor the default.pck file from "Sound Editor/templates", replace all code (make backup before):

for StreamsSpa.pck:

41 4B 50 4B 58 51 00 00 01 00 00 00 28 00 00 00 5C 02 00 00 D8 85 00 00 04 00 00 00 02 00 00 00 14 00 00 00 00 00 00 00 18 00 00 00 01 00 00 00 73 66 78 00 73 70 61 6E 69 73 68 28 73 70 61 69 6E 29 00 00 1E 00 00 00 24 B3 4B 00 01 00 00 00

Fra:

41 4B 50 4B 58 51 00 00 01 00 00 00 28 00 00 00 5C 02 00 00 D8 85 00 00 04 00 00 00 02 00 00 00 14 00 00 00 01 00 00 00 23 00 00 00 00 00 00 00 66 72 65 6E 63 68 28 66 72 61 6E 63 65 29 00 73 66 78 00 00 1E 00 00 00 24 B3 4B 00 01 00 00 00

Ita:

41 4B 50 4B 58 51 00 00 01 00 00 00 20 00 00 00 5C 02 00 00 D8 85 00 00 04 00 00 00 02 00 00 00 14 00 00 00 01 00 00 00 1C 00 00 00 00 00 00 00 69 74 61 6C 69 61 6E 00 73 66 78 00 1E 00 00 00 24 B3 4B 00 01 00 00 00 0A 0D 00 00 74 88 00 00

Ger:

41 4B 50 4B 58 51 00 00 01 00 00 00 20 00 00 00 5C 02 00 00 D8 85 00 00 04 00 00 00 02 00 00 00 14 00 00 00 01 00 00 00 1B 00 00 00 00 00 00 00 67 65 72 6D 61 6E 00 73 66 78 00 00 1E 00 00 00 24 B3 4B 00 01 00 00 00 0A 0D 00 00 74 88 00 00

5,2. export 2428910049.bnk and 1051509953.bnk using HxD Editor

Best Choice:

Custom pcks for Sound Editor: 

[StreamsSpa](https://github.com/GdGohan/SonicRacingTransformedAndroidUpdate-NewVersion/raw/main/CustomPcksForSoundEditor/StreamsSpa.zip)

[StreamsIta](https://github.com/GdGohan/SonicRacingTransformedAndroidUpdate-NewVersion/raw/main/CustomPcksForSoundEditor/StreamsIta.zip)

[StreamsGer](https://github.com/GdGohan/SonicRacingTransformedAndroidUpdate-NewVersion/raw/main/CustomPcksForSoundEditor/StreamsGer.zip)

[StreamsFra](https://github.com/GdGohan/SonicRacingTransformedAndroidUpdate-NewVersion/raw/main/CustomPcksForSoundEditor/StreamsFra.zip)

-Mods

Team Sonic Racing Music Mod And More

-Installation (Mods)

pck: to install the mod manually, just copy the files to the "data/common/data/sound" folder of your obb without compression

xml: to install the mod manually, just copy the files to the "data/common/data/gamedata" folder of your obb without compression

Recommended: MT Manager

compression level: store

-Multiplayer

Go to the first cup, finish it if you haven't already, and press the multiplayer icon (pressing on the home interface will not work)

-Installation (Apk+Obb)

apk:choose one of these versions(to find out which is correct for your device, install the CPU-Z app):
Adreno,Mali,PowerVr,Tegra

obb:move the correct obb to the "Android/obb/com.sega.sonic.transformed" folder
