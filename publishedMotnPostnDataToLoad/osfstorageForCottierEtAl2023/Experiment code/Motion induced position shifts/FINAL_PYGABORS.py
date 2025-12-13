#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on January 21, 2022, at 17:40
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
    # Y coordinates can be altered with topY
    #change to 144hz
    # Making attention check pass conditions stricter. Will fail attention check if you make any keypress not 'r'. 
        #Can now fail attention check, if you press the keyboard during the attention check ISI (cause you're clearly not paying attention)
        #Removed the code allowing for gabor adjustment in the attention check
    
    
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
expName = 'Gabors'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Timot\\Documents\\2021\\Study 1\\September_Final_EXPERIMENTS_LIVE_Python\\Python-Experiments\\Gabors\\PYGABORS.py',
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
    monitor='ASUS_PG248Q', color=[-0.005, -0.005, -0.005], colorSpace='rgb',
    blendMode='avg', waitBlanking=False, useFBO=True, 
    units='pix')
# store frame rate of monitor if we can measure it
FrameRate = expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    print('FrameRate could not be accurately measured!')
    core.quit()
    
# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Welcome = visual.TextStim(win=win, name='Welcome',
    text="In this experiment you will see two moving circles above and below a red cross.\n\n While staring at the red cross, your task is to align the top and bottom circles by pressing the UP and DOWN arrow keys.\n The circles above the cross will always move in the opposite direction to the circles below the cross.\n\n Pressing the UP arrow key moves the top circles apart and the bottom circles closer together.\n Pressing the DOWN arrow keys moves the top circles closer and the bottom circles apart. \n Once these circles are aligned please press the 'space' bar.\n\n At some point the red cross will rapidly change colour. When this happens ONLY press the 'r' key. \n\nPlease press the 's' key to begin the experiment.",
    font='Arial',
    units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
Begin = keyboard.Keyboard()
RefreshHz = 144 #200 #win.getActualFrameRate()

ifi = 1/RefreshHz #We want the inter-frame interval in seconds

## How many trials to do; for test to do less
if int(expInfo['test']) == 1:
    TrialReps = 1
else:
    TrialReps = 10

#Get the size of screen in height:
ScreenHeight = win.size[1]

if int(expInfo['test']) == 0: #1 = true, it's a test; 0 = false, not a test (LIVE TRIALS)
    if FrameRate <140 or FrameRate > 148 or RefreshHz != 144: #Give a 4 frame buffer 
        print('WARNING! ERROR WITH FRAMERATE OR REFRESHHZ. Psychopy detected the FrameRate at: ' +str(FrameRate) + 'RefreshHz was: ' + str(RefreshHz))
        core.quit()

## Check if the exists before we continue:
import os.path

# Initialize components for Routine "trial"
trialClock = core.Clock()
FixationCross = visual.ShapeStim(
    win=win, name='FixationCross', vertices='cross',units='deg', 
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='black',
    opacity=None, depth=0.0, interpolate=True)
#Report warnings to the standard output window
logging.console.setLevel(logging.WARNING)

PastCount = 0

TrialCount = 0
#Right only
TopAdjust = 0 #Top adjustment to apply
BotAdjust = 0 #Bottom adjustment to apply
respHistory = [] #response history of the keys

## Gabor size
#Create stimulus, specify stimulus parameters # GabW = 270 GabH = 270 #Gabor height
GabSizes = 200

## Gabor position
TopY = 300 #Pixels from center
BotY = (TopY * -1)
#in the offset conditions we displace the gabors by this value
OffVal = 76 #This displaces it ~25%

## Response adjustment; How much each key press shifts the position in pixels per frame
AdAmount =  np.round((48/RefreshHz), 2) #48 pixels per second

## Gabor speed 
degPerSec = 360 * 5
degPerFrame = degPerSec * ifi #This will give me a value around 12.4997
PhaseCyc = 2 #Phase Cycle per second
phasestep = (PhaseCyc/RefreshHz) #0.03 #0.03 #how much the phase will change per frame

