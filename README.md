# Custom T-Shirt Tool

***Early Test Version - Bugs and Missing Features are to be expected!***

## Usage

Very Basic Video Tutorial. It is still recommended to read the README.
https://youtu.be/GEjUI7NKBX8

To use the tool you will need to make use of the following scripts found in the main folder:

- **Setup Menu.bat**
- **Texture Converter.bat**
- **Test Environment.bat**

***RUNNING OTHER SCRIPTS FOUND WITHIN THE FOLDERS IS LIKELY TO BREAK THINGS!***

Running the Converter requires Unpackaging and Repackaging some game-files. Depending on your hardware this may take a while.

This toolset is aimed towards people who require a fair bunch of handholding. While capable of more, it is limited on purpose to make it less likely to break. If you require something more advanced i recommend starting from here: https://github.com/Buckminsterfullerene02/UE-Modding-Tools


The Tool was last tested with **Heroes of Valor Playtest** version **0.1.2.377**. Compatibility with other versions is not guaranteed.


## Prerequisites:

- Windows or "insert your favorite compatibility layer / VM". Native Linux Support comes eventually.

- The filepath to your "Heroes of Valor" install location.
    
    Example: ***C:\Program Files (x86)\Steam\steamapps\common\Heroes of Valor Playtest***

    <details>
        <summary>How do I find the install location?</summary>
        <ul>
            <li>Launch the <strong>Steam client</strong> on your computer</li>
            <li>Click on <strong>Library</strong> to see all installed games</li>
            <li>Right-click on <strong>Heroes of Valor Playtest</strong></li>
            <li>Select <strong>Properties</strong> from the context menu</li>
            <li>In the Properties window, go to the <strong>Installed Files</strong> tab</li>
            <li>Click on the <strong>Browse...</strong> button</li>
            <li>Right-click <strong>Heroes of Valor Playtest</strong> in the address bar. Click copy address</li>
        </ul>
    </details>

- Run the Setup and complete every single step of it, do not skip anything the first time you use it! The setup **requires a Internet connection** for downloading the following packages from GitHub:

	- [repak](https://github.com/trumank/repak/releases/tag/v0.2.2)
	- [UE4 DDS Tools Batch](https://github.com/matyalatte/UE4-DDS-Tools/releases/tag/v0.6.1)

## Important Things To Note

### Image Sizes

<details>
        <summary>Supported image resolutions</summary>
        <ul>
            <li>128x128</li>
            <li>256x256</li>
            <li>512x512</li>
            <li>1024x1024</li>
            <li>2048x2028</li>
            <li>4096x4096</li>
        </ul>
    </details>

As you can tell from the list of supported image resolutions all options are a power of 2, this is deliberate and should be adhered to!

See https://www.katsbits.com/site/make-better-textures-correct-size-and-power-of-two/ for more information.

Higher resolution isn't always better when it comes to creating a texture, choose depending on your requirements.

- Consider using copys of the included "Templates" as starting point.
- Do not edit the original templates to reduce the risk of losing them.
- Usage of the templates is optional and not a requierment.

### File Types

- UE4 DDS Tools supports a variety of diffrent filetypes for conversion.
- DDS is currently mostly broken and should be avoided.
- PNG is tested and confirmed as working.

For a list of all supported file types see: https://github.com/matyalatte/UE4-DDS-Tools


### Use the Test Enviroment before moving your modified game files to your main install.

Lets you preview and test your skins/textures much quicker than exporting and launching through Steam each time.


## Credits:

Tools used by the Converter:

- [repak, for packaging operations](https://github.com/trumank/repak)

- [UE4 DDS Tools, for handling the assets](https://github.com/matyalatte/UE4-DDS-Tools)
