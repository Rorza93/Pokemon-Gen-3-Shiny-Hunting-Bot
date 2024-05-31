import pyautogui
import time

shinyFound = False
timeMultiplier = 1
rapidDelay = 0.1
shortDelay = 0.5/timeMultiplier
MediumDelay = 1/timeMultiplier
longerDelay = 3/timeMultiplier
longestDelay = 5/timeMultiplier
n = -1.118
shinyDelay = 10.5 * (timeMultiplier ** n)

def PressX():
    pyautogui.keyDown('x')
    time.sleep(rapidDelay)
    pyautogui.keyUp('x') 

def PressDown():
    pyautogui.keyDown('down')
    time.sleep(rapidDelay)
    pyautogui.keyUp('down')

def PressRight():
    pyautogui.keyDown('right')
    time.sleep(rapidDelay)
    pyautogui.keyUp('right')

def PressReturn():
    pyautogui.keyDown('return')
    time.sleep(rapidDelay)
    pyautogui.keyUp('return')
   
def TestImageFound():
    location_bool = False
    # Define the region to search in (left, top, width, height)
    region = (0, 0, 1920, 1080)  # Adjust these values according to your screen resolution

    # Use raw string to avoid issues with backslashes
    image_path = 'wildPokemonArrow.png'

    try:
        # Try to locate the image on the screen
        location = pyautogui.locateOnScreen(image_path, region=region, confidence=0.8)
        
        # Set location as a boolean
        location_bool = location is not None

        if location_bool:
            print(f"Image found at location: {location}")
        else:
            raise pyautogui.ImageNotFoundException("Image not found on the screen.")
    except pyautogui.ImageNotFoundException as e:
        print(e)

    # Additional check to print if the image was not found
    if not location_bool:
        print('Image not found')

    return location_bool

def RunFromBattle():
    PressX()
    time.sleep(longerDelay)
    PressDown()
    time.sleep(rapidDelay)
    PressRight()
    time.sleep(rapidDelay)
    PressX()
    time.sleep(MediumDelay)
    PressX()

def SweetScent():
    PressReturn()
    time.sleep(shortDelay)
    PressX()
    time.sleep(MediumDelay)
    PressRight()
    time.sleep(MediumDelay)
    PressX()
    time.sleep(MediumDelay)
    PressX()

def RunShinyHunt():
    global shinyFound
    count = 1
    while not shinyFound:
        SweetScent()
        time.sleep(shinyDelay)
        if not TestImageFound():
            shinyFound = True
            print('Shiny found at encounter', count)
            break
        else:
            print('Encounter #', count)
        time.sleep(MediumDelay)
        RunFromBattle()
        count += 1
        time.sleep(longerDelay)

time.sleep(3)

RunShinyHunt()

