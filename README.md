# Postcards
> A CLI for the Swiss Postcard Creator

This project is still in early development. Feedback and support appreciated.

## Install
- Not yet available on pip

## Usage
```
python postcards.py --help

usage: postcards.py [-h] [--config CONFIG] [--accounts-file ACCOUNTS_FILE]
                    [--picture PICTURE] [--message MESSAGE] [--key PASSWORD]
                    [--username USERNAME] [--password PASSWORD]
                    [--encrypt KEY CREDENTIAL] [--mock] [--trace] [--debug]

Postcards is a CLI for the Swiss Postcard Creator

optional arguments:
  -h, --help            show this help message and exit
  --config CONFIG       location to the json config file
  --accounts-file ACCOUNTS_FILE
                        location to a dedicated json file containing postcard creator accounts
  --picture PICTURE     postcard picture. path to an URL or image on disk
  --message MESSAGE     postcard message
  --key PASSWORD        a key to decrypt credentials stored in config files
  --username USERNAME   username credential. otherwise set in config or accounts file
  --password PASSWORD   password credential. otherwise set in config or accounts file
  --encrypt KEY CREDENTIAL
                        encrypt credentials to store in config files
  --mock                do not submit postcard. useful for testing
  --trace               enable tracing. useful for testing
  --debug               enable debug logs. useful for testing

sourcecode: https://github.com/abertschi/postcards
```

## configuration file
```json
{
  "recipient": {
    "firstname": "",
    "lastname": "",
    "street": "",
    "zipcode": "",
    "city": ""
  },
  "sender": {
    "firstname": "",
    "lastname": "",
    "street": "",
    "zipcode": "",
    "city": ""
  },
  "accounts": [
    {
      "username": "",
      "password": ""
    }
  ]
}

```

### Examples
```sh
# Use postcards.py and set the postcard message and picture directly
$ python postcards.py --config /path/to/config.json \
    --picture https://images.pexels.com/photos/365434/pexels-photo-365434.jpeg \
    --message "Happy coding"


# Encrypt user credentials to store in config.json
python postcards.py --encrypt mykey mypassword


# Use key to decrypt credentials
$ python postcards.py --config /path/to/config.json \
    --key mykey \
    --picture https://images.pexels.com/photos/365434/pexels-photo-365434.jpeg \
    --message "Happy coding"

# Mock postcard
$ python postcards.py --config /path/to/config.json \
    --mock --trace
    --picture https://images.pexels.com/photos/365434/pexels-photo-365434.jpeg \
    --message "Happy coding"

```


## Plugins
Note: Your picture (`--picture`) or the message text (`--message`) can always be overwritten by command line arguments if you use a plugin.

Example: 
```
python postcards_folder.py --config ./config.json --message "This overwrites the message set by the plugin"
```
### Send pictures from a folder
Plugin name: `postcards_folder.py`  
This plugin sends pictures from a folder

Add the following object to your configuration file (config.json)
```json
{
 "payload": {
    "folder": "./pictures",
    "move": true
  }
}
```

- folder: location to a folder containing your images (required)
- move: set to false if sent picture should not be moved to a subdirectory `./sent/` (default: true)

#### Example
```
python postcards_folder.py --config ./my-config.json
```

### Send pictures from http://pexels.com
- Plugin name: `postcards_pexels.py`  
This plugin chooses random pictures from pexels.

- No configuration is necessary in your `config.json` file

#### Example
```
python postcards_pexels.py --config ./config.json
```

### Build your own plugin
See `postcards_pexels.py` or `postcards_folder.py` for a sample

1. Extend the class `postcards.Postcards()`
2. Overwrite `def get_img_and_text(self, payload, cli_args)`
3. Optionally add command line args by overwriting `def enrich_parser(self, parser)`

## Related
- [postcard_creator_wrapper](https://github.com/abertschi/postcard_creator_wrapper) - Python API wrapper around the Swiss Postcard Creator

## Author
Andrin Bertschi and [friends](https://github.com/abertschi/postcards/graphs/contributors)

## License

MIT
