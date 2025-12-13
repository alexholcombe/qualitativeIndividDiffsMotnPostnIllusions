#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on January 23, 2022, at 15:14
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
    # Changed to 144hz
    #Final check 11/03
    # 22/04 - Commented out some lingering print statements. Did this after, there is just no need to print htis information. 


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


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'FLE_PY'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Timot\\Documents\\2021\\Study 1\\September_Final_EXPERIMENTS_LIVE_Python\\Python-Experiments\\FLE\\Dec_FlashLag.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
if int(expInfo['test']) == 1: #if test == 1, that means we are testing and need mor einfo
    logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
else:
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)

logging.console.setLevel(logging.WARNING)  # this tells the console to output to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='ASUS_PG248Q', waitBlanking = False, color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
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
Instr_Txt = visual.TextStim(win=win, name='Instr_Txt',
    text='During this experiment a long white line in the center of the screen is going to be rotating clockwise or counterclockwise. At a random point in time, a second white line will be presented on the outside of the center moving white line. \n\nThis second outside white line will appear to be either ahead of or behind the center white line. Your task is to report  which line is ahead. If the outside white line is ahead of the center white line, press "o". If the inside white line is ahead of the outside white line, press "i". \n\nThroughout the experiment there will be a red dot in the centre of the screen. Please stare at this red dot during the experiment.\n\nThe first eight trials are practice trials and will allow you to familarise yourself with the task. Press the \'s\' key when you are ready to begin.',
    font='Arial',
    units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
BeginExp = keyboard.Keyboard()
#MOVE THIS CODE

RefreshHz = 144 #200 #win.getActualFrameRate()
Frame_Dur = 1000/RefreshHz #Frame duration in ms

#Get the size of screen in height (y)
ScreenHeight = win.size[1]

if int(expInfo['test']) == 0: #1 = true, it's a test; 0 = false, not a test (LIVE TRIALS)
    if FrameRate <140 or FrameRate > 148 or RefreshHz != 144: #Give a 4 frame buffer 
        print('WARNING! ERROR WITH FRAMERATE OR REFRESHHZ. Psychopy detected the FrameRate at: ' +str(FrameRate) + 'RefreshHz was: ' + str(RefreshHz))
        core.quit()


## Check if the file already exists
import os.path
FixSize = 11

# Initialize components for Routine "Interstiminterval"
InterstimintervalClock = core.Clock()
Fixboi = visual.ShapeStim(
    win=win, name='Fixboi', vertices=99,units='pix', 
    size=(FixSize, FixSize),
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,-1,-1], fillColor=[1,-1,-1],
    opacity=1, depth=0.0, interpolate=True)

### SPECIFY HOW MANY REPETIONS FOR THE TRIAL LOOP:
'''
if int(expInfo['test']) == 1:
    TrialReps = 1
else:
    TrialReps = NumReps 
'''

# Initialize components for Routine "trial"
trialClock = core.Clock()
## Manually set the parameters

Speed = 180 #How many degrees per second the target rotates
OriStep = Speed/RefreshHz #How much the orientation changes each frames
postFlash = np.round(250/(Frame_Dur))  #Duration in frames of target's movement after the flash's presentation; ~250ms, will be 249.84 at 144hz; 45 degrees of rotation

oriTravelled = 0 #Keeps track of how much orientation is travelled
frameCount = 0 #Counts how many frames post flash
targOri = 0

TargDur = 90 # Placeholder value, Will be overidden in FlashPos code

trialCount = 0

#TargDurPreFlash
#Rotation to cover preflash
OritoTravel = [180, 225, 270, 315]
OriPreFlash = 0

TargEndFrame = 0

TargRad = 135 #Targ Radius in pixels. This is half the size of the rod
TargX = 0
TargY = 0
#Orientation steps in 3
StairSteps =  [4, 2] #, 1]
PracStep = 2 

#RevVal, change stairstep value with this many reversals
RevVal = 3 #3 reversals

#Correct Answer is always 'o'; was the flash ahead, o means yes
#If resp.corr (i.e, outer is ahead) shift flash inwards. Else, the flash must be perceived behind, hence shift outwards
CorrAns = 'o'

#Reversal Occurred?
ReversalOccur = False

''' Staircases, you want an ahead and behind staircase for clockwise and counterclockwise
Aheads are odd numbers (1,3); Behinds are even (2, 4)

Ahead means displaced in direction of motion
Behind, displaced direction opposite motion

FYI: Clockwise is negative; Counterclockwise is positive

            Clockwise
Stair1 = Ahead
Stair2 = Behind

            CounterClockwise
Stair3 = Ahead
Stair4 = Behind

#Staircase direction:
#down means you are moving flash in the direction opposite motion (behind target)
#Up means you are moving flash ahead of the target
'''

