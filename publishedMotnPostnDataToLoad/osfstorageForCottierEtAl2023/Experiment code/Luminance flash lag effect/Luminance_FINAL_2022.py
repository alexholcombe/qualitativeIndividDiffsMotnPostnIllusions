#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on January 23, 2022, at 23:11
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

## TC Modified from builder:
    # Turned window blanking off
    # Removed eye tracking setup
    # Removed the default to 60hz if cannot read frameRate
    # removed an unnecessary win.flip() at the end; causes errors/warnings.
    # For testing mode, log will be made at debugging settings. The last frame interval will be sent to the log files.
    #changed to 144hz
    # Making the attention check 1 second
    # adding a flash to attention check
    # Making attention check more consistent with live paradigm (e.g., 500ms onset e.t.c)
    # Practice trials are now separated from live trials. Practice trials are just one run each, of each live condition


from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

import os.path
from psychopy import tools 


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'FLE_Lum_'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '', 'test': '0'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expName, expInfo['participant'], expInfo['session'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Timot\\Documents\\2021\\Study 1\\September_Final_EXPERIMENTS_LIVE_Python\\Python-Experiments\\Luminance_Flash_Lag_effect\\Final_LumFin.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
    # save a log file for detail verbose info
if int(expInfo['test']) == 1:
    logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
else:
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
    blendMode='avg', waitBlanking=False, useFBO=True, 
    units='deg') ## We want to use a blend mode of averaging for smooth opacity changes for the target, we want the lumince of the targ and flash to be a blended average of the opacity and the background
    # we don't want to change or risk altering the plain grey background with an addition blend
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
Welcome = visual.TextStim(win=win, name='Welcome',
    text="In this experiment you will view a circle increasing in brightness from black to grey, or decreasing in brightness from grey to black.\nAt some point a second circle will be flashed opposite this changing circle. \n\nPlease report which circle was darker (more black)\nPress the 'UP' arrow key if the top circle was darker.\nPress the 'DOWN' arrow key if the bottom circle was darker.\n\nThroughout the experiment a  white circle will be present in the centre of the screen, please stare at this circle for the duration of the experiment. \n This centre circle will randomly change colour throughout the experiment. Please press 'r' when this occurs. \n\nThe first few trials will be practice trials that let you familiarise yourself with the task. \n\nPress the 'space' bar when you are ready to begin the experiment.",
    font='Arial',
    units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
start = keyboard.Keyboard()
####### DIMENSIONS OF THE CIRCLES IN DVA, BASED UPON SHETH ET AL. (2000)

## SIZE OF THE CIRCLES
#FixH = FixW = 12 #Pixels
FixH = FixW = 0.3 #0.4 #DVA; original 0.2
CircW = CircH =  2.9 #4 #Original: 2.9

#FixDot Color
FixCol = (1, 1, 1) #Default, grey (-0.2, -0.2, -0.2)

## Coordinates of circles
RefreshHz = 144 #200

if int(expInfo['test']) == 0: #1 = true, it's a test; 0 = false, not a test (LIVE TRIALS)
    if FrameRate <140 or FrameRate > 148 or RefreshHz != 144: #Give a 4 frame buffer 
        print('WARNING! ERROR WITH FRAMERATE OR REFRESHHZ. Psychopy detected the FrameRate at: ' +str(FrameRate) + 'RefreshHz was: ' + str(RefreshHz))
        core.quit()

## Check the file does not already exist
if os.path.exists(filename + '.csv'):
    print('Warning: Datafile already exists!')
    core.quit()
    
## Specify how many trials:
if int(expInfo['test']) == 1:
    TrialReps = 3
else:
    TrialReps = 30
win.mouseVisible = False

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
Target = visual.ShapeStim(
    win=win, name='Target', vertices=99,units='deg', 
    size=(CircW, CircH),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(-1.0000, -1.0000, -1.0000), fillColor=(-1.0000, -1.0000, -1.0000),
    opacity=1.0, depth=0.0, interpolate=True)
FixPoint = visual.ShapeStim(
    win=win, name='FixPoint', vertices=99,units='deg', 
    size=(FixW, FixH),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=FixCol, fillColor=FixCol,
    opacity=None, depth=-1.0, interpolate=True)

# Initialize components for Routine "TrialRout"
TrialRoutClock = core.Clock()
resp = keyboard.Keyboard()
## Flash duration (original: 13ms) and target duration (833ms)
#Flash occurs halfway through, on frameN (which is frame - 1, cause counts on zero)

FlashDur = 2 #13.88ms, we want ~15ms 
TargDur =  120 # 832ms; want ~830ms
FlashonFrame = (TargDur/2) - 1 #We want the Flash halfway, just remember, FrameN starts counting from 0
ChangeAmount = 0.8 #how much opacity should change over the total trial. Should always be 0.5 half way
stepSize = ChangeAmount/TargDur #~ 0.00666666666667
#0.96/RefreshHz #0.96 is how much luminance we want to change over the whole trial. With a targdur of 830ms, this means we will move (0.8) from 0.9 to 0.1 over the target's duration.

'''
if RefreshHz == 200:
    FlashDur = 3
    TargDur = 166 #(830ms)
    FlashonFrame = 82 #halfway (remember frameN starts counting from zero)
    stepSize = 0.0048
elif RefreshHz == 60:
    FlashDur = 1
    TargDur = 50 #(833ms)
    FlashonFrame = 24 
    stepSize = 0.016
else: #Do dynamic adjustment for other refreshrates
    FlashDur = np.ceil(1 * (RefreshHz/60)) #~16.67ms (Sheth defines for 13ms)
    TargDur = np.ceil(50 * RefreshHz/60) #833ms
    #The opacity starts at 0.9 and 0.1, by halfway we want it to travel 0.4
    stepSize = np.round((0.016 * 60/RefreshHz), 3)#0.4/(TargDur/2) #This is just how much it steps per frame
    FlashonFrame = np.ceil(24 * RefreshHz/60)
'''
##Staircase parameters
#We manipulate brightness via opacity (0-1)
#1 is obaque, 0 is completely transparent
#0 = Grey; 1 = white; -1 in black. #Range: 0:-1
#We want to make the flash brighter, if they say the change is dimmer; if they say the flash is dimmer, make brighter

trialCount = 0
FlashLum = 0 #This is the lum for the flash 
stairStep = [0.05] #This is the stepsize for the staircase
NumRevs = 6 #How many reversals needed to change stairstep

## Live Staircase parameters
#Two staircases per ramp direction (Becoming brighter/dimmer)
#One staircase will start obaque; the other transparent
#Transparent staircases start at 0.1
#Obaque staircases at 1
#Up is becoming more obaque; down is more dimmer 

## Target is ramping to become brighter
#Flash obaque
#StairNum = 1
ST1Opa = 1
ST1Dir = 'down'
ST1NumRevs = 0 #How many reversals have occurred
ST1StairStep = 0 #Indexes from stairstep above
ST1RevVals = [] # A list that stores rev values
ST1TC = 0 #Trial counter for this staircase

#Target becoming brighter; flash transparent
ST2Opa = 0.1
ST2Dir = 'up'
ST2NumRevs = 0
ST2StairStep = 0
ST2RevVals = []
ST2TC = 0 

## TARGET DIMMER STAIRCASES:
#Target is becoming dimmer, flash obaque
ST3Opa = 1
ST3Dir = 'down' #need it to become more transparent
ST3NumRevs = 0
ST3StairStep = 0
ST3RevVals = []
ST3TC = 0

#Dimmer target, flash transparent
ST4Opa = 0.1
ST4Dir = 'up'
ST4NumRevs = 0
ST4StairStep = 0
ST4RevVals = []
ST4TC = 0

#Range enforcement, stop the staircase exceeding opacity range (0.1:1):

MinVal = 0.1 # (Zero is fully transparent
MaxVal = 1 #Above 1 is not possible #Ensure values stay in range

#Store in datafile when one occurred
ReversalOccured = False

flash = visual.ShapeStim(
    win=win, name='flash', vertices=99,units='deg', 
    size=(CircW, CircH),
    ori=0, pos=[0,0],
    lineWidth=4,     colorSpace='rgb',  lineColor=[-1, -1, -1], fillColor=[-1, -1, -1],
    opacity=1.0, depth=-3.0, interpolate=True)
FPTRIAL = visual.ShapeStim(
    win=win, name='FPTRIAL', vertices=99,units='deg', 
    size=(FixW, FixH),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=FixCol, fillColor=FixCol,
    opacity=None, depth=-4.0, interpolate=True)
#Report warnings to the standard output window
logging.console.setLevel(logging.WARNING)

PastCount = 0 #This just store the past frame count, for the last trials

# Initialize components for Routine "Practice"
PracticeClock = core.Clock()
endPrac ='' #This tells participants the practice trials are over 

WasPractice = False #Was this trial a practice

displayPracText = visual.TextStim(win=win, name='displayPracText',
    text='',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
endPracRoutine = keyboard.Keyboard()

# Initialize components for Routine "AttCheckFlash"
AttCheckFlashClock = core.Clock()
resp_ATT = keyboard.Keyboard()
FP_ATT = visual.ShapeStim(
    win=win, name='FP_ATT', vertices=99,units='deg', 
    size=(FixW, FixH),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=FixCol, fillColor=FixCol,
    opacity=None, depth=-1.0, interpolate=True)
TrialCheck = 20 #Do attcheck on this many trials
AttCheckCount = 0 #Counts how many Attention checks happened

MyRed = (1, -1, -1)
myYell = (1.0000, 1.0000, -1.0000)
myGreen = (-1, 1, -1)
myOrange = (1.0000, 0.2941, -1.0000) 
myCyan = (-1.0000, 1.0000, 1.0000)
myMagneta = (1.0000, -1.0000, 1.0000)
myPurple = (0.0039, -1.0000, 0.0039) 
myBlack = (-1, -1, -1)
FixCol = MyRed
ColourList = [myYell, myGreen, MyRed, myPurple, myMagneta, myCyan, myOrange]

ListIdx = 0 #To select a colour from the list
AttentionCheck = False #Will the attention check occur?
FixCol = MyRed #Default is to keep it red
PassCheck = False #Did you pass the attention check
AttISI = RefreshHz #ISI duration of attention check in frames, we want a second

UpdateOn = 18
AttChangeCirc = 206 #Attention check target duration; ~1430ms

'''
if RefreshHz == 60: 
    ResponserTimer = 50 + AttISI #How long the fixation changes colour. Basically, while the grating moves, it will change colour
    UpdateOn = 8
    AttChangeCirc = 86
elif RefreshHz == 200:
    ResponserTimer = 166 + AttISI #How long the fixation changes colour. Basically, while the luminance changes, so will the target
    UpdateOn = 27 #update every 133ms
    AttChangeCirc = 286
else: #dyanmically change for other refreshrates
    UpdateOn = np.ceil(8 * RefreshHz/60) #Update every 133ms
    AttChangeCirc = np.ceil(86 * (RefreshHz/60)) #Attention check target duration (1433ms specified in 60hz)
'''

NumFails = 0 #how many attention checks failed
FailedAtt = False

CorrAns = 'r'

#Display a warning with feedback on he attention check
warning = False

ChangingTarget_ATT = visual.ShapeStim(
    win=win, name='ChangingTarget_ATT', vertices=99,
    size=(CircW, CircH),
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(-1.0000, -1.0000, -1.0000), fillColor=(-1.0000, -1.0000, -1.0000),
    opacity=1.0, depth=-4.0, interpolate=True)
ISI_FP_ATT = visual.ShapeStim(
    win=win, name='ISI_FP_ATT',units='deg', 
    size=(FixW, FixH), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(1, 1, 1), fillColor=(1, 1, 1),
    opacity=None, depth=-5.0, interpolate=True)

# Initialize components for Routine "AttWarning"
AttWarningClock = core.Clock()
ExtraText = ''
ATT_TEXT = visual.TextStim(win=win, name='ATT_TEXT',
    text='',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Att_RESP = keyboard.Keyboard()

# Initialize components for Routine "BREAK"
BREAKClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="This is a break! If you require a break, please rest for as long as necessary.\n\nPress 'space' when you are ready to resume the experiment.",
    font='Open Sans',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
BreakResp = keyboard.Keyboard()

# Initialize components for Routine "Conclusion"
ConclusionClock = core.Clock()
End = visual.TextStim(win=win, name='End',
    text='Thank you completing this experiment.\n\nPlease tell the researcher you are finished. ',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
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
start.keys = []
start.rt = []
_start_allKeys = []
# keep track of which components have finished
InstructionsComponents = [Welcome, start]
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
    
    # *Welcome* updates
    if Welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Welcome.frameNStart = frameN  # exact frame index
        Welcome.tStart = t  # local t and not account for scr refresh
        Welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Welcome, 'tStartRefresh')  # time at next scr refresh
        Welcome.setAutoDraw(True)
    
    # *start* updates
    waitOnFlip = False
    if start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        start.frameNStart = frameN  # exact frame index
        start.tStart = t  # local t and not account for scr refresh
        start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(start, 'tStartRefresh')  # time at next scr refresh
        start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if start.status == STARTED and not waitOnFlip:
        theseKeys = start.getKeys(keyList=['space', 'left'], waitRelease=False)
        _start_allKeys.extend(theseKeys)
        if len(_start_allKeys):
            start.keys = _start_allKeys[-1].name  # just the last key pressed
            start.rt = _start_allKeys[-1].rt
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
thisExp.addData('Welcome.started', Welcome.tStartRefresh)
thisExp.addData('Welcome.stopped', Welcome.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

## set up handler to look after randomisation of conditions etc

#add the loop to choose prac or live
SelectCondFile = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Choose_Cond.xlsx'),
    seed=None, name='SelectCondFile')
thisExp.addLoop(SelectCondFile) #Add loop to experiment
thisSelectCondFile = SelectCondFile.trialList[0] #Initialies stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisSelectCondFile.rgb)
if thisSelectCondFile != None:
    for paramName in thisSelectCondFile:
        exec('{} = thisSelectCondFile[paramName]'.format(paramName))

for thisSelectCondFile in SelectCondFile:
    currentLoop = SelectCondFile
    # abbreviate parameter names if possible (e.g. rgb = thisSelectCondFile.rgb)
    if thisSelectCondFile != None:
        for paramName in thisSelectCondFile:
            exec('{} = thisSelectCondFile[paramName]'.format(paramName))

    ConditionControl = data.TrialHandler(nReps=NumReps, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(CondFile), #('flLuminanceOpacity_DVA.xlsx'),
        seed=None, name='ConditionControl')
    thisExp.addLoop(ConditionControl)  # add the loop to the experiment
    thisConditionControl = ConditionControl.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisConditionControl.rgb)
    if thisConditionControl != None:
        for paramName in thisConditionControl:
            exec('{} = thisConditionControl[paramName]'.format(paramName))

    for thisConditionControl in ConditionControl:
        currentLoop = ConditionControl
        # abbreviate parameter names if possible (e.g. rgb = thisConditionControl.rgb)
        if thisConditionControl != None:
            for paramName in thisConditionControl:
                exec('{} = thisConditionControl[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ISI"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        Target.setOpacity(StartLum)
        Target.setPos((0, ChangeY))
        FixPoint.autoDraw = True
        # keep track of which components have finished
        ISIComponents = [Target, FixPoint]
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
            
            # *Target* updates
            if Target.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                Target.frameNStart = frameN  # exact frame index
                Target.tStart = t  # local t and not account for scr refresh
                Target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Target, 'tStartRefresh')  # time at next scr refresh
                Target.setAutoDraw(True)
            if Target.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Target.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Target.tStop = t  # not accounting for scr refresh
                    Target.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Target, 'tStopRefresh')  # time at next scr refresh
                    Target.setAutoDraw(False)
            
            # *FixPoint* updates
            if FixPoint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixPoint.frameNStart = frameN  # exact frame index
                FixPoint.tStart = t  # local t and not account for scr refresh
                FixPoint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixPoint, 'tStartRefresh')  # time at next scr refresh
                FixPoint.setAutoDraw(True)
            if FixPoint.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > FixPoint.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    FixPoint.tStop = t  # not accounting for scr refresh
                    FixPoint.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FixPoint, 'tStopRefresh')  # time at next scr refresh
                    FixPoint.setAutoDraw(False)
            if t > 0.5: #Draw target after the 0.5 isi (needs to be on to ensure smooth transition between routines)
                Target.autoDraw = True
            
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
        ConditionControl.addData('Target.started', Target.tStartRefresh)
        ConditionControl.addData('Target.stopped', Target.tStopRefresh)
        ConditionControl.addData('FixPoint.started', FixPoint.tStartRefresh)
        ConditionControl.addData('FixPoint.stopped', FixPoint.tStopRefresh)
        FixPoint.autoDraw = False
        
        # ------Prepare to start Routine "TrialRout"-------
        continueRoutine = True
        # update component parameters for each repeat
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
                
        #StartLum specified in condition file
        CircOpa = StartLum #Target alpha
        
        ## FYI, remember frameN begins counting at 0, so if you want 50, frameN will finish at 49, and the flash at halfway, is frameN ==24
        
        #Start of each routine, we set the position of the flash and target
        flash.pos = ([0, FlashY])
        
            #First eight trials are practice
        #Reset staircase for live trials
        trialCount += 1 
        thisExp.addData('trialCount', trialCount)
    
        if trialCount == 9: #We are resetting the staircases here, to undo the practice trial changes 

            #Target is ramping to become brighter
            #Flash obaque
            #StairNum = 1
            ST1Opa = 1
            ST1Dir = 'down'
            ST1NumRevs = 0 #How many reversals have occurred
            ST1StairStep = 0 #Indexes from stairstep above
            ST1RevVals = [] # A list that stores rev values
            ST1TC = 0 #Trial counter for this staircase

            #Brighter target; flash transparent
            ST2Opa = 0.1
            ST2Dir = 'up'
            ST2NumRevs = 0
            ST2StairStep = 0
            ST2RevVals = []
            ST2TC = 0 

            #Target is becoming dimmer, flash obaque
            ST3Opa = 1
            ST3Dir = 'down'
            ST3NumRevs = 0
            ST3StairStep = 0
            ST3RevVals = []
            ST3TC = 0

            #Dimmer target, flash transparent
            ST4Opa = 0.1
            ST4Dir = 'up'
            ST4NumRevs = 0
            ST4StairStep = 0
            ST4RevVals = []
            ST4TC = 0
        
                    
        if StairNum == 1:
            FlashLum = ST1Opa
        elif StairNum == 2:
            FlashLum = ST2Opa
        elif StairNum == 3:
            FlashLum = ST3Opa
        elif StairNum == 4:
            FlashLum = ST4Opa
        
        flash.setOpacity(FlashLum) #, colorSpace='rgb'
        thisExp.addData('FlashLuminance', FlashLum)
        
        #Store the opacity for the trial at the start
        thisExp.addData('ST1Opa', ST1Opa)
        thisExp.addData('ST2Opa', ST2Opa)
        thisExp.addData('ST3Opa', ST3Opa)
        thisExp.addData('ST4Opa', ST4Opa)
        flash.setPos((0, FlashY))
        win.recordFrameIntervals = True #win.nDroppedFrames stores this. 
        
        #Set a 10% tolerance for dropped frames
        win.refreshThreshold = (1/RefreshHz) * 1.1
        
        DisgardTrial = False
        
        #manual frame drop counter
        #FramesDropped = 0
        # keep track of which components have finished
        TrialRoutComponents = [resp, flash, FPTRIAL]
        for thisComponent in TrialRoutComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        TrialRoutClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "TrialRout"-------
        while continueRoutine:
            # get current time
            t = TrialRoutClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=TrialRoutClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            if int(expInfo['test']) == 1: #if test mode, log the frame interval for the last frame
                if len(win.frameIntervals):
                    logging.debug('Last Frame Interval: ' + str(win.frameIntervals[-1])) #This will return the last frame interval appended

            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and frameN >= 20:
                # keep track of start time/frame for later
                resp.frameNStart = frameN  # exact frame index
                resp.tStart = t  # local t and not account for scr refresh
                resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
                resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp.status == STARTED and not waitOnFlip:
                theseKeys = resp.getKeys(keyList=['up', 'down'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    # was this correct?
                    if (resp.keys == str(FlashKey)) or (resp.keys == FlashKey):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            #Larger alpha = darker
            #Smaller alpha = brighter
            if frameN < TargDur:
                if LumChange == 'Brighter': #Makes black circle more transparent
                    CircOpa -= stepSize
                else: #Become dimmer more obaque
                    CircOpa += stepSize
                #Change colour/lum every frame
                Target.setOpacity(CircOpa) #, colorSpace='rgb')#Frame 24 is the halfway point
                Target.draw()
                #Target.draw() not sure why there is two draw commands
                
            if frameN == FlashonFrame:
                #This gives us the changing circles luminance at the onset of the flash
                TargetValatFlashOnset = CircOpa
                thisExp.addData('TargetLumatFlashOnset', CircOpa)
                
            #if t < 1: #Draw FixPoint for first second
            #    FixPoint.draw()
            
            # *flash* updates
            if flash.status == NOT_STARTED and frameN >= FlashonFrame:
                # keep track of start time/frame for later
                flash.frameNStart = frameN  # exact frame index
                flash.tStart = t  # local t and not account for scr refresh
                flash.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(flash, 'tStartRefresh')  # time at next scr refresh
                flash.setAutoDraw(True)
            if flash.status == STARTED:
                if frameN >= (flash.frameNStart + FlashDur):
                    # keep track of stop time/frame for later
                    flash.tStop = t  # not accounting for scr refresh
                    flash.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(flash, 'tStopRefresh')  # time at next scr refresh
                    flash.setAutoDraw(False)
            if flash.status == STARTED:  # only update if drawing
                flash.setOpacity(FlashLum, log=False)
            
            # *FPTRIAL* updates
            if FPTRIAL.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FPTRIAL.frameNStart = frameN  # exact frame index
                FPTRIAL.tStart = t  # local t and not account for scr refresh
                FPTRIAL.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FPTRIAL, 'tStartRefresh')  # time at next scr refresh
                FPTRIAL.setAutoDraw(True)
            if frameN > TargDur: #We no longer have any stimulus updating, stop recording intervals
                win.recordFrameIntervals = False #Do this as a fail safe
            
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialRoutComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "TrialRout"-------
        for thisComponent in TrialRoutComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(FlashKey).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for ConditionControl (TrialHandler)
        ConditionControl.addData('resp.keys',resp.keys)
        ConditionControl.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            ConditionControl.addData('resp.rt', resp.rt)
        ConditionControl.addData('resp.started', resp.tStartRefresh)
        ConditionControl.addData('resp.stopped', resp.tStopRefresh)
        #Remove the target, but draw the fixation
        Target.autoDraw = False
        #FPTRIAL.draw()
        #win.flip() 
        #If response is correct, that means they've said the flash is darker
        #So, we want to make flash brighter (More transparent)
        
        #A correct response means they said the flash was darker
        
        #We don't count reversals to the staircase on the first 8 trials (practice)
        #Hence trialCount >= 9
        
        #Store values:
        
        thisExp.addData('ST1Dir', ST1Dir)
        thisExp.addData('ST1StairStep', ST1StairStep)  
        thisExp.addData('ST2Dir', ST2Dir)
        thisExp.addData('ST2StairStep', ST2StairStep)   
        thisExp.addData('ST3Dir', ST3Dir)
        thisExp.addData('ST3StairStep', ST3StairStep)
        thisExp.addData('ST4Dir', ST4Dir)
        thisExp.addData('ST4StairStep', ST4StairStep)
        
        
        if StairNum == 1:
            if trialCount >= 9: #only store this on live trials, first 8 are prac
                ST1TC += 1
            if resp.corr == 1: #Flash perceived as darker, make flash brighter
                if ST1Dir == 'down': # A reversal occured=
                    ST1Dir = 'up'
                    ST1RevVals.append(ST1Opa) #store reveral value
                    ST1NumRevs += 1
                    ReversalOccured = True
                    thisExp.addData('ReversalOccured', ReversalOccured)
                ST1Opa -= stairStep[ST1StairStep]
                #ST1Opa  = round(ST1Opa, 3)
        
            else: #Flash perceived as brighter, make darker Dimmer (down)
                if ST1Dir == 'up':
                    ST1Dir = 'down'
                    ST1RevVals.append(ST1Opa)
                    ST1NumRevs += 1
                    ReversalOccured = True
                    thisExp.addData('ReversalOccured', ReversalOccured)
                ST1Opa += stairStep[ST1StairStep]
                #ST1Opa = round(ST1Opa, 3)
            if ST1Opa > MaxVal:
                ST1Opa  = 1
            if ST1Opa  < MinVal :
                ST1Opa = 0.1
            if ST1NumRevs == NumRevs:
                ST1NumRevs = 0
        
        elif StairNum == 2:
            if trialCount >= 9: #only does this on live trials
                ST2TC += 1
            if resp.corr == 1: #Flash darker, make brighter
               # ST2Opa  = round(ST2Opa, 3)
                if ST2Dir == 'down':
                    ST2Dir = 'up'
                    ST2RevVals.append(ST2Opa)
                    ST2NumRevs += 1
                    ReversalOccured = True
                    thisExp.addData('ReversalOccured', ReversalOccured)
                ST2Opa -= stairStep[ST2StairStep]
            else:
                if ST2Dir == 'up':
                    ST2Dir = 'down'
                    ST2RevVals.append(ST2Opa)
                    ST2NumRevs += 1
                    ReversalOccured = True
                    thisExp.addData('ReversalOccured', ReversalOccured)
                ST2Opa += stairStep[ST2StairStep] #Flash is brighter, make dimmer
            if ST2Opa > MaxVal:
                ST2Opa  = 1
            if ST2Opa < MinVal :
                ST2Opa = 0.1
            if ST2NumRevs == NumRevs:
               ST2NumRevs = 0
               
        elif StairNum == 3:
            if trialCount >= 9: #only does this on live trials
                ST3TC += 1
            if resp.corr == 1: #Make flash brighte
                if ST3Dir == 'down':
                    ST3Dir = 'up'
                    ST3RevVals.append(ST3Opa)
                    ST3NumRevs += 1
                    ReversalOccured = True
                    thisExp.addData('ReversalOccured', ReversalOccured)
                ST3Opa -= stairStep[ST3StairStep]
              #  ST3Opa  = round(ST3Opa, 3)
            else: #flash perceived as brighter, make dimmer
                if ST3Dir == 'up':
                    ST3Dir = 'down'
                    ST3RevVals.append(ST3Opa)
                    ST3NumRevs += 1
                    ReversalOccured = True
                    thisExp.addData('ReversalOccured', ReversalOccured)
                ST3Opa += stairStep[ST3StairStep]
               # ST3Opa = round(ST3Opa, 3)
            if ST3Opa > MaxVal:
                 ST3Opa   = 1
            if  ST3Opa < MinVal :
                 ST3Opa = 0.1
            if ST3NumRevs == NumRevs:
                ST3NumRevs = 0
            
        elif StairNum == 4:
            if trialCount >= 9:
                ST4TC += 1
            if resp.corr == 1: #Flash perceived as dimmer, make flash brighter
                if ST4Dir == 'down':
                    ST4Dir = 'up'
                    ST4RevVals.append(ST4Opa)
                    ST4NumRevs += 1 
                    ReversalOccured = True
                    thisExp.addData('ReversalOccured', ReversalOccured)
                ST4Opa -= stairStep[ST4StairStep]
              #  ST4Opa  = round(ST4Opa, 3)
            else: #flash perceived as brighter, make flash dimmer
                if ST4Dir == 'up':
                    ST4Dir = 'down'
                    ST4RevVals.append(ST4Opa)
                    ST4NumRevs += 1
                    ReversalOccured = True
                    thisExp.addData('ReversalOccured', ReversalOccured)
                ST4Opa += stairStep[ST4StairStep]
               # ST4Opa = round(ST4Opa, 3)
            if ST4Opa > MaxVal:
                ST4Opa  = 1
            if ST4Opa  < MinVal :
                ST4Opa = 0.1
            if ST4NumRevs == NumRevs:
                ST4NumRevs = 0
        
        ReversalOccured  = False
        
        #we store the Trial count after the fact, as it starts at 0
        thisExp.addData('ST1TC', ST1TC) 
        thisExp.addData('ST2TC', ST2TC)
        thisExp.addData('ST3TC', ST3TC)
        thisExp.addData('ST4TC', ST4TC)
        
        
        ConditionControl.addData('flash.started', flash.tStartRefresh)
        ConditionControl.addData('flash.stopped', flash.tStopRefresh)
        ConditionControl.addData('FPTRIAL.started', FPTRIAL.tStartRefresh)
        ConditionControl.addData('FPTRIAL.stopped', FPTRIAL.tStopRefresh)
        win.recordFrameIntervals = False #Do this as a fail safe
        thisExp.addData('AutoDroppedFrames', win.nDroppedFrames)
        #thisExp.addData('ManualFramesDropped', FramesDropped)
        
        if win.nDroppedFrames > PastCount:
            DisgardTrial = True
        
        thisExp.addData('DisgardTrial', DisgardTrial)
        
        #Past count of dropped frames
        PastCount = win.nDroppedFrames
        # the Routine "TrialRout" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "Practice"-------
        continueRoutine = True
        # update component parameters for each repeat
        #The first 8 trials are practice trials
        
        if trialCount == 8:
            endPrac = 'You have finished all the practice trials.' + '\n' + 'Press space to begin the live experiment.'
        else:
            endPrac = ' Press space when you are ready to continue the practice trials.'
        
        if trialCount >= 9:
            continueRoutine = False
            WasPractice = False
            
        #At time of flash, the target is always 0.5; If resp is correct, they said the flash was darker
        if trialCount < 9:
            WasPractice = True
            if resp.corr == 1: #Flash was perceived as darker
                if FlashLum > 0.5: #>0.5 means it was darker than the target
                    PracText = 'That was correct, good work! ' + '\n' + '\n' + endPrac
                else: #<0.5 means the flash was brighter than the target
                    PracText = 'You said the flashed circle was darker. But the continuously changing circle was darker. ' + '\n' + '\n'+ 'Please try and select the darkest circle.'  + '\n' + '\n' + endPrac
            else: #Flash was perceived as brighter
                if FlashLum < 0.5: #<0.5 means brighter than target flash
                    PracText = 'That was correct, good work!' + '\n' + '\n' + endPrac
                else: #Flash was darker than target flash
                    PracText = 'You said the continuously changing circle was darker, but the flash was darker.' + '\n' + '\n'+ 'Please select the darkest circle.'  + '\n' + '\n' +endPrac
        
        thisExp.addData('WasPractice', WasPractice)
        displayPracText.setText(PracText)
        endPracRoutine.keys = []
        endPracRoutine.rt = []
        _endPracRoutine_allKeys = []
        # keep track of which components have finished
        PracticeComponents = [displayPracText, endPracRoutine]
        for thisComponent in PracticeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Practice"-------
        while continueRoutine:
            # get current time
            t = PracticeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *displayPracText* updates
            if displayPracText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                displayPracText.frameNStart = frameN  # exact frame index
                displayPracText.tStart = t  # local t and not account for scr refresh
                displayPracText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(displayPracText, 'tStartRefresh')  # time at next scr refresh
                displayPracText.setAutoDraw(True)
            
            # *endPracRoutine* updates
            waitOnFlip = False
            if endPracRoutine.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                endPracRoutine.frameNStart = frameN  # exact frame index
                endPracRoutine.tStart = t  # local t and not account for scr refresh
                endPracRoutine.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(endPracRoutine, 'tStartRefresh')  # time at next scr refresh
                endPracRoutine.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(endPracRoutine.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(endPracRoutine.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if endPracRoutine.status == STARTED and not waitOnFlip:
                theseKeys = endPracRoutine.getKeys(keyList=['y', 'n', 'space'], waitRelease=False)
                _endPracRoutine_allKeys.extend(theseKeys)
                if len(_endPracRoutine_allKeys):
                    endPracRoutine.keys = _endPracRoutine_allKeys[-1].name  # just the last key pressed
                    endPracRoutine.rt = _endPracRoutine_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Practice"-------
        for thisComponent in PracticeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ConditionControl.addData('displayPracText.started', displayPracText.tStartRefresh)
        ConditionControl.addData('displayPracText.stopped', displayPracText.tStopRefresh)
        # check responses
        if endPracRoutine.keys in ['', [], None]:  # No response was made
            endPracRoutine.keys = None
        ConditionControl.addData('endPracRoutine.keys',endPracRoutine.keys)
        if endPracRoutine.keys != None:  # we had a response
            ConditionControl.addData('endPracRoutine.rt', endPracRoutine.rt)
        ConditionControl.addData('endPracRoutine.started', endPracRoutine.tStartRefresh)
        ConditionControl.addData('endPracRoutine.stopped', endPracRoutine.tStopRefresh)
        # the Routine "Practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "AttCheckFlash"-------
        continueRoutine = True
        # update component parameters for each repeat
        resp_ATT.keys = []
        resp_ATT.rt = []
        _resp_ATT_allKeys = []
        #Start of each routine, we set the position of the flash and target
        ChangingTarget_ATT.setPos([0, ChangeY])
        
        #We use the trialCount <= TrialCheck, because if trialCount is before this, enough trials have not occcurred to trigger an attention ccheck
        if trialCount < TrialCheck or (trialCount - 8) % TrialCheck != 0 or trialCount >= 240: #We minus by 8 to not consider the first practice trials (there are 240 live trials, so after 240, we don't want another att check)
            continueRoutine = False
        else:    
            AttentionCheck += 1
            AttCheckCount = False
            AttentionCheck = True
            warning = False
            shuffle(ColourList) #Make the RGB random
            thisExp.addData('AttentionCheck', AttentionCheck)
            #During the isi the fixation should be red
            FixCol = (1, 1, 1) #White
            FP_ATT.color = (FixCol)
        
        ## We need to reset the target's starting luminance values
        CircOpa = StartLum #Target alpha
        
        ChangingTarget_ATT.setOpacity(CircOpa)
        ChangingTarget_ATT.setPos((0, ChangeY))
        # keep track of which components have finished
        AttCheckFlashComponents = [resp_ATT, FP_ATT, ChangingTarget_ATT, ISI_FP_ATT]
        for thisComponent in AttCheckFlashComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AttCheckFlashClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AttCheckFlash"-------
        while continueRoutine:
            # get current time
            t = AttCheckFlashClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AttCheckFlashClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *resp_ATT* updates
            waitOnFlip = False
            if resp_ATT.status == NOT_STARTED and frameN >= 60:
                # keep track of start time/frame for later
                resp_ATT.frameNStart = frameN  # exact frame index
                resp_ATT.tStart = t  # local t and not account for scr refresh
                resp_ATT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(resp_ATT, 'tStartRefresh')  # time at next scr refresh
                resp_ATT.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(resp_ATT.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(resp_ATT.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if resp_ATT.status == STARTED and not waitOnFlip:
                theseKeys = resp_ATT.getKeys(keyList=['up', 'down', 'r', 'space'], waitRelease=False)
                _resp_ATT_allKeys.extend(theseKeys)
                if len(_resp_ATT_allKeys):
                    resp_ATT.keys = _resp_ATT_allKeys[-1].name  # just the last key pressed
                    resp_ATT.rt = _resp_ATT_allKeys[-1].rt
                    # was this correct?
                    if (resp_ATT.keys == str(CorrAns)) or (resp_ATT.keys == CorrAns):
                        resp_ATT.corr = 1
                    else:
                        resp_ATT.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *FP_ATT* updates
            if FP_ATT.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
                # keep track of start time/frame for later
                FP_ATT.frameNStart = frameN  # exact frame index
                FP_ATT.tStart = t  # local t and not account for scr refresh
                FP_ATT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FP_ATT, 'tStartRefresh')  # time at next scr refresh
                FP_ATT.setAutoDraw(True)
            #Larger alpha = darker
            #Smaller alpha = brighter
            
            if t > 1: # don't draw the target during the interstimulus interval
                if LumChange == 'Brighter':
                    CircOpa -= stepSize
                else: #Become dimmer by becoming closer to 1
                    CircOpa += stepSize
            #Change colour/lum every frame
            ChangingTarget_ATT.setOpacity(CircOpa) #, colorSpace='rgb')#Frame 24 is the halfway point
            #DON'T NEED TO DRAW, AS I TURN ON THE AUTODRAW BELOW! :)
            #CircOpa = round(CircOpa, 3)
            
            ## Present the flash for one frame
            if frameN <= (RefreshHz + FlashonFrame + FlashDur) and frameN >= (RefreshHz + FlashonFrame): #We want to start the flash when it normally occurs, but consider the ISI
                flash.draw()
            
            if AttentionCheck == True:
                if frameN >= AttISI and t <= (2): #WE only want the fixation to change colour for a second ; the isi is 1 second
                    if frameN % UpdateOn == 0:
                        FixCol = ColourList[ListIdx]
                        #Change colour/lum every frame
                        ChangingTarget_ATT.setAutoDraw(False) #, colorSpace='rgb')#Frame 24 is the halfway point
                        FP_ATT.color = (FixCol)            
                        ListIdx += 1
                        ChangingTarget_ATT.setAutoDraw(True)
                        
                        if ListIdx == (len(ColourList) - 1):
                            ListIdx = 0 #Reset index when it hits max list
                else:
                    FixCol = ([1, 1, 1]) #White
                    FP_ATT.setColor([FixCol]) 
            
            # *ChangingTarget_ATT* updates
            if ChangingTarget_ATT.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                ChangingTarget_ATT.frameNStart = frameN  # exact frame index
                ChangingTarget_ATT.tStart = t  # local t and not account for scr refresh
                ChangingTarget_ATT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ChangingTarget_ATT, 'tStartRefresh')  # time at next scr refresh
                ChangingTarget_ATT.setAutoDraw(True)
            if ChangingTarget_ATT.status == STARTED:
                if frameN >= (ChangingTarget_ATT.frameNStart + AttChangeCirc):
                    # keep track of stop time/frame for later
                    ChangingTarget_ATT.tStop = t  # not accounting for scr refresh
                    ChangingTarget_ATT.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ChangingTarget_ATT, 'tStopRefresh')  # time at next scr refresh
                    ChangingTarget_ATT.setAutoDraw(False)
            
            # *ISI_FP_ATT* updates
            if ISI_FP_ATT.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                ISI_FP_ATT.frameNStart = frameN  # exact frame index
                ISI_FP_ATT.tStart = t  # local t and not account for scr refresh
                ISI_FP_ATT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI_FP_ATT, 'tStartRefresh')  # time at next scr refresh
                ISI_FP_ATT.setAutoDraw(True)
            if ISI_FP_ATT.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ISI_FP_ATT.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    ISI_FP_ATT.tStop = t  # not accounting for scr refresh
                    ISI_FP_ATT.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ISI_FP_ATT, 'tStopRefresh')  # time at next scr refresh
                    ISI_FP_ATT.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AttCheckFlashComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AttCheckFlash"-------
        for thisComponent in AttCheckFlashComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if resp_ATT.keys in ['', [], None]:  # No response was made
            resp_ATT.keys = None
            # was no response the correct answer?!
            if str(CorrAns).lower() == 'none':
               resp_ATT.corr = 1;  # correct non-response
            else:
               resp_ATT.corr = 0;  # failed to respond (incorrectly)
        # store data for ConditionControl (TrialHandler)
        ConditionControl.addData('resp_ATT.keys',resp_ATT.keys)
        ConditionControl.addData('resp_ATT.corr', resp_ATT.corr)
        if resp_ATT.keys != None:  # we had a response
            ConditionControl.addData('resp_ATT.rt', resp_ATT.rt)
        ConditionControl.addData('resp_ATT.started', resp_ATT.tStartRefresh)
        ConditionControl.addData('resp_ATT.stopped', resp_ATT.tStopRefresh)
        ConditionControl.addData('FP_ATT.started', FP_ATT.tStartRefresh)
        ConditionControl.addData('FP_ATT.stopped', FP_ATT.tStopRefresh)
        if AttentionCheck == True:
            FixCol = MyRed
            FP_ATT.color = (FixCol)
           
            if resp_ATT.corr == 1:
                PassCheck = True
            else:
                PassCheck = False
                warning = True
                NumFails += 1
            if NumFails >= 2:
                FailedAtt = True
            thisExp.addData('FailedAtt', FailedAtt)
            thisExp.addData('NumFails', NumFails)
            thisExp.addData('PassCheck', PassCheck)
        ConditionControl.addData('ChangingTarget_ATT.started', ChangingTarget_ATT.tStartRefresh)
        ConditionControl.addData('ChangingTarget_ATT.stopped', ChangingTarget_ATT.tStopRefresh)
        ConditionControl.addData('ISI_FP_ATT.started', ISI_FP_ATT.tStartRefresh)
        ConditionControl.addData('ISI_FP_ATT.stopped', ISI_FP_ATT.tStopRefresh)
        # the Routine "AttCheckFlash" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "AttWarning"-------
        continueRoutine = True
        # update component parameters for each repeat
        ExtraText = 'You took too long to respond. Please try to respond as fast as possible.' + '\n' + "When the center dot changes colour, please press 'r'"
        
        #Only show this message when they fail the attcheck
        if AttentionCheck == False or PassCheck == True:
            continueRoutine = False
        else:
            ExtraText = 'Unfortunately, you pressed the wrong key during the attention check. ' + '\n' + "When the center cross changes colour, please press 'r'"
        
        ATT_TEXT.setText(ExtraText + '\n' + '\n' + 'Just a friendly reminder to please stare at the cross in the center of the screen during the experiment.' + '\n' + '\n' + "Press 's' to resume the experiment. ")
        Att_RESP.keys = []
        Att_RESP.rt = []
        _Att_RESP_allKeys = []
        # keep track of which components have finished
        AttWarningComponents = [ATT_TEXT, Att_RESP]
        for thisComponent in AttWarningComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        AttWarningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "AttWarning"-------
        while continueRoutine:
            # get current time
            t = AttWarningClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=AttWarningClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *ATT_TEXT* updates
            if ATT_TEXT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ATT_TEXT.frameNStart = frameN  # exact frame index
                ATT_TEXT.tStart = t  # local t and not account for scr refresh
                ATT_TEXT.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ATT_TEXT, 'tStartRefresh')  # time at next scr refresh
                ATT_TEXT.setAutoDraw(True)
            
            # *Att_RESP* updates
            waitOnFlip = False
            if Att_RESP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Att_RESP.frameNStart = frameN  # exact frame index
                Att_RESP.tStart = t  # local t and not account for scr refresh
                Att_RESP.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Att_RESP, 'tStartRefresh')  # time at next scr refresh
                Att_RESP.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Att_RESP.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Att_RESP.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Att_RESP.status == STARTED and not waitOnFlip:
                theseKeys = Att_RESP.getKeys(keyList=['s', 'right'], waitRelease=False)
                _Att_RESP_allKeys.extend(theseKeys)
                if len(_Att_RESP_allKeys):
                    Att_RESP.keys = _Att_RESP_allKeys[-1].name  # just the last key pressed
                    Att_RESP.rt = _Att_RESP_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in AttWarningComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "AttWarning"-------
        for thisComponent in AttWarningComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #SEt this v ariable
        AttentionCheck = False
        PassCheck = False
        ConditionControl.addData('ATT_TEXT.started', ATT_TEXT.tStartRefresh)
        ConditionControl.addData('ATT_TEXT.stopped', ATT_TEXT.tStopRefresh)
        # check responses
        if Att_RESP.keys in ['', [], None]:  # No response was made
            Att_RESP.keys = None
        ConditionControl.addData('Att_RESP.keys',Att_RESP.keys)
        if Att_RESP.keys != None:  # we had a response
            ConditionControl.addData('Att_RESP.rt', Att_RESP.rt)
        ConditionControl.addData('Att_RESP.started', Att_RESP.tStartRefresh)
        ConditionControl.addData('Att_RESP.stopped', Att_RESP.tStopRefresh)
        # the Routine "AttWarning" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "BREAK"-------
        continueRoutine = True
        # update component parameters for each repeat
        #We always want the break to be halfway 
        #At the moment there is 240 trials
        if trialCount != 120:
            continueRoutine = False
        BreakResp.keys = []
        BreakResp.rt = []
        _BreakResp_allKeys = []
        # keep track of which components have finished
        BREAKComponents = [text, BreakResp]
        for thisComponent in BREAKComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BREAKClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "BREAK"-------
        while continueRoutine:
            # get current time
            t = BREAKClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BREAKClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # *BreakResp* updates
            waitOnFlip = False
            if BreakResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BreakResp.frameNStart = frameN  # exact frame index
                BreakResp.tStart = t  # local t and not account for scr refresh
                BreakResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BreakResp, 'tStartRefresh')  # time at next scr refresh
                BreakResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(BreakResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(BreakResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if BreakResp.status == STARTED and not waitOnFlip:
                theseKeys = BreakResp.getKeys(keyList=['y', 'space'], waitRelease=False)
                _BreakResp_allKeys.extend(theseKeys)
                if len(_BreakResp_allKeys):
                    BreakResp.keys = _BreakResp_allKeys[-1].name  # just the last key pressed
                    BreakResp.rt = _BreakResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BREAKComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BREAK"-------
        for thisComponent in BREAKComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        ConditionControl.addData('text.started', text.tStartRefresh)
        ConditionControl.addData('text.stopped', text.tStopRefresh)
        # check responses
        if BreakResp.keys in ['', [], None]:  # No response was made
            BreakResp.keys = None
        ConditionControl.addData('BreakResp.keys',BreakResp.keys)
        if BreakResp.keys != None:  # we had a response
            ConditionControl.addData('BreakResp.rt', BreakResp.rt)
        ConditionControl.addData('BreakResp.started', BreakResp.tStartRefresh)
        ConditionControl.addData('BreakResp.stopped', BreakResp.tStopRefresh)
        # the Routine "BREAK" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
    
    # completed NumReps repeats of 'ConditionControl'

    # get names of stimulus parameters
    if ConditionControl.trialList in ([], [None], None):
        params = []
    else:
        params = ConditionControl.trialList[0].keys()
    # save data for this loop
    ConditionControl.saveAsText(filename + 'ConditionControl.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])

#Completed 1.0 repeats of 'SelectCondFile'
# get names of stimulus parameters
if SelectCondFile.trialList in ([], [None], None):
    params = []
else:
    params = SelectCondFile.trialList[0].keys()
# save data for this loop
SelectCondFile.saveAsText(filename + 'SelectCondFile.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])


# ------Prepare to start Routine "Conclusion"-------
continueRoutine = True
# update component parameters for each repeat
thisExp.addData("globalClockTime", globalClock.getTime()) 

##Plot intervals and save in text file
import matplotlib.pyplot as plt

FILE_NAME_TEXT=('Intervals\Text\Lum_' + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + "_FrameIntervals"  + '.log')
FILE_NAME_PNG = ('Intervals\Images\Lum_' + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + "_FrameIntervals" + '.png')

key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
#Calculate threshold over the last 6 reversals
#Note: 60 trials per staircase

#Saves the reversal values for each staircase
thisExp.addData('ST1RevVals', ST1RevVals)
thisExp.addData('ST2RevVals', ST2RevVals)
thisExp.addData('ST3RevVals', ST3RevVals)
thisExp.addData('ST4RevVals', ST4RevVals)

ST1Thresh = average(ST1RevVals[-6:])
ST2Thresh = average(ST2RevVals[-6:])
ST3Thresh = average(ST3RevVals[-6:])
ST4Thresh = average(ST4RevVals[-6:])

#Save the thresholds
thisExp.addData('ST1Thresh', ST1Thresh)
thisExp.addData('ST2Thresh', ST2Thresh)
thisExp.addData('ST3Thresh', ST3Thresh)
thisExp.addData('ST4Thresh', ST4Thresh)
# keep track of which components have finished
ConclusionComponents = [End, key_resp]
for thisComponent in ConclusionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ConclusionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Conclusion"-------
while continueRoutine:
    # get current time
    t = ConclusionClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ConclusionClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *End* updates
    if End.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        End.frameNStart = frameN  # exact frame index
        End.tStart = t  # local t and not account for scr refresh
        End.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(End, 'tStartRefresh')  # time at next scr refresh
        End.setAutoDraw(True)
    
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
        theseKeys = key_resp.getKeys(keyList=['p', 'space'], waitRelease=False)
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
    for thisComponent in ConclusionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Conclusion"-------
for thisComponent in ConclusionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
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
        
    PercentDropped =  100 * nDropped/float(nTotal)
    titleMsg = "Dropped:  %i, total frames: %i, percent dropped = %.3f%%"
    droppedString = titleMsg % (nDropped, nTotal, PercentDropped)
    
    ## Save the intervals:
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

thisExp.addData('End.started', End.tStartRefresh)
thisExp.addData('End.stopped', End.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
####### DIMENSIONS OF THE CIRCLES IN DVA, BASED UPON SHETH ET AL. (2000)

## SIZE OF THE CIRCLES

## Coordinates of circles

## Convert the DVA to pixels and store (Width and height was identical)
Pix_Fix = tools.monitorunittools.deg2pix(FixH, win.monitor)
Pix_Circ = tools.monitorunittools.deg2pix(CircW, win.monitor) #this is the pixels for the target

#Y coordinate position (in pixels)
Pix_Y = tools.monitorunittools.deg2pix(3.5, win.monitor)

## Add pixels to datafile
thisExp.addData('Pix_Fix', Pix_Fix)
thisExp.addData('Pix_Circ', Pix_Circ)
thisExp.addData('stepSize', stepSize)
thisExp.addData('Pix_Y', Pix_Y)
# the Routine "Conclusion" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
