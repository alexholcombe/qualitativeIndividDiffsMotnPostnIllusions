#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on January 18, 2022, at 17:40
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
    # Changed to 144hz
    #REMOVED MULTI-ASSIGNMENT WHICH CAUSES ISSUES

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, tools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions\
import os.path
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'FGE'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '', 'test': '0'} #default the testing off
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName,expInfo['session'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Timot\\Documents\\2021\\Study 1\\September_Final_EXPERIMENTS_LIVE_Python\\Python-Experiments\\Flash Grab\\FG_Final.py',
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
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='ASUS_PG248Q', color=[-0.005, -0.005, -0.005], colorSpace='rgb',
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

# Initialize components for Routine "Instruct"
InstructClock = core.Clock()
Instructions = visual.TextStim(win=win, name='Instructions',
    text='During this experiment you will view a moving disc rotating clockwise or counterclockwise.  At the centre of the moving disc is a white dot, please focus on this dot for the duration of the experiment. \n\nAt some point during the experiment, a red dot will be presented ontop of the disc.\nOnce the disc has stopped moving, please use your mouse to "click" the location of  the red dot.  If you did not see a red dot, please click on the white dot in the center. \n\nPress \'Space\' when you are ready to begin the experiment.',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
ExpStart = keyboard.Keyboard()
## Set the refreshrate for the display
RefreshHz = 144 #200
FrameDur = 1000/RefreshHz #This is frame Duration in ms

if int(expInfo['test']) == 0: #1 = true, it's a test; 0 = false, not a test (LIVE TRIALS)
    if FrameRate <140 or FrameRate > 148 or RefreshHz != 144: #Give a 4 frame buffer 
        print('WARNING! ERROR WITH FRAMERATE OR REFRESHHZ. Psychopy detected the FrameRate at: ' +str(FrameRate) + 'RefreshHz was: ' + str(RefreshHz))
        core.quit()

##Diagnostic or live trials
Diag = False #or false

# Initialize components for Routine "centerplease"
centerpleaseClock = core.Clock()
#Convert from height units to pixels; we coded this  for 1080p screen
## Parameters in pixels
TargSize = tools.monitorunittools.deg2pix(3.2, win.monitor) #was 3.12
Cent_FixSize = 36 #40
FixSize = tools.monitorunittools.deg2pix(0.5, win.monitor)
InstructionsCheck = visual.TextStim(win=win, name='InstructionsCheck',
    text='Please click the white circle in the centre to start the next trial.',
    font='Arial',
    units='height', pos=(-0.3, 0.2), height=0.02, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
CentreMo = event.Mouse(win=win)
x, y = [None, None]
CentreMo.mouseClock = core.Clock()
TargCent = visual.ShapeStim(
    win=win, name='TargCent',
    size=(TargSize, TargSize), vertices='circle',
    ori=90, pos=(0, 0),
    lineWidth=4,     colorSpace='rgb',  lineColor=[1,-1,-1], fillColor=[1,-1,-1],
    opacity=1, depth=-3.0, interpolate=True)
CentFP = visual.ShapeStim(
    win=win, name='CentFP',
    size=(FixSize, FixSize), vertices=99,
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=1.0, depth=-4.0, interpolate=True) #(Cent_FixSize, Cent_FixSize)

## ----- Initialize components for Routine "Trial" --------
TrialClock = core.Clock()
#Initialise variables
TargOn = 9999 #Set to some ludcrious value so it doesn't start

PastCount = 0 #Start at zero 

TDR = 450 #0.42 TDR = Target radius, in pixels
OffDeg = 20 #Offset in polar angle. How much we will offset the target in offset conditions.
TargCentD = -90 #Targets position, bottom centre in degrees

#We want a targe duration around ~ 16.67ms
#if RefreshHz == 200:
#    TargDur = 3 #Target Duration in frames
#elif RefreshHz == 144:
TargDur = 2 #Will be 13.88ms 

#Just specify these here to avoid a javascript error
TargY = -TDR
TargX = 0
XDeg = 0
XRad = 0
XCos = 0
XSin = 0

TrialCount = 0 #Initialise trialcount

anSpeed = 200 #Angles per degree of movement
oriStep = anSpeed/RefreshHz #How much orientation to change each frame; 
OriStop = 0 #On this orientation we stop, this is just a placeholder
NumRevFrames = 72 #np.round(500/FrameDur) #Reversal goes for 500ms; Should be 100 frames at 200hz; 72 at 144hz
RevFrameCount = 0 #Counts how many frames after reversal
BeginReverse = False #Begin reversal
DispTarg = False #COntrol display of target
AddRevFrame = False #Control the storage of the reversal frame

## MS intervals; pre-reversal motion list
#Python index that corresponds with PyCond
#   [0] = 1, 11
#   [1] = 2, 22
#   [2] = 3, 33
#   [3] = 4, 44
#   [4] = 5, 55
#CatchDur is a list of pre-reversal durations in frames that will be randomised for practice trials

#The duration of motion before the reversal occurs
PreRev_Dur_MS= [700, 800, 900, 1000, 1100, 1200] # MS
PreRev_Dur =  [np.round(el/FrameDur) for el in PreRev_Dur_MS] #Frames
CatchDur =  [np.round(el/FrameDur) for el in PreRev_Dur_MS]

Annulus = visual.ImageStim(
    win=win,
    name='Annulus', units='height', 
    image='sin', mask=None,
    ori=1.0, pos=(0, 0), size=(1.05, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-3.0)
Target = visual.ShapeStim(
    win=win, name='Target',
    size=(TargSize, TargSize), vertices='circle',
    ori=90, pos=[0,0],
    lineWidth=4,     colorSpace='rgb',  lineColor=[1,-1,-1], fillColor=[1,-1,-1],
    opacity=1, depth=-4.0, interpolate=True)
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
FixationPoint = visual.ShapeStim(
    win=win, name='FixationPoint',units='pix', 
    size=(FixSize, FixSize), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1, 1, 1], fillColor=[1, 1, 1],
    opacity=1.0, depth=-6.0, interpolate=True)
#Report warnings to the standard output window
#logging.console.setLevel(logging.WARNING) #Uncommnet to log every frame

# Initialize components for Routine "RespWork"
RespWorkClock = core.Clock()
RR = visual.ImageStim(
    win=win,
    name='RR', units='height', 
    image='ReverseRing.png', mask=None,
    ori=0, pos=(0, 0), size=(1.05, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
mouseResp = event.Mouse(win=win)
x, y = [None, None]
mouseResp.mouseClock = core.Clock()
#Valid response, if 1, true, not a valid response
InvalidResp = 0

PassCheck = False

#Count how many of the no dot they missed
NumFails = 0

#Status of no dots, did they pass?
NoDotStat = True

#Placeholder to stop errors
FGEffect = 0
Targ = visual.ShapeStim(
    win=win, name='Targ',
    size=(TargSize, TargSize), vertices='circle',
    ori=90, pos=[0,0],
    lineWidth=4,     colorSpace='rgb',  lineColor=[1,-1,-1], fillColor=[1,-1,-1],
    opacity=1, depth=-3.0, interpolate=True)
RespFP = visual.ShapeStim(
    win=win, name='RespFP',units='pix', 
    size=(FixSize, FixSize), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1, 1, 1], fillColor=[1, 1, 1],
    opacity=1.0, depth=-4.0, interpolate=True)

# Initialize components for Routine "BreakTime"
BreakTimeClock = core.Clock()
BreakText = visual.TextStim(win=win, name='BreakText',
    text="This is a break! Please take as long as you need to rest.\n\nPress 'space' when you are ready to resume the experiment",
    font='Open Sans',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EndBreak = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
Thanks = visual.TextStim(win=win, name='Thanks',
    text='Thank you for finishing this experiment\n\nPlease tell the researcher you have finished',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
endExp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instruct"-------
continueRoutine = True
# update component parameters for each repeat
ExpStart.keys = []
ExpStart.rt = []
_ExpStart_allKeys = []
print('Refreshrate: ', win.getActualFrameRate())

#Get the size of screen in height:
ScreenHeight = win.size[1]
if os.path.exists(filename + '.csv'):
    print('Warning: Datafile already exists!')
    core.quit()
# keep track of which components have finished
InstructComponents = [Instructions, ExpStart]
for thisComponent in InstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
InstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instruct"-------
while continueRoutine:
    # get current time
    t = InstructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=InstructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Instructions* updates
    if Instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Instructions.frameNStart = frameN  # exact frame index
        Instructions.tStart = t  # local t and not account for scr refresh
        Instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Instructions, 'tStartRefresh')  # time at next scr refresh
        Instructions.setAutoDraw(True)
    
    # *ExpStart* updates
    waitOnFlip = False
    if ExpStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ExpStart.frameNStart = frameN  # exact frame index
        ExpStart.tStart = t  # local t and not account for scr refresh
        ExpStart.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ExpStart, 'tStartRefresh')  # time at next scr refresh
        ExpStart.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ExpStart.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ExpStart.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ExpStart.status == STARTED and not waitOnFlip:
        theseKeys = ExpStart.getKeys(keyList=['y', 'space'], waitRelease=False)
        _ExpStart_allKeys.extend(theseKeys)
        if len(_ExpStart_allKeys):
            ExpStart.keys = _ExpStart_allKeys[-1].name  # just the last key pressed
            ExpStart.rt = _ExpStart_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instruct"-------
for thisComponent in InstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Instructions.started', Instructions.tStartRefresh)
thisExp.addData('Instructions.stopped', Instructions.tStopRefresh)
# check responses
if ExpStart.keys in ['', [], None]:  # No response was made
    ExpStart.keys = None
thisExp.addData('ExpStart.keys',ExpStart.keys)
if ExpStart.keys != None:  # we had a response
    thisExp.addData('ExpStart.rt', ExpStart.rt)
thisExp.addData('ExpStart.started', ExpStart.tStartRefresh)
thisExp.addData('ExpStart.stopped', ExpStart.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

##### JUST COMMENTING OUT, TO AVOID ACCIDENTALLY NOT DOING THE CORRECT AMOUNT OF TRIALS :)
# set up handler to look after randomisation of conditions etc
#if int(expInfo['test']) == 1:
#    TrialReps = 1 #Repeat the trials less for testing/diagnostic.
#else:
#    TrialReps = 5
########

Trials = data.TrialHandler(nReps=5, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('FGPara.xlsx'),
    seed=None, name='Trials')
thisExp.addLoop(Trials)  # add the loop to the experiment
thisTrial = Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in Trials:
    currentLoop = Trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "centerplease"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the CentreMo
    CentreMo.clicked_name = []
    gotValidClick = False  # until a click is received
    ## For centering the mouse, we want to show the cursor
    win.mouseVisible = True
    # keep track of which components have finished
    centerpleaseComponents = [InstructionsCheck, CentreMo, TargCent, CentFP]
    for thisComponent in centerpleaseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    centerpleaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "centerplease"-------
    while continueRoutine:
        # get current time
        t = centerpleaseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=centerpleaseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstructionsCheck* updates
        if InstructionsCheck.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            InstructionsCheck.frameNStart = frameN  # exact frame index
            InstructionsCheck.tStart = t  # local t and not account for scr refresh
            InstructionsCheck.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionsCheck, 'tStartRefresh')  # time at next scr refresh
            InstructionsCheck.setAutoDraw(True)
        # *CentreMo* updates
        if CentreMo.status == NOT_STARTED and t >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            CentreMo.frameNStart = frameN  # exact frame index
            CentreMo.tStart = t  # local t and not account for scr refresh
            CentreMo.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CentreMo, 'tStartRefresh')  # time at next scr refresh
            CentreMo.status = STARTED
            CentreMo.mouseClock.reset()
            prevButtonState = CentreMo.getPressed()  # if button is down already this ISN'T a new click
        if CentreMo.status == STARTED:  # only update if started and not finished!
            buttons = CentreMo.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(CentFP)
                        clickableList = CentFP
                    except:
                        clickableList = [CentFP]
                    for obj in clickableList:
                        if obj.contains(CentreMo):
                            gotValidClick = True
                            CentreMo.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *TargCent* updates
        if TargCent.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            TargCent.frameNStart = frameN  # exact frame index
            TargCent.tStart = t  # local t and not account for scr refresh
            TargCent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TargCent, 'tStartRefresh')  # time at next scr refresh
            TargCent.setAutoDraw(True)
        
        # *CentFP* updates
        if CentFP.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            CentFP.frameNStart = frameN  # exact frame index
            CentFP.tStart = t  # local t and not account for scr refresh
            CentFP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CentFP, 'tStartRefresh')  # time at next scr refresh
            CentFP.setAutoDraw(True)
        #There's some memory issue with set every fmrame in components, so doing it here
        if centerpleaseClock.getTime() > 0.02:
            TargCent.setPos((CentreMo.getPos()))
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in centerpleaseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "centerplease"-------
    for thisComponent in centerpleaseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trials.addData('InstructionsCheck.started', InstructionsCheck.tStartRefresh)
    Trials.addData('InstructionsCheck.stopped', InstructionsCheck.tStopRefresh)
    # store data for Trials (TrialHandler)
    x, y = CentreMo.getPos()
    buttons = CentreMo.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter(CentFP)
            clickableList = CentFP
        except:
            clickableList = [CentFP]
        for obj in clickableList:
            if obj.contains(CentreMo):
                gotValidClick = True
                CentreMo.clicked_name.append(obj.name)
    Trials.addData('CentreMo.x', x)
    Trials.addData('CentreMo.y', y)
    Trials.addData('CentreMo.leftButton', buttons[0])
    Trials.addData('CentreMo.midButton', buttons[1])
    Trials.addData('CentreMo.rightButton', buttons[2])
    if len(CentreMo.clicked_name):
        Trials.addData('CentreMo.clicked_name', CentreMo.clicked_name[0])
    Trials.addData('CentreMo.started', CentreMo.tStart)
    Trials.addData('CentreMo.stopped', CentreMo.tStop)
    Trials.addData('TargCent.started', TargCent.tStartRefresh)
    Trials.addData('TargCent.stopped', TargCent.tStopRefresh)
    Trials.addData('CentFP.started', CentFP.tStartRefresh)
    Trials.addData('CentFP.stopped', CentFP.tStopRefresh)
    # the Routine "centerplease" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    win.mouseVisible = False
    
    #Calculate x and y coordinates with degrees
    #270 degrees is the bottom centre
    #XDeg -  position in degrees
    TrialCount += 1
    thisExp.addData('TrialCount', TrialCount)
    
    if OffDir == 'Right':
        XDeg = TargCentD + OffDeg
    elif OffDir == 'Left':
         XDeg = TargCentD - OffDeg
    else:
        XDeg = TargCentD
    
    #Convert degrees to radians
    XRad = ((XDeg * np.pi) / 180)
    
    if OffDir == 'None':
        XCos = 0
        XSin = -1 #-1?      
    else:
        XCos = cos(XRad)
        XSin = sin(XRad)
    
    #Target Degree X (TDX) or Y (TDY)
    TargX = (TDR * XCos)
    TargY = (TDR * XSin)
    
    thisExp.addData('DegTargX', TargX)
    thisExp.addData('DegTargY', TargY)
    
    #How many frames will be spent travelling. The ocmmented out numbers, are the degrees it used to cover pre-reverse
    FrameCount = 0 #This frame counter will not include the isi 
    
    #The degrees that used to be covered pre-reverse, now it' num of frames to cover before stopping
    
    #How many frames pre-reverse, lets calculate this dynamically, so much more fluid than excel
    
    ## ORistop is how many frames we want the orientation movement to occur for:
    #We use np.round because if not 200hz, the frameN will be a decimal value
    if PyCond == 11 or PyCond == 1:
        OriStop = PreRev_Dur[0]
    elif PyCond == 22 or PyCond == 2:
        OriStop = PreRev_Dur[1]
    elif PyCond == 33 or PyCond == 3:
        OriStop = PreRev_Dur[2]
    elif PyCond == 44 or PyCond == 4:
        OriStop = PreRev_Dur[3]
    elif PyCond == 55 or PyCond == 5:
        OriStop = PreRev_Dur[4]
    elif PyCond == 66 or PyCond == 6:
        OriStop = PreRev_Dur[5]
    #elif PyCond == 77 or PyCond == 7:
    #    OriStop = np.round(1500/FrameDur)
    
    #Stop for catch trials, randomly determined
    if CatchCond == 'Yes':
        CIDX = randint(0, (len(CatchDur)-1)) #Catch Index, randomly selects a value from the catch dur list
        OriStop = CatchDur[CIDX] 
    thisExp.addData('OriSTOP', OriStop) #Frames to cover before stopped
    
    #ori it starts on 
    if ClockDir == 'CCW':
        Ori = 360
    else:
        Ori = 0
    
    thisExp.addData('StartingOri', Ori)
    
    Annulus.setOri(Ori)
    Target.setPos((TargX, TargY))    
    #Set a 10% tolerance for dropped frames
    win.refreshThreshold = (1/RefreshHz) * 1.1
    
    DisgardTrial = False
    
    #manual frame drop counter
    #FramesDropped = 0
    # keep track of which components have finished
    TrialComponents = [Annulus, Target, ISI, FixationPoint]
    for thisComponent in TrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Trial"-------
    while continueRoutine:
        # get current time
        t = TrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        #Clockwise is positive; CCW negative
        
        if int(expInfo['test']) == 1: #if test mode, log the frame interval for the last frame
            if len(win.frameIntervals):
                logging.debug('Last Frame Interval: ' + str(win.frameIntervals[-1])) #This will return the last frame interval appended

        #We don't want the orientation changing before the ISI ends
        if TrialClock.getTime() > 0.5:
            if win.recordFrameIntervals != True:
                win.recordFrameIntervals = True #win.nDroppedFrames stores this. 
            FrameCount += 1             
            FixationPoint.setAutoDraw(False)
            if BeginReverse == False:
                if ClockDir == 'CCW':
                    Ori -= oriStep
                else: #clockwise
                    Ori += oriStep 
        
            if FrameCount == OriStop:
                thisExp.addData('OriatReversal', Ori)
                BeginReverse = True
                thisExp.addData('RevFramestart', (frameN)) #just be aware frameN is -1
                AddRevFrame = False
                if CatchCond == 'No':
                    DispTarg = True
                else: #No target displayed during catch conditions
                    DispTarg = False
        
        #Reversal 
            if BeginReverse == True:
                RevFrameCount += 1
                #Reversal is always in the opposite direction to the annulus rotation
                if ClockDir == 'CCW': #Thus reverse clockwise (positive)
                    Ori += oriStep
                else:
                    #Reverse counterclockwise
                    Ori -= oriStep 
        
            if RevFrameCount >= NumRevFrames:
                thisExp.addData('RevDuration', RevFrameCount)
                continueRoutine = False
                #print(t, 'OriStop: ', OriStop, 'FrameCount: ', FrameCount)  
                RevFrameCount = 0
                BeginReverse = False
                DispTarg = False
            
            #Control Annulus ori here. Only draw when necessary
            Annulus.setOri(Ori)
            FixationPoint.setAutoDraw(True)
            #FixationPoint.setImage('FixationPoint.png')
            #FixationPoint.setSize(0.025, 0.025)
            #TrialFP.draw()
        
        # *Annulus* updates
        if Annulus.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            Annulus.frameNStart = frameN  # exact frame index
            Annulus.tStart = t  # local t and not account for scr refresh
            Annulus.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Annulus, 'tStartRefresh')  # time at next scr refresh
            Annulus.setAutoDraw(True)
        
        # *Target* updates
        if Target.status == NOT_STARTED and DispTarg:
            # keep track of start time/frame for later
            Target.frameNStart = frameN  # exact frame index
            Target.tStart = t  # local t and not account for scr refresh
            Target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Target, 'tStartRefresh')  # time at next scr refresh
            Target.setAutoDraw(True)
        if Target.status == STARTED:
            if frameN >= (Target.frameNStart + TargDur):
                # keep track of stop time/frame for later
                Target.tStop = t  # not accounting for scr refresh
                Target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Target, 'tStopRefresh')  # time at next scr refresh
                Target.setAutoDraw(False)
        
        # *FixationPoint* updates
        if FixationPoint.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            FixationPoint.frameNStart = frameN  # exact frame index
            FixationPoint.tStart = t  # local t and not account for scr refresh
            FixationPoint.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixationPoint, 'tStartRefresh')  # time at next scr refresh
            FixationPoint.setAutoDraw(True)
        # *ISI* period
        if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ISI.frameNStart = frameN  # exact frame index
            ISI.tStart = t  # local t and not account for scr refresh
            ISI.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
            ISI.start(0.5)
        elif ISI.status == STARTED:  # one frame should pass before updating params and completing
            # updating other components during *ISI*
            Annulus.setImage('Ring.png')
            # component updates done
            ISI.complete()  # finish the static period
            ISI.tStop = ISI.tStart + 0.5  # record stop time
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()        
        
    # -------Ending Routine "Trial"-------
    for thisComponent in TrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    RevFrameCount = 0 #Counts how many frames after reversal
    BeginReverse = False
    DispTarg = False
    #If AutoDraw is turned on it draws every frame
    FixationPoint.setAutoDraw(False)
    
    Trials.addData('Annulus.started', Annulus.tStartRefresh)
    Trials.addData('Annulus.stopped', Annulus.tStopRefresh)
    Trials.addData('Target.started', Target.tStartRefresh)
    Trials.addData('Target.stopped', Target.tStopRefresh)
    Trials.addData('ISI.started', ISI.tStart)
    Trials.addData('ISI.stopped', ISI.tStop)
    Trials.addData('FixationPoint.started', FixationPoint.tStartRefresh)
    Trials.addData('FixationPoint.stopped', FixationPoint.tStopRefresh)

 ## Stop recording frame dropping:
    win.recordFrameIntervals = False #win.nDroppedFrames store    

    if win.nDroppedFrames > PastCount:
        DisgardTrial = True
    thisExp.addData('DisgardTrial', DisgardTrial)
    thisExp.addData('DroppedFrames', win.nDroppedFrames)
    PastCount = win.nDroppedFrames #Past dropped frames 
    routineTimer.reset()
        

    # ------Prepare to start Routine "RespWork"-------
    continueRoutine = True
    # update component parameters for each repeat
    # setup some python lists for storing info about the mouseResp
    mouseResp.x = []
    mouseResp.y = []
    mouseResp.leftButton = []
    mouseResp.midButton = []
    mouseResp.rightButton = []
    mouseResp.time = []
    mouseResp.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    RespWorkComponents = [RR, mouseResp, Targ, RespFP]
    for thisComponent in RespWorkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RespWorkClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RespWork"-------
    while continueRoutine:
        # get current time
        t = RespWorkClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RespWorkClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *RR* updates
        if RR.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            RR.frameNStart = frameN  # exact frame index
            RR.tStart = t  # local t and not account for scr refresh
            RR.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RR, 'tStartRefresh')  # time at next scr refresh
            RR.setAutoDraw(True)
        # *mouseResp* updates
        if mouseResp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouseResp.frameNStart = frameN  # exact frame index
            mouseResp.tStart = t  # local t and not account for scr refresh
            mouseResp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouseResp, 'tStartRefresh')  # time at next scr refresh
            mouseResp.status = STARTED
            mouseResp.mouseClock.reset()
            prevButtonState = mouseResp.getPressed()  # if button is down already this ISN'T a new click
        if mouseResp.status == STARTED:  # only update if started and not finished!
            buttons = mouseResp.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter(RR)
                        clickableList = RR
                    except:
                        clickableList = [RR]
                    for obj in clickableList:
                        if obj.contains(mouseResp):
                            gotValidClick = True
                            mouseResp.clicked_name.append(obj.name)
                    x, y = mouseResp.getPos()
                    mouseResp.x.append(x)
                    mouseResp.y.append(y)
                    buttons = mouseResp.getPressed()
                    mouseResp.leftButton.append(buttons[0])
                    mouseResp.midButton.append(buttons[1])
                    mouseResp.rightButton.append(buttons[2])
                    mouseResp.time.append(mouseResp.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        if mouseResp.getPos()[1] > -250: #If their mouse is above this, they likely just clicked in the centre of the screen instead of reporting the target's perceived location
            InvalidResp = 1
        else:
            InvalidResp = 0
        thisExp.addData('InvalidResp', InvalidResp)
        
        '''
        if Diag:
            #Effect in radians
            RespRad = np.arctan2(mouseResp.getPos()[1], mouseResp.getPos()[0]) #Response in radians
            RespDeg = RespRad * 180/np.pi #Convert to degrees
        
            thisExp.addData('RespRad', RespRad) 
            thisExp.addData('RespPolarAngle', RespDeg)
        
        
            #Positive error is counterclockwise; clockwise negative
        
            #Arctan 2 units:
            #-90 is the bottom centre of the annulus,
            #centre of screen on right is 0, centre screen left is +/- 180
            if OffDir == 'Left':
                #Right was offset positively 
                respError = RespDeg - (-90 - OffDeg)
            elif OffDir == 'Right':
                #Right was offset positively 
                respError = RespDeg - (-90 + OffDeg)
            else:
                #No offset, x was in centre
                respError = RespDeg - -90
             
            ## Interpreting the efffect:
            # Because of arctan, any negative displacement is clockwise; any positive displacement is ccw
        
            #What I am changing this to, is so that any positive values means it was displaced in direction of motion reversal
        
            #TargCentD = the degrees of the target
            #flashGrabEffect=-(2*reverseDir-1)*respError; %error in the direction of subsequent motion
        
            if RevDir == 'CCW':
                FGEffect = respError 
            else:
                FGEffect = respError * -1 #We multiply by negative, cause clockwise displacement is negative to arctan
        
            if CatchCond == 'Yes':
                FGEffect = 'NaN'
                
        '''
        
        # *Targ* updates
        if Targ.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            Targ.frameNStart = frameN  # exact frame index
            Targ.tStart = t  # local t and not account for scr refresh
            Targ.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Targ, 'tStartRefresh')  # time at next scr refresh
            Targ.setAutoDraw(True)
        if Targ.status == STARTED:  # only update if drawing
            Targ.setPos((mouseResp.getPos()[0], mouseResp.getPos()[1]), log=False)
        
        # *RespFP* updates
        if RespFP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RespFP.frameNStart = frameN  # exact frame index
            RespFP.tStart = t  # local t and not account for scr refresh
            RespFP.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RespFP, 'tStartRefresh')  # time at next scr refresh
            RespFP.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RespWorkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RespWork"-------
    for thisComponent in RespWorkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trials.addData('RR.started', RR.tStartRefresh)
    Trials.addData('RR.stopped', RR.tStopRefresh)
    # store data for Trials (TrialHandler)
    if len(mouseResp.x): Trials.addData('mouseResp.x', mouseResp.x[0])
    if len(mouseResp.y): Trials.addData('mouseResp.y', mouseResp.y[0])
    if len(mouseResp.leftButton): Trials.addData('mouseResp.leftButton', mouseResp.leftButton[0])
    if len(mouseResp.midButton): Trials.addData('mouseResp.midButton', mouseResp.midButton[0])
    if len(mouseResp.rightButton): Trials.addData('mouseResp.rightButton', mouseResp.rightButton[0])
    if len(mouseResp.time): Trials.addData('mouseResp.time', mouseResp.time[0])
    if len(mouseResp.clicked_name): Trials.addData('mouseResp.clicked_name', mouseResp.clicked_name[0])
    Trials.addData('mouseResp.started', mouseResp.tStartRefresh)
    Trials.addData('mouseResp.stopped', mouseResp.tStopRefresh)
    InvalidResp = 0
    
    #RT, relative to start of routine
    thisExp.addData('RoutineRT', t)
    
    #Did they pass the catch trial
    if CatchCond == 'Yes':
        # X and Y coordinates must be within +/- 50 pixels of the centre to passcheck
        if mouseResp.getPos()[1] >= -50 and mouseResp.getPos()[1] <= 50 and mouseResp.getPos()[0] >= -50 and mouseResp.getPos()[0] <= 50:
            PassCheck = True
        else:
            PassCheck = False
            NumFails += 1
            thisExp.addData('NumFails', NumFails)
        if NumFails >= 2:
            NoDotStat = False
            thisExp.addData('NoDotStat', NoDotStat)
            
    else:
        PassCheck = 'NA'
    
    thisExp.addData('PassCheck', PassCheck)
    #Effect in radians
    #np.arctan2(y, x)
    RespRad = np.arctan2(mouseResp.getPos()[1], mouseResp.getPos()[0]) #Response in radians
    RespDeg = RespRad * 180/np.pi #Convert to degrees
    Deg_Sanity = rad2deg(RespRad) #As a sanity check, calculate rad2degrees with np functions
    
    thisExp.addData('RespRad', RespRad) 
    thisExp.addData('RespPolarAngle', RespDeg)
    thisExp.addData('Deg_Sanity', Deg_Sanity)
    
    #Positive error is counterclockwise; clockwise negative
    
    #Arctan 2 units:
    #-90 is the bottom centre of the annulus,
    #centre of screen on right is 0, centre screen left is +/- 180
    if OffDir == 'Left':
        #left was offset negatively 
        respError = RespDeg - (-90 - OffDeg)
    elif OffDir == 'Right':
        #Right was offset positively 
        respError = RespDeg - (-90 + OffDeg)
    else:
        #No offset, x was in centre
        respError = RespDeg - -90
     
    ## Interpreting the efffect:
    # Because of arctan, any negative displacement is clockwise; any positive displacement is ccw
    
    #What I am changing this to, is so that any positive values means it was displaced in direction of motion reversal
    
    #TargCentD = the degrees of the target
    #flashGrabEffect=-(2*reverseDir-1)*respError; %error in the direction of subsequent motion
    
    if RevDir == 'CCW':
        FGEffect = respError 
    else:
        FGEffect = respError * -1 #We multiply by negative, cause clockwise displacement is negative to arctan
    
    if CatchCond == 'Yes':
        FGEffect = 'NaN'
    
    thisExp.addData('respError', respError)
    thisExp.addData('FlashGrabEffect', FGEffect)
    
    
    Trials.addData('Targ.started', Targ.tStartRefresh)
    Trials.addData('Targ.stopped', Targ.tStopRefresh)
    Trials.addData('RespFP.started', RespFP.tStartRefresh)
    Trials.addData('RespFP.stopped', RespFP.tStopRefresh)
    # the Routine "RespWork" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "BreakTime"-------
    continueRoutine = True
    # update component parameters for each repeat
    #180 total trials
    
    if TrialCount != 90:
        continueRoutine = False
    EndBreak.keys = []
    EndBreak.rt = []
    _EndBreak_allKeys = []
    # keep track of which components have finished
    BreakTimeComponents = [BreakText, EndBreak]
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
            theseKeys = EndBreak.getKeys(keyList=['right', 'space'], waitRelease=False)
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
    Trials.addData('BreakText.started', BreakText.tStartRefresh)
    Trials.addData('BreakText.stopped', BreakText.tStopRefresh)
    # check responses
    if EndBreak.keys in ['', [], None]:  # No response was made
        EndBreak.keys = None
    Trials.addData('EndBreak.keys',EndBreak.keys)
    if EndBreak.keys != None:  # we had a response
        Trials.addData('EndBreak.rt', EndBreak.rt)
    Trials.addData('EndBreak.started', EndBreak.tStartRefresh)
    Trials.addData('EndBreak.stopped', EndBreak.tStopRefresh)
    # the Routine "BreakTime" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5 repeats of 'Trials'

