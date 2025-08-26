import time 
from machine import Pin 
from time import sleep 
from sys import stdin 
 
# Horizontal motor pins 
m1 = Pin(10, Pin.OUT) 
m2 = Pin(11, Pin.OUT) 
 
# Vertical motor pins 
m3 = Pin(12, Pin.OUT) 
m4 = Pin(13, Pin.OUT) 
 
# Initialize motor states 
m1.value(0) 
m2.value(0) 
m3.value(0) 
m4.value(0) 
 
# Initial positions 
cur_h = 0  # 0 for center, 1 for left, 2 for right 
cur_v = 0  # 0 for middle, 1 for top, 2 for bottom 
 
while True: 
    ch = stdin.read(1) 
    if ch == '1': 
        tgt_v = 1  # Top 
        tgt_h = 1  # Left 
         
        # vertical 
        # Move vertical motor bottom to top if needed 
        if cur_v != 1 and cur_v == 2: 
            m3.value(0) 
            m4.value(1) 
            sleep(1) 
            m4.value(0) 
            cur_v = tgt_v 
          # Move vertical motor middle to top if needed 
        if cur_v != 1 and cur_v == 0 : 
            m3.value(0) 
            m4.value(1) 
            sleep(0.5) 
            m4.value(0) 
            cur_v = tgt_v 
         
        # horizontal 
        # Move horizontal motor centre to left if needed 
        if cur_h != 1 and cur_h == 0: 
            m1.value(1) 
            m2.value(0) 
            sleep(0.5) 
            m1.value(0) 
            cur_h = tgt_h 
        # Move horizontal motor right to left if needed 
        if cur_h != 1 and cur_h == 2: 
            m1.value(1) 
            m2.value(0) 
            sleep(1) 
            m1.value(0) 
            cur_h = tgt_h 
    elif ch == '2': 
        tgt_v = 1  # Top 
        tgt_h = 0  # Center 
 
        # vertical 
        # Move vertical motor centre to top if needed 
        if cur_v != 1 and cur_v == 0: 
            m3.value(0) 
            m4.value(1) 
            sleep(0.5) 
            m4.value(0) 
            cur_v = tgt_v 
        # Move vertical motor bottom to top if needed 
        if cur_v != 1 and cur_v == 2: 
            m3.value(0) 
            m4.value(1) 
            sleep(1) 
            m4.value(0) 
            cur_v = tgt_v 
 
        # horizontal 
        # Move horizontal motor left to center if needed 
        if cur_h != 0 and cur_h == 1: 
            m1.value(0)
                       m2.value(1) 
            sleep(0.5) 
            m2.value(0) 
            cur_h = tgt_h 
        # Move horizontal motor right to center if needed 
        if cur_h != 0 and cur_h == 2: 
            m1.value(0) 
            m2.value(1) 
            sleep(0.5) 
            m2.value(0) 
            cur_h = tgt_h 
             
    elif ch == '3': 
        tgt_v = 1  # Top 
        tgt_h = 2  # Right 
         
        # Vertical          
        # Move vertical motor center to top if needed 
        if cur_v != 1 and cur_v == 0: 
            m3.value(0) 
            m4.value(1) 
            sleep(0.5) 
            m4.value(0)   
            cur_v = tgt_v 
        # Move vertical motor bottom to top if needed 
        if cur_v != 1 and cur_v == 2: 
            m3.value(0) 
            m4.value(1) 
            sleep(1) 
            m4.value(0)   
            cur_v = tgt_v 
 
        # Horizontal 
        # Move horizontal motor center to right if needed 
        if cur_h != 2 and cur_h == 0: 
            m1.value(0) 
            m2.value(1) 
            sleep(0.5) 
            m2.value(0) 
            cur_h = tgt_h 
        # Move horizontal motor left to right if needed 
        if cur_h != 2 and cur_h == 1: 
            m1.value(0) 
            m2.value(1) 
            sleep(1) 
            m2.value(0) 
            cur_h = tgt_h 
 
    elif ch == '4': 
        tgt_v = 0  # Middle 
        tgt_h = 1  # Left 
 
        # vertical 
        # Move vertical motor top to middle if needed 
        if cur_v != 0 and cur_v == 1: 
            m3.value(1) 
            m4.value(0) 
            sleep(0.5) 
            m3.value(0) 
            cur_v = tgt_v 
        # Move vertical motor bottom to middle if needed 
        if cur_v != 0 and cur_v == 2: 
            m3.value(0) 
            m4.value(1) 
            sleep(0.5) 
            m4.value(0) 
            cur_v = tgt_v 
             
        # horizontal 
        # Move horizontal motor right to left if needed 
        if cur_h != 1 and cur_h == 2: 
            m1.value(1) 
            m2.value(0) 
            sleep(1) 
            m1.value(0) 
            cur_h = tgt_h 
        # Move horizontal motor centre to left if needed 
        if cur_h != 1 and cur_h == 0: 
            m1.value(1) 
            m2.value(0) 
            sleep(0.5) 
            m1.value(0) 
            cur_h = tgt_h
               elif ch == '5': 
        tgt_v = 0  # Middle 
        tgt_h = 0  # Center 
 
        # vertical 
        # Move vertical motor top to middle if needed 
        if cur_v != 0 and cur_v == 1: 
            m3.value(1) 
            m4.value(0) 
            sleep(0.5) 
            m3.value(0) 
            cur_v = tgt_v 
        # Move vertical motor bottom to middle if needed 
        if cur_v != 0 and cur_v == 2: 
            m3.value(0) 
            m4.value(1) 
            sleep(0.5) 
            m4.value(0) 
            cur_v = tgt_v 
         
        # horizontal 
        # Move horizontal motor right to center if needed 
        if cur_h != 0 and cur_h == 2: 
            m1.value(1) 
            m2.value(0) 
            sleep(0.5) 
            m1.value(0) 
 
            cur_h = tgt_h 
        # Move horizontal motor left to center if needed 
        if cur_h != 0 and cur_h == 1: 
            m1.value(0) 
            m2.value(1) 
            sleep(0.5) 
            m2.value(0) 
            cur_h = tgt_h 
             
    elif ch == '6': 
        tgt_v = 0  # Middle 
        tgt_h = 2  # Right 
 
        # Vertical 
        # Move vertical motor top to middle if needed 
        if cur_v != 0 and cur_v == 1: 
            m3.value(1) 
            m4.value(0) 
            sleep(0.5) 
            m3.value(0) 
            cur_v = tgt_v 
        # Move vertical motor bottom to middle if needed 
        if cur_v != 0 and cur_v == 2: 
            m3.value(0) 
            m4.value(1) 
            sleep(0.5) 
            m4.value(0) 
            cur_v = tgt_v 
             
        # Horizontal 
        # Move horizontal motor left to right if needed 
        if cur_h != 2 and cur_h == 1: 
            m1.value(0) 
            m2.value(1) 
            sleep(1) 
            m2.value(0) 
            cur_h = tgt_h 
        # Move horizontal motor center to right if needed 
        if cur_h != 2 and cur_h == 0: 
            m1.value(0) 
            m2.value(1) 
            sleep(0.5) 
            m2.value(0) 
            cur_h = tgt_h 
 
    elif ch == '7': 
        tgt_v = 2  # Bottom 
        tgt_h = 1  # Left 
        # vertical 
        # Move vertical motor top to bottom if needed 
        if cur_v != 2 and cur_v == 1: 
            m3.value(1) 
            m4.value(0) 
            sleep(1) 
            m3.value(0) 
            cur_v = tgt_v
                   # Move vertical motor centre to bottom if needed 
        if cur_v != 2 and cur_v == 0: 
            m3.value(1) 
            m4.value(0) 
            sleep(0.5) 
            m3.value(0) 
            cur_v = tgt_v    
        # horizontal 
        # Move horizontal motor centre to left if needed 
        if cur_h != 1 and cur_h == 0: 
            m1.value(1) 
            m2.value(0) 
            sleep(0.5) 
            m1.value(0) 
            cur_h = tgt_h 
        # Move horizontal motor right to left if needed 
        if cur_h != 1 and cur_h == 2: 
            m1.value(1) 
            m2.value(0) 
            sleep(1) 
            m1.value(0) 
            cur_h = tgt_h 
             
 
    elif ch == '8': 
        tgt_v = 2  # Bottom 
        tgt_h = 0  # Center 
 
        # vertical 
        # Move vertical motor top to bottom if needed 
        if cur_v != 2 and cur_v == 1: 
            m3.value(1) 
            m4.value(0) 
            sleep(1) 
            m3.value(0) 
            cur_v = tgt_v 
        # Move vertical motor centre to bottom if needed 
        if cur_v != 2 and cur_v == 0: 
            m3.value(1) 
            m4.value(0) 
            sleep(0.5) 
            m3.value(0) 
            cur_v = tgt_v 
             
 
        # horizontal 
        # Move horizontal motor left to center if needed 
        if cur_h != 0 and cur_h == 1: 
            m1.value(0) 
            m2.value(1) 
            sleep(0.5) 
            m2.value(0) 
            cur_h = tgt_h 
        # Move horizontal motor right to center if needed 
        if cur_h != 0 and cur_h == 2: 
            m1.value(1) 
            m2.value(0) 
            sleep(0.5) 
            m1.value(0) 
            cur_h = tgt_h 
             
    elif ch == '9': 
        tgt_v = 2  # Bottom 
        tgt_h = 2  # Right 
 
        # Vertical 
        # Move vertical motor top to bottom if needed 
        if cur_v != 2 and cur_v == 1: 
            m3.value(1) 
            m4.value(0) 
            sleep(1) 
            m3.value(0) 
            cur_v = tgt_v 
        # Move vertical motor center to bottom if needed 
        if cur_v != 2 and cur_v == 0: 
            m3.value(1) 
            m4.value(0) 
            sleep(0.5) 
            m3.value(0) 
            cur_v = tgt_v 
         
        # Horizontal 
        # Move horizontal motor left to right if needed 
        if cur_h != 2 and cur_h == 1: 
            m1.value(0) 
            m2.value(1) 
            sleep(1) 
            m2.value(0) 
            cur_h = tgt_h 
        # Move horizontal motor center to right if needed 
        if cur_h != 2 and cur_h == 0: 
            m1.value(0) 
            m2.value(1) 
            sleep(0.5) 
            m2.value(0) 
            cur_h = tgt_h 
 
             
    else: 
        tgt_v = 0  # Middle 
        tgt_h = 0  # Center 
 
        # vertical 
        # Move vertical motor top to middle if needed 
        if cur_v != 0 and cur_v == 1: 
            m3.value(1) 
            m4.value(0) 
            sleep(0.5) 
            m3.value(0) 
            cur_v = tgt_v 
        # Move vertical motor bottom to middle if needed 
        if cur_v != 0 and cur_v == 2: 
            m3.value(0) 
            m4.value(1) 
            sleep(0.5) 
            m4.value(0) 
            cur_v = tgt_v 
         
        # horizontal 
        # Move horizontal motor right to center if needed 
        if cur_h != 0 and cur_h == 2: 
            m1.value(1) 
            m2.value(0) 
            sleep(0.5) 
            m1.value(0) 
 
            cur_h = tgt_h 
        # Move horizontal motor left to center if needed 
        if cur_h != 0 and cur_h == 1: 
            m1.value(0) 
            m2.value(1) 
            sleep(0.5) 
            m2.value(0) 
            cur_h = tgt_h
