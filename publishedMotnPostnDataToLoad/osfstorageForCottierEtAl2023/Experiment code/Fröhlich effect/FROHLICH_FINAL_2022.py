#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on January 23, 2022, at 16:37
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
    #Changed to 144hz
    #attention check changed to finish on red
    #12/03, removed some multi-assignment in the stairs dictionary to avoid errors/issues
        # Additionally,discovered there was a one trial delay in the implementation of the stairstep change after the reversal

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

## STAIRCASE NOTES:

'''STAIRCASE IS BASED ON THAT PROVIDED BY REBECCA HIRST, PSYCHOPY
https://gitlab.pavlovia.org/lpxrh6/interleaved-staircase'''

#One staircase behind, one ahead
#We store a dictionary for each stair in a list
#Stair 1; Behind staircase = 0 (Displaced in direction opposite motion)
#Stair 2; Infront staircase = 1 (displaced in direction of motion)

#Start value will be offset 45 degrees from vertical for both
#Start val needs to be added to 90 degrees for ccw, and subtracted for CW
#Max value will be 60 degrees in the direction opposite motion, so for CCW 60 + 90, and CW 90- 60
#Min value, is 60 degrees in the direction of motion (which is opposite the effect)

#1 up 1 down staircase
#ReversalVals, stores the values at reversal

#StartVal have been defined with addition to CW in mind
#For CCW, *-1. #CW is positive, #CCW is positive

## Staircase parameters

#StepSizes: TheStepVals = [6, 3, 2, 1] #Stepsizes in degree
#startVal: OffsetDeg = 45 #Value to offset by at start; pos = clockwise

