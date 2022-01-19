import time

import pygame
import sys
from classes_and_functions.class_text import Text
from txt_managers.manager_settings import SettingsManager as Sm

raw_input = ""
test = False
chars = {pygame.K_a: "A", pygame.K_b: "B", pygame.K_c: "C", pygame.K_d: "D",
         pygame.K_e: "E", pygame.K_f: "F", pygame.K_g: "G", pygame.K_h: "H",
         pygame.K_i: "I", pygame.K_j: "J", pygame.K_k: "K", pygame.K_l: "L",
         pygame.K_m: "M", pygame.K_n: "N", pygame.K_o: "O", pygame.K_p: "P",
         pygame.K_q: "Q", pygame.K_r: "R", pygame.K_s: "S", pygame.K_t: "T",
         pygame.K_u: "U", pygame.K_v: "V", pygame.K_w: "W", pygame.K_x: "X",
         pygame.K_y: "Y", pygame.K_z: "Z", pygame.K_0: "0", pygame.K_1: "1",
         pygame.K_2: "2", pygame.K_3: "3", pygame.K_4: "4", pygame.K_5: "5",
         pygame.K_6: "6", pygame.K_7: "7", pygame.K_8: "8", pygame.K_9: "9",
         pygame.K_SPACE: " ", pygame.K_BACKSPACE: "BACKSPACE",
         pygame.K_RETURN: "ENTER", pygame.K_ESCAPE: "CANCEL"}


def get(prompt, emulator):
    """Replaces the input function, to allow for input from a test file."""
    if not test:  # If this is the main program, just run the normal input
        # function
        prompt_text = Text(prompt, emulator, 20, 750)
        typed_text = ""
        userinput = Text(f"{typed_text}|", emulator, 20, 770)
        end = False
        while not end:
            emulator.screen.fill(Sm().get_screen_colour(), (0, 700, 450, 800))
            prompt_text.blit()
            userinput.blit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    char = ""
                    for k, v in chars.items():
                        if event.key == k:
                            char = v
                    if char == "BACKSPACE":
                        typed_text = typed_text[:-1]
                    elif char == "ENTER":
                        end = True
                        break
                    elif char == "CANCEL":
                        return None
                    else:
                        if len(typed_text) > 20:
                            old_text = typed_text
                            userinput = Text(f"{typed_text}| LINE TOO LONG",
                                             emulator, 20, 770)
                            userinput.blit()
                            pygame.display.flip()
                            time.sleep(0.25)
                            typed_text = old_text
                        else:
                            typed_text += str(char)
                            typed_text = typed_text.title()
                    pygame.display.flip()
            if time.time() % 1 >= 0.5:
                userinput = Text(f"{typed_text}|", emulator, 20,  770)
            else:
                userinput = Text(typed_text, emulator, 20, 770)
            pygame.display.flip()
        return_value = typed_text
    else:  # If in testing mode, return the input from the test program
        return_value = str(raw_input)
    return_value = return_value.title()
    if "Cancel" in return_value:
        return None
    return return_value
