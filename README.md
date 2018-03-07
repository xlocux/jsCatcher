# jsCatcher
Grab javascript links/files from a single url or list.

-----------------------------------------------------------------------

## Installation:

$ git clone https://github.com/xlocux/jsCatcher.git

$ cd jsCatcher

$ pip install -r requirements.txt OR python setup.py install

------------------------------------------------------------------------

## Dependencies

jsCatcher depends on the `requests`, `argparse`, `jsbeautifier` and `requests-file` python modules. These dependencies can all be installed using [pip](https://pypi.python.org/pypi/pip).

-------------------------------------------------------------------------

## Usage:

jsCatcher.py [-h] [-u URL] [-l LIST] [-d DOWNLOAD] [-o OUTPUT]

optional arguments:

  -h, --help            show this help message and exit
  
  -u URL, --url URL     Input a: URL
  
  -l LIST, --list LIST  Input a: URL list
  
  -d DOWNLOAD, --download DOWNLOAD  Download javascript files
  
  -o OUTPUT, --output OUTPUT  Save javascript link to file
  
  ------------------------------------------------------------------------
  
  ### Examples

* Collect links from a single URL (CLI output):

 $ python jsCatcher.py -u https://www.example.com

* Collect links from a list of URL and save to file:

 $ python jsCatcher.py -l url.txt -o jslinks.txt

* Collect javascript files from a list and save them sorted by domain:

 $ python jsCatcher.py -l url.txt -d test/


