# Knmlpro2-File-SHare-Bot

<p align="center">
  <a href="https://www.python.org">
    <img src="http://ForTheBadge.com/images/badges/made-with-python.svg" width ="250">
  </a>
  <a href="https://telegram.me/Knmlpro2">
    <img src="https://telegram.me/Knmlpro2/PyrogramGenStr/blob/main/resources/madebycodex-badge.svg" width="250">
  </a><br>
  <a href="https://telegram.me/Knmlpro2">
    &nbsp;<img src="https://img.shields.io/badge/MoTech-Channel-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <a href="https://telegram.me/Knmlpro2_group">
    &nbsp;<img src="https://img.shields.io/badge/MoTech-Group-blue?style=flat-square&logo=telegram" width="130" height="18">&nbsp;
  </a>
  <br>
  <a href="https://github.com/akrcreation2/Knmlpro2-File-Share-Bot">
    <img src="https://img.shields.io/github/stars/COLD-ONEZ/File-SHare-Bot?style=social">
  </a>
  <a href="https://github.com/akrcreation2/Knmlpro2-File-Share-Bot/fork">
    <img src="https://img.shields.io/github/forks/COLD-ONEZ/File-SHare-Bot?label=Fork&style=social">
  </a>  
</p>


Telegram Bot To Store Posts And Documents And it Can Access By Special Links.
I Guess This Will Be Usefull For Many People.....😇. 

##

**If you need any more modes in repo or If you find out any bugs, mention in [@Knmlpro2_group](https://telegram.me/Knmlpro2_group)**

### Features
- Fully customisable.
- Customisable welcome & Forcesub messages.
- More than one Posts in One Link.
- Can be deployed on heroku directly.

### Setup

- Add the bot to Database Channel with all permission
- Add bot to ForceSub channel as Admin with Invite Users via Link Permission if you enabled ForceSub 

##
### Installation
#### Deploy on Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/akrcreation2/Knmlpro2-File-Share-Bot)</br>
<a href="https://youtu.be/ep3u-n_DI_Q">
  <img src="https://img.shields.io/badge/How%20to-Deploy-red?logo=youtube" width="147">
</a><br>

#### Deploy in your VPS
````bash
git clone https://github.com/akrcreation2/Knmlpro2-File-Share-Bot
cd File-SHare-Bot
pip3 install -r requirements.txt
# <Create config.py appropriately>
python3 main.py
````

### Admin Commands

```
/start - start the bot or get posts

/batch - create link for more than one posts

/genlink - create link for one post

/users - view bot statistics

/broadcast - broadcast any messages to bot users
```

### Variables

* `API_HASH` Your API Hash from [my.telegram.org](https://my.telegram.org)
* `API_ID` Your API ID from [my.telegram.org](https://my.telegram.org)
* `TG_BOT_TOKEN` Your bot token from [@BotFather](https://telegram.me/BotFather)
* `OWNER_ID` Must enter Your Telegram Id
* `CHANNEL_ID` Your Channel ID eg:- -100xxxxxxxx
* `ADMINS` Optional: A space separated list of user_ids of Admins, they can only create links
* `START_MESSAGE` Optional: start message of bot, use HTML and <a href='https://github.com/akrcreation2/Knmlpro2-File-Share-Bot/blob/main/README.md#start_message'>fillings</a>
* `FORCE_SUB_MESSAGE`Optional:Force sub message of bot, use HTML and Fillings
* `FORCE_SUB_CHANNEL` Optional: ForceSub Channel ID, leave 0 if you want disable force sub


### Fillings
#### START_MESSAGE | FORCE_SUB_MESSAGE

* `{first}` - User first name
* `{last}` - User last name
* `{id}` - User ID
* `{mention}` - Mention the user
* `{username}` - Username

#### CUSTOM_CAPTION

* `{filename}` - file name of the Document
* `{previouscaption}` - Original Caption


## Support   
Join Our [Telegram Group](https://telegram.me/Knmlpro2_group) For Support/Assistance.     

### Credits

- Thanks To [CodeXBotz](https://t.me/CodeXBotz) & [Knmlpro2](https://t.me/Knmlpro2)

##

   **Star this Repo if you Liked it ⭐⭐⭐**

