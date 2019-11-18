# BreakingNews (NDS Exploit)
A "New York Times Crossword" stack smash exploit for the Nintendo DS that can execute unsigned code from the savegame.

* These are ARM9 exploits that takes over a NDS mode cartridge. These type of exploits are very limited since there's no SD or NAND access. They can be used to run a small payload. These exploits are almost useless.

## Requirements:
* A copy of the `New York Times Crossword` NDS game (US/EUR)
* Any DS that's in the NDS family (NDS, NDSL, DSi, DSiXL, 3DS, 3DSXL, NEW3DS, NEW3DSXL, 2DS, 2DSXL, etc.)
* A way to inject the save. (DSi users can use [ndsi-savedumper](https://github.com/edo9300/ndsi-savedumper) and 3DS users can use [TWLSaveTool](https://github.com/TuxSH/TWLSaveTool/releases).
###
## Triggering the exploit
* Select the `rename` button on the bottom screen while the `BreakingNews` save-slot is selected
* The payload should load! :D
###
## Support:
* Supports both US & EUR versions of the game.
* Works with emulators. (no$gba, TWiLightMenu++, etc.)
###
## Credits:
* [ihaveamac](https://github.com/ihaveamac): Creating the python script
* [St4rkDev](https://twitter.com/St4rkDev): Original payload code
###
## Video Demonstration:
<a href="http://www.youtube.com/watch?feature=player_embedded&v=drayJZ3LNZQ
" target="_blank"><img src="http://img.youtube.com/vi/drayJZ3LNZQ/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