#multiple stimulus:
n_gratings = 4
#Odd numbered gratings are top; Even are bottom
grating_coords = [[300, TopY], [300, BotY], [-300, TopY], [-300, BotY]] #Top right, bot right, top left, bot right
contrast = 0.8
GaborDimPix = win.size[1]/n_gratings #y coordinate/n_gratings
#numCycles = 5
#freq = numCycles/GaborDimPix
#Sigma of gaussian
#sigma = GaborDimPix/14 #Not sure why divide 14

#Pair 1: Top right, bot left, G1 and G4; #Pair 2: G2 and G3

## Create the stimulus
grating_stim = visual.ElementArrayStim(
    win,
    units= 'pix',
    nElements=n_gratings,
    sizes= GabSizes, #400 pixels
    xys=grating_coords,
    opacities=1.0,
    oris=0,
    sfs= 3 , #Cycles per pixel; 5 ~ high SF, 
    contrs=0.8,
    phases= ([0, 0, 0, 0]), #([phase1, phase2, phase3, phase4]),
    elementTex='sin',
    elementMask='gauss',
    texRes=128) #256

#grating_stim.sgog(False) #Turn autolog off to reduce frame dropping; we already store the starting position and ending, we don't need the inbetween; onset and offset can be inferred from other comps
    
InterstimInterval = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='InterstimInterval')
EndRout = keyboard.Keyboard()

# Initialize components for Routine "AttCheck"
AttCheckClock = core.Clock()
#During the attention check, the fixation point will fluctuate in colour
#Define the colours
MyRed = (1, -1, -1)
myYell = (1.0000, 1.0000, -1.0000)
myGreen = (-1, 1, -1)
myOrange = (1.0000, 0.2941, -1.0000) 
myCyan = (-1.0000, 1.0000, 1.0000)
myMagneta = (1.0000, -1.0000, 1.0000)
myPurple = (0.0039, -1.0000, 0.0039) 
MyBlack = (-1, -1, -1)
ColourList = [myYell, myGreen, MyRed, myPurple, myMagneta, myCyan, myOrange]

ListIdx = 0 #To select a colour from the list
CheckTime = [15, 30, 45] #Trials that the attention check will occur on
AttentionCheck = False #Will the attention check occur?
FixCol = MyBlack #Default is to keep it red
PassCheck = False #Did you pass the attention check
AttISI = 1 #ISI of the attention check

#Update colour after how many frames; 1 is super quick
UpdateOn = 18
'''
if RefreshHz == 60:
    UpdateOn = 8
elif RefreshHz == 200:
    UpdateOn = 27
'''
NumFails = 0
FailedAtt = False

AttCorrAns = 'r'
RoutineHistory_ATT = keyboard.Keyboard()
FP_AttCheck = visual.ShapeStim(
    win=win, name='FP_AttCheck', vertices='cross',units='deg', 
    size=(0.5, 0.5),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-4.0, interpolate=True)

# Initialize components for Routine "Warning"
WarningClock = core.Clock()
statTimeLimit = 15 #If they don't respond to this, it ends for good

