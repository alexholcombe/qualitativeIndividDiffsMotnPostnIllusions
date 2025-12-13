#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on January 19, 2022, at 00:21
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""


## TC Modified from builder:
    # Turned window blanking off
    # Removed eye tracking setup
    # Removed the default to 60hz if cannot read frameRate
    # removed an unnecessary win.flip() at the end; causes errors/warnings as win.flip() is called beforehand for plotting.
    # For testing mode, log will be made at debugging settings. The last frame interval will be sent to the log files. 
    # Added Trialreps for testing mode, runs less repeats when testing
    # Changing to run at 144hz
    # participants get 5 repeats to pass the attention check. The attention check only appears on the first repeat. By 5 repeats, if they haven't passed att check, unlikely they will.
    # REMOVE THE MULTI-ASSIGNMENT
    
## 11/04 Change. After 43 partiicpants (N < 46), it became clear there was an occasional bugging with the response key sticking (i.e, psychopy thought it was down when it wasn't)
# Comments marked 11/04 indicate changes made that fixed hte issue. 

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, tools
from psychopy.hardware import keyboard
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import os.path
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'FlashJump'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '', 'test': '0'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s_%s' % (expName, expInfo['participant'], expInfo['session'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Timot\\Documents\\2021\\Study 1\\September_Final_EXPERIMENTS_LIVE_Python\\Python-Experiments\\Flash Jump\\Final_FJ.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='ASUS_PG248Q', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', waitBlanking=False,useFBO=True, 
    units='pix') #default is waitBlanking = True 
