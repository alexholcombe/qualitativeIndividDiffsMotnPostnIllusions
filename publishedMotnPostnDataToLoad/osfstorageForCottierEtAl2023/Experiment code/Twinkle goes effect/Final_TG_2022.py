#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on January 21, 2022, at 12:49
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y
"""
#Tim Cottier modified this script in coder to run more efficiently/without errors. 
#E.g., porting directly from builder invokes a "needs to be int" not float error for the noise stim

## TC Modified from builder:
    # Turned window blanking off
    # Removed eye tracking setup
    # Removed the default to 60hz if cannot read frameRate
    # removed an unnecessary win.flip() at the end; causes errors/warnings as win.flip() is called beforehand for plotting.
    # Changed to 144hz. Were initially coded for 200hz, but 200hz was causing issues (on other paradigms, not this one)
    # Slowed speed to 18.1 Dva/Sec
    # Participants cannot respond before noise disappears.
    #Will no longer preesnt a "Good work passing attention check" if they pass, onl ya message on fails.
    # Attention check no longer times out after 3 seconds"

## CHANGES AFTER FIRST 6 PARTICIPANTS:
# No longer doing multi-assignment of variables, this was causing more issues than solutions (it broke the recording of reversals in python, because all were assigned to the same list)

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
#we use tools to do monitor unit conversions
from psychopy import tools

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'TwinkleGoes'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Timot\\Documents\\2021\\Study 1\\September_Final_EXPERIMENTS_LIVE_Python\\Python-Experiments\\Twinkle Goes\\TG_2022_NewNoise.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info

## If test, set logging level to debugging
if int(expInfo['test']) == 1:
    logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
else:
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='ASUS_PG248Q', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', waitBlanking=False, useFBO=True, 
    units='pix')
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
WelTXT = visual.TextStim(win=win, name='WelTXT',
    text=' In this experiment you will see a black dot on the centre of the screen, please stare at this black dot at all times.\n\nWhile you\'re staring at the dot, there will be one square above the centre of the screen and one below the centre of the screen. These two squares will move towards each other.  Eventually, the squares and background will disappear. When everything has disappeared, your task is to report the top square\'s final location, the position it was in when it disappeared. \n\nIf the top square disappeared to the left of the bottom square, press the "left" arrow key.\nif the top square disappeared to the right of the bottom square, press the \'right\' arrow key.\n\n The first few trials are practice trials. Press \'space\' when you are ready to begin the experiment. ',
    font='Arial',
    units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
StartExp = keyboard.Keyboard()
## Check the file does not already exist
if os.path.exists(filename + '.csv'):
    print('Warning: Datafile already exists!')
    core.quit()

## Refresh rate
RefreshHz = 144 #win.getActualFrameRate()
CurrentMonitor = win.monitor

if int(expInfo['test']) == 0: #1 = true, it's a test; 0 = false, not a test (LIVE TRIALS)
    if FrameRate <140 or FrameRate > 148 or RefreshHz != 144: #Give a 4 frame buffer 
        print('WARNING! ERROR WITH FRAMERATE OR REFRESHHZ. Psychopy detected the FrameRate at: ' +str(FrameRate) + 'RefreshHz was: ' + str(RefreshHz))
        core.quit()


# Initialize components for Routine "ISI"
ISIClock = core.Clock()
#Dynamically set ISI 
ISIDUR = 116 #805ms
'''
if RefreshHz == 60:
    ISIDUR = 48
elif RefreshHz == 200:
    ISIDUR = 160
else:
    ISIDUR = np.ceil(0.8/(1/RefreshHz)) #800ms, in frames
'''
FixSurr_ISI = visual.ShapeStim(
    win=win, name='FixSurr_ISI', vertices=99,units='deg', 
    size=(1.1, 1.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0],
    opacity=None, depth=-1.0, interpolate=True)
FixationPoint_ISI = visual.ShapeStim(
    win=win, name='FixationPoint_ISI', vertices=99,units='deg', 
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=None, depth=-2.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
#tools.monitorunittools.deg2pix(degrees, monitor[, correctFlat])
SqSizeW = tools.monitorunittools.deg2pix(2.9, CurrentMonitor) #200
SqSizeH = tools.monitorunittools.deg2pix(7.7, CurrentMonitor)#324

#Y coordinates of the top square
topSqY = tools.monitorunittools.deg2pix(7.7, CurrentMonitor) #0.2
botSqY = topSqY * -1
SquareSpeedSec = tools.monitorunittools.deg2pix(18.1, CurrentMonitor) #SPEED; Default: 18.1; we want it to be 20% faster than the original (18.1)
trialCount = 0

CurrentStair = 0 #Offset of currentstair to apply

## STAIRCASE PARAMETERS: 

#We want the offset value (I.e, to be about ~25% of the way from the opposite starting position (I.e, if starts at 400, it should finish 100 pixels)
Off = SquareSpeedSec * 0.25

StairStep = Off/10 # 14Pixels - Denominator specifies how many steps of offset to zero; I ant 10

'''Specify staircase parameters:
                !! STATIC STAIRS !! 
    Stair1 - STAHR - Static noise, ahead, right to left
    Stair2 STAHL - Static noise, ahead, left to right
    Stair3 STBEHR - Static noise behind, right to left
    Stair4 STBEHL - Static noise behind,left to right
    
                !! DYNAMIC STAIRS !!
    Stair 5 DYAHR - Dynamic noise, ahead, right to left
    Stair 6 DYAHL - Dynamic noise, ahead, left to right
    Stair 7 DYBEHR - Dyanmic noise, behind, right to left
    Stair 8 DYBEHL - Dyanmic noise, behind, left to right
    
    '''

''' Direction offset:
    Ahead = displaced in direction of motion
    Behind = displaced in direction opposite motion
    Ahead - Left to right, positive is offset ahead
    Ahead, right to left, negative is offset ahead
    Behind, left to right, negative is offset behind
    Behind, right to left, positive is offset behind
    '''

#Initialise practice staircases
Prac1 = 0
Prac2 = 0

#Staircase, static noise, squares are displaced in the direction of motion
#RtL
Stair1 = -Off
Stair4 = -Off 
Stair5 = -Off 
Stair8 = -Off #How much offset we make to make the Staircase offset

Stair2 = Off
Stair3 = Off
Stair6 = Off
Stair7 = Off #How much offset we make to make the Staircase offset

Stair1TC = 0
Stair2TC = 0
Stair3TC = 0
Stair4TC = 0
Stair5TC = 0
Stair6TC = 0
Stair7TC = 0
Stair8TC = 0 #Trialcount

Stair1NumRevs = 0
Stair2NumRevs = 0
Stair3NumRevs = 0
Stair4NumRevs = 0
Stair5NumRevs = 0
Stair6NumRevs = 0
Stair7NumRevs = 0
Stair8NumRevs = 0 #Count how many reversals

#Down means, opposite the direction of motion; up means in the direction of motion
Stair1Dir = 'down'
Stair2Dir = 'down'
Stair5Dir = 'down'
Stair6Dir = 'down' #Staircase direction
Stair3Dir = 'up'
Stair4Dir = 'up'
Stair7Dir = 'up'
Stair8Dir = 'up'

Stair1RevVals = []
Stair2RevVals = [] 
Stair3RevVals = []  
Stair4RevVals = []
Stair5RevVals = []
Stair6RevVals = []
Stair7RevVals = []
Stair8RevVals = [] #List of reversal

#Reversal occurred, store reversal value
ReversalOccur = False
RevVal = 0 #Store reversal value here
#how many frames to subtract to start noise
#Should be about 55ms to subtract
'''
if RefreshHz == 144:
    SubtractFrames = 8 #8 should be around 55ms
elif RefreshHz == 200:
    SubtractFrames = 11 # 55ms
elif RefreshHz == 60:
    SubtractFrames = 4 #66ms
'''

SubtractFrames = 8 #8 should be around 55ms

noise = visual.NoiseStim(
    win=win, name='noise',units='pix', 
    noiseImage=None, mask=None,
    ori=0.0, pos=(0, 0), size=(2048, 2048), 
    sf=None, phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=None, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Uniform', noiseElementSize=(8, 8), #4,4 causes dropped frames
    noiseBaseSf=8.0, noiseBW=1.0,
    noiseBWO=30.0, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=0.0) #depth = -4
noise.buildNoise()
TopSQ = visual.Rect(
    win=win, name='TopSQ',
    width=(SqSizeW, SqSizeH)[0], height=(SqSizeW, SqSizeH)[1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-5.0, interpolate=True)
BotSQ = visual.Rect(
    win=win, name='BotSQ',
    width=(SqSizeW, SqSizeH)[0], height=(SqSizeW, SqSizeH)[1],
    ori=0, pos=[0,0],
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-6.0, interpolate=True)
Resp = keyboard.Keyboard()
FixSurround = visual.ShapeStim(
    win=win, name='FixSurround', vertices=99,units='deg', 
    size=(1.1, 1.1),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[0,0,0], fillColor=[0,0,0],
    opacity=None, depth=-8.0, interpolate=True)
FixationPoint = visual.ShapeStim(
    win=win, name='FixationPoint', vertices=99,units='deg', 
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=None, depth=-9.0, interpolate=True)
#Report warnings to the standard output window
logging.console.setLevel(logging.WARNING)

PastCount = 0

# Initialize components for Routine "PracticeTrials"
PracticeTrialsClock = core.Clock()
EndPrac = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text="That is the end of the practice trials.\n\nPress 'space' to continue the experiment.\n\nIf you would like to exit the experiment or redo the practice trials, please tell the researcher.",
    font='Open Sans',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ISICheck"
ISICheckClock = core.Clock()
ATT_RESP = keyboard.Keyboard()
#Initialise variables
AttentionCheck = False

## TROUBLE SHOOT CODE:
#TROUBLE_ATT_IDX = 0 

#want the check trials every 20 trials (half a staircase ~)
CheckList = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300]

MyRed = (1, -1, -1)
myYell = (1.0000, 1.0000, -1.0000)
myGreen = (-1, 1, -1)
myOrange = (1.0000, 0.2941, -1.0000) 
myCyan = (-1.0000, 1.0000, 1.0000)
myMagneta = (1.0000, -1.0000, 1.0000)
myPurple = (0.0039, -1.0000, 0.0039) 
myBlack = (-1, -1, -1)
FixCol = myBlack
ColourList = [myYell, myGreen, MyRed, myPurple, myMagneta, myCyan, myOrange]


#Update colour after how many frames; 1 is super quick
UpdateOn = 18 #125 ms

ListIdx = 0 #To select a colour from the list

PassCheck = False

CorrAns = 'r'

#Failed more than two checks
FailedCheck = False
NumFails = 0
ISI_2 = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI_2')

# Initialize components for Routine "warningDisplay"
warningDisplayClock = core.Clock()
ExtraText = 'Unfortunately, you pressed the wrong key during the attention check. ' + '\n' + "When the center dot changes colour, please press 'r'"
warningText = visual.TextStim(win=win, name='warningText',
    text='',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
ContinueExp = keyboard.Keyboard()

# Initialize components for Routine "BreakTime"
BreakTimeClock = core.Clock()
BreakText = visual.TextStim(win=win, name='BreakText',
    text="This is a break. Rest for as long as you need.\n\nPress 'space' when you are ready to resume the experiment.",
    font='Open Sans',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
BreakResp = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
goodbye = visual.TextStim(win=win, name='goodbye',
    text='',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

#Initialise RevCheck - This variable will check if the NumRevs == the length of the reversal list
# 1 means revcheck is equal; 0 = not equal
ST1RevCheck = 1
ST2RevCheck = 1
ST3RevCheck = 1
ST4RevCheck = 1
ST5RevCheck = 1
ST6RevCheck = 1
ST7RevCheck = 1
ST8RevCheck = 1

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
StartExp.keys = []
StartExp.rt = []
_StartExp_allKeys = []
win.mouseVisible = False
print(win.getActualFrameRate())
# keep track of which components have finished
InstructionsComponents = [WelTXT, StartExp]
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
    
    # *WelTXT* updates
    if WelTXT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        WelTXT.frameNStart = frameN  # exact frame index
        WelTXT.tStart = t  # local t and not account for scr refresh
        WelTXT.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(WelTXT, 'tStartRefresh')  # time at next scr refresh
        WelTXT.setAutoDraw(True)
    
    # *StartExp* updates
    waitOnFlip = False
    if StartExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        StartExp.frameNStart = frameN  # exact frame index
        StartExp.tStart = t  # local t and not account for scr refresh
        StartExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(StartExp, 'tStartRefresh')  # time at next scr refresh
        StartExp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(StartExp.clock.reset)  # t=0 on next screen flip
    if StartExp.status == STARTED and not waitOnFlip:
        theseKeys = StartExp.getKeys(keyList=['space', 'p', 'l'], waitRelease=False)
        _StartExp_allKeys.extend(theseKeys)
        if len(_StartExp_allKeys):
            StartExp.keys = _StartExp_allKeys[-1].name  # just the last key pressed
            StartExp.rt = _StartExp_allKeys[-1].rt
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
thisExp.addData('WelTXT.started', WelTXT.tStartRefresh)
thisExp.addData('WelTXT.stopped', WelTXT.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SelectCondFile = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('CondFile.xlsx'),
    seed=None, name='SelectCondFile')
thisExp.addLoop(SelectCondFile)  # add the loop to the experiment
thisSelectCondFile = SelectCondFile.trialList[0]  # so we can initialise stimuli with some values
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
    
    # set up handler to look after randomisation of conditions etc
    if int(expInfo['test']) == 1:
        TrialReps = 2
    else:
        TrialReps = NumReps
    
    trials = data.TrialHandler(nReps=NumReps, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(SelectCond),
        seed=None, name='trials')
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "ISI"-------
        continueRoutine = True
        # update component parameters for each repeat
        ## Select the 
        
        if SelectCond == 'PracCond.xlsx':
            PracTrial = True
        else:
            PracTrial = False
        
        thisExp.addData('PracTrial', PracTrial)
        # keep track of which components have finished
        ISIComponents = [FixSurr_ISI, FixationPoint_ISI]
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
        while continueRoutine:
            # get current time
            t = ISIClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISIClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FixSurr_ISI* updates
            if FixSurr_ISI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixSurr_ISI.frameNStart = frameN  # exact frame index
                FixSurr_ISI.tStart = t  # local t and not account for scr refresh
                FixSurr_ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixSurr_ISI, 'tStartRefresh')  # time at next scr refresh
                
                ## TC - Draw the background Noise
                #Noise will be same duration as the other ISI components, therefore, don't need to irecord start or offset time
                if noise._needBuild and NoiseTy == 'DY': #Don't change the noise on static, or the background moves at the start of the isi
                    noise.buildNoise()
                noise.setAutoDraw(True)  
                
                FixSurr_ISI.setAutoDraw(True)
                
            if FixSurr_ISI.status == STARTED:
                if frameN >= (FixSurr_ISI.frameNStart + ISIDUR):
                    # keep track of stop time/frame for later
                    FixSurr_ISI.tStop = t  # not accounting for scr refresh
                    FixSurr_ISI.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FixSurr_ISI, 'tStopRefresh')  # time at next scr refresh
                    FixSurr_ISI.setAutoDraw(False)
            
            # *FixationPoint_ISI* updates
            if FixationPoint_ISI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixationPoint_ISI.frameNStart = frameN  # exact frame index
                FixationPoint_ISI.tStart = t  # local t and not account for scr refresh
                FixationPoint_ISI.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixationPoint_ISI, 'tStartRefresh')  # time at next scr refresh
                FixationPoint_ISI.setAutoDraw(True)
            if FixationPoint_ISI.status == STARTED:
                if frameN >= (FixationPoint_ISI.frameNStart + ISIDUR):
                    # keep track of stop time/frame for later
                    FixationPoint_ISI.tStop = t  # not accounting for scr refresh
                    FixationPoint_ISI.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FixationPoint_ISI, 'tStopRefresh')  # time at next scr refresh
                    FixationPoint_ISI.setAutoDraw(False)
                    ##Tc stop drawing the noise
                    noise.setAutoDraw(False)
            
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
        trials.addData('FixSurr_ISI.started', FixSurr_ISI.tStartRefresh)
        trials.addData('FixSurr_ISI.stopped', FixSurr_ISI.tStopRefresh)
        trials.addData('FixationPoint_ISI.started', FixationPoint_ISI.tStartRefresh)
        trials.addData('FixationPoint_ISI.stopped', FixationPoint_ISI.tStopRefresh)
        # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        trialCount += 1 #Increase trial counter
        thisExp.addData('trialCount', trialCount)
        
        idx = -1
        idxhistory = [] #This is just to store the history
        
        #randomly pick square duration from 0.8 - 1 second
        SqDurSecs = np.random.uniform(0.8, 1) #secs
        SqDur = np.ceil(SqDurSecs * RefreshHz) #in frames
        
        #Store this to datafile
        thisExp.addData('SqDurSecs', SqDurSecs)
        thisExp.addData('SqDur', SqDur)
        
        #Created x coordinate list for an aligned condition; round to stop going int
        RightStartPos = (SquareSpeedSec * SqDurSecs) #Speed * duration
        LeftStartPos = (-RightStartPos)
        thisExp.addData('RightStartPos', RightStartPos)
        thisExp.addData('LeftStartPos', LeftStartPos)
        
        LtRCoordinates = np.linspace(int(LeftStartPos), int(0), int(SqDur))
        RtLCoordinates = np.linspace(int(RightStartPos), int(0), int(SqDur))
        
        #Core.wait at 0, disable the staircases and check they are ending in alignment
        #thisExp.addData('LtRXCoords', LtRCoordinates)
        #thisExp.addData('RtLXCoords', RtLCoordinates)
        
        #Pick Staircase
        if StairNoEx == 1:
            CurrentStair = Stair1
        elif StairNoEx == 2:
            CurrentStair = Stair2
        elif StairNoEx == 3:
            CurrentStair = Stair3
        elif StairNoEx == 4:
            CurrentStair = Stair4
        elif StairNoEx == 5:
            CurrentStair = Stair5
        elif StairNoEx == 6:
            CurrentStair = Stair6
        elif StairNoEx == 7:
            CurrentStair = Stair7
        elif StairNoEx == 8:
            CurrentStair = Stair8
        elif StairNoEx == 11:
            if TopDir == 'RtL':
                CurrentStair = Prac1
            else:
                CurrentStair = -Prac1
        elif StairNoEx == 22:
            if TopDir == 'RtL':
                CurrentStair = Prac2
            else:
                CurrentStair = -Prac2 #*-1 for left to right offset
        
        #Reset the starting position of the squares Set StartPos
        if TopDir == 'RtL':
            TopX = RtLCoordinates[idx] + (CurrentStair)
        else: 
            TopX = LtRCoordinates[idx] + (CurrentStair)
        BotX = TopX * -1
        
        #Set the squares position
        TopSQ.setPos((TopX, topSqY))
        BotSQ.setPos((BotX, botSqY))
        
        #Add the current stair value
        thisExp.addData('CurrentStair', CurrentStair)
        
        StoreCount = 0 #When this is 1 SQ ended
        
        TopXHist = [] #History of all top x coordinates  
        #Save Staircase value sbefore applied:
        
        thisExp.addData('Stair1', Stair1)
        thisExp.addData('Stair2', Stair2)
        thisExp.addData('Stair3', Stair3)
        thisExp.addData('Stair4', Stair4)
        thisExp.addData('Stair5', Stair5)
        thisExp.addData('Stair6', Stair6)
        thisExp.addData('Stair7', Stair7)
        thisExp.addData('Stair8', Stair8)
        
        
        #Add Practice trials
        thisExp.addData('Prac1', Prac1)
        thisExp.addData('Prac2', Prac2)
        ''' The noise needs to be dynamic 80ms before the squares disppear
        Noise is rebuilt every trial in the ISI routine
        Autodraw for the noise is turned on in the isi routine
        
        '''
        #We want the noise to continue for 400ms after Squares disappearance
        '''
        if RefreshHz == 200:
            BackFin = SqDur + 80
        elif RefreshHz == 60:
            BackFin = SqDur + 24
        else:
            BackFin = np.ceil(SqDur + (400/(1000/RefreshHz))) #noise continues for 400ms post disappearance (So 400ms/IFI in ms)
        '''
        BackFin = SqDur + 58  #noise continues for 400ms post disappearance
        
        NoiseStartFrame = SqDur - SubtractFrames #Start the noise in the 80ms before square's disappearance
        
        thisExp.addData('NoiseStartFrame', NoiseStartFrame)
        thisExp.addData('BackFin', BackFin)
        
        Resp.keys = []
        Resp.rt = []
        _Resp_allKeys = []
        win.recordFrameIntervals = True #win.nDroppedFrames stores this. 
        
        #Set a 10% tolerance for dropped frames
        win.refreshThreshold = (1/RefreshHz) * 1.1
        
        DisgardTrial = False
        
        #manual frame drop counter
        #FramesDropped = 0
        # keep track of which components have finished
        trialComponents = [noise, TopSQ, BotSQ, Resp, FixSurround, FixationPoint]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            if int(expInfo['test']) == 1: #if test mode, log the frame interval for the last frame
                if len(win.frameIntervals):
                    logging.debug('Last Frame Interval: ' + str(win.frameIntervals[-1])) #This will return the last frame interval appended

            if frameN <= SqDur: # <=
                if idx < (SqDur-1):
                    idx += 1
                    idxhistory.append(idx)
                
                if TopDir == 'RtL':
                    TopX = RtLCoordinates[idx] + (CurrentStair)
                else:
                    TopX = LtRCoordinates[idx] + (CurrentStair)
                    
                TopXHist.append(TopX)
                BotX = TopX * -1
            
                TopX = round(TopX * 100000)/100000
                BotX = round(BotX * 100000)/100000
            
            #This will let me verify if it's hitting 0 by the last frame (144 or 200)
            if frameN <= SqDur+2 and frameN >= SqDur-2:
                thisExp.addData('TopX' + str(frameN), TopX)
                
            if TopSQ.status==FINISHED:
                StoreCount += 1
                if StoreCount == 1:
                    thisExp.addData('SQFinishedonFrame', frameN) #This tells me what frames the square finished
                    
            # *noise* updates
            if noise.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                noise.frameNStart = frameN  # exact frame index
                noise.tStart = t  # local t and not account for scr refresh
                noise.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(noise, 'tStartRefresh')  # time at next scr refresh
                noise.setAutoDraw(True) # AutoDraw turned on in ISI
            if noise.status == STARTED:
                if frameN >= (noise.frameNStart + BackFin):
                    # keep track of stop time/frame for later
                    noise.tStop = t  # not accounting for scr refresh
                    noise.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(noise, 'tStopRefresh')  # time at next scr refresh
                    noise.setAutoDraw(False)
            if noise.status == STARTED:
                if noise._needBuild:
                    noise.buildNoise()
                else:
                    if NoiseTy == 'DY': #We only want to update the noise on dynamic trials
                        if frameN >= NoiseStartFrame and frameN < BackFin:
                            if (frameN-noise.frameNStart) % 1 == 0: #update the noise every frame
                                noise.updateNoise()
            
            # *TopSQ* updates
            if TopSQ.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                TopSQ.frameNStart = frameN  # exact frame index
                TopSQ.tStart = t  # local t and not account for scr refresh
                TopSQ.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TopSQ, 'tStartRefresh')  # time at next scr refresh
                TopSQ.setAutoDraw(True)
            if TopSQ.status == STARTED:
                if frameN >= (TopSQ.frameNStart + SqDur):
                    # keep track of stop time/frame for later
                    TopSQ.tStop = t  # not accounting for scr refresh
                    TopSQ.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(TopSQ, 'tStopRefresh')  # time at next scr refresh
                    TopSQ.setAutoDraw(False)
            if TopSQ.status == STARTED:  # only update if drawing
                TopSQ.setPos((TopX, topSqY), log=False)
            
            # *BotSQ* updates
            if BotSQ.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                BotSQ.frameNStart = frameN  # exact frame index
                BotSQ.tStart = t  # local t and not account for scr refresh
                BotSQ.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BotSQ, 'tStartRefresh')  # time at next scr refresh
                BotSQ.setAutoDraw(True)
            if BotSQ.status == STARTED:
                if frameN >= (BotSQ.frameNStart + SqDur):
                    # keep track of stop time/frame for later
                    BotSQ.tStop = t  # not accounting for scr refresh
                    BotSQ.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(BotSQ, 'tStopRefresh')  # time at next scr refresh
                    BotSQ.setAutoDraw(False)
            if BotSQ.status == STARTED:  # only update if drawing
                BotSQ.setPos((BotX, botSqY), log=False)
            
            # *Resp* updates
            waitOnFlip = False
            if Resp.status == NOT_STARTED and frameN > (BackFin): #Give the monitor time to swap to grey screen before response
                # keep track of start time/frame for later
                Resp.frameNStart = frameN  # exact frame index
                Resp.tStart = t  # local t and not account for scr refresh
                Resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Resp, 'tStartRefresh')  # time at next scr refresh
                Resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Resp.status == STARTED and not waitOnFlip:
                theseKeys = Resp.getKeys(keyList=['left', 'right'], waitRelease=False)
                _Resp_allKeys.extend(theseKeys)
                if len(_Resp_allKeys):
                    Resp.keys = _Resp_allKeys[-1].name  # just the last key pressed
                    Resp.rt = _Resp_allKeys[-1].rt
                    # was this correct?
                    if (Resp.keys == str(ExpAns)) or (Resp.keys == ExpAns):
                        Resp.corr = 1
                    else:
                        Resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *FixSurround* updates
            if FixSurround.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixSurround.frameNStart = frameN  # exact frame index
                FixSurround.tStart = t  # local t and not account for scr refresh
                FixSurround.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixSurround, 'tStartRefresh')  # time at next scr refresh
                FixSurround.setAutoDraw(True)
            if FixSurround.status == STARTED:
                if frameN >= (FixSurround.frameNStart + BackFin):
                    # keep track of stop time/frame for later
                    FixSurround.tStop = t  # not accounting for scr refresh
                    FixSurround.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FixSurround, 'tStopRefresh')  # time at next scr refresh
                    FixSurround.setAutoDraw(False)
            
            # *FixationPoint* updates
            if FixationPoint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixationPoint.frameNStart = frameN  # exact frame index
                FixationPoint.tStart = t  # local t and not account for scr refresh
                FixationPoint.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixationPoint, 'tStartRefresh')  # time at next scr refresh
                FixationPoint.setAutoDraw(True)
            if FixationPoint.status == STARTED:
                if frameN >= (FixationPoint.frameNStart + BackFin):
                    # keep track of stop time/frame for later
                    FixationPoint.tStop = t  # not accounting for scr refresh
                    FixationPoint.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(FixationPoint, 'tStopRefresh')  # time at next scr refresh
                    FixationPoint.setAutoDraw(False)
            
            #if TopSQ.status==FINISHED: #When the squares stop moving, the screen is no longer refreswhing
            #    win.recordFrameIntervals = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #This stores what indexes were used
        thisExp.addData('IndexHistory', idxhistory)
        
        #Store what x coordinates were used
        thisExp.addData('TopXHist', TopXHist)
        #First 8 trials are practice
        #We only want staircase on the live trials 9+
        
        #A correct response means it was displaced in the direction motion
        
        #Save direction before reversal
        thisExp.addData('Stair1Dir', Stair1Dir)
        thisExp.addData('Stair2Dir', Stair2Dir)
        thisExp.addData('Stair3Dir', Stair3Dir)
        thisExp.addData('Stair4Dir', Stair4Dir)
        thisExp.addData('Stair5Dir', Stair5Dir)
        thisExp.addData('Stair6Dir', Stair6Dir)
        thisExp.addData('Stair7Dir', Stair7Dir)
        thisExp.addData('Stair8Dir', Stair8Dir)
        
        #The practice trial staircases are coded for rtl, we multiply by -1 for LtR
        if StairNoEx == 11:
            if Resp.corr == 1:
                Prac1 += StairStep
            else: #It was going RtL, they saw it more rightwards, so shift left
                Prac1 -= StairStep
        elif StairNoEx == 22:
            if Resp.corr == 1:
                Prac2 += StairStep
            else:
                Prac2 -= StairStep
                
        elif StairNoEx == 1:
            Stair1TC += 1
            if Resp.corr == 1:
                if Stair1Dir == 'up':
                    Stair1Dir = 'down'
                    Stair1RevVals.append(Stair1)
                    Stair1NumRevs += 1
                    RevVal = Stair1
                Stair1 += StairStep
            else:
                if Stair1Dir == 'down':
                    Stair1Dir = 'up'
                    Stair1RevVals.append(Stair1)
                    Stair1NumRevs += 1
                    RevVal = Stair1
                Stair1 -= StairStep
            Stair1 = round(Stair1 * 100000)/ 100000
        elif StairNoEx == 2:
            Stair2TC += 1
            if Resp.corr == 1:
                if Stair2Dir == 'up':
                    Stair2Dir = 'down'
                    Stair2RevVals.append(Stair2)
                    Stair2NumRevs += 1
                    RevVal = Stair2
                Stair2 -= StairStep
            else:
                if Stair2Dir == 'down':
                    Stair2Dir = 'up'
                    Stair2RevVals.append(Stair2)
                    Stair2NumRevs += 1
                    RevVal = Stair2
                Stair2 += StairStep
            Stair2 = round(Stair2 * 100000)/ 100000
        
        elif StairNoEx == 3:
            Stair3TC += 1
            if Resp.corr == 1:
                if Stair3Dir == 'up':
                    Stair3Dir = 'down'
                    Stair3RevVals.append(Stair3)
                    Stair3NumRevs += 1
                    RevVal = Stair3
                Stair3 += StairStep
            else:
                if Stair3Dir == 'down':
                    Stair3Dir = 'up'
                    Stair3RevVals.append(Stair3)
                    Stair3NumRevs += 1
                    RevVal = Stair3
                Stair3 -= StairStep
            Stair3 = round(Stair3 * 100000)/ 100000
        
        elif StairNoEx == 4:
            Stair4TC += 1
            if Resp.corr == 1:
                if Stair4Dir == 'up':
                    Stair4Dir = 'down'
                    Stair4RevVals.append(Stair4)
                    Stair4NumRevs += 1
                    RevVal = Stair4
                Stair4 -= StairStep
            else:
                if Stair4Dir == 'down':
                    Stair4Dir = 'up'
                    Stair4RevVals.append(Stair4)
                    Stair4NumRevs += 1
                    RevVal = Stair4
                Stair4 += StairStep
            Stair4 = round(Stair4 * 100000)/ 100000
        
        elif StairNoEx == 5:
            Stair5TC += 1
            if Resp.corr == 1:
                if Stair5Dir == 'up':
                    Stair5Dir = 'down'
                    Stair5RevVals.append(Stair5)
                    Stair5NumRevs += 1
                    RevVal = Stair5
                Stair5 += StairStep
            else:
                if Stair5Dir == 'down':
                    Stair5Dir = 'up'
                    Stair5RevVals.append(Stair5)
                    Stair5NumRevs += 1
                    RevVal = Stair5
                Stair5 -= StairStep
            Stair5 = round(Stair5 * 100000)/ 100000
        
        elif StairNoEx == 6:
            Stair6TC += 1
            if Resp.corr == 1:
                if Stair6Dir == 'up':
                    Stair6Dir = 'down'
                    Stair6RevVals.append(Stair6)
                    Stair6NumRevs += 1
                    RevVal = Stair6
                Stair6 -= StairStep
            else:
                if Stair6Dir == 'down':
                    Stair6Dir = 'up'
                    Stair6RevVals.append(Stair6)
                    Stair6NumRevs += 1
                    RevVal = Stair6
                Stair6 += StairStep
            Stair6 = round(Stair6 * 100000)/ 100000
        
        elif StairNoEx == 7:
            Stair7TC += 1
            if Resp.corr == 1:
                if Stair7Dir == 'up':
                    Stair7Dir = 'down'
                    Stair7RevVals.append(Stair7)
                    Stair7NumRevs += 1
                    RevVal = Stair7
                Stair7 += StairStep
            else:
                if Stair7Dir == 'down':
                    Stair7Dir = 'up'
                    Stair7RevVals.append(Stair7)
                    Stair7NumRevs += 1
                    RevVal = Stair7
                Stair7 -= StairStep
            Stair7 = round(Stair7 * 100000)/ 100000
        
        elif StairNoEx == 8:
            Stair8TC += 1
            if Resp.corr == 1:
                if Stair8Dir == 'up':
                    Stair8Dir = 'down'
                    Stair8RevVals.append(Stair8)
                    Stair8NumRevs += 1
                    RevVal = Stair8
                Stair8 -= StairStep
            else:
                if Stair8Dir == 'down':
                    Stair8Dir = 'up'
                    Stair8RevVals.append(Stair8)
                    Stair8NumRevs += 1
                    RevVal = Stair8
                Stair8 += StairStep
            Stair8 = round(Stair8 * 100000)/ 100000
        
        #Save staircase parameters
        thisExp.addData('Stair1TC', Stair1TC)
        thisExp.addData('Stair2TC', Stair2TC)
        thisExp.addData('Stair3TC', Stair3TC)
        thisExp.addData('Stair4TC', Stair4TC)
        thisExp.addData('Stair5TC', Stair5TC)
        thisExp.addData('Stair6TC', Stair6TC)
        thisExp.addData('Stair7TC', Stair7TC)
        thisExp.addData('Stair8TC', Stair8TC)
        
        thisExp.addData('Stair1NumRevs', Stair1NumRevs)
        thisExp.addData('Stair2NumRevs', Stair2NumRevs)
        thisExp.addData('Stair3NumRevs', Stair3NumRevs)
        thisExp.addData('Stair4NumRevs', Stair4NumRevs)
        thisExp.addData('Stair5NumRevs', Stair5NumRevs)
        thisExp.addData('Stair6NumRevs', Stair6NumRevs)
        thisExp.addData('Stair7NumRevs', Stair7NumRevs)
        thisExp.addData('Stair8NumRevs', Stair8NumRevs)
        
        thisExp.addData('ReversalValue', RevVal)
        
        trials.addData('noise.started', noise.tStartRefresh)
        trials.addData('noise.stopped', noise.tStopRefresh)
        trials.addData('TopSQ.started', TopSQ.tStartRefresh)
        trials.addData('TopSQ.stopped', TopSQ.tStopRefresh)
        trials.addData('BotSQ.started', BotSQ.tStartRefresh)
        trials.addData('BotSQ.stopped', BotSQ.tStopRefresh)
        # check responses
        if Resp.keys in ['', [], None]:  # No response was made
            Resp.keys = None
            # was no response the correct answer?!
            if str(ExpAns).lower() == 'none':
               Resp.corr = 1;  # correct non-response
            else:
               Resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('Resp.keys',Resp.keys)
        trials.addData('Resp.corr', Resp.corr)
        if Resp.keys != None:  # we had a response
            trials.addData('Resp.rt', Resp.rt)
        trials.addData('Resp.started', Resp.tStartRefresh)
        trials.addData('Resp.stopped', Resp.tStopRefresh)
        trials.addData('FixSurround.started', FixSurround.tStartRefresh)
        trials.addData('FixSurround.stopped', FixSurround.tStopRefresh)
        trials.addData('FixationPoint.started', FixationPoint.tStartRefresh)
        trials.addData('FixationPoint.stopped', FixationPoint.tStopRefresh)
        win.recordFrameIntervals = False #As a fail save, add this here
        thisExp.addData('AutoDroppedFrames', win.nDroppedFrames)
        #thisExp.addData('ManualFramesDropped', FramesDropped)
        
        if win.nDroppedFrames > PastCount:
            DisgardTrial = True
        
        thisExp.addData('DisgardTrial', DisgardTrial)
        
        #Past count of dropped frames
        PastCount = win.nDroppedFrames
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "PracticeTrials"------- UPTO HERE
        continueRoutine = True
        # update component parameters for each repeat
        if trialCount != 12:
            continueRoutine = False 
        if PracTrial == False:
            continueRoutine = False 
        else:
            if trialCount == 12:
                trialCount = 0
        
        EndPrac.keys = []
        EndPrac .rt = []
        _EndPrac_allKeys = []
        # keep track of which components have finished
        PracticeTrialsComponents = [EndPrac, text]
        for thisComponent in PracticeTrialsComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracticeTrialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "PracticeTrials"-------
        while continueRoutine:
            # get current time
            t = PracticeTrialsClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracticeTrialsClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *EndPrac* updates
            waitOnFlip = False
            if EndPrac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                EndPrac.frameNStart = frameN  # exact frame index
                EndPrac.tStart = t  # local t and not account for scr refresh
                EndPrac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(EndPrac, 'tStartRefresh')  # time at next scr refresh
                EndPrac.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(EndPrac.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(EndPrac.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if EndPrac.status == STARTED and not waitOnFlip:
                theseKeys = EndPrac.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
                _EndPrac_allKeys.extend(theseKeys)
                if len(_EndPrac_allKeys):
                    EndPrac.keys = _EndPrac_allKeys[-1].name  # just the last key pressed
                    EndPrac.rt = _EndPrac_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracticeTrialsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracticeTrials"-------
        for thisComponent in PracticeTrialsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if EndPrac.keys in ['', [], None]:  # No response was made
            EndPrac.keys = None
        trials.addData('EndPrac.keys',EndPrac.keys)
        if EndPrac.keys != None:  # we had a response
            trials.addData('EndPrac.rt', EndPrac.rt)
        trials.addData('EndPrac.started', EndPrac.tStartRefresh)
        trials.addData('EndPrac.stopped', EndPrac.tStopRefresh)
        trials.addData('text.started', text.tStartRefresh)
        trials.addData('text.stopped', text.tStopRefresh)
        # the Routine "PracticeTrials" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "ISICheck"-------
        continueRoutine = True
        #routineTimer.add(4.000000) - > We want participants to have unlimited time to respond to the attention check
        # update component parameters for each repeat
        ATT_RESP.keys = []
        ATT_RESP.rt = []
        _ATT_RESP_allKeys = []
        ListIdx = 0
        
        #ATT_IDX = 0; we can get away with using frameN in the attention check
        
        PassCheck = False
        
        ## TROUBLESHOOTING ATTCHECK PURPOSES
        #TROUBLE_ATT_IDX +=1
        #trialCount = CheckList[TROUBLE_ATT_IDX]
                
        if trialCount not in CheckList:
             continueRoutine = False
             AttentionCheck = False
             FixCol = myBlack
        
        else:
             AttentionCheck = True
             PassCheck = False #Set it default false, has to be changed to true
             shuffle(ColourList) #Make the RGB random
             thisExp.addData('AttentionCheck', AttentionCheck)
        
        ## DRAW THE COMPONENTS
        if AttentionCheck:
            noise.buildNoise()
        # keep track of which components have finished
        ISICheckComponents = [ATT_RESP, ISI_2]
        for thisComponent in ISICheckComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISICheckClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISICheck"-------
        while continueRoutine: #and routineTimer.getTime() > 0:
            # get current time
            t = ISICheckClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISICheckClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            #print("The t is: " + str(t) + " and the frameN is " + str(frameN))
            
            # *ATT_RESP* updates
            waitOnFlip = False
            ## Don't allow for ta response till the movement stops
            if ATT_RESP.status == NOT_STARTED and frameN >= BackFin:
                # keep track of start time/frame for later
                ATT_RESP.frameNStart = frameN  # exact frame index
                ATT_RESP.tStart = t  # local t and not account for scr refresh
                ATT_RESP.tStartRefresh = tThisFlipGlobal  # on global time 
                win.timeOnFlip(ATT_RESP, 'tStartRefresh')  # time at next scr refresh
                ATT_RESP.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ATT_RESP.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ATT_RESP.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ATT_RESP.status == STARTED and not waitOnFlip:
                theseKeys = ATT_RESP.getKeys(keyList=['r', 'left', 'right', 's'], waitRelease=False)
                _ATT_RESP_allKeys.extend(theseKeys)
                if len(_ATT_RESP_allKeys):
                    ATT_RESP.keys = _ATT_RESP_allKeys[-1].name  # just the last key pressed
                    ATT_RESP.rt = _ATT_RESP_allKeys[-1].rt
                    # was this correct?
                    if (ATT_RESP.keys == str(CorrAns)) or (ATT_RESP.keys == CorrAns):
                        ATT_RESP.corr = 1
                    else:
                        ATT_RESP.corr = 0
                    # a response ends the routine; use win.flip() to purge the screen, set all the autodraws to false so they stop being naughty and drawing
                    continueRoutine = False
                    
            if AttentionCheck == True:
                if t >= 1 and frameN < (RefreshHz): #exclude isi, but only do the colour change for one second( a single refresh Hz). The isi is also another second (1 refreshHz) w
                    if frameN % UpdateOn == 0: #Only update every 133ms
                        FixCol = ColourList[ListIdx]
                        ListIdx += 1
                        if ListIdx == (len(ColourList) - 1):
                            ListIdx = 0 #Reset index when it hits max list
                else:
                    FixCol = (-1, -1, -1) #Set fixation point to a default black 
                    
                FixationPoint.setColor(FixCol)
                    
                if frameN < (BackFin): #We just want these displayed for their normal duration
                    noise.autoDraw = True
                    FixSurround.autoDraw = True
                    FixationPoint.autoDraw = True
                    
                    if (frameN) < (SqDur) and t > 1:
                        TopSQ.autoDraw = True
                        BotSQ.autoDraw = True
                                        
                        
                        # Using frameN as the index, should ensure thta incase frameN doesn't incrementally perfectly sequentially, it still finishes in alignment
                        if TopDir == 'RtL':
                            TopX = RtLCoordinates[frameN]
                        else:
                            TopX = LtRCoordinates[frameN]
                        BotX = TopX * -1 
                        TopSQ.pos = (TopX, topSqY)
                        BotSQ.pos = (BotX, botSqY)
                    
                    else:
                        TopSQ.autoDraw = False
                        BotSQ.autoDraw = False
                    
                else:
                    FixSurround.autoDraw = False
                    FixationPoint.autoDraw = False
                    noise.autoDraw = False
                        
                if ATT_RESP.corr == 1:
                    PassCheck = True
            # *ISI_2* period
            if ISI_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ISI_2.frameNStart = frameN  # exact frame index
                ISI_2.tStart = t  # local t and not account for scr refresh
                ISI_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ISI_2, 'tStartRefresh')  # time at next scr refresh
                ISI_2.start(1.0)
            elif ISI_2.status == STARTED:  # one frame should pass before updating params and completing
                ISI_2.complete()  # finish the static period
                ISI_2.tStop = ISI_2.tStart + 1.0  # record stop time
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISICheckComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISICheck"-------
        for thisComponent in ISICheckComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if ATT_RESP.keys in ['', [], None]:  # No response was made
            ATT_RESP.keys = None
            # was no response the correct answer?!
            if str(CorrAns).lower() == 'none':
               ATT_RESP.corr = 1;  # correct non-response
            else:
               ATT_RESP.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('ATT_RESP.keys',ATT_RESP.keys)
        trials.addData('ATT_RESP.corr', ATT_RESP.corr)
        if ATT_RESP.keys != None:  # we had a response
            trials.addData('ATT_RESP.rt', ATT_RESP.rt)
        trials.addData('ATT_RESP.started', ATT_RESP.tStartRefresh)
        trials.addData('ATT_RESP.stopped', ATT_RESP.tStopRefresh)
        FixationPoint.setLineColor(FixCol)
        FixationPoint.setFillColor(FixCol)
        
        thisExp.addData('PassCheck', PassCheck)
        
        if AttentionCheck == True:
            if PassCheck == False:
                NumFails += 1
        
        if NumFails >= 2:
            FailedCheck = True
        
        thisExp.addData('NumFails', NumFails)
        thisExp.addData('FailedCheck', FailedCheck)
        trials.addData('ISI_2.started', ISI_2.tStart)
        trials.addData('ISI_2.stopped', ISI_2.tStop)
        
        # the Routine "ISICheck" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        
        # ------Prepare to start Routine "warningDisplay"-------
        continueRoutine = True
        # update component parameters for each repeat
        if trialCount not in CheckList or PassCheck == True:
            continueRoutine = False
            AttentionCheck = False
            FixCol = myBlack
        warningText.setText(ExtraText + '\n' + '\n' + 'Just a friendly reminder to please stare at the dot in the center of the screen during the experiment.' + '\n' + '\n' + "Press 's' to resume the experiment. ")
        ContinueExp.keys = []
        ContinueExp.rt = []
        _ContinueExp_allKeys = []
        # keep track of which components have finished
        warningDisplayComponents = [warningText, ContinueExp]
        for thisComponent in warningDisplayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        warningDisplayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "warningDisplay"-------
        while continueRoutine:
            # get current time
            t = warningDisplayClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=warningDisplayClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *warningText* updates
            if warningText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                warningText.frameNStart = frameN  # exact frame index
                warningText.tStart = t  # local t and not account for scr refresh
                warningText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(warningText, 'tStartRefresh')  # time at next scr refresh
                warningText.setAutoDraw(True)
            
            # *ContinueExp* updates
            waitOnFlip = False
            if ContinueExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                ContinueExp.frameNStart = frameN  # exact frame index
                ContinueExp.tStart = t  # local t and not account for scr refresh
                ContinueExp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ContinueExp, 'tStartRefresh')  # time at next scr refresh
                ContinueExp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(ContinueExp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(ContinueExp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if ContinueExp.status == STARTED and not waitOnFlip:
                theseKeys = ContinueExp.getKeys(keyList=['p', 's'], waitRelease=False)
                _ContinueExp_allKeys.extend(theseKeys)
                if len(_ContinueExp_allKeys):
                    ContinueExp.keys = _ContinueExp_allKeys[-1].name  # just the last key pressed
                    ContinueExp.rt = _ContinueExp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in warningDisplayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "warningDisplay"-------
        for thisComponent in warningDisplayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('warningText.started', warningText.tStartRefresh)
        trials.addData('warningText.stopped', warningText.tStopRefresh)
        # check responses
        if ContinueExp.keys in ['', [], None]:  # No response was made
            ContinueExp.keys = None
        trials.addData('ContinueExp.keys',ContinueExp.keys)
        if ContinueExp.keys != None:  # we had a response
            trials.addData('ContinueExp.rt', ContinueExp.rt)
        trials.addData('ContinueExp.started', ContinueExp.tStartRefresh)
        trials.addData('ContinueExp.stopped', ContinueExp.tStopRefresh)
        # the Routine "warningDisplay" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "BreakTime"-------
        continueRoutine = True
        # update component parameters for each repeat
        #Total trials 320, break halfway
        if trialCount != 160:
            continueRoutine = False
        BreakResp.keys = []
        BreakResp.rt = []
        _BreakResp_allKeys = []
        # keep track of which components have finished
        BreakTimeComponents = [BreakText, BreakResp]
        for thisComponent in BreakTimeComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BreakTimeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "BreakTime"-------
        while continueRoutine:
            # get current time
            t = BreakTimeClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BreakTimeClock)
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
                theseKeys = BreakResp.getKeys(keyList=['space', 'l'], waitRelease=False)
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
            for thisComponent in BreakTimeComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BreakTime"-------
        for thisComponent in BreakTimeComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('BreakText.started', BreakText.tStartRefresh)
        trials.addData('BreakText.stopped', BreakText.tStopRefresh)
        # check responses
        if BreakResp.keys in ['', [], None]:  # No response was made
            BreakResp.keys = None
        trials.addData('BreakResp.keys',BreakResp.keys)
        if BreakResp.keys != None:  # we had a response
            trials.addData('BreakResp.rt', BreakResp.rt)
        trials.addData('BreakResp.started', BreakResp.tStartRefresh)
        trials.addData('BreakResp.stopped', BreakResp.tStopRefresh)
        # the Routine "BreakTime" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed NumReps repeats of 'trials'
    
    # get names of stimulus parameters
    if trials.trialList in ([], [None], None):
        params = []
    else:
        params = trials.trialList[0].keys()
    # save data for this loop
    trials.saveAsText(filename + 'trials.csv', delim=',',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'SelectCondFile'

# get names of stimulus parameters
if SelectCondFile.trialList in ([], [None], None):
    params = []
else:
    params = SelectCondFile.trialList[0].keys()
# save data for this loop
SelectCondFile.saveAsText(filename + 'SelectCondFile.csv', delim=',',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
thisExp.addData("globalClockTime", globalClock.getTime()) 

txtmsg = "Thank you for completing this experiment." + "\n" + " Press tell the experimenter you have completed the experiment."


key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
#Calculate threshold
NumRevs = 6 #Number of reversals to average over for threshold

#Save the reversal vlaues before you average
thisExp.addData('Stair1RevVals', Stair1RevVals)
thisExp.addData('Stair2RevVals', Stair2RevVals)
thisExp.addData('Stair3RevVals', Stair3RevVals)
thisExp.addData('Stair4RevVals', Stair4RevVals)
thisExp.addData('Stair5RevVals', Stair5RevVals)
thisExp.addData('Stair6RevVals', Stair6RevVals)
thisExp.addData('Stair7RevVals', Stair7RevVals)
thisExp.addData('Stair8RevVals', Stair8RevVals)

ST1Thresh = average(Stair1RevVals[-NumRevs:])
ST2Thresh = average(Stair2RevVals[-NumRevs:])
ST3Thresh = average(Stair3RevVals[-NumRevs:])
ST4Thresh = average(Stair4RevVals[-NumRevs:])
ST5Thresh = average(Stair5RevVals[-NumRevs:])
ST6Thresh = average(Stair6RevVals[-NumRevs:])
ST7Thresh = average(Stair7RevVals[-NumRevs:])
ST8Thresh = average(Stair8RevVals[-NumRevs:])

#Save the threshold
thisExp.addData('ST1Thresh', ST1Thresh)
thisExp.addData('ST2Thresh', ST2Thresh)
thisExp.addData('ST3Thresh', ST3Thresh)
thisExp.addData('ST4Thresh', ST4Thresh)
thisExp.addData('ST5Thresh', ST5Thresh)
thisExp.addData('ST6Thresh', ST6Thresh)
thisExp.addData('ST7Thresh', ST7Thresh)
thisExp.addData('ST8Thresh', ST8Thresh)

#Check length of the list of reversal vlaues matches how many reversals occurred
#Should be 1 if fine
if Stair1NumRevs != len(Stair1RevVals):
    ST1RevCheck = 0
if Stair2NumRevs != len(Stair2RevVals):
    ST2RevCheck = 0
if Stair3NumRevs != len(Stair3RevVals):
    ST3RevCheck = 0
if Stair4NumRevs != len(Stair4RevVals):
    ST4RevCheck = 0
if Stair5NumRevs != len(Stair5RevVals):
    ST5RevCheck = 0
if Stair6NumRevs != len(Stair6RevVals):
    ST6RevCheck = 0
if Stair7NumRevs != len(Stair7RevVals):
    ST7RevCheck = 0
if Stair8NumRevs != len(Stair8RevVals):
    ST8RevCheck = 0    
    
thisExp.addData('ST1RevCheck', ST1RevCheck)
thisExp.addData('ST2RevCheck', ST2RevCheck)
thisExp.addData('ST3RevCheck', ST3RevCheck)
thisExp.addData('ST4RevCheck', ST4RevCheck)
thisExp.addData('ST5RevCheck', ST5RevCheck)
thisExp.addData('ST6RevCheck', ST6RevCheck)
thisExp.addData('ST7RevCheck', ST7RevCheck)
thisExp.addData('ST8RevCheck', ST8RevCheck)
## Save the DVA units as pixels

##Plot intervals and save in text file
import matplotlib.pyplot as plt

FILE_NAME_TEXT=('Intervals\Text\TG_' + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + "_FrameIntervals"  + '.log')
FILE_NAME_PNG = ('Intervals\Images\TG_' + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + "_FrameIntervals" + '.png')

# keep track of which components have finished
EndComponents = [goodbye, key_resp]
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
    
    # *goodbye* updates
    if goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        goodbye.frameNStart = frameN  # exact frame index
        goodbye.tStart = t  # local t and not account for scr refresh
        goodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(goodbye, 'tStartRefresh')  # time at next scr refresh
        goodbye.setAutoDraw(True)
    if goodbye.status == STARTED:  # only update if drawing
        goodbye.setText(txtmsg, log=False)
    
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
thisExp.addData('goodbye.started', goodbye.tStartRefresh)
thisExp.addData('goodbye.stopped', goodbye.tStopRefresh)
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
Pix_Fix_surround = tools.monitorunittools.deg2pix(1.1, win.monitor)
Pix_Fix_Circ = tools.monitorunittools.deg2pix(0.5, win.monitor)


## Add pixels to datafile
thisExp.addData('Pix_Fix_surround', Pix_Fix_surround)
thisExp.addData('Pix_Fix_Circ', Pix_Fix_Circ)

#Already converted:
#tools.monitorunittools.deg2pix(degrees, monitor[, correctFlat])
thisExp.addData('SqSizeW', SqSizeW) 
thisExp.addData('SqSizeH', SqSizeH)

#Y coordinates of the top square
thisExp.addData('topSqY', topSqY)
thisExp.addData('botSqY', botSqY)
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
    titleMsg = "Dropped/Frames = %i%i = %.3f%%"
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