# get names of stimulus parameters
if Trials.trialList in ([], [None], None):
    params = []
else:
    params = Trials.trialList[0].keys()
# save data for this loop
Trials.saveAsExcel(filename + '.xlsx', sheetName='Trials',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
import matplotlib.pyplot as plt

FILE_NAME_TEXT=('Intervals\Text\FlashGrab' + "_FrameIntervals_" + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + '.log')
FILE_NAME_PNG = ('Intervals\Images\FlashGrab' + expName + "_FrameIntervals_" + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + '.png')

endExp.keys = []
endExp.rt = []
_endExp_allKeys = []
# keep track of which components have finished
EndComponents = [Thanks, endExp]
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
    
    # *Thanks* updates
    if Thanks.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Thanks.frameNStart = frameN  # exact frame index
        Thanks.tStart = t  # local t and not account for scr refresh
        Thanks.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Thanks, 'tStartRefresh')  # time at next scr refresh
        Thanks.setAutoDraw(True)
    
    # *endExp* updates
    waitOnFlip = False
    if endExp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        endExp.frameNStart = frameN  # exact frame index
        endExp.tStart = t  # local t and not account for scr refresh
        endExp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(endExp, 'tStartRefresh')  # time at next scr refresh
        endExp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(endExp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(endExp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if endExp.status == STARTED and not waitOnFlip:
        theseKeys = endExp.getKeys(keyList=['right', 'space'], waitRelease=False)
        _endExp_allKeys.extend(theseKeys)
        if len(_endExp_allKeys):
            endExp.keys = _endExp_allKeys[-1].name  # just the last key pressed
            endExp.rt = _endExp_allKeys[-1].rt
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
#Save time to it takes participants to complete experiment
thisExp.addData("globalClockTime", globalClock.getTime()) 

#plt.plot(win.frameIntervals)
#plt.show()

if endExp.keys == 'space':
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
    titleMsg = "Dropped = %i Total Frames = %i Percent =  %.3f%%"
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

thisExp.addData('Thanks.started', Thanks.tStartRefresh)
thisExp.addData('Thanks.stopped', Thanks.tStopRefresh)
# check responses
if endExp.keys in ['', [], None]:  # No response was made
    endExp.keys = None
thisExp.addData('endExp.keys',endExp.keys)
if endExp.keys != None:  # we had a response
    thisExp.addData('endExp.rt', endExp.rt)
thisExp.addData('endExp.started', endExp.tStartRefresh)
thisExp.addData('endExp.stopped', endExp.tStopRefresh)
thisExp.nextEntry()
# the Routine "End" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
## Save DVA as pixels
thisExp.addData('TargSize', TargSize)
thisExp.addData('FixSize', FixSize)
## Save important values
thisExp.addData('NumRevFrames', NumRevFrames) 
thisExp.addData('oriStep', oriStep)
thisExp.addData('CatchDur', CatchDur)

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
