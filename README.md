# "Automating" Cornell's Daily Check

Here's a small python script to convenience your life just a little bit, regardless of how well you know your way around the terminal.

Note: this was developed/tested on a Mac with a zsh shell.

## Setup

1. If you have not installed `chromedriver`, do so with with `brew install chromedriver`. If you don't have brew installed, 
do that [here](https://brew.sh/). (You can check to see if it's already installed by running `chromedriver --version`)
2. Download the files from this repo and save them to your computer (ideally in a separate folder called `daily_check` or something like that).
3. Navigate to the new folder and run the following commands:
   ```
   python3 -m venv venv
   source ./venv/bin/activate
   pip3 install -r ./requirements.txt
   ````
   Note: You may need to use `pip` or `python` instead of `pip3` and `python3`.
4. Create alias for this script, which you can do by:
    ```
    vim ~/.aliases
    # press the letter 'i'
    alias dailycheck='<path_to_venv>/lib/python3 <path_to>/daily_check.py'
    # press ESC then type ':wq' and press ENTER
    open ~/.zshrc
    # add the following line somewhere in .zshrc
    source $HOME/.aliases
    ```

## Usage

To actually run the script, just type `dailycheck` in the terminal then enter your netid and password when prompted. 
Your password won't actually appear when you type it in (which is a good thing).

#### Common Problems
If you already have `chromedriver` installed but run into a `selenium.common.exceptions.SessionNotCreatedException`
run `brew upgrade chromedriver`.

You may also need to allow `chromedriver` to run in System Preferences (your computer will provide a prompt for this).

If your terminal ever gets stuck or freezes (it won't), press `⌘C`.

#### Crontab

If you have your own server running (you could set up a free micro.t2 instance on AWS), or you are always on your computer 
at a certian time, using crontab would automate the entire process. I do not have either set up. 

## Disclaimer
This script allows you to complete the daily check from the terminal, but is not full "automation".
If you actually have COVID symptoms, were in contact with someone who tested positive, or anything that warrants a non-no response, make sure you 
don't use this script, as this submits exclusively "no" responses. And if you fully automated to script, make it later in the day, so you could fill the daily check out manually, just in case. 

:)