#Offset Amount, amount the ahead and behind offset
OffSetAmount = 28

## Stair 1
Stair1 = OffSetAmount #Degrees position of flash
ST1Step = 0 #Idx of the stairstep value from StairSteps
ST1RevCount = 0 #How many reversals?
ST1TC = 0 #Trial counter
ST1Dir = 'Down'
ST1Reversals = []#Store reversal values in here

##Stair 2
Stair2 = -OffSetAmount
ST2Step = 0 #Idx of the stairstep value from StairSteps
ST2RevCount = 0 #How many reversals?
ST2TC = 0 #Trial counter
ST2Dir = 'Up'
ST2Reversals = []#Store reversal values in here

## Stair 3
Stair3 = -OffSetAmount
ST3Step = 0 #Idx of the stairstep value from StairSteps
ST3RevCount = 0 #How many reversals?
ST3TC = 0 #Trial counter
ST3Dir = 'Down'
ST3Reversals = []#Store reversal values in here

## Stair 4
Stair4 = OffSetAmount
ST4Step = 0 #Idx of the stairstep value from StairSteps
ST4RevCount = 0 #How many reversals?
ST4TC = 0 #Trial counter
ST4Dir = 'Up'
ST4Reversals = []#Store reversal values in here

off = 110 #Separation between target and flash in pixels

flashoff = 0 #Orientation to Offset ahead or behind

#Stairapply, is whether to apply practice or live stair variable
stairApply = 0

# Flash Duration; at 60hz was 3 frames (50ms)
#FlashDur = int(np.ceil(3 * (RefreshHz/60)))
#50ms Flash duration

'''
if RefreshHz == 200:
    FlashDur = 10
elif RefreshHz = 144:
    FlashDur = 7
else:
    FlashDur = np.round(50/(1000/RefreshHz)) #60hz
'''
FlashDur = 7 #50ms at 144hz

##Attention check variables
CheckCond = False #Was this an attention check, not pulling from datafile
PassCheck = 'NA'
Check_Counter = 0
Failed_Att = False

Att_Offset = OffSetAmount #The offset for the attention check needs to be so blatantly obvious
Flash = visual.Line(
    win=win, name='Flash',units='pix', 
    start=(-(160, 160)[0]/2.0, 0), end=(+(160, 160)[0]/2.0, 0),
    ori=1.0, pos=[0,0],
    lineWidth=6,     colorSpace='rgb',  lineColor=[1.000, 1.000,1.000], fillColor=[1.000, 1.000,1.000],
    opacity=1, depth=-3.0, interpolate=True)
Targ = visual.Line(
    win=win, name='Targ',units='pix', 
    start=(-(270, 270)[0]/2.0, 0), end=(+(270, 270)[0]/2.0, 0),
    ori=targOri, pos=(TargX, TargY),
    lineWidth=6,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=-4.0, interpolate=True)
FixP = visual.ShapeStim(
    win=win, name='FixP', vertices=99,units='pix', 
    size=(FixSize, FixSize),
    ori=0, pos=(0, 0),
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,-1,-1], fillColor=[1,-1,-1],
    opacity=1, depth=-5.0, interpolate=True)
resp = keyboard.Keyboard()

# Initialize components for Routine "PracDisplay"
PracDisplayClock = core.Clock()
endedExp = False #Did they end the experiment early

EndText = "Press 'space' to continue."