ExtraText = ''
AttCheckFailedWarning = keyboard.Keyboard()
AttchecktextGood = visual.TextStim(win=win, name='AttchecktextGood',
    text='',
    font='Open Sans',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "Break"
BreakClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text="This is a break. Please take as long as you need to rest.\n\nPlease stare at the cross in the center of the screen during the experiment. \n\nPress 's' when you are ready to resume the experiment. ",
    font='Open Sans',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
EndBreak = keyboard.Keyboard()

# Initialize components for Routine "End"
EndClock = core.Clock()
Conslusion = visual.TextStim(win=win, name='Conslusion',
    text='Thank you completing this experiment!\n\nPlease inform the researcher you have completed this experiment. ',
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
Begin.keys = []
Begin.rt = []
_Begin_allKeys = []
win.mouseVisible = False
getFrameRate = win.getActualFrameRate()
#print(getFrameRate)
## Check the file does not already exist
if os.path.exists(filename + '.csv'):
    print('Warning: Datafile already exists!')
    core.quit()
    
# keep track of which components have finished
InstructionsComponents = [Welcome, Begin]
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
    
    # *Begin* updates
    waitOnFlip = False
    if Begin.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Begin.frameNStart = frameN  # exact frame index
        Begin.tStart = t  # local t and not account for scr refresh
        Begin.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Begin, 'tStartRefresh')  # time at next scr refresh
        Begin.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(Begin.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(Begin.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if Begin.status == STARTED and not waitOnFlip:
        theseKeys = Begin.getKeys(keyList=['y', 'n', 's'], waitRelease=False)
        _Begin_allKeys.extend(theseKeys)
        if len(_Begin_allKeys):
            Begin.keys = _Begin_allKeys[-1].name  # just the last key pressed
            Begin.rt = _Begin_allKeys[-1].rt
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
# check responses
if Begin.keys in ['', [], None]:  # No response was made
    Begin.keys = None
thisExp.addData('Begin.keys',Begin.keys)
if Begin.keys != None:  # we had a response
    thisExp.addData('Begin.rt', Begin.rt)
thisExp.addData('Begin.started', Begin.tStartRefresh)
thisExp.addData('Begin.stopped', Begin.tStopRefresh)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=TrialReps, method='fullRandom', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('GaborParametersNew.xlsx'),
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
    
    # ------Prepare to start Routine "trial"------- 
    continueRoutine = True
    # update component parameters for each repeat
    win.recordFrameIntervals = True #win.nDroppedFrames stores this. 
    
    #Set a 10% tolerance for dropped frames
    win.refreshThreshold = (1/RefreshHz) * 1.1
    
    DisgardTrial = False #Tells me if the trial needs to be disregarded cause of framedropping
    
    TrialCount += 1
    thisExp.addData('TrialCount', TrialCount)
    #Old code:
    #Trial clock
    #RoutineClock.reset()
    
    #manual frame drop counter
    #FramesDropped = 0
    #event.clearEvents()
    
    KeyDur = 0 #This measures the duration of the keypress and increments it
    
    #End experiment when space pressed, count this so it does it once
    #EndExp = False
    #EndExpCount = 0 #If >= 1 then don't do
    
    #Set up the keyboard
    kb = keyboard.Keyboard()
    kb.clock.reset() #Restart the timer
    
    #Pair 1: Top right, bot left, G1 and G4; #Pair 2: G2 and G3 
    #Reset grating coordinates to vertical alignment
    grating_coords = [[300, TopY], [300, BotY], [-300, TopY], [-300, BotY]] #Top right, bot right, top left, bot left
    
    #OffsetDir is always specified in the context of the top Gabors. #When top one is out, bot is in; and vice-versa
    
    #Set right gratings xcoords
    if OffsetDir == 'Out':
        grating_coords[0][0] += OffVal
        grating_coords[1][0] -= OffVal
    elif OffsetDir == 'In':
        grating_coords[0][0] -= OffVal
        grating_coords[1][0] += OffVal
    
    #Left gratings should always be right * -1 
    grating_coords[2][0] = grating_coords[0][0] * -1
    grating_coords[3][0] = grating_coords[1][0] * -1
    
    grating_stim.xys = grating_coords
    #Save starting positions
    thisExp.addData('Starting_coords', grating_coords)
    
    #Store the starting position, so in final routine we can calculate total change
    STTopR = grating_coords[0][0]
    STBOTR = grating_coords[1][0]
    thisExp.addData('StartingTopRight', STTopR)
    thisExp.addData('StartingBotRight', STBOTR)
    
    #Reset phase to zero
    pair1 = 0
    pair2 = 0
    
    EndRout.keys = []
    EndRout.rt = []
    _EndRout_allKeys = []
    # keep track of which components have finished
    trialComponents = [FixationCross, InterstimInterval, EndRout]
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
        
        # *FixationCross* updates
        if FixationCross.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            FixationCross.frameNStart = frameN  # exact frame index
            FixationCross.tStart = t  # local t and not account for scr refresh
            FixationCross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FixationCross, 'tStartRefresh')  # time at next scr refresh
            FixationCross.setAutoDraw(True)
        #Based upon: https://discourse.psychopy.org/t/failure-to-detect-pressed-key/24884/8
        #https://discourse.psychopy.org/t/visual-analog-scale-press-and-hold-key/21098/4
        
        # Get, but don't clear, pressed keys
        keys = kb.getKeys(['up', 'down'], waitRelease=False, clear=False)
        
        if keys and not keys[-1].duration: #if keys means, there is a key here and NOT keys[-1].duration means THERE IS NO DURATION. Duration only recorded when key lifted 
            resp = keys[-1].name #the last key's name
            if resp == 'up':
                #respHistory.append('up')
                if TopAdjust == -1:
                    TopAdjust = 0
                elif TopAdjust == 0:
                    TopAdjust = 1
                #Bot goes down
                if BotAdjust == 1:
                    BotAdjust = 0
                elif BotAdjust == 0:
                    BotAdjust = -1
            #Top closer, bot apart
            elif resp == 'down': #keys[-1] == 'down': #'down' in keys:
                #respHistory.append('down')
                #Top decreases in value
                if TopAdjust == 1:
                    TopAdjust = 0
                elif TopAdjust == 0:
                    TopAdjust = -1
                #Bot increases in value
                if BotAdjust == 0:
                    BotAdjust = 1
                elif BotAdjust == -1:
                    BotAdjust = 0
                    
        
        #Set image
        
        if t >= 1: #RoutineClock.getTime() >= 1: #seconds duration of ISI
            '''
            if int(expInfo['test']) == 1: #if test mode, log the frame interval for the last frame
                if len(win.frameIntervals):
                    logging.debug('Last Frame Interval: ' + str(win.frameIntervals[-1])) #This will return the last frame interval appended
        '''
            #Position
            #Impose some limits to stop the issues
            if grating_coords[0][0]  < 700 and grating_coords[1][0] < 700:
                grating_coords[0][0] += (AdAmount * TopAdjust) #Top right x
                TopAdjust = 0
                grating_coords[1][0] += (AdAmount * BotAdjust) #Bot right x
                BotAdjust = 0
        
            if grating_coords[0][0] > 700:
                grating_coords[0][0] = 690
                 
            if grating_coords[1][0] > 700:
                grating_coords[1][0] = 690
        
            if grating_coords[0][0]  < -200: #This means they can take it 200 pixels left, before issues occur
                TopRG = -195
        
            if grating_coords[1][0] < -200:
                BotRG = -195
                
            grating_coords[2][0] = grating_coords[0][0] * -1
            grating_coords[3][0] = grating_coords[1][0] * -1
        
            grating_stim.xys = grating_coords
            
            #Pair 1: Top right, bot left, G1 and G4; #Pair 2: bottom right and top left G2 and G3 
            #Top in, bot out
            
            if TopGabDir == 'Out': #Specified base on right gabor directions
                pair1 += phasestep
                pair2 -= phasestep
            else:
                pair1 -= phasestep
                pair2 += phasestep
            #Set phases
            grating_stim.phases = ([pair1, pair2, pair2, pair1]) 
            grating_stim.draw()
            #win.flip() not needed, auto-done
        
        # *EndRout* updates
        waitOnFlip = False
        if EndRout.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            EndRout.frameNStart = frameN  # exact frame index
            EndRout.tStart = t  # local t and not account for scr refresh
            EndRout.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(EndRout, 'tStartRefresh')  # time at next scr refresh
            EndRout.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(EndRout.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(EndRout.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if EndRout.status == STARTED and not waitOnFlip:
            theseKeys = EndRout.getKeys(keyList=['1', 'space'], waitRelease=False)
            _EndRout_allKeys.extend(theseKeys)
            if len(_EndRout_allKeys):
                EndRout.keys = _EndRout_allKeys[-1].name  # just the last key pressed
                EndRout.rt = _EndRout_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
            
        # *InterstimInterval* period
        if InterstimInterval.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InterstimInterval.frameNStart = frameN  # exact frame index
            InterstimInterval.tStart = t  # local t and not account for scr refresh
            InterstimInterval.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InterstimInterval, 'tStartRefresh')  # time at next scr refresh
            InterstimInterval.start(1)
        elif InterstimInterval.status == STARTED:  # one frame should pass before updating params and completing
            InterstimInterval.complete()  # finish the static period
            InterstimInterval.tStop = InterstimInterval.tStart + 1  # record stop time
        
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
    trials.addData('FixationCross.started', FixationCross.tStartRefresh)
    trials.addData('FixationCross.stopped', FixationCross.tStopRefresh)
    #Print the dropped frames
    win.recordFrameIntervals = False
    thisExp.addData('DroppedFrames', win.nDroppedFrames)
    #thisExp.addData('ManualFramesDropped', FramesDropped)
    
    if win.nDroppedFrames > PastCount:
        DisgardTrial = True
    
    thisExp.addData('DisgardTrial', DisgardTrial)
    
    #Past count of dropped frames
    PastCount = win.nDroppedFrames
    TopAdjust = 0
    BotAdjust = 0
    #Remove the gabors
    FixationCross.draw()
    win.flip()
    
    ## Calculate the effect!!!! 
    #This gives you the difference between the final reported position of the gabors, and their starting position
    AbsTopREF = (grating_coords[0][0] - STTopR) #Top right effect
    AbsBotREF = (grating_coords[1][0] - STBOTR) #bottom right effect
    thisExp.addData('AbsTopDiff', AbsTopREF) 
    thisExp.addData('AbsBotDiff', AbsBotREF)
    
    #Difference between final gabor position and vertical alignment position
    TopREF = (grating_coords[0][0]  - 300)
    BotREF = (grating_coords[1][0] - 300)
    thisExp.addData('TopAlignDiff', TopREF) 
    thisExp.addData('BotAlignDiff', BotREF)
    
    #Final coordinates
    thisExp.addData('grating_coords', grating_coords)
    thisExp.addData('FinalTopRight', grating_coords[0][0])
    thisExp.addData('FinalBotRight', grating_coords[1][0])
    
    #Effect - > difference between the two gabors (Top right - bottom right's x-coordinates)
    RawEff = grating_coords[0][0]  - grating_coords[1][0] 
    AvEff = (grating_coords[0][0]  - grating_coords[1][0])/2
    
    thisExp.addData('RawEff', RawEff)
    thisExp.addData('AvEff', AvEff)
    trials.addData('InterstimInterval.started', InterstimInterval.tStart)
    trials.addData('InterstimInterval.stopped', InterstimInterval.tStop)
    # check responses
    if EndRout.keys in ['', [], None]:  # No response was made
        EndRout.keys = None
    trials.addData('EndRout.keys',EndRout.keys)
    if EndRout.keys != None:  # we had a response
        trials.addData('EndRout.rt', EndRout.rt)
    trials.addData('EndRout.started', EndRout.tStartRefresh)
    trials.addData('EndRout.stopped', EndRout.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    ## ATTENTION CHECK
    # ------Prepare to start Routine "AttCheck"-------
    continueRoutine = True
    # update component parameters for each repeat
    if TrialCount not in CheckTime:
        continueRoutine = False
        AttentionCheck = False
        FixCol = MyBlack
    else:
        AttentionCheck = True
        shuffle(ColourList) #Make the RGB random
        thisExp.addData('AttentionCheck', AttentionCheck)
    RoutineHistory_ATT.keys = []
    RoutineHistory_ATT.rt = []
    _RoutineHistory_ATT_allKeys = []
    PracKB = keyboard.Keyboard()
    #Pair 1: Top right, bot left, G1 and G4; #Pair 2: G2 and G3 
    #Reset grating coordinates to vertical alignment
    grating_coords = [[300, TopY], [300, BotY], [-300, TopY], [-300, BotY]] #Top right, bot right, top left, bot right
    
    #OffsetDir is always specified in the context of the top Gabors
    #When top one is out, bot is in; and vice-versa
    
    #Set right gratings xcoords
    if OffsetDir == 'Out':
        grating_coords[0][0] += OffVal
        grating_coords[1][0] -= OffVal
    elif OffsetDir == 'In':
        grating_coords[0][0] -= OffVal
        grating_coords[1][0] += OffVal
    
    #Left gratings should always be right * -1 
    grating_coords[2][0] = grating_coords[0][0] * -1
    grating_coords[3][0] = grating_coords[1][0] * -1
    
    grating_stim.xys = grating_coords
    
    #Phase, reset to zero
    pair1 = 0
    pair2 = 0
    
    # keep track of which components have finished
    AttCheckComponents = [RoutineHistory_ATT, FP_AttCheck]
    for thisComponent in AttCheckComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AttCheckClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "AttCheck"-------
    while continueRoutine:
        # get current time
        t = AttCheckClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AttCheckClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if AttentionCheck == True:
            if t > AttISI and t < (1 + AttISI): #We only want the fixation to change colour for 1 second
                if frameN % UpdateOn == 0:
                    FixCol = ColourList[ListIdx]
                    FP_AttCheck.setColor(FixCol) #Set the Colour
                    ListIdx += 1
                    if ListIdx == (len(ColourList) - 1):
                        ListIdx = 0 #Reset index when it hits max list
            else:
                FixCol = MyBlack
                FP_AttCheck.setColor(FixCol)
        
        # *RoutineHistory_ATT* updates
        waitOnFlip = False
        if RoutineHistory_ATT.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            RoutineHistory_ATT.frameNStart = frameN  # exact frame index
            RoutineHistory_ATT.tStart = t  # local t and not account for scr refresh
            RoutineHistory_ATT.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RoutineHistory_ATT, 'tStartRefresh')  # time at next scr refresh
            RoutineHistory_ATT.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(RoutineHistory_ATT.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(RoutineHistory_ATT.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if RoutineHistory_ATT.status == STARTED and not waitOnFlip:
            theseKeys = RoutineHistory_ATT.getKeys(keyList=['space', 'r', 'up', 'down'], waitRelease=False)
            _RoutineHistory_ATT_allKeys.extend(theseKeys)
            if len(_RoutineHistory_ATT_allKeys):
                RoutineHistory_ATT.keys = _RoutineHistory_ATT_allKeys[-1].name  # just the last key pressed
                RoutineHistory_ATT.rt = _RoutineHistory_ATT_allKeys[-1].rt
                # was this correct?
                if (RoutineHistory_ATT.keys == str(AttCorrAns)) or (RoutineHistory_ATT.keys == AttCorrAns):
                    RoutineHistory_ATT.corr = 1
                else:
                    RoutineHistory_ATT.corr = 0
                # a response ends the routine
                continueRoutine = False

        
        if AttentionCheck == True:
            #Only can pass if the fixation is being displayed (after ISI)
            if RoutineHistory_ATT.corr and t > AttISI: 
                continueRoutine = False
                PassCheck = True #Passed the attention check
                respHistory.append('r')
                thisExp.addData('RespHistoryTOTAL', respHistory)
                
            else:
                PassCheck = False #Will the attention check occur?
            FixCol = MyRed #Default is to keep it red
              
        #Set image
        
        if t >= 1: #RoutineClock.getTime() >= 1: #seconds duration of ISI
            #Position
            #Pair 1: Top right, bot left, G1 and G4; #Pair 2: G2 and G3 
            #Top in, bot out
            
            if TopGabDir == 'Out': #Specified base on right gabor directions
                pair1 += phasestep
                pair2 -= phasestep
            else:
                pair1 -= phasestep
                pair2 += phasestep
            #Set phases
            grating_stim.phases = ([pair1, pair2, pair2, pair1])   #Top right, bot right, top left, bot right
            grating_stim.draw()
            #win.flip() not needed, auto-done
        
        # *FP_AttCheck* updates
        if FP_AttCheck.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            FP_AttCheck.frameNStart = frameN  # exact frame index
            FP_AttCheck.tStart = t  # local t and not account for scr refresh
            FP_AttCheck.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(FP_AttCheck, 'tStartRefresh')  # time at next scr refresh
            FP_AttCheck.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AttCheckComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "AttCheck"-------
    for thisComponent in AttCheckComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    FixCol = MyBlack
    FP_AttCheck.setColor(FixCol)
    
    if NumFails >= 2:
        FailedAtt = True
    thisExp.addData('FailedAtt', FailedAtt)
    # check responses
    if RoutineHistory_ATT.keys in ['', [], None]:  # No response was made
        RoutineHistory_ATT.keys = None
        # was no response the correct answer?!
        if str(AttCorrAns).lower() == 'none':
           RoutineHistory_ATT.corr = 1;  # correct non-response
        else:
           RoutineHistory_ATT.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('RoutineHistory_ATT.keys',RoutineHistory_ATT.keys)
    trials.addData('RoutineHistory_ATT.corr', RoutineHistory_ATT.corr)
    if RoutineHistory_ATT.keys != None:  # we had a response
        trials.addData('RoutineHistory_ATT.rt', RoutineHistory_ATT.rt)
    trials.addData('RoutineHistory_ATT.started', RoutineHistory_ATT.tStartRefresh)
    trials.addData('RoutineHistory_ATT.stopped', RoutineHistory_ATT.tStopRefresh)
    TopAdjust = 0
    BotAdjust = 0
    
    if AttentionCheck == True:
        if PassCheck == False:
            NumFails += 1
            thisExp.addData('NumFails', NumFails)
        thisExp.addData('PassCheck', PassCheck) #Log value in datafile
    
    #Remove the gabors from the screen
    FP_AttCheck.draw()
    win.flip()
    
    trials.addData('FP_AttCheck.started', FP_AttCheck.tStartRefresh)
    trials.addData('FP_AttCheck.stopped', FP_AttCheck.tStopRefresh)
    # the Routine "AttCheck" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Warning"-------
    continueRoutine = True
    # update component parameters for each repeat
    #Regardless of if they pass the attention check or not, give them a friendly reminder to fixate on the center :)
    if TrialCount not in CheckTime or PassCheck == True:
        continueRoutine = False
    
    #if PassCheck == True: #Did you pass the attention check
    #    ExtraText = 'Good work! You passed the attention check!'
    #else:
    ExtraText = 'Unfortunately, you pressed the wrong key during the attention check. ' + '\n' + "When the center cross changes colour, please press 'r'"
    AttCheckFailedWarning.keys = []
    AttCheckFailedWarning.rt = []
    _AttCheckFailedWarning_allKeys = []
    AttchecktextGood.setText(ExtraText + '\n' + '\n' + 'Just a friendly reminder to please stare at the cross in the center of the screen during the experiment.' + '\n' + '\n' + "Press 's' to resume the experiment. ")
    # keep track of which components have finished
    WarningComponents = [AttCheckFailedWarning, AttchecktextGood]
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
        
        # *AttCheckFailedWarning* updates
        waitOnFlip = False
        if AttCheckFailedWarning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AttCheckFailedWarning.frameNStart = frameN  # exact frame index
            AttCheckFailedWarning.tStart = t  # local t and not account for scr refresh
            AttCheckFailedWarning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AttCheckFailedWarning, 'tStartRefresh')  # time at next scr refresh
            AttCheckFailedWarning.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(AttCheckFailedWarning.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(AttCheckFailedWarning.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if AttCheckFailedWarning.status == STARTED and not waitOnFlip:
            theseKeys = AttCheckFailedWarning.getKeys(keyList=['y', 's'], waitRelease=False)
            _AttCheckFailedWarning_allKeys.extend(theseKeys)
            if len(_AttCheckFailedWarning_allKeys):
                AttCheckFailedWarning.keys = _AttCheckFailedWarning_allKeys[-1].name  # just the last key pressed
                AttCheckFailedWarning.rt = _AttCheckFailedWarning_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *AttchecktextGood* updates
        if AttchecktextGood.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            AttchecktextGood.frameNStart = frameN  # exact frame index
            AttchecktextGood.tStart = t  # local t and not account for scr refresh
            AttchecktextGood.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(AttchecktextGood, 'tStartRefresh')  # time at next scr refresh
            AttchecktextGood.setAutoDraw(True)
        
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
    Failed = False
    # check responses
    if AttCheckFailedWarning.keys in ['', [], None]:  # No response was made
        AttCheckFailedWarning.keys = None
    trials.addData('AttCheckFailedWarning.keys',AttCheckFailedWarning.keys)
    if AttCheckFailedWarning.keys != None:  # we had a response
        trials.addData('AttCheckFailedWarning.rt', AttCheckFailedWarning.rt)
    trials.addData('AttCheckFailedWarning.started', AttCheckFailedWarning.tStartRefresh)
    trials.addData('AttCheckFailedWarning.stopped', AttCheckFailedWarning.tStopRefresh)
    trials.addData('AttchecktextGood.started', AttchecktextGood.tStartRefresh)
    trials.addData('AttchecktextGood.stopped', AttchecktextGood.tStopRefresh)
    # the Routine "Warning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Break"-------
    continueRoutine = True
    # update component parameters for each repeat
    print('trials.thisN' + str(trials.thisN))
    if trials.thisN != 30-1:
        continueRoutine = False
    EndBreak.keys = []
    EndBreak.rt = []
    _EndBreak_allKeys = []
    # keep track of which components have finished
    BreakComponents = [text, EndBreak]
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
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
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
            theseKeys = EndBreak.getKeys(keyList=['y', 'n', 'left', 'right', 's'], waitRelease=False)
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
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
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
    
# completed 10 repeats of 'trials'


# ------Prepare to start Routine "End"-------
continueRoutine = True
# update component parameters for each repeat
thisExp.addData("globalClockTime", globalClock.getTime()) 

##Plot intervals and save in text file
import matplotlib.pyplot as plt

FILE_NAME_TEXT=('Intervals\Text\Gabors_' + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + "_FrameIntervals"  + '.log')
FILE_NAME_PNG = ('Intervals\Images\Gabors_' + str(expInfo['participant']) + '_session_' + str(expInfo['session']) + "_FrameIntervals" + '.png')

key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
EndComponents = [Conslusion, key_resp]
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
    
    # *Conslusion* updates
    if Conslusion.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        Conslusion.frameNStart = frameN  # exact frame index
        Conslusion.tStart = t  # local t and not account for scr refresh
        Conslusion.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Conslusion, 'tStartRefresh')  # time at next scr refresh
        Conslusion.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
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
      
    ## Save the intervals
    PercentDropped =  100 * nDropped/float(nTotal)
    titleMsg = "Dropped/Frames = %i%i = %.3f%%"
    droppedString = titleMsg % (nDropped, nTotal, PercentDropped)
    
    #Plot the intervals   
    plt.plot(win.frameIntervals)
    plt.xlabel('n frames')
    plt.ylabel('t (ms)')
    plt.title(droppedString)
    plt.savefig(FILE_NAME_PNG)
    plt.show()

##save intervals as file
win.saveFrameIntervals(fileName=FILE_NAME_TEXT, clear=True) #FILE_NAME_TEXT

thisExp.addData('Conslusion.started', Conslusion.tStartRefresh)
thisExp.addData('Conslusion.stopped', Conslusion.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
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
