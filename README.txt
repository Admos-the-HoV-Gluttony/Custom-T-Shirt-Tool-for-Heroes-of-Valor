Early Test Version - Bugs and Missing Features are to be expected!


DO NOT RUN SCRIPTS ASIDE FROM THE FOLLOWING FOUND IN THE MAIN FOLDER:

- Setup Menu.bat
- Texture Converter.bat
- Test Enviorment.bat

RUNNING OTHER SCRIPTS FOUND WITHIN THE FOLDERS WILL CLUTTER OR BREAK STUFF!


Running the Converter requires Unpackaging and Repackaging some game-files.
Depending on your hardware this may take a while.


This toolset is aimed towards people who require a fair bunch of handholding.
While capable of more, it is limited on purpose to make it less likely to break.
If you require something more advanced i recommend starting from here:
https://github.com/Buckminsterfullerene02/UE-Modding-Tools


The Tool was last tested with "Heroes of Valor Playtest" version "0.1.2.377"
Compatibility with other versions is not guaranteed.


Perquisites:

1. Windows or "insert your favorite compatibility layer / VM". Support for Linux comes eventually.


2. The path to the "Heroes of Valor" game-files.
   
	Launch the Steam client on your computer.
	
	Click on "Library" to see all installed games.
	
	Right-click on "Heroes of Valor Playtest."
	
	Select "Properties" from the context menu.
	
	In the Properties window, go to the "Installed Files" tab.
	
	Click on the "Browse local files..." button.
	
	Right-click "Heroes of Valor Playtest" in the address bar. Click copy address.


3. Run the Setup and complete every single step of it, do not skip anything the first time you use it!
   The setup requires a Internet connection for downloading the following packages from GitHub:

	repak: https://github.com/trumank/repak/releases/tag/v0.2.2
	 
	UE4 DDS Tools Batch: https://github.com/matyalatte/UE4-DDS-Tools/releases/tag/v0.6.1


4. Providing Images for the conversion.

	It only accepts paths without "" will be fixed at a later point, for now just remove them.

	Heroes of Valor does currently use textures with the following sizes (from what i saw):
	
	- 128x128
	- 256x256
	- 512x512
	- 1024x1024
	- 2048x2028

	There is a obvious pattern and its not a coincidence, keep that in mind!
	https://www.katsbits.com/site/make-better-textures-correct-size-and-power-of-two/
	Higher isn't always better, choose depending on your requirements.
	Consider using copys of the included "Templates" as starting point.
	Do not edit the original templates to reduce the risk of loosing them.
	Usage of the templates is optional and not a requierment.

	UE4 DDS Tools supports a variety of diffrent filetypes for conversion.
	DDS is currently mostly broken and should be avoided.
	PNG is tested and confirmed as working.
	For a list of all supported file types see: https://github.com/matyalatte/UE4-DDS-Tools


Use the "Test Enviorment" before moving your modified game files to your main install.
Faster than exporting and launching through Steam for every test.


Credits:

Tools used by the Converter:

repak, for packaging operations
https://github.com/trumank/repak

UE4 DDS Tools, for handling the assets
https://github.com/matyalatte/UE4-DDS-Tools
