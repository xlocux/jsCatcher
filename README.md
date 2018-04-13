# jsCatcher
Grab javascript links/files from a single url or list. 
I'm pretty new to python coding so any help to improve the script will be appreciated, expecially for multi-threading support ^_^

-----------------------------------------------------------------------

## Installation:

$ git clone https://github.com/xlocux/jsCatcher.git

$ cd jsCatcher

$ pip install -r requirements.txt

------------------------------------------------------------------------

## Dependencies

jsCatcher depends on the `requests`, `argparse`, `jsbeautifier` and `requests-file` python modules. These dependencies can all be installed using [pip](https://pypi.python.org/pypi/pip).
RetireJS https://github.com/retirejs/retire.js/


-------------------------------------------------------------------------

## Usage:


usage: jsCatcher.py [-h] [-u URL] [-l LIST] [-d DOWNLOAD] [-o OUTPUT]
                    [-r RETIRE]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Input a: URL
  -l LIST, --list LIST  Input a: URL list
  -d DOWNLOAD, --download DOWNLOAD
                        Download javascript files (it is also possible to
                        specify the download path)
  -o OUTPUT, --output OUTPUT
                        Save javascript link to file
  -r RETIRE, --retire RETIRE
                        Run Retire against downloaded javascripts (output file
                        .json required and also retire js installed)

  ------------------------------------------------------------------------
  
  ### Examples

* Collect links from a single URL (CLI output):

 $ python jsCatcher.py -u https://www.example.com

* Collect links from a list of URL and save to file:

 $ python jsCatcher.py -l url.txt -o jslinks.txt

* Collect javascript files from a list and save them sorted by domain:

 $ python jsCatcher.py -l url.txt -d test/

* Collect javascript files from a list and save them sorted by domain and run Retire JS:

 $ python jsCatcher.py -l url.list -d /url/ -r example.json


 ### Then you can also run LinkFinder (https://github.com/GerbenJavado/LinkFinder) to cach others links or endpoints
