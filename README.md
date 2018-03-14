# GSFacebookLeads
Facebook Script to generate Sales Leads for GigSync

## Setup

1. Clone repository `git clone https://github.com/ttanay/GSFacebookLeads.git` and press Enter.

2. Install sqlite3 and python3 (if not installed)

3. In terminal type `bash setup.sh` and press Enter.

4. Restart Terminal.


## Usage
1. Right click on GSFacebookLeads.
2. Click on New Terminal on Folder.
3. Paste "fbscript" and press Enter.

## Options

There are 3 major cmd line arguments to the script:
* `-s` or `--start_url`: This is to specify the start_url
* `-n` or `--number_of_leads`: This is to specify the number of leads needed
* `-d`: This is to delete all currently unexplored leads from DB

## Note
You will need to create a file named access.py with 
`access_token = "<long-term access token for FB Graph API>"`
and save it to `src/`.
For more info: [https://developers.facebook.com/docs/facebook-login/access-tokens/expiration-and-extension]