AhExp = '. Because, the outside line was ahead of the inside line'
BehExp = '. Because, the inside line was ahead of the outside line' 
SelExp = 'a'
PracticeTrialText = visual.TextStim(win=win, name='PracticeTrialText',
    text='',
    font='Arial',
    units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
pracResp = keyboard.Keyboard()

# Initialize components for Routine "BREAKTIME"
BREAKTIMEClock = core.Clock()
BreakText = visual.TextStim(win=win, name='BreakText',
    text="This is a break. Please take as long as you need before resuming the experiment.\n\nPress 'space' or 'r'  to resume. ",
    font='Open Sans',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
BREAKRESP = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
Goodbye = visual.TextStim(win=win, name='Goodbye',
    text='Thank you for completing this Experiment. \n\nPlease tell the researcher you have completed this experiment.',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
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
BeginExp.keys = []
BeginExp.rt = []
_BeginExp_allKeys = []
if os.path.exists(filename + '.csv'):
    print('Warning: Datafile already exists!')
    core.quit()


win.mouseVisible = False
# keep track of which components have finished
InstructionsComponents = [Instr_Txt, BeginExp]
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
    
    # *Instr_Txt* updates
    if Instr_Txt.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instr_Txt.frameNStart = frameN  # exact frame index
        Instr_Txt.tStart = t  # local t and not account for scr refresh
        Instr_Txt.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instr_Txt, 'tStartRefresh')  # time at next scr refresh
        Instr_Txt.setAutoDraw(True)
    
    # *BeginExp* updates
    waitOnFlip = False
    if BeginExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BeginExp.frameNStart = frameN  # exact frame index
        BeginExp.tStart = t  # local t and not account for scr refresh
        BeginExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BeginExp, 'tStartRefresh')  # time at next scr refresh
        BeginExp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(BeginExp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(BeginExp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if BeginExp.status == STARTED and not waitOnFlip:
        theseKeys = BeginExp.getKeys(keyList=['s', 'u'], waitRelease=False)
        _BeginExp_allKeys.extend(theseKeys)
        if len(_BeginExp_allKeys):
            BeginExp.keys = _BeginExp_allKeys[-1].name  # just the last key pressed
            BeginExp.rt = _BeginExp_allKeys[-1].rt
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
thisExp.addData('Instr_Txt.started', Instr_Txt.tStartRefresh)
thisExp.addData('Instr_Txt.stopped', Instr_Txt.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
SelectCondFile = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('SelectConditionFile.xlsx'),
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
    trialLoop = data.TrialHandler(nReps=NumReps, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(CondFile),
        seed=None, name='trialLoop')
    thisExp.addLoop(trialLoop)  # add the loop to the experiment
    thisTrialLoop = trialLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
    if thisTrialLoop != None:
        for paramName in thisTrialLoop:
            exec('{} = thisTrialLoop[paramName]'.format(paramName))
    
    for thisTrialLoop in trialLoop:
        currentLoop = trialLoop
        # abbreviate parameter names if possible (e.g. rgb = thisTrialLoop.rgb)
        if thisTrialLoop != None:
            for paramName in thisTrialLoop:
                exec('{} = thisTrialLoop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Interstiminterval"-------
        continueRoutine = True
        routineTimer.add(0.500000)
        # update component parameters for each repeat
        # keep track of which components have finished
        InterstimintervalComponents = [Fixboi]
        for thisComponent in InterstimintervalComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        InterstimintervalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Interstiminterval"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = InterstimintervalClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=InterstimintervalClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Fixboi* updates
            if Fixboi.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Fixboi.frameNStart = frameN  # exact frame index
                Fixboi.tStart = t  # local t and not account for scr refresh
                Fixboi.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Fixboi, 'tStartRefresh')  # time at next scr refresh
                Fixboi.setAutoDraw(True)
            if Fixboi.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Fixboi.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    Fixboi.tStop = t  # not accounting for scr refresh
                    Fixboi.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Fixboi, 'tStopRefresh')  # time at next scr refresh
                    Fixboi.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in InterstimintervalComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Interstiminterval"-------
        for thisComponent in InterstimintervalComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trialLoop.addData('Fixboi.started', Fixboi.tStartRefresh)
        trialLoop.addData('Fixboi.stopped', Fixboi.tStopRefresh)
        
        # ------Prepare to start Routine "trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        #CW is +; CCW is -
        shuffle(OritoTravel) #randomise how much orientation will occur preflash
        OriPreFlash = OritoTravel[-1] #the orientation to travel before the flash
        thisExp.addData('OritoTravelPreFlash', OriPreFlash)
        
        #FlashFrame, frame flash occurs on; fyi first frame is 0 in python
        FlashFrame = (int(OriPreFlash/OriStep) - 1)
        #print('FlashFrame', FlashFrame)
        
        #We want it the target to continue after the flash for ~250ms(15 frames at 60hz) 
        TargEndFrame = FlashFrame + postFlash #This is the targets duration in frames
        #print('TargEndFrame', TargEndFrame)
        
        if TargDir == 'CCW':
            targOri = FlashonOri + OriPreFlash
        elif TargDir == 'CW':
            targOri = FlashonOri - OriPreFlash
        
        #Set the position of the target
        Xrad = np.radians(targOri) # ((targOri * np.pi) / 180)
        XCos = np.cos(Xrad)
        XSin = -(np.sin(Xrad))
        
        TargX = (TargRad * XCos)
        TargY = (TargRad * XSin)
        
        #Ensure no lingering after effects
        Targ.ori = (targOri)
        Targ.pos = (TargX, TargY)
        
        oriTravelled = 0
        
        trialCount += 1
        thisExp.addData('trialCount', trialCount)
        
        #print('FlashonOri', FlashonOri) - 22/04, commented out after participant 58
        
        #Reset the staircase values after the practice trials are done
        if trialCount == 9:    
            ## Stair 1
            Stair1 = OffSetAmount #Degrees position of flash
            ST1Step = 0 #Idx of the stairstep value from StairSteps
            ST1RevCount = 0 #How many reversals?
            ST1TC = 0 #Trial counter
            ST1Dir = 'Down'
            ST1Reversals = []#Store reversal values in here
        
            ##Stair 2
            Stair2 = -OffSetAmount
            ST2Step = 0 #Idx of the stairstep value from StairSteps
            ST2RevCount = 0 #How many reversals?
            ST2TC = 0 #Trial counter
            ST2Dir = 'Up'
            ST2Reversals = []#Store reversal values in here
        
            ## Stair 3
            Stair3 = -OffSetAmount
            ST3Step = 0 #Idx of the stairstep value from StairSteps
            ST3RevCount = 0 #How many reversals?
            ST3TC = 0 #Trial counter
            ST3Dir = 'Down'
            ST3Reversals = []#Store reversal values in here
        
            ## Stair 4
            Stair4 = OffSetAmount
            ST4Step = 0 #Idx of the stairstep value from StairSteps
            ST4RevCount = 0 #How many reversals?
            ST4TC = 0 #Trial counter
            ST4Dir = 'Up'
            ST4Reversals = []#Store reversal values in here
        
        Rad = 270 #Target's width (0.5) /2
        #Targ Rad is 135
        
        ##Reset correct answer and whether this is a practice condition
        CorrAns = 'o' 
        CheckCond = False
        PassCheck = 'NA' 
        
        ## Choose staircase
        if StairNum == 1:
            flashoff = Stair1
        elif StairNum == 2:
            flashoff = Stair2
        elif StairNum == 3:
            flashoff = Stair3
        elif StairNum == 4:
            flashoff = Stair4
        ##ATTENTION CHECKS BELOW:
        elif StairNum == 100: #behind
            CheckCond = True
            if TargDir == 'CCW':
                flashoff = Att_Offset
                CorrAns = 'i'
            else: #CW
                flashoff = -Att_Offset
                CorrAns = 'i'
        elif StairNum == 90: #ahead
            CheckCond = True
            if TargDir == 'CCW':
                flashoff = -Att_Offset
                CorrAns = 'o'
            else: #CW
                flashoff = Att_Offset
                CorrAns = 'o'
        thisExp.addData('OffsetFlash', abs(flashoff))
        
        #Flash Coordiantes
        flashori =  FlashonOri + flashoff #FlashonOri + flashoff
        thisExp.addData('OriginalFlashOri', flashori)
        
        #If it is a negative value and going CW, we need to wrap it around
        #Don't need to do it, just neater to look at
        
        if flashori < 0 :
            flashori = flashori + 360
        elif flashori > 360:
            flashori = flashori - 360
        #you don't need to do this, I just like it to be within 0-360
        thisExp.addData('CleanFlashori', flashori)
        
        #Converts degrees to radians
        flashRadians = ((flashori * pi)/180)
        #Math.sin and cos only work on radians
        FlashCos = cos(flashRadians)
        FlashSin = -(sin(flashRadians)) #We do te negative, because negative sin is clockwise with this function, and in psychopy, positive is cockwise
        
        FlashX = ((Rad + off) * FlashCos)
        FlashY = ((Rad + off) * FlashSin)
        #To make sure it updates new pos and ori on first frame
        Flash.pos = (FlashX, FlashY)
        Flash.ori = (flashori)
        
        thisExp.addData('FlashOri', flashori)
        thisExp.addData('FlashX', FlashX)
        thisExp.addData('FlashY', FlashY)
        Flash.setPos((FlashX, FlashY))
        Flash.setOri(flashori)
        resp.keys = []
        resp.rt = []
        _resp_allKeys = []
        win.recordFrameIntervals = True #win.nDroppedFrames stores this. 
        
        #Set a 10% tolerance for dropped frames
        win.refreshThreshold = (1/RefreshHz) * 1.1
        
        DisgardTrial = False
        
        #manual frame drop counter
        #FramesDropped = 0
        # keep track of which components have finished
        trialComponents = [Flash, Targ, FixP, resp]
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
            #Only change ori, when ISI is over. 
            #ISI Duration is 0.5
            if int(expInfo['test']) == 1: #if test mode, log the frame interval for the last frame
                if len(win.frameIntervals):
                    logging.debug('Last Frame Interval: ' + str(win.frameIntervals[-1])) #This will return the last frame interval appended
            
            if frameN <= TargEndFrame: #Only draw when there are changes!!! 
                if TargDir == 'CCW':
                    targOri -= OriStep
                elif TargDir == 'CW':
                    targOri += OriStep 
                FixP.setAutoDraw(False)
                    #Ensure no lingering after effects
                Targ.ori = (targOri)
                FixP.setAutoDraw(True)
                
                ## Set the position of the target
                Xrad = np.radians(targOri) #((targOri * np.pi) / 180)
                XCos = np.cos(Xrad)
                XSin = -(np.sin(Xrad))
                TargX = (TargRad * XCos)
                TargY = (TargRad * XSin)
                Targ.pos = (TargX, TargY)
                #print('Ori: ',(targOri), 'X: ', TargX, 'Y: ', TargY)
            
            ## To just nicely record how much orientation was traversed; sanity check
            if frameN <= FlashFrame:
                oriTravelled += OriStep
            
            # *Flash* updates
            if Flash.status == NOT_STARTED and frameN >= FlashFrame:
                # keep track of start time/frame for later
                Flash.frameNStart = frameN  # exact frame index
                Flash.tStart = t  # local t and not account for scr refresh
                Flash.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Flash, 'tStartRefresh')  # time at next scr refresh
                Flash.setAutoDraw(True)
            if Flash.status == STARTED:
                if frameN >= (Flash.frameNStart + FlashDur):
                    # keep track of stop time/frame for later
                    Flash.tStop = t  # not accounting for scr refresh
                    Flash.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Flash, 'tStopRefresh')  # time at next scr refresh
                    Flash.setAutoDraw(False)
            
            # *Targ* updates
            if Targ.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Targ.frameNStart = frameN  # exact frame index
                Targ.tStart = t  # local t and not account for scr refresh
                Targ.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Targ, 'tStartRefresh')  # time at next scr refresh
                Targ.setAutoDraw(True)
            if Targ.status == STARTED:
                if frameN >= (Targ.frameNStart + TargEndFrame):
                    # keep track of stop time/frame for later
                    Targ.tStop = t  # not accounting for scr refresh
                    Targ.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Targ, 'tStopRefresh')  # time at next scr refresh
                    Targ.setAutoDraw(False)
            
            # *FixP* updates
            if FixP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                FixP.frameNStart = frameN  # exact frame index
                FixP.tStart = t  # local t and not account for scr refresh
                FixP.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(FixP, 'tStartRefresh')  # time at next scr refresh
                FixP.setAutoDraw(True)
            
            # *resp* updates
            waitOnFlip = False
            if resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
                theseKeys = resp.getKeys(keyList=['i', 'o', 'space'], waitRelease=False)
                _resp_allKeys.extend(theseKeys)
                if len(_resp_allKeys):
                    resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                    resp.rt = _resp_allKeys[-1].rt
                    # was this correct?
                    if (resp.keys == str(CorrAns)) or (resp.keys == CorrAns):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            if Targ.status==FINISHED: #Stop recording the intervals when the target stops moving
                win.recordFrameIntervals = False #win.nDroppedFrames store
            
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
        thisExp.addData('oriTravelled', oriTravelled)
        
        KeysPressed = resp.keys
        #print('KeysPressed', KeysPressed) - 22/04, commented out
        #First eight trials are practice
        
        'SAVE STAIRCASE PARAMETERS OF THE CURRENT TRIAL BEFORE CHANGING THEM'
        
        #How much offset was applied
        thisExp.addData('Stair1', Stair1)
        thisExp.addData('Stair2', Stair2)
        thisExp.addData('Stair3', Stair3)
        thisExp.addData('Stair4', Stair4)
        
        #Store the stair direction
        thisExp.addData('ST1Dir', ST1Dir)
        thisExp.addData('ST2Dir', ST2Dir)
        thisExp.addData('ST3Dir', ST3Dir)
        thisExp.addData('ST4Dir', ST4Dir)
        
        #store step values
        thisExp.addData('ST1Step', ST1Step)
        thisExp.addData('ST2Step', ST2Step)
        thisExp.addData('ST3Step', ST3Step)
        thisExp.addData('ST4Step', ST4Step)
        
        #Live staircase
        
        ## CLOCKWISE STAIRS
        #Alter the trialcount of the staircase
        if StairNum == 1:
            ST1TC += 1
            if resp.keys == 'o': #Outer flash is reported ahead
                #Reversal happened
                if ST1Dir == 'Up':
                    ST1Dir = 'Down'
                    ST1RevCount += 1
                    ST1Reversals.append(Stair1)
                    thisExp.addData('ReversalValue', Stair1)
                    #Only after every 3 reversals, do we want to decrease step size
                    if ST1RevCount % RevVal == 0:
                        if ST1Step <(len(StairSteps) -1): # < 1 (len(StairSteps) = 2
                            ST1Step += 1
                Stair1 -= StairSteps[ST1Step]
            
            else: #Flash is reported behind
                if ST1Dir == 'Down':
                    ST1Dir = 'Up'
                    ST1RevCount += 1
                    ST1Reversals.append(Stair1)
                    thisExp.addData('ReversalValue', Stair1)
                    #Only after every 3 reversals, do we want to decrease step size
                    if ST1RevCount % RevVal == 0:
                        if ST1Step <(len(StairSteps) -1):
                            ST1Step += 1
                Stair1 += StairSteps[ST1Step]
        elif StairNum == 2:
            ST2TC += 1
            if resp.keys == 'o': #Outer flash is reported ahead
                #Reversal happened
                if ST2Dir == 'Up':
                    ST2Dir = 'Down'
                    ST2RevCount += 1
                    ST2Reversals.append(Stair2)
                    thisExp.addData('ReversalValue', Stair2)
                    #Only after every 3 reversals, do we want to decrease step size
                    if ST2RevCount  % RevVal == 0:
                        if ST2Step <(len(StairSteps) -1):
                            ST2Step += 1
                Stair2 -= StairSteps[ST2Step]
            else: #outer flash reported behinw
                if ST2Dir == 'Down':
                    ST2Dir = 'Up'
                    ST2RevCount += 1
                    ST2Reversals.append(Stair2)
                    thisExp.addData('ReversalValue', Stair2)
                    #Only after every 3 reversals, do we want to decrease step size
                    if ST2RevCount  % RevVal == 0:
                        if ST2Step <(len(StairSteps) -1):
                            ST2Step += 1
                Stair2 += StairSteps[ST2Step]
        
        ## COUNTERCLOCKWISE 
        elif StairNum == 3:
            ST3TC += 1
            if resp.keys == 'o': #Outer flash is reported ahead
                #Reversal happened
                if ST3Dir == 'Up':
                    ST3Dir = 'Down' # means to move it more behind the target
                    ST3RevCount += 1
                    ST3Reversals.append(Stair3)
                    thisExp.addData('ReversalValue', Stair3)
                    #Only after every 3 reversals, do we want to decrease step size
                    if ST3RevCount  % RevVal == 0:
                        if ST3Step <(len(StairSteps) -1):
                            ST3Step += 1
                Stair3 += StairSteps[ST3Step]
            else: #outer flash behind
                if ST3Dir == 'Down':
                    ST3Dir = 'Up' #shift the flash more infront of the target
                    ST3RevCount += 1
                    ST3Reversals.append(Stair3)
                    thisExp.addData('ReversalValue', Stair3)
                    #Only after every 3 reversals, do we want to decrease step size
                    if ST3RevCount  % RevVal == 0:
                        if ST3Step <(len(StairSteps) -1):
                            ST3Step += 1
                Stair3 -= StairSteps[ST3Step] #moves flash in front of target for CCW
        
        elif StairNum == 4:
            ST4TC += 1
            if resp.keys == 'o': #Outer flash is reported ahead
                #Reversal happened
                if ST4Dir == 'Up':
                    ST4Dir = 'Down'
                    ST4RevCount += 1
                    ST4Reversals.append(Stair4)
                    thisExp.addData('ReversalValue', Stair4)
                    #Only after every 3 reversals, do we want to decrease step size
                    if ST4RevCount % RevVal == 0:
                        if ST4Step <(len(StairSteps) -1):
                            ST4Step += 1
                Stair4 += StairSteps[ST4Step]
            else:
                if ST4Dir == 'Down':
                    ST4Dir = 'Up'
                    ST4RevCount += 1
                    ST4Reversals.append(Stair4)
                    thisExp.addData('ReversalValue', Stair4)
                    #Only after every 3 reversals, do we want to decrease step size
                    if ST4RevCount % RevVal == 0:
                        if ST4Step <(len(StairSteps) -1):
                            ST4Step += 1
                Stair4 -= StairSteps[ST4Step]
        
        #Store trialcount
        thisExp.addData('ST1TC', ST1TC)
        thisExp.addData('ST2TC', ST2TC)
        thisExp.addData('ST3TC', ST3TC)
        thisExp.addData('ST4TC', ST4TC)
        
        ## sSAVE THE NUMBER OF REVERSALS 
        thisExp.addData('ST1RevCount', ST1RevCount)
        thisExp.addData('ST2RevCount', ST2RevCount)
        thisExp.addData('ST3RevCount', ST3RevCount)
        thisExp.addData('ST4RevCount', ST4RevCount)
        
        if CheckCond == True:
            if resp.corr == 1:
                PassCheck = True
            else:
                PassCheck = False
                Check_Counter +=1 
        if Check_Counter >= 4: #Failed 25% of the attention checks
            Failed_Att = True
        
        thisExp.addData('CorrAns', CorrAns)
        thisExp.addData('CheckCond', CheckCond)
        thisExp.addData('PassCheck', PassCheck)
        thisExp.addData('Check_Counter', Check_Counter)
        thisExp.addData('Failed_Att', Failed_Att)
        trialLoop.addData('Flash.started', Flash.tStartRefresh)
        trialLoop.addData('Flash.stopped', Flash.tStopRefresh)
        trialLoop.addData('Targ.started', Targ.tStartRefresh)
        trialLoop.addData('Targ.stopped', Targ.tStopRefresh)
        trialLoop.addData('FixP.started', FixP.tStartRefresh)
        trialLoop.addData('FixP.stopped', FixP.tStopRefresh)
        # check responses
        if resp.keys in ['', [], None]:  # No response was made
            resp.keys = None
            # was no response the correct answer?!
            if str(CorrAns).lower() == 'none':
               resp.corr = 1;  # correct non-response
            else:
               resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trialLoop (TrialHandler)
        trialLoop.addData('resp.keys',resp.keys)
        trialLoop.addData('resp.corr', resp.corr)
        if resp.keys != None:  # we had a response
            trialLoop.addData('resp.rt', resp.rt)
        trialLoop.addData('resp.started', resp.tStartRefresh)
        trialLoop.addData('resp.stopped', resp.tStopRefresh)
        win.recordFrameIntervals = False #win.nDroppedFrames store
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "PracDisplay"-------
        continueRoutine = True
        # update component parameters for each repeat
        #Only want this text to display after the 10th trial
        if trialCount >= 9:
            continueRoutine = False
        if trialCount == 8:
            EndText = "This is the end of the practice trials. Press 'space' to begin the live expeirment"
            
        #provide feedback on the practice trials
        
        if Offset == 'Ahead':
            PracCorr = 'o'
            SelExp = AhExp
        else:
            PracCorr = 'i'
            SelExp = BehExp
        if KeysPressed == PracCorr:
            PracText = "That was correct! " + EndText 
        else:
            PracText = "That was incorrect. Unfortunately, the correct response was: " + PracCorr + SelExp + '\n' + '\n' + EndText
        PracticeTrialText.setText(PracText)
        pracResp.keys = []
        pracResp.rt = []
        _pracResp_allKeys = []
        # keep track of which components have finished
        PracDisplayComponents = [PracticeTrialText, pracResp]
        for thisComponent in PracDisplayComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        PracDisplayClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "PracDisplay"-------
        while continueRoutine:
            # get current time
            t = PracDisplayClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=PracDisplayClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *PracticeTrialText* updates
            if PracticeTrialText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                PracticeTrialText.frameNStart = frameN  # exact frame index
                PracticeTrialText.tStart = t  # local t and not account for scr refresh
                PracticeTrialText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(PracticeTrialText, 'tStartRefresh')  # time at next scr refresh
                PracticeTrialText.setAutoDraw(True)
            
            # *pracResp* updates
            waitOnFlip = False
            if pracResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                pracResp.frameNStart = frameN  # exact frame index
                pracResp.tStart = t  # local t and not account for scr refresh
                pracResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(pracResp, 'tStartRefresh')  # time at next scr refresh
                pracResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(pracResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(pracResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if pracResp.status == STARTED and not waitOnFlip:
                theseKeys = pracResp.getKeys(keyList=['s', 'q', 'space'], waitRelease=False)
                _pracResp_allKeys.extend(theseKeys)
                if len(_pracResp_allKeys):
                    pracResp.keys = _pracResp_allKeys[-1].name  # just the last key pressed
                    pracResp.rt = _pracResp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PracDisplayComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "PracDisplay"-------
        for thisComponent in PracDisplayComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trialLoop.addData('PracticeTrialText.started', PracticeTrialText.tStartRefresh)
        trialLoop.addData('PracticeTrialText.stopped', PracticeTrialText.tStopRefresh)
        # check responses
        if pracResp.keys in ['', [], None]:  # No response was made
            pracResp.keys = None
        trialLoop.addData('pracResp.keys',pracResp.keys)
        if pracResp.keys != None:  # we had a response
            trialLoop.addData('pracResp.rt', pracResp.rt)
        trialLoop.addData('pracResp.started', pracResp.tStartRefresh)
        trialLoop.addData('pracResp.stopped', pracResp.tStopRefresh)
        # the Routine "PracDisplay" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "BREAKTIME"-------
        continueRoutine = True
        # update component parameters for each repeat
        #Break at halfway
        #There are 160 trials, the first 8 trials are practice and we don't include those in the count
        if trialCount != 88:
            continueRoutine = False
        BREAKRESP.keys = []
        BREAKRESP.rt = []
        _BREAKRESP_allKeys = []
        # keep track of which components have finished
        BREAKTIMEComponents = [BreakText, BREAKRESP]
        for thisComponent in BREAKTIMEComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BREAKTIMEClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "BREAKTIME"-------
        while continueRoutine:
            # get current time
            t = BREAKTIMEClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BREAKTIMEClock)
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
            
            # *BREAKRESP* updates
            waitOnFlip = False
            if BREAKRESP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BREAKRESP.frameNStart = frameN  # exact frame index
                BREAKRESP.tStart = t  # local t and not account for scr refresh
                BREAKRESP.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BREAKRESP, 'tStartRefresh')  # time at next scr refresh
                BREAKRESP.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(BREAKRESP.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(BREAKRESP.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if BREAKRESP.status == STARTED and not waitOnFlip:
                theseKeys = BREAKRESP.getKeys(keyList=['r', 'space'], waitRelease=False)
                _BREAKRESP_allKeys.extend(theseKeys)
                if len(_BREAKRESP_allKeys):
                    BREAKRESP.keys = _BREAKRESP_allKeys[-1].name  # just the last key pressed
                    BREAKRESP.rt = _BREAKRESP_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BREAKTIMEComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BREAKTIME"-------
        for thisComponent in BREAKTIMEComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trialLoop.addData('BreakText.started', BreakText.tStartRefresh)
        trialLoop.addData('BreakText.stopped', BreakText.tStopRefresh)
        # check responses
        if BREAKRESP.keys in ['', [], None]:  # No response was made
            BREAKRESP.keys = None
        trialLoop.addData('BREAKRESP.keys',BREAKRESP.keys)
        if BREAKRESP.keys != None:  # we had a response
            trialLoop.addData('BREAKRESP.rt', BREAKRESP.rt)
        trialLoop.addData('BREAKRESP.started', BREAKRESP.tStartRefresh)
        trialLoop.addData('BREAKRESP.stopped', BREAKRESP.tStopRefresh)
        # the Routine "BREAKTIME" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trialLoop'
    
    # get names of stimulus parameters
    if trialLoop.trialList in ([], [None], None):
        params = []
    else:
        params = trialLoop.trialList[0].keys()
    # save data for this loop
    trialLoop.saveAsText(filename + 'trialLoop.csv', delim=',',
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

key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
#Store reversal values
thisExp.addData('ST1Reversals', ST1Reversals)
thisExp.addData('ST2Reversals', ST2Reversals)
thisExp.addData('ST3Reversals', ST3Reversals)
thisExp.addData('ST4Reversals', ST4Reversals)

#calculate the threshold
#How many reversals to calculate over

ThreshOverRev = 6 #Last 6 reversals

ST1Thresh = average(ST1Reversals[-ThreshOverRev:])
ST2Thresh = average(ST2Reversals[-ThreshOverRev:])
ST3Thresh = average(ST3Reversals[-ThreshOverRev:])
ST4Thresh = average(ST4Reversals[-ThreshOverRev:])

thisExp.addData('ST1Thresh', ST1Thresh)
thisExp.addData('ST2Thresh', ST2Thresh)
thisExp.addData('ST3Thresh', ST3Thresh)
thisExp.addData('ST4Thresh', ST4Thresh)
##Plot intervals and save in text file
import matplotlib.pyplot as plt

FILE_NAME_TEXT=('Intervals\Text\FLE_' + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + "_FrameIntervals"  + '.log')
FILE_NAME_PNG = ('Intervals\Images\FLE_' + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + "_FrameIntervals" + '.png')

# keep track of which components have finished
EndComponents = [Goodbye, key_resp]
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
    
    # *Goodbye* updates
    if Goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Goodbye.frameNStart = frameN  # exact frame index
        Goodbye.tStart = t  # local t and not account for scr refresh
        Goodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Goodbye, 'tStartRefresh')  # time at next scr refresh
        Goodbye.setAutoDraw(True)
    
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
        theseKeys = key_resp.getKeys(keyList=['y', 'n', 'space'], waitRelease=False)
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
thisExp.addData('Goodbye.started', Goodbye.tStartRefresh)
thisExp.addData('Goodbye.stopped', Goodbye.tStopRefresh)
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
print('Did the participant fail the attention check?', Failed_Att)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
