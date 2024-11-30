# functor-bot

# How to run

1. Update system and install pip
  ```bash
  sudo apt update && sudo apt install python3-pip -y

2. Install *request* module
   ```bash
    pip3 install requests

3. Get bearer token: Chrome Dev Console > Network > Fetch/XHR > Response Headers > Authorization
4. Go to https://jwt.io/ and paste your bearer token. Under 'payload', get the value of 'sub'. That's your user id
5. Edit main.py and replace the user id and bearer tokens
6. Run script
   ```python3 main.py```
