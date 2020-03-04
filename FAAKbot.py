import cv2
import pyautogui
from skimage.metrics import structural_similarity as compare_ssim
import random
import time
import numpy as np
from pathlib import Path

#### We need some kind of check to see if the game is running before we start trying to match templates ####
############################################################################################################
pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True

while True:
    template_path_Berserkers = ['C:\TarkvaraProjekt\FAAKbot\Templates\Champs\Aatrox.jpg', 'C:\TarkvaraProjekt\FAAKbot\Templates\Champs\Brand.jpg', 
    'C:\TarkvaraProjekt\FAAKbot\Templates\Champs\Braum.jpg', 'C:\TarkvaraProjekt\FAAKbot\Templates\Champs\Diana.jpg', 
    'C:\TarkvaraProjekt\FAAKbot\Templates\Champs\Dr_Mundo.jpg', 'C:\TarkvaraProjekt\FAAKbot\Templates\Champs\Ezreal.jpg',
    'C:\TarkvaraProjekt\FAAKbot\Templates\Champs\Ivern.jpg', 'C:\TarkvaraProjekt\FAAKbot\Templates\Champs\Kindred.jpg' ]

    image = pyautogui.screenshot()
    image = np.array(image)
    image = image[:, :, ::-1].copy()
    #image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image.show()
    
    # Loop for template checking
    for i in range(len(template_path_Berserkers)):
        path = template_path_Berserkers[i]
        template = cv2.imread(path)
        tmp_height= template.shape[0]
        tmp_widght = template.shape[1]

        # Template matching with the screenshot
        matching_result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matching_result)

        # Crop the image to correct size for an ssim compare check to see if the template is actually the searchable champ
        crop_img = image[max_loc[1]:(max_loc[1]+tmp_height), max_loc[0]:(max_loc[0]+tmp_widght)]
        #cv2.imshow("cropped", crop_img)    # just a precation to see if the cropped image is the correct image
        #cv2.waitKey(0)

        crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
        template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        # Match found, move mouse to location and buy champ
        if (compare_ssim(template, crop_img) > 0.95) :
            pyautogui.moveTo(random.randrange(max_loc[0], (max_loc[0]+tmp_widght)), random.randrange(max_loc[1], (max_loc[1]+tmp_height)), random.randrange(1, 3))
            pyautogui.click()
        
    time.sleep(30)
    # If none of the champs occured
    #ReRoll

    # check if the keyboard button '' is pressed, if so break the loop and stop the program
    k = cv2.waitKey(500)
    if k == ord('p') :
        break

