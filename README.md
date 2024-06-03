Pokemon Gen 3 Shiny hunting bot.  
  
Currently confirmed working on Pokemon Sapphire but should work on Ruby and Emerald.  
FILE SETUP  
Ensure you have pyton installed and pyautogui and pillow installed if not you can run the following in terminal  
pip install pyautogui pillow opencv-python  
in the pokemon_shiny_bot.py file you can set your timeMultiplier, 1 is running the game at normal speed or approx 59.7 seconds, 10 would be 10x speed on the emulator  
The program is also set to 1920x1080 this may need to be adjusted to suit another setup  
  
SHINY SETUP  
Ensure lead pokemon has a higher speed value that the pokemon you want to hunt.  
Set your 2nd pokemon to have sweet scent   
Go to a patch of grass  
Manually use sweet scent  
Run from the battle  
Run the script in vs code   
swich back to the emulator window and let it run  
note: this program will cease running once a shiny is found  
