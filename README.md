# functor-bot

1. Update system and install pip
  ```bash```
  sudo apt update && sudo apt install python3-pip -y
3. Install *request* module
   ```pip3 install requests```
4. Get bearer token: Chrome Dev Console > Network > Fetch/XHR > Response Headers > Authorization
5. Go to https://jwt.io/ and paste your bearer token. Under 'payload', get the value of 'sub'. That's your user id
6. Edit main.py and replace the user id and bearer tokens
7. Run script
   ```python3 main.py```
