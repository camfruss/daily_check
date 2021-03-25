## Automating Cornell's Daily Check

Here's a small python script to convenience your life just a little bit, regardless of how well you know your way around the terminal.

Note: this was developed/tested on a Mac with a zsh shell.

#### Prerequisites

First, install chromedriver if you haven't already with `brew install chromedriver`. If you don't have brew installed, 
do that [here](https://brew.sh/).

Download the files and save them somewhere on your computer. Then create a virtual environment with `python3 -m venv venv`. To activate 
this environment, run `source <path_before_venv>/venv/bin/activate`. Finally, to install the required dependencies, run 
`pip3 install -r requirements.txt`. 

Note: You may need to use `pip` or `python` instead of `pip3` and `python3`. You may also need to allow `chromedriver` to 
run in System Preferences since it's downloaded from the internet.

If you already have `chromedriver` installed but run into a `selenium.common.to run `brew upgrade chromedriver`.
exceptions.SessionNotCreatedException` exception, you'll need

I recommend creating an alias for this script, which you can do by:
```
vim ~/.aliases
<press the letter 'i'>
alias dailycheck='<path>/<to>/<venv>/lib/python3 <path>/<to>/daily_check.py'
<press esc then type 'wq' and press ENTER>
open ~/.zshrc
<add> source $HOME/.aliases
```

#### Usage

To actually run the script, just type `dailycheck` in the terminal then enter your netid and password when prompted. 
Your password won't actually appear when you type it in.

If your terminal ever gets stuck or freezes (hopefully it won't), press `⌘C`.

#### Crontab

If you have your own server running (you could set up a free micro.t2 instance on AWS), or you are always on your computer 
at a certian time, using crontab would automate the entire process. I do not have either set up. 

### Disclaimer
If you actually have COVID symptoms, were in contact with someone who tested positive, or anything that warrants a non-no response, make sure you 
don't use this script. If automated, make it later in the day so you could fill the daily check out manually, just in case. 
