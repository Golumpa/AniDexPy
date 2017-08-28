# AniDexPy

A simple Python tool for uploading to AniDex via its API

## Getting Started

These instructions will direct you on how to use AniDexPy and also a way to make your life easier when submitting torrents to AniDex.

### Prerequisites

What things you need to run AniDexPy

```
Python (tested with 2.7, 3.4, 3.5 and 3.6)
Python requests
Pythong getopy
```

### Installing

Simply just download AniDex.py, make it excutable and run with python with the command line options.

## Usage

The command you will use to execute AniDexPy will look like the following

```AniDex.py -a APIKEY -n TORRENTNAME -f TORRENTFILE``` etc.
***
You can also edit the common variables in the file itself such as your API key and group ID to save you time, so you dont have to enter them in command line. (line 22 - 38)
***
The variables you can use and are currently available are (the arguments marked with * before the descrip[tion are required either in the config or command line):

* ```-a 12345-44...``` *Allows you to set your API key. This is obtained from your [AniDex settings](https://anidex.info/settings)
* ```-f /home/Golumpa/BokuNoPico.torrent``` *Allows you to set the torrent file you wish to upload
* ```-c 1``` *Allows you to set the catagory by its ID (list of IDs can be found [here](https://golu.mp/adc))
* ```-l 1``` *Allows you to set the main sub or dub laguage by its ID (list of laguage IDs can be found [here](https://golu.mp/adl))
* ```-n "[Golumpa] etc...``` Allows you to set the display name for the entry on AniDex
* ```-d "some description"``` Allows you to set a description for the torrent (Will show an example below that allows the use of new lines)
* ```-g 248``` Allows you to set this upload to go under a group. Group IDs are in the URL of your group and "0" is no group.
* ```-u "http://apiurl.com"``` Allows you to customise the api URL which should NEVER be needed but its an option.
* ```--tt``` Toggles the option to upload to TokyoTosho at the same time (through AniDex)
* ```--batch``` Toggles the option for this torrent to be marked as a batch (for whole seasons only!)
* ```--hentai``` Toggles the option for this torrent to be marked as henati (NSFW, 18+)
* ```--reencode``` Toggles the option for this torrent to be marked as a re-encode
* ```--private``` Toggles the option for this torrent to be marked as private so it is not visable to anone else or not in your group (if released under a group)
* ```--debug``` Toggles the option for this torrent to not actually be uploaded to AniDex and to return information and if the torrent upload would have been successful
***
If you would like to add newlines in the description, you can do the following:

```-n $'1st Line\n2nd Line\n3rd Line\n4th Line'```

Note that this now uses single quotes and an dollar sign infront of the quotes. This also has a downside that variables will no longer be able to be used. To fix that we can do this:

```-n $'1st Line\n2nd Line\n'"${variable}"'\n3rd Line\n4th Line'```


## Contributing

All push requests are welcome. This was just a quick script I made for my own use but decided to upload it anyway. So if you want to make this little python script better, you more than welcome to.

## License

This project is licensed under the DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* AniDex.info (For making the API)
* You (For reading this far and possible using this tool)
