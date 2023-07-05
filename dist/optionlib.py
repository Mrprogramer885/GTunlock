import time
import os
import requests



def mainopt():
  print("""===================================
=                                 =
=        SoundPatcher 1.0.0       =
=          ®ThatGuyFromCZ®        =
=                                 =
===================================""")
  input()
  time.sleep(0.8)
  print("...loading scripts...")
  time.sleep(0.5)
  print("...loading encryption keys...")
  print("""
      (1): Unlock game files
      (2): Modify game files
      (3): Script Injector (BETA)
      (4): UI script editor (BETA)
      (5): Upgrade/install libraries
      (6): Creators and Github
      (7): Show supported games
      (8): Other
      (0): Quit GTunlock
      """)
  pyvar = input("select option and write its number here >>> ")
  if pyvar == '1':
    from optionlib import selopt1
    selopt1()
  if pyvar == '2':
    from optionlib import future
    future()  
  if pyvar == '3':  
    from optionlib import future
    future()
  if pyvar == '4':
    from optionlib import future
    future()
  if pyvar == '5':
    from optionlib import selopt5
    selopt5()  
  if pyvar == '6':
    from optionlib import selopt6
    selopt6()
  if pyvar == '7':
    from optionlib import future
    future()
  if pyvar == '0':
    from optionlib import exit
    exit()  
  
def selopt1():  
  input("enter game folder path >> ")
  time.sleep(0.5)
  print("Game folder is valid")
  time.sleep(1.2)
  print("starting Unlocker32.dll...")
  time.sleep(0.2)
  print("Validating game files")
  print("Patching...")
  time.sleep(0.5)
  input("Game file unlocking finished...")
  from GTunlock import mainopt
  mainopt()
  
def selopt2():
  input("enter path to archive or .dll file >>> ")
  time.sleep(0.7)
  print("checking")
  time.sleep(0.2)
  print("Validating")
  time.sleep(1.3)
  print("Valid!")
  time.sleep(0.4)
  input("enter game folder path you wanna modify >>> ")
  time.sleep(1.2)
  print("folder valid!")
  print("extracting into memory")   

def future():
  print("This function will be available in future")
  time.sleep(0.5)
  print("for now, you can only use options that are available")
  
def selopt5():
  print("select libraries to install:")
  time.sleep(1.0)
  print("""
        (1): LibOS 5.0 (installed)
        (2): ClosedCC (insalled)
        (3): Check for updates
        (4): exit
         """)
  liboption = input("select opton >> ")
  if liboption == '1':
    input("library already installed")
    from optionlib import selopt5
    selopt5()
  if liboption == '2':
    input("library already installed")
    from optionlib import selopt5
    selopt5()
  if liboption == '3':
    print("version: 1.1.0")
    print("build = 1.0015.7785-beta")
    print("version state: newest (no updates needed)")
    input("")
    from optionlib import selopt5
    selopt5()
  if liboption == '4':
    from optionlib import mainopt
    mainopt()
  else:
    print("Invalid selection")
    time.sleep("1.0")
    from optionlib import selopt5
    selopt5()
          
def selopt6():
  print("""
        (1): Creators
        (2): Github
        (3): Contribute
        (4): License
        (5): Exit
        """) 
  devoption = input("select option >>> ")
  if devoption == '1':
    print("---Project Leader: TheCzechCEO---")
    time.sleep(1.0)
    print("""developers:
          SmileTH
          Schnookums
          TheGuyWhoAnswered
          NerdiesInc
          """)
    print("""Helpers:
          TheLowkeyNigga
          Atroumen
          nodeless58
          """)
    time.sleep(1.0)
    from optionlib import selopt6
    selopt6()  
  if devoption == '2':
    print("opt2")
  if devoption == '3':
    print("opt3")
  if devoption == '4':
    print("opt4")
  if devoption == '5':
    from optionlib import mainopt
    mainopt()
  else:
    print("Invalid selection")
    from optionlib import selopt6
    selopt6()          
      
def selopt8():
  print("""
        (1): Reset Telemetry
        (2): Check internet Connection
        (3): Privacy Policy
        (4): Clear Cached data
        (5): Delete GTunlock (safe way)
        (6): Exit
        
        
        """)