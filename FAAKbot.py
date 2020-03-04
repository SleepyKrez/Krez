import cv2
import pyautogui
from skimage.metrics import structural_similarity as compare_ssim
import random
import time
import numpy as np
from pathlib import Path

#### We need some kind of check to see if the game is running before we start trying to match templates ####
############################################################################################################
#pyautogui.PAUSE = 2
#pyautogui.FAILSAFE = True

while True:
    template_path_Berserkers = ['C:\TarkvaraProjekt\FAAKbot\Templates\Aatrox.jpg', 'C:\TarkvaraProjekt\FAAKbot\Templates\Brand.jpg', 
    'C:\TarkvaraProjekt\FAAKbot\Templates\Braum.jpg', 'C:\TarkvaraProjekt\FAAKbot\Templates\Diana.jpg', 
    'C:\TarkvaraProjekt\FAAKbot\Templates\Dr_Mundo.jpg', 'C:\TarkvaraProjekt\FAAKbot\Templates\Ezreal.jpg',
    'C:\TarkvaraProjekt\FAAKbot\Templates\Ivern.jpg', 'C:\TarkvaraProjekt\FAAKbot\Templates\Kindred.jpg' ]

    #image.astype(np.float32)
    image = pyautogui.screenshot()
    print(type(image))
    image = np.array(image)
    image = image[:, :, ::-1].copy()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #image.show()
    
    # Loop for template checking
    for i in range(len(template_path_Berserkers)):
        path = Path(template_path_Berserkers[i])    
        path2 = r'', template_path_Berserkers[i]

        # Reading in the necessary template to buy the champion
        template = cv2.imread(path2[1], 0)
        tmp_height = template.shape[0]
        tmp_widght = template.shape[1]

        # Template matching with the screenshot
        #image.astype(np.float32)
        matching_result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(matching_result)

        # Crop the image to correct size for an ssim compare check to see if the template is actually the searchable champ
        crop_img = img[max_loc[1]:(max_loc[1]+tmp_height), max_loc[0]:(max_loc[0]+tmp_widght)]
        #cv2.imshow("cropped", crop_img)    # just a precation to see if the cropped image is the correct image

        # Match found, move mouse to location and buy champ
        if (compare_ssim(template, crop_img) > 0.95) :
            pyautogui.move(random.randrange(max_loc[1], (maxloc[1]+tmp_height)), random.randrange(max_loc[0], (max_loc[0]+tmp_widght)), random.random())
            pyautogui.click()
        
    # check if the keyboard button '' is pressed, if so break the loop and stop the program
    k = cv2.waitKey(3000)
    if k == ord('p') :
        break

