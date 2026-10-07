# Unreal Engine 1 Renderers

# [DOWNLOAD HERE](https://github.com/theastropath/UnrealEngine1Renderers/releases)

For information regarding the settings, please [SEE THIS PAGE](https://github.com/theastropath/UnrealEngine1Renderers/blob/main/notes/RendererSettings.md)

Newly updated renderers for various Unreal Engine 1 games.

 - DirectX 9
 - DirectX 10
 - OpenGL 1.x

DirectX 9 and OpenGL based on [prior work by Chris W. Dohnal](https://www.cwdohnal.com/utglr/)

DirectX 10 based on [prior work by Marijn Kentie](https://kentie.net/article/d3d10drv/index.htm)

---

These renderers are built for the following games:
 - Deus Ex
 - Harry Potter and the Philosopher's Stone
 - Nerf Arena Blast
 - Rune 1.00/1.07
 - Star Trek The Next Generation: Klingon Honor Guard
 - Unreal 224
 - Unreal Gold 226
 - Unreal Tournament
 - X-Com: Enforcer

---

## To Compile

### Prerequisites
 * "DirectX SDK (June 2010)" from [HERE](https://www.microsoft.com/en-ca/download/details.aspx?id=6812) extracted, place the contents of the extracted "DXSDK" folder into a folder called "dxsdk-jun2010" in the "src" directory of this repository, alongside the "D3D10" directory.
 * Extract the "Games" directory from the [game headers](https://www.kentie.net/article/d3d10drv/files/src/games.zip) into the common "Games" directory of this repository in the "src" folder (Alongside the "D3D9", "D3D10", "OpenGL" folders)
 * Grab copies of the headers for Unreal 224v, Nerf Arena Blast, Klingon Honor Guard, Harry Potter, and X-Com: Enforcer from [HERE](https://coding.hanfling.de/launch/) and extract their contents into "Unreal_224", "Nerf", "Klingon", "HarryPotter", and "XComEnforcer" directories respectively in the "Games" directory.
   * Apply the patches from the "HeaderPatches" directory to the set of headers associated with each patch.  This step is necessary, as these headers will not compile otherwise.

 ### Direct3D 9
  * Navigate into the "D3D9" directory and run the build script: ```.\build.bat <GameName>```
    * If no game name is provided, it will default to "UnrealTournament".  
    * If an invalid name is provided, it will list all of the possible build targets.
  * The compiled output will be placed into the ```System/<GameName>``` directories in the "D3D9" folder.

### OpenGL
  * Navigate into the "OpenGL" directory and run the build script: ```.\build.bat <Release|Debug> <GameName>```
    * if no parameters are provided, it will default to "Release UnrealTournament".
    * If an invalid game name is provided, it will list all of the possible build targets.
  * The compiled output will be placed into the ```System/<GameName>``` directories in the "OpenGL" folder.

### Direct3D 10
  * Navigate into the "D3D10" directory and run the Powershell build script: ```powershell.exe -file ./build.ps1```
    * This build script will compile all build targets, both "debug" and "release".
  * Alternately, a single product can be built instead by providing a "configuration" parameter: ```powershell.exe -file ./build.ps1 -Configuration "Your Build Target"```
    * "Your Build Target" can be specified in the form of ```"<Game Name> <Debug|Release>```, such as "Deus Ex Release" or "Unreal Tournament Debug"
  * The compiled output will be placed into the ```packages/<GameName>``` directories in the "D3D10" folder.

### Compile and Package all Renderers
  * Run ```python src\BuildRelease.py```, which will compile all the renderers and package individual ZIP files for each game containing all the renderers in the "dist" directory.
    * Without any parameters, this will compile the renderers for all of the supported games.
    * Alternately, you can provide a space separated list of games to compile, such as ```python src\BuildRelease.py DeusEx UnrealTournament```