stairs = [{'StairNumber':1, 'name': 'behind', 'Direction': 'CW', 'startVal': -45, 'this_ori': 0, 'thisStep': 0, 
'stepSizes': [6, 3, 2, 1],  'nUp':1, 'nDown': 1, 'maxVal': 60, 'minVal': 30, 'currentDirection': 'up', 'reversalVals':[], 'trialCount': 1}, 
{'StairNumber': 2, 'name': 'behind', 'Direction': 'CCW', 'startVal': 45, 'this_ori': 0, 'stepSizes': [6, 3, 2, 1],
'thisStep': 0, 'nUp':1, 'nDown': 1, 'maxVal': 60, 'minVal': 30, 'currentDirection': 'up', 'reversalVals':[], 'trialCount': 1},
{'StairNumber': 3, 'name': 'ahead', 'Direction': 'CW', 'startVal': 45, 'this_ori': 0, 'thisStep': 0, 'stepSizes': [6, 3, 2, 1], 
'nUp':1, 'nDown': 1, 'maxVal': 60, 'minVal': 30, 'currentDirection': 'down', 'reversalVals':[], 'trialCount': 1}, 
{'StairNumber': 4, 'name': 'ahead', 'Direction': 'CCW', 'startVal': -45, 'this_ori': 0, 'thisStep': 0, 'stepSizes': [6, 3, 2, 1], 
'nUp':1, 'nDown': 1, 'maxVal': 60, 'minVal': 30, 'currentDirection': 'down', 'reversalVals':[], 'trialCount': 1}]

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Frohlich'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Timot\\Documents\\2021\\Study 1\\September_Final_EXPERIMENTS_LIVE_Python\\Python-Experiments\\Frohlich_Effect\\Frohlich_PY.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
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
BeginEXP = keyboard.Keyboard()
introtext = visual.TextStim(win=win, name='introtext',
    text='In this experiment you will see a rod move right or left.\n\nWhen the rod first appears, it will be pointing towards the left or right side of your screen. Your task is to report what side of the screen the rod is pointing towards when it first appears. \n\nYou will report the rod\'s starting position using the \'left\' and \'right\' arrow keys. You can report the rod\'s starting position as soon as you see the rod.\n\nAt the centre of this rod is a red dot, please stare at this dot for the duration of the experiment. As an attention check, throughout the experiment this dot will change colour. When it changes colour press \'r\'. \n\nPress "space" when you are ready to begin this experiment.',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0,  #height=0.04
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
RefreshHz = 144 #Device refreshRate 
FrameDur = 1000/RefreshHz #MS per frame (IFI)

if int(expInfo['test']) == 0: #1 = true, it's a test; 0 = false, not a test (LIVE TRIALS)
    if FrameRate <140 or FrameRate > 148 or RefreshHz != 144: #Give a 4 frame buffer 
        print('WARNING! ERROR WITH FRAMERATE OR REFRESHHZ. Psychopy detected the FrameRate at: ' +str(FrameRate) + 'RefreshHz was: ' + str(RefreshHz))
        core.quit()

import os.path
FixSize = 11

# Initialize components for Routine "PreTrialIsi"
PreTrialIsiClock = core.Clock()
FixDotISI = visual.ShapeStim(
    win=win, name='FixDotISI', vertices=99,units='pix', 
    size=(FixSize, FixSize),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=(1.0000, -1.0000, -1.0000), fillColor=(1.0000, -1.0000, -1.0000),
    opacity=None, depth=0.0, interpolate=False)

# Initialize components for Routine "trial"
trialClock = core.Clock()
## STAIRCASE PARAMETERS 
completedStairs = []

#CorrAns is basically, yes, they respond in the direction of motion, offset direction opposite motion
CorrAns = [] #if cw = right; CCW = left
StopReason = 'Has not stopped' #reason the stairs stopped

#Number of trials for each staircase
NumTrials = 40 #50

#as a placeholder so asarray doesn't melt
RodOri = 270

#Average over this many reverals for threshold
avRevs = 4 #6 is too many with 40 trials

storeStair = []

#Overall Trial Count
OverallTrialCount = 0

#Placeholder variables to stop asarray collapsing
Stair1 = 0
Stair2 = 0
Stair3 = 0
Stair4 = 0 #Staircase offset amounts
Stair1TC = 0 
Stair2TC = 0
Stair3TC = 0
Stair4TC = 0 #Staircase trialcounts
ST1Thresh = 0
ST2Thresh = 0
ST3Thresh = 0
ST4Thresh = 0 #Staircase thresholds
ST1RevVals = []
ST2RevVals = []
ST3RevVals = []
ST4RevVals = [] #Store reversal values

##################### ATTENTION CHECK PARAMETERS ####################
#Attention check: To occur randomly after the first twenty trials
NumAttChecks = 0 #How many have actually occurred
AttentionCheck = False #Is an attention check occurring
AttGap = 5 #This is the minimum number of trials between each attention checks
CheckList = [20, 40, 60, 80, 100, 120, 140, 160] #do the first one after twnety trials; 160 total trials

## Initialise colours:
myRed = (1, -1, -1)
myYell = (1.0000, 1.0000, -1.0000)
myGreen = (-1, 1, -1)
myOrange = (1.0000, 0.2941, -1.0000) 
myCyan = (-1.0000, 1.0000, 1.0000)
myMagneta = (1.0000, -1.0000, 1.0000)
myPurple = (0.0039, -1.0000, 0.0039) 
myBlack = (-1, -1, -1)

ColourList = [myYell, myGreen, myRed, myPurple, myMagneta, myCyan, myOrange]
ListIdx = 0 #To select a colour from the list
FixCol = myRed #Default is to keep it red

UpdateOn = 18 #Update colour after how many 125ms
NumFails = 0
FailedAtt = False
PassCheck = True

StartRod = 1 #Display Rod, on att check should be false (0)

SecDur = 0.6 #Seconds duration of movement
RodDur = 87 #np.ceil(SecDur/(1/RefreshHz)) #Should be same as secdur

Speed = 200 #Deg speed of rotation per second
OriStep = Speed/RefreshHz #Ori change per frame (deg per sec/FrameRate); #1 deg/sec for 200hz

RodLength = 330

AttDir_List = ['CW', 'CCW'] #Initialise a list for the directions for an attention check we can shuffle.

#Radius of the circle the rod will traverse
RodRad = RodLength/2 #

TargRod = visual.Line(
    win=win, name='TargRod',
    start=(-(RodLength, RodLength)[0]/2.0, 0), end=(+(RodLength, RodLength)[0]/2.0, 0),
    ori=1.0, pos=(0, 0),
    lineWidth=10.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
FixDot = visual.ShapeStim(
    win=win, name='FixDot', vertices=99,
    size=(FixSize, FixSize),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=False)
resp = keyboard.Keyboard()
#Initialise to stop errors:
LastNumDropped = 0

# Initialize components for Routine "AttCheckWarning"
AttCheckWarningClock = core.Clock()
ExtraText = '' 
WarningResp = keyboard.Keyboard()
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Break"
BreakClock = core.Clock()
Breaktext = visual.TextStim(win=win, name='Breaktext',
    text="This is a break. Please rest for as long as you need.\n\nPress 'space' when you are ready to continue the experiment.",
    font='Open Sans',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EndBreak = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
Goodbye = visual.TextStim(win=win, name='Goodbye',
    text='Thank you for finishing this experiment.\n\nPlease tell the researcher you are finished. ',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EndExp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
BeginEXP.keys = []
BeginEXP.rt = []
_BeginEXP_allKeys = []
win.mouseVisible = False

## Check the file does not already exist

if os.path.exists(filename + '.csv'):
    print('Warning: Datafile already exists!')
    core.quit()

# keep track of which components have finished
InstructionsComponents = [BeginEXP, introtext]
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
    
    # *BeginEXP* updates
    waitOnFlip = False
    if BeginEXP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        BeginEXP.frameNStart = frameN  # exact frame index
        BeginEXP.tStart = t  # local t and not account for scr refresh
        BeginEXP.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(BeginEXP, 'tStartRefresh')  # time at next scr refresh
        BeginEXP.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(BeginEXP.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(BeginEXP.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if BeginEXP.status == STARTED and not waitOnFlip:
        theseKeys = BeginEXP.getKeys(keyList=['u', 'p', 'space'], waitRelease=False)
        _BeginEXP_allKeys.extend(theseKeys)
        if len(_BeginEXP_allKeys):
            BeginEXP.keys = _BeginEXP_allKeys[-1].name  # just the last key pressed
            BeginEXP.rt = _BeginEXP_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *introtext* updates
    if introtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        introtext.frameNStart = frameN  # exact frame index
        introtext.tStart = t  # local t and not account for scr refresh
        introtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(introtext, 'tStartRefresh')  # time at next scr refresh
        introtext.setAutoDraw(True)
    
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
# check responses
if BeginEXP.keys in ['', [], None]:  # No response was made
    BeginEXP.keys = None
thisExp.addData('BeginEXP.keys',BeginEXP.keys)
if BeginEXP.keys != None:  # we had a response
    thisExp.addData('BeginEXP.rt', BeginEXP.rt)
thisExp.addData('BeginEXP.started', BeginEXP.tStartRefresh)
thisExp.addData('BeginEXP.stopped', BeginEXP.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('introtext.started', introtext.tStartRefresh)
thisExp.addData('introtext.stopped', introtext.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=200, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
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
    
    # ------Prepare to start Routine "PreTrialIsi"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    PreTrialIsiComponents = [FixDotISI]
    for thisComponent in PreTrialIsiComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PreTrialIsiClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "PreTrialIsi"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PreTrialIsiClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PreTrialIsiClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *FixDotISI* updates
        if FixDotISI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixDotISI.frameNStart = frameN  # exact frame index
            FixDotISI.tStart = t  # local t and not account for scr refresh
            FixDotISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixDotISI, 'tStartRefresh')  # time at next scr refresh
            FixDotISI.setAutoDraw(True)
        if FixDotISI.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > FixDotISI.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                FixDotISI.tStop = t  # not accounting for scr refresh
                FixDotISI.frameNStop = frameN  # exact frame index
                win.timeOnFlip(FixDotISI, 'tStopRefresh')  # time at next scr refresh
                FixDotISI.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PreTrialIsiComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PreTrialIsi"-------
    for thisComponent in PreTrialIsiComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('FixDotISI.started', FixDotISI.tStartRefresh)
    trials.addData('FixDotISI.stopped', FixDotISI.tStopRefresh)
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    ## Increase the overall trial counter
    OverallTrialCount += 1
    thisExp.addData('trialCount', OverallTrialCount)
    
    ## Attention check
    if OverallTrialCount in CheckList:
        AttentionCheck = True
        CorrAns = 'r'
        TargRod.setAutoDraw(False) #Don't draw rod on attention checks
        StartRod = 1 #We now want the rod during attention checks
        shuffle(AttDir_List)
        AttDir = AttDir_List[-1] #The direction the rod will rotate for the attention check is randomised
        currentDir = AttDir
        RodOri = 270 #Start the rod in vertical alignment on attention checks
    
    ## Live normal trials
    if AttentionCheck == False:
        FixCol = myRed #Return fix to default
        StartRod = 1
        
        shuffle(stairs) #randomise stairs
        thisStair = stairs[-1] #select stair
               
        #Set starting val and stepsize - > This is added to the dictionary
        if thisStair['trialCount'] == 1:
            thisStair['this_ori'] = thisStair['startVal']
            thisStair['thisStep'] = 0
    
        #Select current stepsize; by indexing from step list
        thisStair['stepSize'] = thisStair['stepSizes'][thisStair['thisStep']]
    
        #We add 270 because 270 is vertical meridian + thisStair is the offset
        RodOri = 270 + thisStair['this_ori']
    
        #A correct response, is a response in the dir of motion
        if thisStair['Direction'] == 'CW':
            CorrAns ='right'
        elif thisStair['Direction'] == 'CCW':
            CorrAns = 'left'
        currentDir = thisStair['Direction']
        thisExp.addData('currentDir', currentDir)
    
        #Store the stair orientation at the beginning of the trial
        for el in range(0, len(stairs)):
            storeStair = stairs[el]
            if storeStair['StairNumber'] == 1:
                Stair1 = storeStair['this_ori']
                Stair1TC = storeStair['trialCount']
            elif storeStair['StairNumber'] == 2:
                Stair2 = storeStair['this_ori']
                Stair2TC = storeStair['trialCount']
            elif storeStair['StairNumber'] == 3:
                Stair3 = storeStair['this_ori']
                Stair3TC = storeStair['trialCount']
            elif storeStair['StairNumber'] == 4:
                Stair4 = storeStair['this_ori']
                Stair4TC = storeStair['trialCount']
                
        thisExp.addData('StartingRodOri', RodOri)
        
        ##Save values
        #Add Stair values
        thisExp.addData('Stair1', Stair1)
        thisExp.addData('Stair2', Stair2)
        thisExp.addData('Stair3', Stair3)
        thisExp.addData('Stair4', Stair4)
    
        #Trial counts
        thisExp.addData('Stair1TC', Stair1TC)
        thisExp.addData('Stair2TC', Stair2TC)
        thisExp.addData('Stair3TC', Stair3TC)
        thisExp.addData('Stair4TC', Stair4TC)
    
    
    #Start in vertical alignment (270)
    Xrad = np.radians(RodOri)
    XCos = np.cos(Xrad)
    XSin = -(np.sin(Xrad))
    
    RodX = (RodRad * XCos) #Radius of the rod x cos and sin
    RodY = (RodRad * XSin)
    
    TargRod.ori = (RodOri)
    TargRod.pos = (RodX, RodY)
    
    FixDot.setFillColor(FixCol)
    FixDot.setLineColor(FixCol)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    win.recordFrameIntervals = True
    
    #Set a 10% tolerance for dropped frames
    win.refreshThreshold = (1/RefreshHz) * 1.1
    
    DisgardTrial = False
    
    # keep track of which components have finished
    trialComponents = [TargRod, FixDot, resp]
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
        if AttentionCheck == True:
            if t < 1: #We only want the fixation to change colour for 1 second
                if frameN % UpdateOn == 0:
                    FixCol = ColourList[ListIdx]
                    ListIdx += 1
                    if ListIdx == (len(ColourList) - 1):
                        ListIdx = 0 #Reset index when it hits max list
            else:
                FixCol = myRed
 
        #Move, depending on rod direction in condition file
#        if int(expInfo['test']) == 1: #if test mode, log the frame interval for the last frame
 #           if len(win.frameIntervals):
  #              logging.debug('Last Frame Interval: ' + str(win.frameIntervals[-1])) #This will return the last frame interval appended

        TargRod.ori = (RodOri)
        FixDot.setAutoDraw(False)
        if currentDir == 'CW':
            RodOri += OriStep
        elif currentDir == 'CCW':
            RodOri -= OriStep
        TargRod.ori = (RodOri)
        FixDot.setAutoDraw(True)
        FixDot.color = (FixCol)
               
        #Rod Pos, Convert deg to radians
        Xrad = np.radians(RodOri)
        XCos = np.cos(Xrad)
        XSin = -(np.sin(Xrad))
        RodX = (RodRad * XCos)
        RodY = (RodRad * XSin)
        TargRod.pos = (RodX, RodY)
        
        # *TargRod* updates
        if TargRod.status == NOT_STARTED and StartRod==1:
            # keep track of start time/frame for later
            TargRod.frameNStart = frameN  # exact frame index
            TargRod.tStart = t  # local t and not account for scr refresh
            TargRod.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TargRod, 'tStartRefresh')  # time at next scr refresh
            TargRod.setAutoDraw(True)
        if TargRod.status == STARTED:
            if frameN >= (TargRod.frameNStart + RodDur):
                # keep track of stop time/frame for later
                TargRod.tStop = t  # not accounting for scr refresh
                TargRod.frameNStop = frameN  # exact frame index
                win.timeOnFlip(TargRod, 'tStopRefresh')  # time at next scr refresh
                TargRod.setAutoDraw(False)
        if TargRod.status == STARTED:  # only update if drawing
            TargRod.setOri(RodOri, log=False)
        
        # *FixDot* updates
        if FixDot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixDot.frameNStart = frameN  # exact frame index
            FixDot.tStart = t  # local t and not account for scr refresh
            FixDot.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixDot, 'tStartRefresh')  # time at next scr refresh
            FixDot.setAutoDraw(True)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
            theseKeys = resp.getKeys(keyList=['left', 'right', 'r', 'space'], waitRelease=False)
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
        #When the rod stops movement, the screen is no longer updating.
        if frameN > RodDur:
            win.recordFrameIntervals = False
        
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
    ## Attention check
    if AttentionCheck == True:
        FixCol = myRed
        FixDot.setColor(myRed)
        if resp.corr == 1:
            PassCheck = True
        else:
            NumFails += 1
            if NumFails >= 2:
                FailedAtt = True
                thisExp.addData('FailedAtt', FailedAtt)
        thisExp.addData('NumFails', NumFails)
        thisExp.addData('PassCheck', PassCheck)
    
    ## Staircases
    if AttentionCheck == False:
        #Save data
        thisExp.addData('StairNumber', thisStair['StairNumber'])
        thisExp.addData('CurrentStair', thisStair['name'])
        thisExp.addData('RodDir', thisStair['Direction']) #Direction of the rod
        thisExp.addData('StairDirection', thisStair['currentDirection'])
        thisExp.addData('CorrAns', CorrAns)
        thisExp.addData('currentStepSize', thisStair['thisStep']) #This saves the index
        thisExp.addData('StairTrialCount', thisStair['trialCount'])
    
        #If response is correct, offset in direction opp motion (down)
        #if incorrect, offset in direction of motion (UP)
        #The up and down are respective of threshold of (0)
        if resp.corr == 1: #Means they reported the starting position displaced in direction of motion
            if thisStair['currentDirection'] == 'up':
                thisStair['currentDirection'] = 'down'
                thisStair['reversalVals'].append(thisStair['this_ori']) #This appends a list storing reversal values
                if thisStair['stepSize'] != thisStair['stepSizes'][-1]: #change step size with every reversal
                    thisStair['thisStep'] += 1
            #Select step size to apply
            thisStair['stepSize'] = thisStair['stepSizes'][thisStair['thisStep']] #thisStep is the index of the current stairstep to be applied
            if thisStair['Direction'] == 'CW':
                thisStair['this_ori'] -= thisStair['stepSize']
            elif thisStair['Direction'] == 'CCW':
                thisStair['this_ori'] += thisStair['stepSize']
                
        elif resp.corr == 0: #not perceived displaced in direction of motion, so shift in direction of motion
            if thisStair['currentDirection'] == 'down':
                thisStair['currentDirection'] = 'up'
                thisStair['reversalVals'].append(thisStair['this_ori'])
                if thisStair['stepSize'] != thisStair['stepSizes'][-1]:#if this is not the minimal stepsize
                    thisStair['thisStep'] +=1
            #Select step size
            thisStair['stepSize'] = thisStair['stepSizes'][thisStair['thisStep']]
            if thisStair['Direction'] == 'CW':
                thisStair['this_ori'] += thisStair['stepSize']
            elif thisStair['Direction'] == 'CCW':
                thisStair['this_ori'] -= thisStair['stepSize']
    
        #If a stair has hit n trials, remove from list of stairs:
        if thisStair['trialCount'] == NumTrials:
            completedStairs.append(thisStair)
            StairThresh = average(thisStair['reversalVals'][-avRevs:])
            if thisStair['StairNumber'] == 1:
                ST1Thresh = StairThresh
                ST1RevVals = thisStair['reversalVals']
            elif thisStair['StairNumber'] == 2:
                ST2Thresh = StairThresh
                ST2RevVals = thisStair['reversalVals']
            elif thisStair['StairNumber'] == 3:
                ST3Thresh = StairThresh
                ST3RevVals = thisStair['reversalVals']
            elif thisStair['StairNumber'] == 4:
                ST4Thresh = StairThresh
                ST4RevVals = thisStair['reversalVals']
            stairs.pop() #We have been referring to the last index this whole time. Pop removes the last index
    
        if len(stairs) == 0: #finished all the stairs!
            continueRoutine = False
            trials.finished = True
    
        thisStair['trialCount'] +=1
    
    
    FixDot.setAutoDraw(False)
    trials.addData('TargRod.started', TargRod.tStartRefresh)
    trials.addData('TargRod.stopped', TargRod.tStopRefresh)
    trials.addData('FixDot.started', FixDot.tStartRefresh)
    trials.addData('FixDot.stopped', FixDot.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(CorrAns).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp.keys',resp.keys)
    trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    trials.addData('resp.started', resp.tStartRefresh)
    trials.addData('resp.stopped', resp.tStopRefresh)
    win.recordFrameIntervals = False #As a safety check
    
    NumberDroppedFrames = win.nDroppedFrames - LastNumDropped #How many frames dropped this routine
    
    #if more than 10% of the frames drop, bin
    if NumberDroppedFrames > (np.round(RodDur*0.1)):
        DisgardTrial = True
    
    thisExp.addData('DisgardTrial', DisgardTrial)
    thisExp.addData('NumberDroppedFrames', NumberDroppedFrames)
    
    LastNumDropped = win.nDroppedFrames #The previous amount of dropped frames
    
    DisgardTrial = False
    
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "AttCheckWarning"-------
    continueRoutine = True
    # update component parameters for each repeat
    if AttentionCheck == False or PassCheck == True:
        continueRoutine = False
        
    else:
        #if PassCheck == True: #pased check
        #    ExtraText = 'Good work! You passed the attention check!'
        #else:
        ExtraText = 'Unfortunately, you pressed the wrong key during the attention check. ' + '\n' + "When the center dot changes colour, please press 'r'"
    WarningResp.keys = []
    WarningResp.rt = []
    _WarningResp_allKeys = []
    text.setText(ExtraText + '\n' + '\n' + 'Just a friendly reminder to please stare at the dot in the center of the screen during the experiment.' + '\n' + '\n' + "Press 's' to resume the experiment. ")
    # keep track of which components have finished
    AttCheckWarningComponents = [WarningResp, text]
    for thisComponent in AttCheckWarningComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AttCheckWarningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AttCheckWarning"-------
    while continueRoutine:
        # get current time
        t = AttCheckWarningClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AttCheckWarningClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
            theseKeys = WarningResp.getKeys(keyList=['y', 's'], waitRelease=False)
            _WarningResp_allKeys.extend(theseKeys)
            if len(_WarningResp_allKeys):
                WarningResp.keys = _WarningResp_allKeys[-1].name  # just the last key pressed
                WarningResp.rt = _WarningResp_allKeys[-1].rt
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
        for thisComponent in AttCheckWarningComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AttCheckWarning"-------
    for thisComponent in AttCheckWarningComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    #Attention check, reset variables
    AttentionCheck = False #Is an attention check occurring
    PassCheck = False
    # check responses
    if WarningResp.keys in ['', [], None]:  # No response was made
        WarningResp.keys = None
    trials.addData('WarningResp.keys',WarningResp.keys)
    if WarningResp.keys != None:  # we had a response
        trials.addData('WarningResp.rt', WarningResp.rt)
    trials.addData('WarningResp.started', WarningResp.tStartRefresh)
    trials.addData('WarningResp.stopped', WarningResp.tStopRefresh)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    # the Routine "AttCheckWarning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Break"-------
    continueRoutine = True
    # update component parameters for each repeat
    #Total trials = 160
    #Want this halfway
    if OverallTrialCount != 80:
        continueRoutine = False
    EndBreak.keys = []
    EndBreak.rt = []
    _EndBreak_allKeys = []
    # keep track of which components have finished
    BreakComponents = [Breaktext, EndBreak]
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
        
        # *Breaktext* updates
        if Breaktext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Breaktext.frameNStart = frameN  # exact frame index
            Breaktext.tStart = t  # local t and not account for scr refresh
            Breaktext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Breaktext, 'tStartRefresh')  # time at next scr refresh
            Breaktext.setAutoDraw(True)
        
        # *EndBreak* updates
        waitOnFlip = False
        if EndBreak.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EndBreak.frameNStart = frameN  # exact frame index
            EndBreak.tStart = t  # local t and not account for scr refresh
            EndBreak.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndBreak, 'tStartRefresh')  # time at next scr refresh
            EndBreak.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(EndBreak.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(EndBreak.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if EndBreak.status == STARTED and not waitOnFlip:
            theseKeys = EndBreak.getKeys(keyList=['y', 'space'], waitRelease=False)
            _EndBreak_allKeys.extend(theseKeys)
            if len(_EndBreak_allKeys):
                EndBreak.keys = _EndBreak_allKeys[-1].name  # just the last key pressed
                EndBreak.rt = _EndBreak_allKeys[-1].rt
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
    trials.addData('Breaktext.started', Breaktext.tStartRefresh)
    trials.addData('Breaktext.stopped', Breaktext.tStopRefresh)
    # check responses
    if EndBreak.keys in ['', [], None]:  # No response was made
        EndBreak.keys = None
    trials.addData('EndBreak.keys',EndBreak.keys)
    if EndBreak.keys != None:  # we had a response
        trials.addData('EndBreak.rt', EndBreak.rt)
    trials.addData('EndBreak.started', EndBreak.tStartRefresh)
    trials.addData('EndBreak.stopped', EndBreak.tStopRefresh)
    # the Routine "Break" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed TrialReps repeats of 'trials'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
##Plot intervals and save in text file
import matplotlib.pyplot as plt

FILE_NAME_TEXT=('Intervals\Text\Frohlich_' + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + "_FrameIntervals"  + '.log')
FILE_NAME_PNG = ('Intervals\Images\Frohlich_' + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + "_FrameIntervals" + '.png')

EndExp.keys = []
EndExp.rt = []
_EndExp_allKeys = []
thisExp.addData('completedStairs', completedStairs)

thisExp.addData('ST1Thresh', ST1Thresh)
thisExp.addData('ST1RevVals', ST1RevVals)
thisExp.addData('ST2Thresh', ST2Thresh)
thisExp.addData('ST2RevVals', ST2RevVals)
thisExp.addData('ST3Thresh', ST3Thresh)
thisExp.addData('ST3RevVals', ST3RevVals)
thisExp.addData('ST4Thresh', ST4Thresh)
thisExp.addData('ST4RevVals', ST4RevVals)

# keep track of which components have finished
EndComponents = [Goodbye, EndExp]
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
    
    # *EndExp* updates
    waitOnFlip = False
    if EndExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndExp.frameNStart = frameN  # exact frame index
        EndExp.tStart = t  # local t and not account for scr refresh
        EndExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndExp, 'tStartRefresh')  # time at next scr refresh
        EndExp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(EndExp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(EndExp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if EndExp.status == STARTED and not waitOnFlip:
        theseKeys = EndExp.getKeys(keyList=['y', 'n', 'space'], waitRelease=False)
        _EndExp_allKeys.extend(theseKeys)
        if len(_EndExp_allKeys):
            EndExp.keys = _EndExp_allKeys[-1].name  # just the last key pressed
            EndExp.rt = _EndExp_allKeys[-1].rt
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
thisExp.addData("globalClockTime", globalClock.getTime()) 

if EndExp.keys == 'space':
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
    titleMsg = "Dropped: %i, total: %i, percent = %.3f%%"
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

thisExp.addData('Goodbye.started', Goodbye.tStartRefresh)
thisExp.addData('Goodbye.stopped', Goodbye.tStopRefresh)
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