# store frame rate of monitor if we can measure it
FrameRate = expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else: #FrameRate was none
    print('FrameRate could not be accurately measured!')
    core.quit()

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instr = visual.TextStim(win=win, name='Instr',
    text="During this experiment you will view two bars moving left to right, or right to left. The bars will decrease or increase in height during this experiment.\n \nHalfway during their movement the bars will briefly become white.\nYour task is to make sure the bars height are the same height when they become white. To do this you will adjust the height of one of the bars.\n \nThere is a circle in the centre of the screen. Please stare at this circle at all times. Either the top or bottom half of the circle will be red. The circle will indicate which bar you will adjust. \n\nIf the top half of the circle is red, you will adjust the top bar.\nIf the bottom half of the circle is red, you will adjust the bottom bar. \nPressing the 'UP' arrow key increases the bars height, pressing the 'DOWN' arrow key decreases the bars height. \n\nThe bars will keep repeating until you press 'space'. Press 'space' when the bars are the same height\n\nAs an attention check on some trials the centre circle will change colours. On these trials ONLY press 'r'. \n\nThe first few trials are practice trials that will allow you to familiarise yourself with the task. \n\nPress 's' when you're ready to begin!",
    font='Arial',
    units='height', pos=(0, 0), height=0.027, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
begin = keyboard.Keyboard()

RefreshHz = 144 #win.getActualFrameRate()
if int(expInfo['test']) == 0: #1 = true, it's a test; 0 = false, not a test (LIVE TRIALS)
    if FrameRate <140 or FrameRate > 148 or RefreshHz != 144: #Give a 4 frame buffer 
        print('WARNING! ERROR WITH FRAMERATE OR REFRESHHZ. Psychopy detected the FrameRate at: ' +str(FrameRate) + 'RefreshHz was: ' + str(RefreshHz))
        core.quit()

##Size, in pixels
FixSize = 11

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
FPISI = visual.ImageStim(
    win=win,
    name='FPISI', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(FixSize, FixSize),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)

# Initialize components for Routine "Trials"
TrialsClock = core.Clock()
## This defines the parameters of the square 

## Define temporal parameters
DurSecs = 2 #Total duration of the trial; was 1.5
HalfTime = DurSecs/2 #This is halftime during the tiral
BarDur = int(np.ceil((DurSecs * RefreshHz))) #Get the total duration in frames
DurFrames = int(np.ceil((DurSecs * RefreshHz))) #Get the total duration in frames
Speed = 450 # Pixels per second; 550 is too fast

## Define Square parameters
#FYI: We want the squares to be at zero at halftime
Start_Position = np.floor((Speed * HalfTime)/2) * 2 #Round down to nearest even number

''' SQUARE POSITION'''
#Starting/stopping positions of the squares
LeftX = -Start_Position
RightX = Start_Position

## X coordinate lists:

#We need the squares to be on zero halfway, so we need to specify zero as the endpoint and combine the arrays
LtRX_tozero = np.linspace(LeftX, 0, int(DurFrames/2))
LtRX_FromZero = np.linspace(0, RightX, int(DurFrames/2))
#They double-up on zero as a position, so use unique to remove duplicate values. We then convert this into a python list, so  we can get the index
LtRX = np.unique(np.concatenate((LtRX_tozero, LtRX_FromZero), 0))
RtLX = LtRX * -1 #Right to left
#Convert from numpy arrays to python lists
LtRX = np.ndarray.tolist(LtRX)
RtLX = np.ndarray.tolist(RtLX)
thisExp.addData('Left-Right', LtRX)
thisExp.addData('Right-Left', RtLX)

ZeroPoint = LtRX.index(0) #The array index where the Squares are in alignment (i.e, X = 0)
#print('ZeroPoint', ZeroPoint) #Print this to check it only goes zero once
#print(LtRX[ZeroPoint]) #Print this index to double-check it's returning zero

#Y coordinates of the squares
BarY = 220 #250 #216

''' SQUARE HEIGHT LISTS'''
MinValue = 30 #Smallest size of the bar
MaxValue = MinValue + DurFrames #308 Largest size of the bar - Determined by changing one pixel per frame
 
Growing_List = np.linspace(MinValue, MaxValue, DurFrames)
Shrinking_List = np.linspace(MaxValue, MinValue, DurFrames)

## THESE TWO SAVES BREAK THE MATLAB AUTOIMPORTER FOR CSVS. 
#thisExp.addData('Growing_List', Growing_List)
#thisExp.addData('Shrinking_List', Shrinking_List)

#Actual size of the bars when the squares are in vertical alignment
ActualSizeGrowing = Growing_List[ZeroPoint]
ActualSizeShrinking = Shrinking_List[ZeroPoint]
thisExp.addData('ActualSizeGrowing', ActualSizeGrowing)
thisExp.addData('ActualSizeShrinking', ActualSizeShrinking) 

loopCount = 0 #Count the loop 

#If this is true, practice trials will play until set false
practiceTrials =  True

trialcount = 0
#barCol is black
barCol = [-1,-1,-1]
#How much to adjust the height of the bar   (this is the effect
Adjust = 0
AdjustHistory = []
KeyHistory = [] #Response of keys over the trial

#How much the height of the bar will change per keypress
AdjustmentAmount = 2 #2 # 5 #Offset is 60 Old: 21

#If they make 8 key presses, the bar becomes zero, so stop them at 8 keypresses from making more
MaxNumDumPress = 8 #Max number of presses they are allowed
DownKeyCount = 0 #Ultimate count, basically stops them from just pressing it down into infinitity and making it hard to move upwards

# Sometimes, the up application breaks, and it just keeps applying up changes without a keypress. This is to stop that
Accumulator = 0

resp = 'placeholder'

#Place holder to stop javascript erroring
AdjustedBarHeight = 0
RefBarHeight = 0 #The bar height of the referefence stimulus

#Placeholder values to stop crashing
XAdjustedBarHeight  = 0
XRefBarHeight = 0
FrameNAdjustedBarHeight  = 0
FrameNRefBarHeight = 0

#At the time of the flash, the squares are normally .16
#So offset 25% larger or smaller, 50% broke it
offsetAmount = 60 #80

CorrAdjust = False #If True, then we correct adjustment
## Define flash change parameters
#Zeropoint is the point when the squares are in vertical alignment.
#We want the colour change to occur for ~16.67ms BEFORE and AFTER the colour change (3 frames at 200hz, 2 at 144hz)

#These are the thresholds of colour change

if RefreshHz == 60:
    Low_Frame_Colour = int(ZeroPoint) - 1 #141
    High_Frame_Colour = int(ZeroPoint) + 1 #145
elif RefreshHz == 144: #This is approximately 13.88ms
    Low_Frame_Colour = int(ZeroPoint) - 2 #141
    High_Frame_Colour = int(ZeroPoint) + 2 #145
elif RefreshHz == 200: #15ms
    Low_Frame_Colour = int(ZeroPoint) - 3
    High_Frame_Colour = int(ZeroPoint) + 3

warning = True #IS ALWAYS TRUE, SET TO FALSE IF THEY PRESS SPACE
noKeyResp = True #Has to be a default state, goes to false if they press ANY KEY
warnCount = 0
endTask = False
TopBar = visual.Rect(
    win=win, name='TopBar',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor=barCol, fillColor=barCol,
    opacity=1, depth=-6.0, interpolate=True)
BotBar = visual.Rect(
    win=win, name='BotBar',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor=barCol, fillColor=barCol,
    opacity=1, depth=-7.0, interpolate=True)
FixationPoint = visual.ImageStim(
    win=win,
    name='FixationPoint', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(FixSize, FixSize),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-8.0)
#Define variable here
wasprac = 'no'
#Report warnings to the standard output window
logging.console.setLevel(logging.WARNING)

PastCount = 0

# Initialize components for Routine "PracRout"
PracRoutClock = core.Clock()
pracTrialCount = 0 #We only want to display this routine every second trial
Practext = visual.TextStim(win=win, name='Practext',
    text="You have just completed the practice trials.\n\nJust a friendly reminder that during the experiment, please stare at the red and white dot in the center of the screen. \n\nTo start the live experiment press 's'\n",
    font='Open Sans',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Pracresp = keyboard.Keyboard()

# Initialize components for Routine "AttISI"
AttISIClock = core.Clock()
FPISI_ATT = visual.ImageStim(
    win=win,
    name='FPISI_ATT', units='pix', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(FixSize, FixSize),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)

# Initialize components for Routine "AttentionCheck"
AttentionCheckClock = core.Clock()
#Do check trials after this many trials
CheckOn = 15 #The trial count + 1 at the end of the trial
#Without - 1, trialcount15 is actually trial 16 e.t.c

respATT = [] #Placeholder

## Define attention check colour change parameters
#During the attention check, the fixation point will fluctuate in colour
#Define the colours
MyRed = (1, -1, -1)
myYell = (1.0000, 1.0000, -1.0000)
myGreen = (-1, 1, -1)
myOrange = (1.0000, 0.2941, -1.0000) 
myCyan = (-1.0000, 1.0000, 1.0000)
myMagneta = (1.0000, -1.0000, 1.0000)
myPurple = (0.0039, -1.0000, 0.0039) 
myBlack = (-1, -1, -1)
ColourList = [myYell, myGreen, MyRed, myPurple, myMagneta, myCyan, myOrange]

CheckColor = myBlack

AttCheck_Timer = core.Clock() ## INITIALISE TIMER FOR THE ATTENTION CHECK


ListIdx = 0 #To select a colour from the list
CheckTrials = False #Do check trials now?
CheckPass = False #Did they fail the attention check

#Update colour after how many frames; 1 is super quick
if RefreshHz == 144:
    UpdateOn = 18 #125ms
elif RefreshHz == 60:
    UpdateOn = 8
elif RefreshHz == 200:
    UpdateOn  = 26

NumFails = 0
FailedAtt = False

FIX_ATT = visual.ShapeStim(
    win=win, name='FIX_ATT', vertices=99,
    size=[1.0, 1.0],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=CheckColor, fillColor=CheckColor,
    opacity=None, depth=-1.0, interpolate=True)
AttloopCount = 0 
TopBar_ATT = visual.Rect(
    win=win, name='TopBar_ATT',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor=barCol, fillColor=barCol,
    opacity=1, depth=-6.0, interpolate=True)
BotBar_ATT = visual.Rect(
    win=win, name='BotBar_ATT',units='pix', 
    width=[1.0, 1.0][0], height=[1.0, 1.0][1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor=barCol, fillColor=barCol,
    opacity=1, depth=-7.0, interpolate=True)

# Initialize components for Routine "Warning"
WarningClock = core.Clock()
DisplayMSG = visual.TextStim(win=win, name='DisplayMSG',
    text='',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
WarningResp = keyboard.Keyboard()

# Initialize components for Routine "Break"
BreakClock = core.Clock()
BreakText = visual.TextStim(win=win, name='BreakText',
    text="This is a break. Rest for as long as  you need! \n\nJust a friendly reminder that during the experiment, please stare at the red and white dot in the center of the screen. \n\nPress 'e' when you are ready to resume the experiment.\n\n",
    font='Open Sans',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Endbreak = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
letHeight = 0
Farewell = visual.TextStim(win=win, name='Farewell',
    text='Thank you for completing this experiment.\n\nPlease tell the researcher you have finished.\n',
    font='Arial',
    units='height', pos=(0, 0), height=1.0, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
begin.keys = []
begin.rt = []
_begin_allKeys = []
win.mouseVisible = False
## Check the file does not already exist

if os.path.exists(filename + '.csv'):
    print('Warning: Datafile already exists!')
    core.quit()
# keep track of which components have finished
InstructionsComponents = [Instr, begin]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instr* updates
    if Instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instr.frameNStart = frameN  # exact frame index
        Instr.tStart = t  # local t and not account for scr refresh
        Instr.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instr, 'tStartRefresh')  # time at next scr refresh
        Instr.setAutoDraw(True)
    
    # *begin* updates
    waitOnFlip = False
    if begin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        begin.frameNStart = frameN  # exact frame index
        begin.tStart = t  # local t and not account for scr refresh
        begin.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(begin, 'tStartRefresh')  # time at next scr refresh
        begin.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(begin.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(begin.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if begin.status == STARTED and not waitOnFlip:
        theseKeys = begin.getKeys(keyList=['s', 'a', 'd', 'w'], waitRelease=False)
        _begin_allKeys.extend(theseKeys)
        if len(_begin_allKeys):
            begin.keys = _begin_allKeys[-1].name  # just the last key pressed
            begin.rt = _begin_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instr.started', Instr.tStartRefresh)
thisExp.addData('Instr.stopped', Instr.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
ChooseCondFile = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SelectCondFile.xlsx'),
    seed=None, name='ChooseCondFile')
thisExp.addLoop(ChooseCondFile)  # add the loop to the experiment
thisChooseCondFile = ChooseCondFile.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisChooseCondFile.rgb)
if thisChooseCondFile != None:
    for paramName in thisChooseCondFile:
        exec('{} = thisChooseCondFile[paramName]'.format(paramName))

for thisChooseCondFile in ChooseCondFile:
    currentLoop = ChooseCondFile
    # abbreviate parameter names if possible (e.g. rgb = thisChooseCondFile.rgb)
    if thisChooseCondFile != None:
        for paramName in thisChooseCondFile:
            exec('{} = thisChooseCondFile[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    ## BCAUSE THERE IS ONLY ONE REPEAT FOR THIS LOOP, EFFECTIVELY, RANDOM OR FULLY RANDOM IS TRULY RANDOM. They're the same. 
    OverarchingLoops = data.TrialHandler(nReps=1, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(condFile),
        seed=None, name='OverarchingLoops')
    thisExp.addLoop(OverarchingLoops)  # add the loop to the experiment
    thisOverarchingLoop = OverarchingLoops.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisOverarchingLoop.rgb)
    if thisOverarchingLoop != None:
        for paramName in thisOverarchingLoop:
            exec('{} = thisOverarchingLoop[paramName]'.format(paramName))
    
    for thisOverarchingLoop in OverarchingLoops:
        currentLoop = OverarchingLoops
        # abbreviate parameter names if possible (e.g. rgb = thisOverarchingLoop.rgb)
        if thisOverarchingLoop != None:
            for paramName in thisOverarchingLoop:
                exec('{} = thisOverarchingLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ISI"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        FPISI.setImage(FP)
        # keep track of which components have finished
        ISIComponents = [FPISI]
        for thisComponent in ISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FPISI* updates
            if FPISI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FPISI.frameNStart = frameN  # exact frame index
                FPISI.tStart = t  # local t and not account for scr refresh
                FPISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FPISI, 'tStartRefresh')  # time at next scr refresh
                FPISI.setAutoDraw(True)
            if FPISI.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FPISI.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    FPISI.tStop = t  # not accounting for scr refresh
                    FPISI.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FPISI, 'tStopRefresh')  # time at next scr refresh
                    FPISI.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI"-------
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        OverarchingLoops.addData('FPISI.started', FPISI.tStartRefresh)
        OverarchingLoops.addData('FPISI.stopped', FPISI.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        RepeatTrials = data.TrialHandler(nReps=45, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='RepeatTrials')
        thisExp.addLoop(RepeatTrials)  # add the loop to the experiment
        thisRepeatTrial = RepeatTrials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisRepeatTrial.rgb)
        if thisRepeatTrial != None:
            for paramName in thisRepeatTrial:
                exec('{} = thisRepeatTrial[paramName]'.format(paramName))
        
        for thisRepeatTrial in RepeatTrials:
            currentLoop = RepeatTrials
            # abbreviate parameter names if possible (e.g. rgb = thisRepeatTrial.rgb)
            if thisRepeatTrial != None:
                for paramName in thisRepeatTrial:
                    exec('{} = thisRepeatTrial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Trials"-------
            continueRoutine = True
            # update component parameters for each repeat
            #CoordsX is the top Coordinates
            FlashDur = 0 #I need to understand how long the flash goes on for
            
            Idx = 0 #Use this to loop through the x coordinates and size lists on each frame. The list lengths are identical
            
            if Condition == 'Cond1':
                CoordsX = LtRX[Idx] 
                TopSize = Growing_List[Idx]  
                BotSize = Shrinking_List[Idx]
            elif Condition == 'Cond2':
                CoordsX = RtLX[Idx] 
                TopSize = Growing_List[Idx]  
                BotSize = Shrinking_List[Idx]
            elif Condition == 'Cond3': #These are also practice trials now
                CoordsX = LtRX[Idx]
                BotSize = Growing_List[Idx]  
                TopSize = Shrinking_List[Idx]
            elif Condition == 'Cond4':
                CoordsX = RtLX[Idx] 
                BotSize = Growing_List[Idx]  
                TopSize = Shrinking_List[Idx]
            
            BotX = CoordsX * -1
            
            #Set position every beginning of routine
            TopBar.setPos((CoordsX, BarY))
            BotBar.setPos((BotX, -BarY))    
            #setColor is hard
            # or .color both do lines and object simulatenously
            TopBar.color = (barCol)
            BotBar.color = (barCol)
            
            respHistory = [] #response history of the keys
            
            ## Initialise keyboard.
            #The idea is, it will store a single key, before it drops the old one
            kb = keyboard.Keyboard() #bufferSize
            kb.clock.reset() #Restart the timer
            
            #You need to draw the size before the frame
            #To avoid animation issues
            
            #Ensure the first frame loads correctly
            loopCount += 1
            
            if FP == 'FixationPointup.png':
                Tsize = TopSize + Adjust 
                Bsize = BotSize
            else:
                Bsize = BotSize + Adjust 
                Tsize = TopSize
            
            BotBar.setSize((11, Bsize))
            TopBar.setSize((11, Tsize)) 
            
            
            #Flip counter, this counts the flip from white back to black
            #We only wanna flip once back to black (to save frames)
            flipCol = False
            
            FixationPoint.setImage(FP)
            #This code component simply exists to tell me if it was a practice trial
            #For my first four participants, I had to manually do this in excel
            if condFile == 'FJPrac.xlsx':
                wasprac = 'yes'
            else:
                wasprac = 'no'
            
            thisExp.addData('wasprac', wasprac)
            win.recordFrameIntervals = True #win.nDroppedFrames stores this. 
            
            #Set a 10% tolerance for dropped frames
            win.refreshThreshold = (1/RefreshHz) * 1.1
            
            DisgardTrial = False
            
            #manual frame drop counter
            #FramesDropped = 0
            # keep track of which components have finished
            TrialsComponents = [TopBar, BotBar, FixationPoint]
            for thisComponent in TrialsComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            TrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "Trials"-------
            while continueRoutine:
                # get current time
                t = TrialsClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=TrialsClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                #Conditions are selected by the excel condition file
                if Condition == 'Cond1':
                    CoordsX = LtRX[Idx] 
                    TopSize = Growing_List[Idx]  
                    BotSize = Shrinking_List[Idx]
                elif Condition == 'Cond2':
                    CoordsX = RtLX[Idx] 
                    TopSize = Growing_List[Idx]  
                    BotSize = Shrinking_List[Idx]
                elif Condition == 'Cond3': #These are also practice trials now
                    CoordsX = LtRX[Idx]
                    BotSize = Growing_List[Idx]  
                    TopSize = Shrinking_List[Idx]
                elif Condition == 'Cond4':
                    CoordsX = RtLX[Idx] 
                    BotSize = Growing_List[Idx]
                    TopSize = Shrinking_List[Idx]
                
                BotX = CoordsX * -1
                
                #Moved Idx increment to the applyajust tab
                '''
                ## Move through the lists:
                if Idx < (len(LtRX) - 1):
                    Idx += 1
                '''
                
                ## Change Bar Height with key press
                #Based on Griegner's solution here: https://discourse.psychopy.org/t/visual-analog-scale-press-and-hold-key/21098/2
                
                keys = kb.getKeys(['up', 'down', 'space'], waitRelease=False, clear=False) #waitRealse = False
                
                if keys and not keys[-1].duration: #if keys means, there is a key here and NOT keys[-1].duration means THERE IS NO DURATION. Duration only recorded when key lifted 
                    resp = keys[-1].name #the last key's name
                   
                    if resp == 'up':
                        noKeyResp = False
                        DownKeyCount -= 1
                        if Accumulator < 200:
                            Adjust += AdjustmentAmount
                            Accumulator += 1
                            if Accumulator >= 199: #11/04 Change, after 199 presses, reset the buffer so they have to repress
                                kb.clearEvents()
                        KeyHistory.append("up")
                        #print('Adjust', Adjust)
                    elif resp == 'down': #'down' in resp:
                        noKeyResp = False
                        if DownKeyCount < 200: #200; This will control how small it gets
                            Adjust -= AdjustmentAmount
                            KeyHistory.append("down")
                            DownKeyCount += 1
                            if DownKeyCount >= 199: #11/04 Change, after 199 presses, reset it so they have to repress
                                kb.clearEvents()
                    elif resp == 'space': #'space' in resp:
                        warning = False
                        noKeyResp = False
                        thisExp.addData('BarAdjustmentAmount', Adjust)
                        DownKeyCount = 0
                        count = 0
                        #Reset loopcount once people have pressed the routine
                        Adjust = 0
                        loopCount = 0
                        KeyHistory.append("space")
                        thisExp.addData('KeyHistoryTOTAL', KeyHistory) #Save a list of all Keypresses 
                        KeyHistory = []
                        thisExp.addData('Adjust', AdjustHistory)
                        AdjustHistory = []
                        BackAdjust = 0 #Reset backadjust
                        if wasprac == 'no':
                            trialcount += 1
                        thisExp.addData('trialcount', trialcount) 
                        kb.clearEvents() #Clear all the keyboard presses to stop issues.
                        continueRoutine = False
                        RepeatTrials.finished = True #End the loop that maintains a continuous rerun
                    Adjust = np.round(Adjust) #Adjust and adjustment amount should be a whole pixel value
                    AdjustHistory.append(Adjust)
                else:
                    #resp ='placeholder'
                    Accumulator = 0 #As no key is down, it's safe to reset up accumulator, so it is applied
                if FP == 'FixationPointup.png':
                    #Apply adjustment
                    Tsize = TopSize + Adjust 
                    
                    #This stops bar height going negative
                    if Tsize < 0:
                        Tsize = 6
                
                   # Offset height
                    if OffsetDir == 'BotLrg': #Bottom Square Taller
                        Bsize = BotSize + offsetAmount 
                    elif OffsetDir == 'BotSml': #Bottom square smaller
                        Bsize = BotSize - offsetAmount 
                    else:
                        Bsize = BotSize #No changes in size
                    
                    #Stop reference going less than zero
                    if Bsize < 0:
                        Bsize = 6
                else:
                    #Applys keyboard adjusment
                    Bsize = BotSize + Adjust 
                    
                    #Stops value going negative
                    if Bsize < 0:
                        Bsize = 6
                        
                    #Offset height:
                    if OffsetDir == 'TopLRG':
                        Tsize = TopSize + offsetAmount  #TopSQ taller
                    elif OffsetDir == 'TopSML':
                        Tsize = TopSize - offsetAmount #TopSQ smaller
                    else:
                        Tsize = TopSize #no changes in size
                    
                    #Need to stop the reference stimuli going in reverse
                    if Tsize < 0:
                        Tsize = 6
                
                #Store the height of the adjusted bar, at time of flash (x = 0)
                if Idx == ZeroPoint:
                    if FP == 'FixationPointup.png':
                        XAdjustedBarHeight  = Tsize
                        XRefBarHeight = Bsize
                        if Condition == 'Cond1' or Condition == 'Cond2': #Cond 1 and 2 top growing, 3 and 4 shrinking        
                            OriginalSize = Growing_List[ZeroPoint]
                        else:
                            OriginalSize = Shrinking_List[ZeroPoint]      
                    else:
                        if Condition == 'Cond1' or Condition == 'Cond2': #Cond 1 and 2 top growing, 3 and 4 shrinking        
                            OriginalSize = Shrinking_List[ZeroPoint]   
                        else:
                            OriginalSize = Growing_List[ZeroPoint]    
                            
                        XAdjustedBarHeight  = Bsize  
                        XRefBarHeight = Tsize 
                    thisExp.addData('XCoord_AdjustedBarHeight', XAdjustedBarHeight)
                    thisExp.addData('XCoord_ReferenceBar', XRefBarHeight)
                    thisExp.addData('OriginalSize', OriginalSize) #Size of the bar to be adjusted, pre-adjustment
                
                '''
                Tsize = np.round(Tsize) #keep the pixels in whole numbers
                Bsize = np.round(Bsize) #keep the pixels in whole numbers
                '''
                
                #thisExp.addData('BackupAdjust', BackAdjust)
                thisExp.addData('TopSize', Tsize)
                thisExp.addData('BotSize', Bsize)
                
                ## Move through the lists:
                if Idx < (len(LtRX) - 1):
                    Idx += 1
                #Change colour
                #Flash on these X Coords
                #When speedcontrol was 1.5:
                #if CoordsX < 0.013 and CoordsX > -0.013:
                #Flash is displayed for 3 frames; 50ms
                
                if Idx <= High_Frame_Colour and Idx >= Low_Frame_Colour:
                    barCol = [1,1,1] #White
                    TopBar.color = (barCol)
                    BotBar.color = (barCol)
                    FlashDur += 1
                    thisExp.addData('FlashonFrame', frameN)
                    thisExp.addData('FlashDuration', FlashDur)
                    flipCol = True
                
                else:
                    if flipCol == True:
                        barCol = [-1,-1,-1] #black
                        flipCol = False
                        TopBar.color = (barCol)
                        BotBar.color = (barCol)
                
                
                # *TopBar* updates
                if TopBar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TopBar.frameNStart = frameN  # exact frame index
                    TopBar.tStart = t  # local t and not account for scr refresh
                    TopBar.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TopBar, 'tStartRefresh')  # time at next scr refresh
                    TopBar.setAutoDraw(True)
                if TopBar.status == STARTED:
                    if frameN >= (TopBar.frameNStart + BarDur):
                        # keep track of stop time/frame for later
                        TopBar.tStop = t  # not accounting for scr refresh
                        TopBar.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(TopBar, 'tStopRefresh')  # time at next scr refresh
                        TopBar.setAutoDraw(False)
                if TopBar.status == STARTED:  # only update if drawing
                    TopBar.setPos((CoordsX, BarY), log=False)
                    TopBar.setSize((11, Tsize), log=False)
                
                # *BotBar* updates
                if BotBar.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BotBar.frameNStart = frameN  # exact frame index
                    BotBar.tStart = t  # local t and not account for scr refresh
                    BotBar.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BotBar, 'tStartRefresh')  # time at next scr refresh
                    BotBar.setAutoDraw(True)
                if BotBar.status == STARTED:
                    if frameN >= (BotBar.frameNStart + BarDur):
                        # keep track of stop time/frame for later
                        BotBar.tStop = t  # not accounting for scr refresh
                        BotBar.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(BotBar, 'tStopRefresh')  # time at next scr refresh
                        BotBar.setAutoDraw(False)
                if BotBar.status == STARTED:  # only update if drawing
                    BotBar.setPos((BotX, -BarY), log=False)
                    BotBar.setSize((11, Bsize), log=False)
                
                # *FixationPoint* updates
                if FixationPoint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    FixationPoint.frameNStart = frameN  # exact frame index
                    FixationPoint.tStart = t  # local t and not account for scr refresh
                    FixationPoint.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(FixationPoint, 'tStartRefresh')  # time at next scr refresh
                    FixationPoint.setAutoDraw(True)
                if FixationPoint.status == STARTED:
                    if frameN >= (FixationPoint.frameNStart + BarDur):
                        # keep track of stop time/frame for later
                        FixationPoint.tStop = t  # not accounting for scr refresh
                        FixationPoint.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(FixationPoint, 'tStopRefresh')  # time at next scr refresh
                        FixationPoint.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in TrialsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "Trials"-------
            for thisComponent in TrialsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            #reset flip, we only want to flip from white to black once
            flipCol = False
            barCol = [-1,-1,-1] #Black
            #Each trial is approximately 2-3 seconds long.
            #This gives participants 60 seconds to respond/make a key press
            
            #Participants did not make a single key press at all in 1 minute
            #Participants are taking too long, give them a friendly warning
            if loopCount >= 30:
                warning = True
                if len(KeyHistory) == 0:
                #if resp.keys != 'up' and resp.keys != 'down' and resp.keys != 'space':
                    continueRoutine = False
                    thisExp.addData('BarAdjustmentAmount', Adjust)
                    Adjust = 0
                    loopCount = 0
                    count = 0
                    RepeatTrials.finished = True
                    warning = True
                    noKeyResp = True
                    warnCount += 1
                    KeyHistory = []
                    trialcount += 1
                    thisExp.addData('trialcount', trialcount)
            thisExp.addData('loopCount', loopCount)
            thisExp.addData('DidNotMakeaKeyPress', noKeyResp)
            
            #Participants are spending too long, give them a polite reminder
            #They don't have to be perfect
            if loopCount >= 45:
                loopCount = 0
                if KeyHistory[-1] == "space":
                    thisExp.addData('BarAdjustmentAmount', Adjust)
                    Adjust = 0
                    count = 0
                    warning = True
                    KeyHistory = []
                    thisExp.addData('trialcount', trialcount)
            #Adjusted bar height - reference bar height
            #Bar heights at time of flash
            
            #Positive numbers represent extrapolation along the trajectory
            #Thus, if shrinking we need to *-1
            #They produce the same value
            
            CoordsX_CaiEffect = XAdjustedBarHeight - XRefBarHeight
            
            '''
            if SidetoAdjustis == 'Shrinking':
                CoordsX_CaiEffect = CoordsX_CaiEffect * -1
            '''
            
            if resp == 'space': #'space' in resp::
                thisExp.addData('CoordsX_FinalCaieff', CoordsX_CaiEffect)
            
            else:
                thisExp.addData('CoordsX_interimCaiEffect', CoordsX_CaiEffect)
            
            
            #Thsi way we know what side and offset was associated with each effect
            #To stop SidetoAdjustis going nan:
            SideSave = SidetoAdjustis
            thisExp.addData('SideSave', SideSave)
            
            #To stop offsetDir = blank
            OffSetDirBack = OffsetDir
            thisExp.addData('OffsetDirBack', OffSetDirBack)
            RepeatTrials.addData('TopBar.started', TopBar.tStartRefresh)
            RepeatTrials.addData('TopBar.stopped', TopBar.tStopRefresh)
            RepeatTrials.addData('BotBar.started', BotBar.tStartRefresh)
            RepeatTrials.addData('BotBar.stopped', BotBar.tStopRefresh)
            RepeatTrials.addData('FixationPoint.started', FixationPoint.tStartRefresh)
            RepeatTrials.addData('FixationPoint.stopped', FixationPoint.tStopRefresh)
            #Print the dropped frames
            win.recordFrameIntervals = False
            thisExp.addData('AutoDroppedFrames', win.nDroppedFrames)
            #thisExp.addData('ManualFramesDropped', FramesDropped)
            
            if win.nDroppedFrames > PastCount:
                DisgardTrial = True
            
            thisExp.addData('DisgardTrial', DisgardTrial)
            
            #Past count of dropped frames
            PastCount = win.nDroppedFrames
            # the Routine "Trials" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 45 repeats of 'RepeatTrials'
        
        
        # ------Prepare to start Routine "PracRout"-------
        continueRoutine = True
        # update component parameters for each repeat
        pracTrialCount += 1
        
        if pracTrialCount != 3:
            continueRoutine = False
        Pracresp.keys = []
        Pracresp.rt = []
        _Pracresp_allKeys = []
        # keep track of which components have finished
        PracRoutComponents = [Practext, Pracresp]
        for thisComponent in PracRoutComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracRoutClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "PracRout"-------
        while continueRoutine:
            # get current time
            t = PracRoutClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracRoutClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Practext* updates
            if Practext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Practext.frameNStart = frameN  # exact frame index
                Practext.tStart = t  # local t and not account for scr refresh
                Practext.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Practext, 'tStartRefresh')  # time at next scr refresh
                Practext.setAutoDraw(True)
            
            # *Pracresp* updates
            waitOnFlip = False
            if Pracresp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Pracresp.frameNStart = frameN  # exact frame index
                Pracresp.tStart = t  # local t and not account for scr refresh
                Pracresp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Pracresp, 'tStartRefresh')  # time at next scr refresh
                Pracresp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Pracresp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Pracresp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Pracresp.status == STARTED and not waitOnFlip:
                theseKeys = Pracresp.getKeys(keyList=['s', 'p'], waitRelease=False)
                _Pracresp_allKeys.extend(theseKeys)
                if len(_Pracresp_allKeys):
                    Pracresp.keys = _Pracresp_allKeys[-1].name  # just the last key pressed
                    Pracresp.rt = _Pracresp_allKeys[-1].rt
                    # was this correct?
                    if (Pracresp.keys == str("'s'")) or (Pracresp.keys == "'s'"):
                        Pracresp.corr = 1
                    else:
                        Pracresp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracRoutComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracRout"-------
        for thisComponent in PracRoutComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        OverarchingLoops.addData('Practext.started', Practext.tStartRefresh)
        OverarchingLoops.addData('Practext.stopped', Practext.tStopRefresh)
        # check responses
        if Pracresp.keys in ['', [], None]:  # No response was made
            Pracresp.keys = None
            # was no response the correct answer?!
            if str("'s'").lower() == 'none':
               Pracresp.corr = 1;  # correct non-response
            else:
               Pracresp.corr = 0;  # failed to respond (incorrectly)
        # store data for OverarchingLoops (TrialHandler)
        OverarchingLoops.addData('Pracresp.keys',Pracresp.keys)
        OverarchingLoops.addData('Pracresp.corr', Pracresp.corr)
        if Pracresp.keys != None:  # we had a response
            OverarchingLoops.addData('Pracresp.rt', Pracresp.rt)
        OverarchingLoops.addData('Pracresp.started', Pracresp.tStartRefresh)
        OverarchingLoops.addData('Pracresp.stopped', Pracresp.tStopRefresh)
        # the Routine "PracRout" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "AttISI"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        FPISI_ATT.setImage(FP)
        if trialcount >=1 and trialcount % CheckOn != 0:
            continueRoutine = False
        
        if trialcount == 0:
            continueRoutine = False
        # keep track of which components have finished
        AttISIComponents = [FPISI_ATT]
        for thisComponent in AttISIComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AttISIClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AttISI"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = AttISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AttISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FPISI_ATT* updates WE ONLY WANT TO 
            if FPISI_ATT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FPISI_ATT.frameNStart = frameN  # exact frame index
                FPISI_ATT.tStart = t  # local t and not account for scr refresh
                FPISI_ATT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FPISI_ATT, 'tStartRefresh')  # time at next scr refresh
                FPISI_ATT.setAutoDraw(True)
            if FPISI_ATT.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FPISI_ATT.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    FPISI_ATT.tStop = t  # not accounting for scr refresh
                    FPISI_ATT.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FPISI_ATT, 'tStopRefresh')  # time at next scr refresh
                    FPISI_ATT.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AttISIComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AttISI"-------
        for thisComponent in AttISIComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        OverarchingLoops.addData('FPISI_ATT.started', FPISI_ATT.tStartRefresh)
        OverarchingLoops.addData('FPISI_ATT.stopped', FPISI_ATT.tStopRefresh)
        
        # set up handler to look after randomisation of conditions etc
        AttRepeatTrials = data.TrialHandler(nReps=40.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=[None],
            seed=None, name='AttRepeatTrials')
        thisExp.addLoop(AttRepeatTrials)  # add the loop to the experiment
        thisAttRepeatTrial = AttRepeatTrials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisAttRepeatTrial.rgb)
        if thisAttRepeatTrial != None:
            for paramName in thisAttRepeatTrial:
                exec('{} = thisAttRepeatTrial[paramName]'.format(paramName))
        
        for thisAttRepeatTrial in AttRepeatTrials:
            currentLoop = AttRepeatTrials
            # abbreviate parameter names if possible (e.g. rgb = thisAttRepeatTrial.rgb)
            if thisAttRepeatTrial != None:
                for paramName in thisAttRepeatTrial:
                    exec('{} = thisAttRepeatTrial[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "AttentionCheck"-------
            continueRoutine = True
            # update component parameters for each repeat
            #Do check trials on how many trials (Do not do on first trial)
            if trialcount >=1 and trialcount % CheckOn == 0:
                CheckTrials = True
                shuffle(ColourList) #Make the RGB random
            else:
                CheckTrials = False
                CheckPass = False
                continueRoutine = False
                AttRepeatTrials.finished = True
                
            #Was it a check trial?
            thisExp.addData('CheckTrials', CheckTrials)
            
            
                
            
            Att_Idx = 0 #Use this to loop through the x coordinates and size lists on each frame. The list lengths are identical
            
            if Condition == 'Cond1':
                CoordsX = LtRX[Att_Idx] 
                TopSize = Growing_List[Att_Idx]  
                BotSize = Shrinking_List[Att_Idx]
            elif Condition == 'Cond2':
                CoordsX = RtLX[Att_Idx] 
                TopSize = Growing_List[Att_Idx]  
                BotSize = Shrinking_List[Att_Idx]
            elif Condition == 'Cond3': #These are also practice trials now
                CoordsX = LtRX[Att_Idx]
                BotSize = Growing_List[Att_Idx]  
                TopSize = Shrinking_List[Att_Idx]
            elif Condition == 'Cond4':
                CoordsX = RtLX[Att_Idx] 
                BotSize = Growing_List[Att_Idx]  
                TopSize = Shrinking_List[Att_Idx]
            
            BotX = CoordsX * -1
            TopBar_ATT.color = (barCol)
            BotBar_ATT.color = (barCol)
            
            #If they accidentally hit space during the break or start of the exp
            #It will skip a trial
            
            ATTKB = keyboard.Keyboard()
            #You need to draw the size before the frame
            #To avoid animation issues
            
            if FP == 'FixationPointup.png':
                Tsize = TopSize + Adjust 
                Bsize = BotSize
            else:
                Bsize = BotSize + Adjust 
                Tsize = TopSize
            
            BotBar.setSize((11, Bsize))
            TopBar.setSize((11, Tsize)) 
            
            
            if CheckTrials == True:
                AttloopCount += 1
            # keep track of which components have finished
                #If the loopcount = 1, reset the timer
                if AttloopCount == 1:
                    AttCheck_Timer.reset()
            
            AttentionCheckComponents = [FIX_ATT, TopBar_ATT, BotBar_ATT]
            for thisComponent in AttentionCheckComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            AttentionCheckClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "AttentionCheck"-------
            while continueRoutine:
                # get current time
                t = AttentionCheckClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AttentionCheckClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                ## Set the colour of the fixation to fluctuate each frame:
                if CheckTrials == True and AttloopCount == 1 and frameN < RefreshHz: #We only want to update the attention check first second of the first trial
                    if frameN % UpdateOn == 0:
                        CheckColor = ColourList[ListIdx]
                        FIX_ATT.color = (CheckColor) #Set the Colour
                        #FIX_ATT.setFillColor(CheckColor) #Set the Colour
                        ListIdx += 1
                        if ListIdx == (len(ColourList) - 1):
                            ListIdx = 0 #Reset index when it hits max list
                if FIX_ATT.status == FINISHED or AttloopCount > 1: # When the colour change is done, we just want to draw the regular fixaiton
                    FixationPoint.draw()
                    
                ## WE ONLY WANT TO DRAW FIX_ATT ON THE FIRST LOOP REPEAT
                # *FIX_ATT* updates 
                if FIX_ATT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance and AttloopCount <= 1:
                    # keep track of start time/frame for later
                    FIX_ATT.frameNStart = frameN  # exact frame index
                    FIX_ATT.tStart = t  # local t and not account for scr refresh
                    FIX_ATT.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(FIX_ATT, 'tStartRefresh')  # time at next scr refresh
                    FIX_ATT.setAutoDraw(True)
                #If we are not drawing the changing fixation, we want to just draw our regular fixation               
                
                if FIX_ATT.status == STARTED or AttloopCount >= 1:
                    if frameN >= (FIX_ATT.frameNStart + RefreshHz): #Because we only want to change colour for a second
                        # keep track of stop time/frame for later
                        FIX_ATT.tStop = t  # not accounting for scr refresh
                        FIX_ATT.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(FIX_ATT, 'tStopRefresh')  # time at next scr refresh
                        FIX_ATT.setAutoDraw(False)
                        FIX_ATT.status = FINISHED
                if FIX_ATT.status == STARTED:  # only update if drawing
                    FIX_ATT.setPos((0, 0), log=False)
                    FIX_ATT.setSize((FixSize, FixSize), log=False)
                if Condition == 'Cond1':
                    CoordsX = LtRX[Att_Idx] 
                    TopSize = Growing_List[Att_Idx]  
                    BotSize = Shrinking_List[Att_Idx]
                elif Condition == 'Cond2':
                    CoordsX = RtLX[Att_Idx] 
                    TopSize = Growing_List[Att_Idx]  
                    BotSize = Shrinking_List[Att_Idx]
                elif Condition == 'Cond3': #These are also practice trials now
                    CoordsX = LtRX[Att_Idx]
                    BotSize = Growing_List[Att_Idx]  
                    TopSize = Shrinking_List[Att_Idx]
                elif Condition == 'Cond4':
                    CoordsX = RtLX[Att_Idx] 
                    BotSize = Growing_List[Att_Idx]  
                    TopSize = Shrinking_List[Att_Idx]
                
                BotX = CoordsX * -1
                
                ## Change Bar Height with key press
                #Based on Griegner's solution here: https://discourse.psychopy.org/t/visual-analog-scale-press-and-hold-key/21098/2
                
                ATTkeys = ATTKB.getKeys(['r', 'R', 'space', 'down', 'up'], waitRelease=False, clear=False) #waitRealse = False
                '''    if respATT == 'up':
                        noKeyResp = False
                        DownKeyCount -= 1
                        Adjust += AdjustmentAmount
                        KeyHistory.append("up")
                        #print('Adjust', Adjust)
                    elif respATT == 'down': #'down' in resp:
                        noKeyResp = False
                        if DownKeyCount < 100: #This will control how small it gets
                            Adjust -= AdjustmentAmount
                            KeyHistory.append("down")
                            DownKeyCount += 1  
                '''
                if ATTkeys and not ATTkeys[-1].duration: #if keys means, there is a key here and NOT keys[-1].duration means THERE IS NO DURATION. Duration only recorded when key lifted 
                    respATT = ATTkeys[-1].name #the last key's name
                    if respATT == 'r' or respATT == 'R': #'space' in resp:
                        DownKeyCount = 0
                        count = 0
                        CheckPass = True
                        #Reset loopcount once people have pressed the routine
                        Adjust = 0
                        loopCount = 0
                        KeyHistory.append("r")
                        thisExp.addData('KeyHistoryTOTAL', KeyHistory) #Save a list of all Keypresses 
                        KeyHistory = []
                        BackAdjust = 0 #Reset backadjust
                        ATTKB.clearEvents()
                        continueRoutine = False
                        AttRepeatTrials.finished = True #End the loop that maintains a continuous rerun
                    elif respATT == 'space' or respATT == 'up' or respATT == 'down': 
                        DownKeyCount = 0
                        count = 0
                        #Reset loopcount once people have pressed the routine
                        Adjust = 0
                        loopCount = 0
                        KeyHistory.append("space")
                        thisExp.addData('KeyHistoryTOTAL', KeyHistory) #Save a list of all Keypresses 
                        KeyHistory = []
                        CheckPass = False
                        ATTKB.clearEvents()
                        continueRoutine = False
                        AttRepeatTrials.finished = True #End the loop that maintains a continuous rerun
                
                    Adjust = np.round(Adjust) #Adjust and adjustment amount should be a whole pixel value
                
                if FP == 'FixationPointup.png':
                    #Apply adjustment
                    Tsize = TopSize + Adjust 
                    
                    #This stops 0 going negative
                    if Tsize < 0:
                        Tsize = 6
                
                   # Offset height
                    if OffsetDir == 'BotLrg': #Bottom Square Taller
                        Bsize = BotSize + offsetAmount 
                    elif OffsetDir == 'BotSml': #Bottom square smaller
                        Bsize = BotSize - offsetAmount 
                    else:
                        Bsize = BotSize #No changes in size
                    
                    #Stop reference going less than zero
                    if Bsize < 0:
                        Bsize = 6
                else:
                    #Applys keyboard adjusment
                    Bsize = BotSize + Adjust 
                    
                    #Stops value going negative
                    if Bsize < 0:
                        Bsize = 6
                        
                    #Offset height:
                    if OffsetDir == 'TopLRG':
                        Tsize = TopSize + offsetAmount  #TopSQ taller
                    elif OffsetDir == 'TopSML':
                        Tsize = TopSize - offsetAmount #TopSQ smaller
                    else:
                        Tsize = TopSize #no changes in size
                    
                    #Need to stop the reference stimuli going in reverse
                    if Tsize < 0:
                        Tsize = 6
                
                
                Tsize = np.round(Tsize) #keep the pixels in whole numbers
                Bsize = np.round(Bsize) #keep the pixels in whole numbers
                
                ## Move through the lists:
                if Att_Idx < (len(LtRX) - 1):
                    Att_Idx += 1
                
                # *TopBar_ATT* updates
                if TopBar_ATT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    TopBar_ATT.frameNStart = frameN  # exact frame index
                    TopBar_ATT.tStart = t  # local t and not account for scr refresh
                    TopBar_ATT.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(TopBar_ATT, 'tStartRefresh')  # time at next scr refresh
                    TopBar_ATT.setAutoDraw(True)
                if TopBar_ATT.status == STARTED:
                    if frameN >= (TopBar_ATT.frameNStart + BarDur):
                        # keep track of stop time/frame for later
                        TopBar_ATT.tStop = t  # not accounting for scr refresh
                        TopBar_ATT.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(TopBar_ATT, 'tStopRefresh')  # time at next scr refresh
                        TopBar_ATT.setAutoDraw(False)
                if TopBar_ATT.status == STARTED:  # only update if drawing
                    TopBar_ATT.setPos((CoordsX, BarY), log=False)
                    TopBar_ATT.setSize((11, Tsize), log=False)
                
                # *BotBar_ATT* updates
                if BotBar_ATT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    BotBar_ATT.frameNStart = frameN  # exact frame index
                    BotBar_ATT.tStart = t  # local t and not account for scr refresh
                    BotBar_ATT.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(BotBar_ATT, 'tStartRefresh')  # time at next scr refresh
                    BotBar_ATT.setAutoDraw(True)
                if BotBar_ATT.status == STARTED:
                    if frameN >= (BotBar_ATT.frameNStart + BarDur):
                        # keep track of stop time/frame for later
                        BotBar_ATT.tStop = t  # not accounting for scr refresh
                        BotBar_ATT.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(BotBar_ATT, 'tStopRefresh')  # time at next scr refresh
                        BotBar_ATT.setAutoDraw(False)
                if BotBar_ATT.status == STARTED:  # only update if drawing
                    BotBar_ATT.setPos((BotX, -BarY), log=False)
                    BotBar_ATT.setSize((11, Bsize), log=False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in AttentionCheckComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "AttentionCheck"-------
            for thisComponent in AttentionCheckComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            AttRepeatTrials.addData('FIX_ATT.started', FIX_ATT.tStartRefresh)
            AttRepeatTrials.addData('FIX_ATT.stopped', FIX_ATT.tStopRefresh)
            thisExp.addData('CheckPass', CheckPass)
            ## Timeout parameters
            ##For attention check, each iteration is 2 second
            #5 loops to press 'r' is fair
            
            
            if CheckTrials == True and AttloopCount >= 5:
                #if resp.keys != 'up' and resp.keys != 'down' and resp.keys != 'space':
                continueRoutine = False
                Adjust = 0
                AttloopCount = 0
                count = 0
                AttRepeatTrials.finished = True
                warning = True
                noKeyResp = True 
                warnCount += 1
                KeyHistory = []
            
            if len(respATT):
                AttloopCount = 0
                respATT = [] #Reset the key variable, to stop it resetting loopcount
            
            AttRepeatTrials.addData('TopBar_ATT.started', TopBar_ATT.tStartRefresh)
            AttRepeatTrials.addData('TopBar_ATT.stopped', TopBar_ATT.tStopRefresh)
            AttRepeatTrials.addData('BotBar_ATT.started', BotBar_ATT.tStartRefresh)
            AttRepeatTrials.addData('BotBar_ATT.stopped', BotBar_ATT.tStopRefresh)
            # the Routine "AttentionCheck" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
        # completed 40.0 repeats of 'AttRepeatTrials'
        
        
        # ------Prepare to start Routine "Warning"-------
        continueRoutine = True
        # update component parameters for each repeat
        if CheckTrials != True or CheckPass == True:
            continueRoutine = False
        if CheckPass == True:
            ExtraText = 'Good work! You passed the attention check!'
        else:
             ExtraText = 'Unfortunately, you pressed the wrong key during the attention check. ' + '\n' + "When the center dot changes colour, please press 'r'"
        DisplayMSG.setText(ExtraText + '\n' + '\n' + 'Just a friendly reminder to please stare at the cross in the center of the screen during the experiment.' + '\n' + '\n' + "Press 's' to resume the experiment. ")
        WarningResp.keys = []
        WarningResp.rt = []
        _WarningResp_allKeys = []
        # keep track of which components have finished
        WarningComponents = [DisplayMSG, WarningResp]
        for thisComponent in WarningComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        WarningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Warning"-------
        while continueRoutine:
            # get current time
            t = WarningClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=WarningClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *DisplayMSG* updates
            if DisplayMSG.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                DisplayMSG.frameNStart = frameN  # exact frame index
                DisplayMSG.tStart = t  # local t and not account for scr refresh
                DisplayMSG.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(DisplayMSG, 'tStartRefresh')  # time at next scr refresh
                DisplayMSG.setAutoDraw(True)
            
            # *WarningResp* updates
            waitOnFlip = False
            if WarningResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                WarningResp.frameNStart = frameN  # exact frame index
                WarningResp.tStart = t  # local t and not account for scr refresh
                WarningResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(WarningResp, 'tStartRefresh')  # time at next scr refresh
                WarningResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(WarningResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(WarningResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if WarningResp.status == STARTED and not waitOnFlip:
                theseKeys = WarningResp.getKeys(keyList=['s', '6'], waitRelease=False)
                _WarningResp_allKeys.extend(theseKeys)
                if len(_WarningResp_allKeys):
                    WarningResp.keys = _WarningResp_allKeys[-1].name  # just the last key pressed
                    WarningResp.rt = _WarningResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in WarningComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Warning"-------
        for thisComponent in WarningComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        CheckPass = False
        CheckTrials = False
        OverarchingLoops.addData('DisplayMSG.started', DisplayMSG.tStartRefresh)
        OverarchingLoops.addData('DisplayMSG.stopped', DisplayMSG.tStopRefresh)
        # check responses
        if WarningResp.keys in ['', [], None]:  # No response was made
            WarningResp.keys = None
        OverarchingLoops.addData('WarningResp.keys',WarningResp.keys)
        if WarningResp.keys != None:  # we had a response
            OverarchingLoops.addData('WarningResp.rt', WarningResp.rt)
        OverarchingLoops.addData('WarningResp.started', WarningResp.tStartRefresh)
        OverarchingLoops.addData('WarningResp.stopped', WarningResp.tStopRefresh)
        # the Routine "Warning" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Break"-------
        continueRoutine = True
        # update component parameters for each repeat
        if trialcount != 24:
            continueRoutine = False
        Endbreak.keys = []
        Endbreak.rt = []
        _Endbreak_allKeys = []
        # keep track of which components have finished
        BreakComponents = [BreakText, Endbreak]
        for thisComponent in BreakComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BreakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Break"-------
        while continueRoutine:
            # get current time
            t = BreakClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BreakClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *BreakText* updates
            if BreakText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BreakText.frameNStart = frameN  # exact frame index
                BreakText.tStart = t  # local t and not account for scr refresh
                BreakText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BreakText, 'tStartRefresh')  # time at next scr refresh
                BreakText.setAutoDraw(True)
            
            # *Endbreak* updates
            waitOnFlip = False
            if Endbreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Endbreak.frameNStart = frameN  # exact frame index
                Endbreak.tStart = t  # local t and not account for scr refresh
                Endbreak.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Endbreak, 'tStartRefresh')  # time at next scr refresh
                Endbreak.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Endbreak.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Endbreak.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Endbreak.status == STARTED and not waitOnFlip:
                theseKeys = Endbreak.getKeys(keyList=['E', 'l', 'l', 'e'], waitRelease=False)
                _Endbreak_allKeys.extend(theseKeys)
                if len(_Endbreak_allKeys):
                    Endbreak.keys = _Endbreak_allKeys[-1].name  # just the last key pressed
                    Endbreak.rt = _Endbreak_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BreakComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Break"-------
        for thisComponent in BreakComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        OverarchingLoops.addData('BreakText.started', BreakText.tStartRefresh)
        OverarchingLoops.addData('BreakText.stopped', BreakText.tStopRefresh)
        # check responses
        if Endbreak.keys in ['', [], None]:  # No response was made
            Endbreak.keys = None
        OverarchingLoops.addData('Endbreak.keys',Endbreak.keys)
        if Endbreak.keys != None:  # we had a response
            OverarchingLoops.addData('Endbreak.rt', Endbreak.rt)
        OverarchingLoops.addData('Endbreak.started', Endbreak.tStartRefresh)
        OverarchingLoops.addData('Endbreak.stopped', Endbreak.tStopRefresh)
        # the Routine "Break" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'OverarchingLoops'
    
# completed 1.0 repeats of 'ChooseCondFile'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
#This tells us if the experiment ended early
thisExp.addData("globalClockTime", globalClock.getTime()) 
Farewell.setHeight(0.05)
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
##Plot intervals and save in text file
import matplotlib.pyplot as plt

FILE_NAME_TEXT=('Intervals\Text\FlashJump_' + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + "_FrameIntervals"  + '.log')
FILE_NAME_PNG = ('Intervals\Images\FlashJump_' + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + "_FrameIntervals" + '.png')

# keep track of which components have finished
EndComponents = [Farewell, key_resp]
for thisComponent in EndComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "End"-------
while continueRoutine:
    # get current time
    t = EndClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Farewell* updates
    if Farewell.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Farewell.frameNStart = frameN  # exact frame index
        Farewell.tStart = t  # local t and not account for scr refresh
        Farewell.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Farewell, 'tStartRefresh')  # time at next scr refresh
        Farewell.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['i', 'space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Farewell.started', Farewell.tStartRefresh)
thisExp.addData('Farewell.stopped', Farewell.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
if key_resp.keys == 'space':
    #Clear the existing screen
    win.fullscr = False
    win.close()
    
    ## Plot the intervals; based upon the timeByFrames psychopy coder demo
    #Do some basic descriptives
    intervalsMS = np.array(win.frameIntervals) * 1000
    mean_Intervals = np.mean(intervalsMS)
    sd_Intervals = np.std(intervalsMS)
    nTotal = len(intervalsMS)
    if int(expInfo['test']) == 1:
        nDropped = np.sum(intervalsMS > 1.1 * (1000/FrameRate)) + np.sum(intervalsMS < 0.9 * (1000/FrameRate)) #10% cut off 
    else:
        nDropped = np.sum(intervalsMS > 1.1 * (1000/RefreshHz)) + np.sum(intervalsMS < 0.9 * (1000/RefreshHz)) #10% cut off 
    titleMsg = "Dropped/Frames = %i%i = %.3f%%"
    PercentDropped = 100 * nDropped/float(nTotal)
    droppedString = titleMsg % (nDropped, nTotal, PercentDropped)
    
    ## Save the intervals
    thisExp.addData('nDropped_Frames', nDropped)
    thisExp.addData('nTotal_Frames', nTotal)
    thisExp.addData('PercentDropped', PercentDropped)
    
    #Plot the intervals   
    plt.plot(win.frameIntervals)
    plt.xlabel('n frames')
    plt.ylabel('t (ms)')
    plt.title(droppedString)
    plt.savefig(FILE_NAME_PNG)
    plt.show()

##save intervals as file
win.saveFrameIntervals(fileName=FILE_NAME_TEXT, clear=True) #FILE_NAME_TEXT

# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
