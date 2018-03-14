# GSFacebookLeads
Facebook Script to generate Sales Leads for GigSync

## Setup

1. Clone repository `git clone https://github.com/ttanay/GSFacebookLeads.git` and press Enter.

2. Install sqlite3 and python3 (if not installed)

3. In terminal type `python3 -m venv src/env` and press Enter.

4. In terminal type `pip3 install -r requirements.txt` and press Enter.

5. In terminal type `bash setup.sh` and press Enter.


## Usage
1. Right click on GSFacebookLeads.
2. Click on New Terminal on Folder.
3. Paste "fb_script" and press Enter.

## Options

There are 3 major cmd line arguments to the script:
* `-s` or `--start_url`: This is to specify the start_url
* `-n` or `--number_of_leads`: This is to specify the number of leads needed
* `-d`: This is to delete all currently unexplored leads from DB

