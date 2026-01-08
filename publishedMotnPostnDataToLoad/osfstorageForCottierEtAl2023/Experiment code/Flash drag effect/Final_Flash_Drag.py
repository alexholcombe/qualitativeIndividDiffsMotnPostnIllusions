#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on January 17, 2022, at 17:25
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
    # adding a break
    # Correcting the attention check typo which is biasing/causing issues
    #Noticed for first 6 participants (pilot), that the reversal value saved AFTER the stairstep was applied to the flash's y coordinates. NOW, the reversal value is stored PROPERLY
        # Additionally, there was a 1 trial delay in applying the reversal value
    #Checked 10/03, looks good, staircases good
    
from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('2021.2.3')


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
expName = 'FD'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '', 'test':'0'} #Test (0 if live trials; 1 if test)
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
    originPath='C:\\Users\\Timot\\Documents\\2021\\Study 1\\September_Final_EXPERIMENTS_LIVE_Python\\Python-Experiments\\Remade_FD\\Reamde_FD_1601.py',
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
    units='deg') #waitBlank by default = True
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
    text='This is experiment A. In this experiment you will stare at a red cross, on both sides of the cross you will see black and white bars moving up and down.\n\nNext to these moving bars two lines will be flashed. There will be a line flashed on the right side of the screen and on the left side of the screen. \nPlease use the \'right\' and \'left\' arrow keys to report which line is higher than the other. If the left line is the highest, press \'left\'. If the right line is higher, press \'right\'.\nAs an attention check, throughout the experiment the cross will begin change colour. When the cross changes colour, please press \'r\'.\n\nBefore the experiment you will complete some practice trials that will test your understanding of the instructions. \n\nPress "s" when you are ready to begin.  ',
    font='Arial',
    units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
## Set refreshRate, check it's set to 200hz
RefreshHz = 144

if int(expInfo['test']) == 0: #1 = true, it's a test; 0 = false, not a test (LIVE TRIALS)
    if FrameRate <140 or FrameRate > 148 or RefreshHz != 144: #Give a 4 frame buffer 
        print('WARNING! ERROR WITH FRAMERATE OR REFRESHHZ. Psychopy detected the FrameRate at: ' +str(FrameRate) + 'RefreshHz was: ' + str(RefreshHz))
        core.quit()

win.mouseVisible = False #hide the mouse

#Check if the file already exists
if os.path.exists(filename + '.csv'):
    print('Warning: Datafile already exists!')
    core.quit()
    
#Fixation point size in degrees
FPSize = 0.5

# Initialize components for Routine "Trials"
TrialsClock = core.Clock()
ISI = clock.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
FP = visual.ShapeStim(
    win=win, name='FP', vertices='cross',
    size=(FPSize, FPSize),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor='red', fillColor='red',
    opacity=None, depth=-1.0, interpolate=True)
##Attention check:
check = False #Only true for the check
Tnum = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200] #Att checks every 20 trials

trialCount = 0 #This tells us what trial it is.

ISIDUR = np.ceil(800/(1000/RefreshHz)) #In frames, approximately 800ms. At 144hz, this is 805ms; 116 frames
ChangeStepVal = 3 #Change step size after how many reversals
stairStepList = tools.monitorunittools.pix2deg(np.array([13.5, 6.75]), win.monitor) #Stair Step Size [0.0125, 0.00625] convert from HU to pixels
stairstep = 0

#Correct answer for the staircase
CorrAns = 'right' 

#Number of reversals to trigger change in stairstep value
NumRev = 4
revVal = 0 #Store the reversal value of each trial

#After every initial direction, the subsequent  direction reverses
#I.e, if an up staircase goes, the next iteration must be a down staircase
#There are 8 possible combinations (of up and down staircases)
NumRepeats = 0 #We use Combo Num to pick a stair depending on number of repeats

'''General Staircase parameters
    Specified within the context of the right gratings behaviour
    There are two staircases for when the grating is going up
    And for when the staircase is going down'''

#The staircase will always be applied on the RIGHT GRATING
#Converting from screen heights to pixels
OffsetValue = tools.monitorunittools.pix2deg(108, win.monitor)

#Up staircases
#Stair 1, ahead
ST1Step = 0 #Indexes from stairstep list to choose stairstep
ST1TC = 0 #Trial counter
ST1RevVals = [] #Stores the values that the staircase reverses on
ST1NumRevs = 0 #This is used to dictate stairstep value
ST1Fl = OffsetValue #Flash Y coordinates
ST1Dir = 'down' #Stair starts displaced in the direction of motion
ST1G = 'up' #Movement of grating

#Stair2, Behind
ST2Step = 0 #Indexes from stairstep list to choose stairstep
ST2TC = 0 #Trial counter
ST2RevVals = [] #Stores the values that the staircase reverses on
ST2NumRevs = 0 #This is used to dictate stairstep value
ST2Fl = -OffsetValue #Flash Y coordinates
ST2Dir = 'up' #Stair starts displaced in the direction opposite motion
ST2G = 'up' #Movement of grating

#Starcases, grating moving  downwards

#Stair3, Ahead
ST3Step = 0 #Indexes from stairstep list to choose stairstep
ST3TC = 0 #Trial counter
ST3RevVals = [] #Stores the values that the staircase reverses on
ST3NumRevs = 0 #This is used to dictate stairstep value
ST3Fl = -OffsetValue #Flash Y coordinates
ST3Dir = 'up' #Flash starts offset UNDER THE HORIZONTAL MERIDIAN
ST3G = 'down' #Movement of grating

#Stair4, behind
ST4Step = 0 #Indexes from stairstep list to choose stairstep
ST4TC = 0 #Trial counter
ST4RevVals = [] #Stores the values that the staircase reverses on
ST4NumRevs = 0 #This is used to dictate stairstep value
ST4Fl = OffsetValue #Flash Y coordinates
ST4Dir = 'down' #As grating is moved downwards and it's "behind motion", the flash will start ABOVE the horizontal meridian
ST4G = 'down' #Movement of grating

#Did a reversal occur
ReversalOccur = False #If True, then add all the good stuff

CurrentStairNum = 0 #What Num we are using now 
secdur = 2.3 #Second duration of grating
GratingDur = np.ceil(secdur * RefreshHz) #Grating duration in frames

#Grating dimensions, in DVA
GRHeight = 20.5
GRWidth = 3.6

#Grating x coordinates; y always zero
#Grating position (Inner gratings should be 3.85, outer gratings 8.98)
InnerRightX = 3.85

#Original paper had a 75hz monitor, at 0.2 luminance modulationsper dVA (this was just he spatial frequency!)
#As mentioned in building exps in psychoPY, phase is unconventional and done by cycles 
PhaseStep = 4/RefreshHz #How much the phase will change on each frame); (Number of cycles second/framerate)

## Record frame duration:
logging.console.setLevel(logging.WARNING) #Report warnings to the standard output window
PastCount = 0
win.refreshThreshold = (1/RefreshHz) * 1.1#Set a 10% tolerance for dropped frames

flashdur = 8 #np.ceil(60/(1000/RefreshHz)) # Flash duration should be ~ 60ms; THIS SHOULD BE 55MS, 

#GrateDur is 2.3ms in frames; flash 1200ms 900ms, 600ms, and 300ms before reversal (the end of our grating)
flashOnList = [np.round(GratingDur - (RefreshHz * (1200/1000))), np.round(GratingDur - (RefreshHz * (900/1000))), np.round(GratingDur - (RefreshHz * (600/1000))), np.round(GratingDur - (RefreshHz * (300/1000)))]
dist = 1.54 #Separation of the flash from the grating in dVA 

Rnormadj =0
Lnormadj = 0
Roffadj = 0
Loffadj = 0 #Set the adjustment values at 0
rflashY = 0 #placeholder to stop errors

#Size in degrees
FlW = 2.05
FlH = 0.25

FlashVal = 0 #Select flash value from staircases

#The x coordiantes are the centre of the rectangle. We want the edge of the rectangle to be exactly 1.54 from the edge of the grating
#So we shift the rectangle + half a rectangle, Also want to add it from THE EDGE OF THE GRATING 
RFlashX = InnerRightX + dist + (FlW/2) + (GRWidth/2) #Right flash xcoords
LeftFlash = visual.Rect(
    win=win, name='LeftFlash',
    width=(FlW, FlH)[0], height=(FlW, FlH)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1.0, depth=-6.0, interpolate=True)
RightFlash = visual.Rect(
    win=win, name='RightFlash',
    width=(FlW, FlH)[0], height=(FlW, FlH)[1],
    ori=0.0, pos=[0,0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1.0, depth=-7.0, interpolate=True)
resp = keyboard.Keyboard()
InnerLeftGrate = visual.GratingStim(
    win=win, name='InnerLeftGrate',units='deg', 
    tex='sin', mask=None,
    ori=90.0, pos=(-InnerRightX, 0.0), size=(GRHeight, GRWidth), sf=0.15, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=0.995, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-9.0)
InnerRightGrate = visual.GratingStim(
    win=win, name='InnerRightGrate',units='deg', 
    tex='sin', mask=None,
    ori=90.0, pos=(InnerRightX, 0.0), size=(GRHeight, GRWidth), sf=0.15, phase=0.0,
    color=[1,1,1], colorSpace='rgb',
    opacity=1.0, contrast=0.995, blendmode='avg',
    texRes=128.0, interpolate=True, depth=-10.0)
text = visual.TextStim(win=win, name='text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "PracRout"
PracRoutClock = core.Clock()
PracCount = 0 
PracEndText = "Press 'space' to continue."  #Placeholder

PassedPrac = False #Pass the practice trials
PracAns = '' #Correct answer for this trial
DispPracText = visual.TextStim(win=win, name='DispPracText',
    text='',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
finPrac = keyboard.Keyboard()

# Initialize components for Routine "AttentionCheck"
AttentionCheckClock = core.Clock()
attcheckstat = 0 #1 = passed, 2 = failed

PassCheck = False

AttAns = 'space' #The correct answer

NumFails = 0 #Count how many failed attention checked

FailedAtt = False #Did they fail the attention check

MyRed = (1, -1, -1)
myYell = (1.0000, 1.0000, -1.0000)
myGreen = (-1, 1, -1)
myOrange = (1.0000, 0.2941, -1.0000) 
myCyan = (-1.0000, 1.0000, 1.0000)
myMagneta = (1.0000, -1.0000, 1.0000)
myPurple = (0.0039, -1.0000, 0.0039) 

FixCol = MyRed

ColourList = [myYell, myGreen, MyRed, myPurple, myMagneta, myCyan, myOrange]
ListIdx = 0 #To select a colour from the list
updateon = 18 #Change colour after this many frames

AttISI = 0.8
timeLimit = 5 # 5 seconds is timeout, 2.5 seconds is time of exp
AttCheckResp = keyboard.Keyboard()
FPATT = visual.ShapeStim(
    win=win, name='FPATT', vertices='cross',
    size=(FPSize, FPSize),
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     colorSpace='rgb',  lineColor=FixCol, fillColor=FixCol,
    opacity=None, depth=-2.0, interpolate=True)

# Initialize components for Routine "Warning"
WarningClock = core.Clock()
WarningText = visual.TextStim(win=win, name='WarningText',
    text='',
    font='Arial',
    units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
Alt_Resp = keyboard.Keyboard()

# Initialise components for routien "Break" - TC, copied from another paradigm
BreakClock = core.Clock()
BreakText = visual.TextStim(win=win, name='BreakText',
    text="This is a break. Rest for as long as  you need! \n\nJust a friendly reminder that during the experiment, please stare at the red cross in the center of the screen. \n\nPress 's' when you are ready to resume the experiment.\n\n",
    font='Open Sans',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
Endbreak = keyboard.Keyboard()

# Initialize components for Routine "Conclusion"
ConclusionClock = core.Clock()
EndText = visual.TextStim(win=win, name='EndText',
    text='Thank you for participating in this experiment!\n\nPlease tell the researcher you have completed this experiment.',
    font='Arial',
    units='height', pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-1.0);
end_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
InstructionsComponents = [Welcome, key_resp]
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
        theseKeys = key_resp.getKeys(keyList=['right', 's'], waitRelease=False)
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
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Prac_or_live = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Select_Cond_File.xlsx'),
    seed=None, name='Prac_or_live')
thisExp.addLoop(Prac_or_live)  # add the loop to the experiment
thisPrac_or_live = Prac_or_live.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPrac_or_live.rgb)
if thisPrac_or_live != None:
    for paramName in thisPrac_or_live:
        exec('{} = thisPrac_or_live[paramName]'.format(paramName))

for thisPrac_or_live in Prac_or_live:
    currentLoop = Prac_or_live
    # abbreviate parameter names if possible (e.g. rgb = thisPrac_or_live.rgb)
    if thisPrac_or_live != None:
        for paramName in thisPrac_or_live:
            exec('{} = thisPrac_or_live[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    Condition_Loop = data.TrialHandler(nReps=NumReps, method='fullRandom', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(TypeFile),
        seed=None, name='Condition_Loop')
    thisExp.addLoop(Condition_Loop)  # add the loop to the experiment
    thisCondition_Loop = Condition_Loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCondition_Loop.rgb)
    if thisCondition_Loop != None:
        for paramName in thisCondition_Loop:
            exec('{} = thisCondition_Loop[paramName]'.format(paramName))
    
    for thisCondition_Loop in Condition_Loop:
        currentLoop = Condition_Loop
        # abbreviate parameter names if possible (e.g. rgb = thisCondition_Loop.rgb)
        if thisCondition_Loop != None:
            for paramName in thisCondition_Loop:
                exec('{} = thisCondition_Loop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        Reversal = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions(CondFile),
            seed=None, name='Reversal')
        thisExp.addLoop(Reversal)  # add the loop to the experiment
        thisReversal = Reversal.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisReversal.rgb)
        if thisReversal != None:
            for paramName in thisReversal:
                exec('{} = thisReversal[paramName]'.format(paramName))
        
        for thisReversal in Reversal:
            currentLoop = Reversal
            # abbreviate parameter names if possible (e.g. rgb = thisReversal.rgb)
            if thisReversal != None:
                for paramName in thisReversal:
                    exec('{} = thisReversal[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "Trials"-------
            continueRoutine = True
            # update component parameters for each repeat
            ## Was it a practice or live trial; is there an attention check soon?
            
            if TypeFile == 'PracCond.xlsx':
                wasPrac = True
            else:
                wasPrac = False
            
            thisExp.addData('wasPrac', wasPrac)
            
            if not wasPrac:
                trialCount += 1 #This counts the trials
            
            if trialCount in Tnum:
                #continueRoutine = False
                check = True
            ##Initialise the trial parameters in isi
            
            NumRepeats += 1 #This is to control reversal and stair enactment
            
            if ComboNum == 1:
                if NumRepeats == 1:
                    CurrentStairNum = 1
                elif NumRepeats  == 2:
                    CurrentStairNum = 3
            elif ComboNum == 2:
                if NumRepeats == 1:
                    CurrentStairNum = 1
                elif NumRepeats == 2:
                    CurrentStairNum = 4
            elif ComboNum == 3:
                if NumRepeats == 1:
                    CurrentStairNum = 2
                elif NumRepeats == 2:
                    CurrentStairNum = 3
            elif ComboNum == 4:
                if NumRepeats == 1:
                    CurrentStairNum = 2
                elif NumRepeats == 2:
                    CurrentStairNum = 4
            elif ComboNum == 5:
                if NumRepeats == 1:
                    CurrentStairNum = 3
                elif NumRepeats == 2:
                    CurrentStairNum = 1
            elif ComboNum == 6:
                if NumRepeats == 1:
                    CurrentStairNum = 3
                elif NumRepeats == 2:
                    CurrentStairNum = 2
            elif ComboNum == 7:
                if NumRepeats == 1:
                    CurrentStairNum = 4
                elif NumRepeats == 2:
                    CurrentStairNum = 1
            elif ComboNum == 8:
                if NumRepeats == 1:
                    CurrentStairNum = 4
                elif NumRepeats == 2:
                    CurrentStairNum = 2
            
            #At start of routine reset phase to 0
            InnerLeftGrate.setPhase(0)
            InnerRightGrate.setPhase(0)
            
            PhaseCounter = 0
            
            DisgardTrial = False
            #Randomly choose flash onset
            idx = randint(0, 4)
            flashon = flashOnList[idx]
            thisExp.addData('FlashOnset', flashon)
            
            if CurrentStairNum == 1:
                    FlashVal = ST1Fl
            elif CurrentStairNum == 2:
                    FlashVal = ST2Fl
            elif CurrentStairNum == 3:
                    FlashVal = ST3Fl 
            elif CurrentStairNum == 4:
                    FlashVal = ST4Fl
            
            if wasPrac:
                if Offset == 'Ahead':
                    if RightG == 'up':
                        FlashVal = OffsetValue
                    elif RightG == 'down':
                        FlashVal = - OffsetValue
                elif Offset == 'Behind':
                    if RightG == 'up':
                        FlashVal = -OffsetValue
                    elif RightG == 'down':
                        FlashVal = OffsetValue
            
            #The staircases were specified in the context of the right grating
            rflashY = FlashVal
            resp.keys = []
            resp.rt = []
            _resp_allKeys = []
            # keep track of which components have finished
            TrialsComponents = [ISI, FP, LeftFlash, RightFlash, resp, InnerLeftGrate, InnerRightGrate, text]
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
                
                
                #if int(expInfo['test']) == 1: #if test mode, log the frame interval for the last frame
                #    if len(win.frameIntervals):
                #        logging.debug('Last Frame Interval: ' + str(win.frameIntervals[-1])) #This will return the last frame interval appended

                # *FP* updates
                if FP.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    FP.frameNStart = frameN  # exact frame index
                    FP.tStart = t  # local t and not account for scr refresh
                    FP.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(FP, 'tStartRefresh')  # time at next scr refresh
                    FP.setAutoDraw(True)
                if t > 0.8 and win.recordFrameIntervals == True: #is isi over?
                    if LeftG == 'down':
                        InnerLeftGrate.setPhase(PhaseStep, '+')
                        InnerRightGrate.setPhase(PhaseStep, '-')
                    elif LeftG == 'up':
                        InnerLeftGrate.setPhase(PhaseStep, '-')
                        InnerRightGrate.setPhase(PhaseStep, '+')
                
                elif t > 0.8 and win.recordFrameIntervals == False:
                    win.recordFrameIntervals = True #Want to set this true only once
                
                # *LeftFlash* updates
                if LeftFlash.status == NOT_STARTED and frameN >= flashon:
                    # keep track of start time/frame for later
                    LeftFlash.frameNStart = frameN  # exact frame index
                    LeftFlash.tStart = t  # local t and not account for scr refresh
                    LeftFlash.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(LeftFlash, 'tStartRefresh')  # time at next scr refresh
                    LeftFlash.setAutoDraw(True)
                if LeftFlash.status == STARTED:
                    if frameN >= (LeftFlash.frameNStart + flashdur):
                        # keep track of stop time/frame for later
                        LeftFlash.tStop = t  # not accounting for scr refresh
                        LeftFlash.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(LeftFlash, 'tStopRefresh')  # time at next scr refresh
                        LeftFlash.setAutoDraw(False)
                
                # *RightFlash* updates
                if RightFlash.status == NOT_STARTED and frameN >= flashon:
                    # keep track of start time/frame for later
                    RightFlash.frameNStart = frameN  # exact frame index
                    RightFlash.tStart = t  # local t and not account for scr refresh
                    RightFlash.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(RightFlash, 'tStartRefresh')  # time at next scr refresh
                    RightFlash.setAutoDraw(True)
                if RightFlash.status == STARTED:
                    if frameN >= (RightFlash.frameNStart + flashdur):
                        # keep track of stop time/frame for later
                        RightFlash.tStop = t  # not accounting for scr refresh
                        RightFlash.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(RightFlash, 'tStopRefresh')  # time at next scr refresh
                        RightFlash.setAutoDraw(False)
                
                # *resp* updates
                waitOnFlip = False
                if resp.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
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
                    theseKeys = resp.getKeys(keyList=['right', 'left'], waitRelease=False)
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
                
                # *InnerLeftGrate* updates
                if InnerLeftGrate.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                    # keep track of start time/frame for later
                    InnerLeftGrate.frameNStart = frameN  # exact frame index
                    InnerLeftGrate.tStart = t  # local t and not account for scr refresh
                    InnerLeftGrate.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(InnerLeftGrate, 'tStartRefresh')  # time at next scr refresh
                    InnerLeftGrate.setAutoDraw(True)
                if InnerLeftGrate.status == STARTED:
                    if frameN >= (InnerLeftGrate.frameNStart + GratingDur):
                        # keep track of stop time/frame for later
                        InnerLeftGrate.tStop = t  # not accounting for scr refresh
                        InnerLeftGrate.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(InnerLeftGrate, 'tStopRefresh')  # time at next scr refresh
                        InnerLeftGrate.setAutoDraw(False)
                
                # *InnerRightGrate* updates
                if InnerRightGrate.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                    # keep track of start time/frame for later
                    InnerRightGrate.frameNStart = frameN  # exact frame index
                    InnerRightGrate.tStart = t  # local t and not account for scr refresh
                    InnerRightGrate.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(InnerRightGrate, 'tStartRefresh')  # time at next scr refresh
                    InnerRightGrate.setAutoDraw(True)
                if InnerRightGrate.status == STARTED:
                    if frameN >= (InnerRightGrate.frameNStart + GratingDur):
                        # keep track of stop time/frame for later
                        InnerRightGrate.tStop = t  # not accounting for scr refresh
                        InnerRightGrate.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(InnerRightGrate, 'tStopRefresh')  # time at next scr refresh
                        InnerRightGrate.setAutoDraw(False)
                
                # *ISI* period
                if ISI.status == NOT_STARTED and t >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ISI.frameNStart = frameN  # exact frame index
                    ISI.tStart = t  # local t and not account for scr refresh
                    ISI.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI, 'tStartRefresh')  # time at next scr refresh
                    ISI.start(0.8)
                elif ISI.status == STARTED:  # one frame should pass before updating params and completing
                    # updating other components during *ISI*
                    LeftFlash.setPos((-RFlashX, -rflashY))
                    RightFlash.setPos((RFlashX, rflashY))
                    # component updates done
                    ISI.complete()  # finish the static period
                    ISI.tStop = ISI.tStart + 0.8  # record stop time
                
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
            Reversal.addData('ISI.started', ISI.tStart)
            Reversal.addData('ISI.stopped', ISI.tStop)
            Reversal.addData('FP.started', FP.tStartRefresh)
            Reversal.addData('FP.stopped', FP.tStopRefresh)
            ## Save values
            thisExp.addData('TrialCount', trialCount)
            thisExp.addData('NumRepeats', NumRepeats)
            
            #You need to tell it what staircase it is, in the datafile:
            thisExp.addData("CurrentStair", CurrentStairNum)
            
            #Store the flash values for each staircase:
            thisExp.addData('ST1Fl', ST1Fl)
            thisExp.addData('ST2Fl', ST2Fl)
            thisExp.addData('ST3Fl', ST3Fl)
            thisExp.addData('ST4Fl', ST4Fl)
            
            #Add current staircase direction
            thisExp.addData('ST1Dir', ST1Dir)
            thisExp.addData('ST2Dir', ST2Dir)
            thisExp.addData('ST3Dir', ST3Dir)
            thisExp.addData('ST4Dir', ST4Dir)
            
            #Add staircase stepsize that will be applied
            thisExp.addData('ST1Step', stairStepList[ST1Step])
            thisExp.addData('ST2Step', stairStepList[ST2Step])
            thisExp.addData('ST3Step', stairStepList[ST3Step])
            thisExp.addData('ST4Step', stairStepList[ST4Step])
            
            #A correct response means the grating that was going up, was reported as higher
            # A stair direction of up means we're increasing the flash's height; down decreasing flash's height
            
            ## Change staircase
            #if check == False:
            if CurrentStairNum == 1:
                ST1TC += 1
                if resp.corr == 1:
                    if ST1Dir == 'up': #IF STAIR = UP, it means a reversal NEEDS TO occur
                        ST1Dir = 'down' #Down means lower the flash's height
                        ReversalOccur = True
                        revVal = ST1Fl
                        ST1NumRevs += 1
                        ST1RevVals.append(ST1Fl) #Store the value that triggered the reversal
                        if ST1NumRevs >= NumRev: #The index for the Steplist is [0, 1]
                            ST1Step = 1
                    ST1Fl -= stairStepList[ST1Step]
                else:
                    if ST1Dir == 'down': 
                        ST1Dir = 'up'
                        ReversalOccur = True
                        revVal = ST1Fl
                        ST1NumRevs += 1
                        ST1RevVals.append(ST1Fl)
                        if ST1NumRevs >= NumRev:
                            ST1Step = 1
                    ST1Fl += stairStepList[ST1Step]
                ST1Fl = round(ST1Fl  * 100000)/100000

            elif CurrentStairNum == 2:
                ST2TC += 1
                if resp.corr == 1:
                    if ST2Dir == 'up':
                        ST2Dir = 'down'
                        ReversalOccur = True
                        revVal = ST2Fl
                        ST2NumRevs += 1
                        ST2RevVals.append(ST2Fl)
                        if ST2NumRevs >= NumRev:
                            ST2Step = 1
                    ST2Fl -= stairStepList[ST2Step]
                else:
                    if ST2Dir == 'down': 
                        ST2Dir = 'up'
                        ReversalOccur = True
                        revVal = ST2Fl
                        ST2NumRevs += 1
                        ST2RevVals.append(ST2Fl)
                        if ST2NumRevs >= NumRev:
                            ST2Step = 1
                    ST2Fl += stairStepList[ST2Step]
                ST2Fl = round(ST2Fl  * 100000)/100000
            elif CurrentStairNum == 3:
                ST3TC += 1
                if resp.corr == 1:
                    if ST3Dir == 'up':
                        ST3Dir = 'down'
                        ReversalOccur = True
                        ST3NumRevs += 1
                        revVal = ST3Fl
                        ST3RevVals.append(ST3Fl)
                        if ST3NumRevs >= NumRev:
                            ST3Step = 1
                    ST3Fl -= stairStepList[ST3Step]
                else:
                    if ST3Dir == 'down': 
                        ST3Dir = 'up'
                        ReversalOccur = True
                        ST3NumRevs += 1
                        revVal = ST3Fl #RevVal basically serves as a check/guarantee on what the reversal value was
                        ST3RevVals.append(ST3Fl)
                        if ST3NumRevs >= NumRev:
                            ST3Step = 1
                    ST3Fl += stairStepList[ST3Step]
                ST3Fl = round(ST3Fl  * 100000)/100000
            elif CurrentStairNum == 4:
                ST4TC += 1
                if resp.corr == 1:
                    if ST4Dir == 'up':
                        ST4Dir = 'down'
                        ReversalOccur = True
                        revVal = ST4Fl
                        ST4NumRevs += 1
                        ST4RevVals.append(ST4Fl)
                        if ST4NumRevs >= NumRev:
                            ST4Step = 1
                    ST4Fl -= stairStepList[ST4Step]
                else:
                    if ST4Dir == 'down': 
                        ST4Dir = 'up'
                        ReversalOccur = True
                        revVal = ST4Fl
                        ST4NumRevs += 1
                        ST4RevVals.append(ST4Fl)
                        if ST4NumRevs >= NumRev:
                            ST4Step = 1
                    ST4Fl += stairStepList[ST4Step]
                ST4Fl = round(ST4Fl  * 100000)/100000
            
            if ReversalOccur == True: #We do this as just a sanity check
                thisExp.addData('revVal', revVal)
            
            ReversalOccur = False
            
            #Store reversal values
            thisExp.addData('ST1NumRevs', ST1NumRevs)
            thisExp.addData('ST2NumRevs', ST2NumRevs)
            thisExp.addData('ST3NumRevs', ST3NumRevs)
            thisExp.addData('ST4NumRevs', ST4NumRevs)
            
            #Add stair trial counts
            #if check == False:
            thisExp.addData('ST1TC', ST1TC)
            thisExp.addData('ST2TC', ST2TC)
            thisExp.addData('ST3TC', ST3TC)
            thisExp.addData('ST4TC', ST4TC)
            
            
            #Whenever the second repeat hits 2, reset to 0
            if NumRepeats == 2:
                NumRepeats = 0
            win.recordFrameIntervals = False ## In the event the grating never officially ends, do this here:
            thisExp.addData('AutoDroppedFrames', win.nDroppedFrames)
            
            if win.nDroppedFrames > PastCount:
                DisgardTrial = True
            
            thisExp.addData('DisgardTrial', DisgardTrial)
            
            PastCount = win.nDroppedFrames #Previous trials dropped frames
            thisExp.addData('RIGHTflash', rflashY)
            Reversal.addData('LeftFlash.started', LeftFlash.tStartRefresh)
            Reversal.addData('LeftFlash.stopped', LeftFlash.tStopRefresh)
            Reversal.addData('RightFlash.started', RightFlash.tStartRefresh)
            Reversal.addData('RightFlash.stopped', RightFlash.tStopRefresh)
            # check responses
            if resp.keys in ['', [], None]:  # No response was made
                resp.keys = None
                # was no response the correct answer?!
                if str(CorrAns).lower() == 'none':
                   resp.corr = 1;  # correct non-response
                else:
                   resp.corr = 0;  # failed to respond (incorrectly)
            # store data for Reversal (TrialHandler)
            Reversal.addData('resp.keys',resp.keys)
            Reversal.addData('resp.corr', resp.corr)
            if resp.keys != None:  # we had a response
                Reversal.addData('resp.rt', resp.rt)
            Reversal.addData('resp.started', resp.tStartRefresh)
            Reversal.addData('resp.stopped', resp.tStopRefresh)
            Reversal.addData('InnerLeftGrate.started', InnerLeftGrate.tStartRefresh)
            Reversal.addData('InnerLeftGrate.stopped', InnerLeftGrate.tStopRefresh)
            Reversal.addData('InnerRightGrate.started', InnerRightGrate.tStartRefresh)
            Reversal.addData('InnerRightGrate.stopped', InnerRightGrate.tStopRefresh)
            # the Routine "Trials" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "PracRout"-------
            continueRoutine = True
            routineTimer.add(10.000000)
            # update component parameters for each repeat
            if not wasPrac:
                continueRoutine = False
            else:
                PRFlashYRight = FlashVal
                PRFlashYLeft = PRFlashYRight * -1
                
                #resp.corr means they said it was right that was higher
                if Offset == 'Ahead':
                    if resp.corr:
                        if RightG == 'up':
                            PassedPrac = True
                        else: #rightg down, so flash is down
                            PassedPrac = False
                            PracAns = 'left'
                    else: #Grating must be moving down, flash would be offset at the bottom
                        if RightG == 'up':
                            PassedPrac = False
                            PracAns = 'right'
                        else: #If right g is going down, for ahead, the right flash will be neg y.
                            PassedPrac = True
                elif Offset == 'Behind':
                    if resp.corr:
                        if RightG == 'up':
                            PassedPrac = False #flash would be below 0
                            PracAns = 'left'
                        else: #right going down, so flash will be above 0
                            PassedPrac = True
                    else: #they said left was higher
                        if RightG == 'up':
                            PassedPrac = True #Flash would be offset above
                        else: #right going down, so behind puts flash above 0
                            PassedPrac = False
                            PracAns = 'right'
            
                PracCount += 1 #Count how many practice trials
                thisExp.addData('PracCount', PracCount)
                if PracCount == 4: #End of prac trials
                    PracEndText = '\n' + ' This is the end of the practice trials. ' + "Press 'space' to begin the live experiment"
            
                if PassedPrac == 1:
                    PracText = "That response is correct! Good work" + '\n' + PracEndText
                else:
                    PracText = "Unfortunately, that response was incorrect. The correct answer was: " + PracAns + '. As this flash was the highest.' + "\n" + "\n" + "Friendly reminder, please use the 'right' and 'left' arrow keys to report which flash is higher than the other" + "\n" + "If the left flash is the highest, press 'left'. If the right flash is higher, press 'right'" + '\n' + PracEndText
            DispPracText.setText(PracText)
            finPrac.keys = []
            finPrac.rt = []
            _finPrac_allKeys = []
            # keep track of which components have finished
            PracRoutComponents = [DispPracText, finPrac]
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
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = PracRoutClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=PracRoutClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *DispPracText* updates
                if DispPracText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    DispPracText.frameNStart = frameN  # exact frame index
                    DispPracText.tStart = t  # local t and not account for scr refresh
                    DispPracText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(DispPracText, 'tStartRefresh')  # time at next scr refresh
                    DispPracText.setAutoDraw(True)
                if DispPracText.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > DispPracText.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        DispPracText.tStop = t  # not accounting for scr refresh
                        DispPracText.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(DispPracText, 'tStopRefresh')  # time at next scr refresh
                        DispPracText.setAutoDraw(False)
                
                # *finPrac* updates
                waitOnFlip = False
                if finPrac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    finPrac.frameNStart = frameN  # exact frame index
                    finPrac.tStart = t  # local t and not account for scr refresh
                    finPrac.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(finPrac, 'tStartRefresh')  # time at next scr refresh
                    finPrac.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(finPrac.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(finPrac.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if finPrac.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > finPrac.tStartRefresh + 10.0-frameTolerance:
                        # keep track of stop time/frame for later
                        finPrac.tStop = t  # not accounting for scr refresh
                        finPrac.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(finPrac, 'tStopRefresh')  # time at next scr refresh
                        finPrac.status = FINISHED
                if finPrac.status == STARTED and not waitOnFlip:
                    theseKeys = finPrac.getKeys(keyList=['y', 'n', 'space'], waitRelease=False)
                    _finPrac_allKeys.extend(theseKeys)
                    if len(_finPrac_allKeys):
                        finPrac.keys = _finPrac_allKeys[-1].name  # just the last key pressed
                        finPrac.rt = _finPrac_allKeys[-1].rt
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
            # check responses
            if finPrac.keys in ['', [], None]:  # No response was made
                finPrac.keys = None
            Reversal.addData('finPrac.keys',finPrac.keys)
            if finPrac.keys != None:  # we had a response
                Reversal.addData('finPrac.rt', finPrac.rt)
            
            # ------Prepare to start Routine "AttentionCheck"-------
            continueRoutine = True
            #routineTimer.add(4.600000) - > Commenting out as they get unlimited time for this now (like in other paradigms)
            # update component parameters for each repeat
            if check != True:
                continueRoutine = False
            else:
                PassCheck = False
                FixCol = MyRed
                FPATT.setColor(FixCol)
            AttCheckResp.keys = []
            AttCheckResp.rt = []
            _AttCheckResp_allKeys = []
            # keep track of which components have finished
            AttentionCheckComponents = [AttCheckResp, FPATT]
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
            while continueRoutine: #and routineTimer.getTime() > 0: : #WE WANT TO GIVE UNLIMITED TIME FOR THE ATTENTION CHCK 
                # get current time
                t = AttentionCheckClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=AttentionCheckClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                if t >= AttISI and t <= (AttISI + 1): #We want only want the fixation to change colour for 1 second
                    if frameN % updateon == 0:
                        FixCol = ColourList[ListIdx]
                        FPATT.setColor(FixCol)
                        ListIdx += 1
                        if ListIdx == (len(ColourList) - 1):
                            ListIdx = 0 #Reset index when it hits max list
                else:
                    FixCol = MyRed
                    FPATT.setColor(FixCol)
                
                if t >= AttISI and t <= (AttISI + secdur):  ## We want the grating to move for the same duration as the trials. 
                    ## Only draw/update the grating when appropriate
                    if LeftG == 'down':
                        InnerLeftGrate.setPhase(PhaseStep, '+')
                        InnerRightGrate.setPhase(PhaseStep, '-')
                    elif LeftG == 'up':
                        InnerLeftGrate.setPhase(PhaseStep, '-')
                        InnerRightGrate.setPhase(PhaseStep, '+')
                    InnerLeftGrate.draw()
                    InnerRightGrate.draw()
                                    
                
                # *AttCheckResp* updates
                waitOnFlip = False
                if AttCheckResp.status == NOT_STARTED and tThisFlip >= 0.8-frameTolerance:
                    # keep track of start time/frame for later
                    AttCheckResp.frameNStart = frameN  # exact frame index
                    AttCheckResp.tStart = t  # local t and not account for scr refresh
                    AttCheckResp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(AttCheckResp, 'tStartRefresh')  # time at next scr refresh
                    AttCheckResp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(AttCheckResp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(AttCheckResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                    
                if AttCheckResp.status == STARTED and not waitOnFlip:
                    theseKeys = AttCheckResp.getKeys(keyList=['space', 'left', 'right', 'r'], waitRelease=False)
                    _AttCheckResp_allKeys.extend(theseKeys)
                    if len(_AttCheckResp_allKeys):
                        AttCheckResp.keys = _AttCheckResp_allKeys[-1].name  # just the last key pressed
                        AttCheckResp.rt = _AttCheckResp_allKeys[-1].rt
                        # was this correct?
                        if (AttCheckResp.keys == str(AttAns)) or (AttCheckResp.keys == AttAns):
                            AttCheckResp.corr = 1
                        else:
                            AttCheckResp.corr = 0
                        # a response ends the routine, WE ALSO NEED TO PURGE OFF THE GRATINGS PLEASE so that the ISI occurs for the trials
                        FP.draw()
                        win.flip()
                        continueRoutine = False
                
                # *FPATT* updates
                if FPATT.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    FPATT.frameNStart = frameN  # exact frame index
                    FPATT.tStart = t  # local t and not account for scr refresh
                    FPATT.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(FPATT, 'tStartRefresh')  # time at next scr refresh
                    FPATT.setAutoDraw(True)
                
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
            if check == True:
                if AttCheckResp.corr == 1 or AttCheckResp.keys == 'r':
                    PassCheck = True #Att check passed
                else:
                    PassCheck = False #Att check failed
                    warning = True
                    NumFails += 1
                    if NumFails >= 2:
                        FailedAtt = True
                thisExp.addData('NumFails', NumFails)
                thisExp.addData('FailedAtt', FailedAtt)
                thisExp.addData('PassCheck', PassCheck)
            
            FixCol = MyRed
            FPATT.setColor(FixCol)
            # check responses
            if AttCheckResp.keys in ['', [], None]:  # No response was made
                AttCheckResp.keys = None
                # was no response the correct answer?!
                if str(AttAns).lower() == 'none':
                   AttCheckResp.corr = 1;  # correct non-response
                else:
                   AttCheckResp.corr = 0;  # failed to respond (incorrectly)
            # store data for Reversal (TrialHandler)
            Reversal.addData('AttCheckResp.keys',AttCheckResp.keys)
            Reversal.addData('AttCheckResp.corr', AttCheckResp.corr)
            if AttCheckResp.keys != None:  # we had a response
                Reversal.addData('AttCheckResp.rt', AttCheckResp.rt)
            Reversal.addData('AttCheckResp.started', AttCheckResp.tStartRefresh)
            Reversal.addData('AttCheckResp.stopped', AttCheckResp.tStopRefresh)
            Reversal.addData('FPATT.started', FPATT.tStartRefresh)
            Reversal.addData('FPATT.stopped', FPATT.tStopRefresh)
            
            # ------Prepare to start Routine "Warning"-------
            continueRoutine = True
            # update component parameters for each repeat
            ExtraText = "Oops. It looks like you took a little too long to respond to the last appearance of the illusion." + "\n" + " Please try to respond as fast as possible!"
            
            if check != True or PassCheck == True:
                continueRoutine = False
                
            if PassCheck == False: #Did you pass the attention check
                ExtraText = 'Unfortunately, you pressed the wrong key during the attention check or you did not respond.' + '\n' + "When you see the cross in the centre of the screen change colour, please press 'r'" 
            else:
                ExtraText = 'Good work! You passed the attention check!'
            WarningText.setText(ExtraText + '\n' + '\n' + 'Just a friendly reminder to please stare at the cross in the center of the screen during the experiment.' + '\n' + '\n' + "Press 's' to resume the experiment. ")
            Alt_Resp.keys = []
            Alt_Resp.rt = []
            _Alt_Resp_allKeys = []
            # keep track of which components have finished
            WarningComponents = [WarningText, Alt_Resp]
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
                
                # *WarningText* updates
                if WarningText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    WarningText.frameNStart = frameN  # exact frame index
                    WarningText.tStart = t  # local t and not account for scr refresh
                    WarningText.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(WarningText, 'tStartRefresh')  # time at next scr refresh
                    WarningText.setAutoDraw(True)
                
                # *Alt_Resp* updates
                waitOnFlip = False
                if Alt_Resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    Alt_Resp.frameNStart = frameN  # exact frame index
                    Alt_Resp.tStart = t  # local t and not account for scr refresh
                    Alt_Resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Alt_Resp, 'tStartRefresh')  # time at next scr refresh
                    Alt_Resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(Alt_Resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(Alt_Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if Alt_Resp.status == STARTED and not waitOnFlip:
                    theseKeys = Alt_Resp.getKeys(keyList=['y', 'n', 's'], waitRelease=False)
                    _Alt_Resp_allKeys.extend(theseKeys)
                    if len(_Alt_Resp_allKeys):
                        Alt_Resp.keys = _Alt_Resp_allKeys[-1].name  # just the last key pressed
                        Alt_Resp.rt = _Alt_Resp_allKeys[-1].rt
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
            warning = False
            check = False
            Reversal.addData('WarningText.started', WarningText.tStartRefresh)
            Reversal.addData('WarningText.stopped', WarningText.tStopRefresh)
            # check responses
            if Alt_Resp.keys in ['', [], None]:  # No response was made
                Alt_Resp.keys = None
            Reversal.addData('Alt_Resp.keys',Alt_Resp.keys)
            if Alt_Resp.keys != None:  # we had a response
                Reversal.addData('Alt_Resp.rt', Alt_Resp.rt)
            Reversal.addData('Alt_Resp.started', Alt_Resp.tStartRefresh)
            Reversal.addData('Alt_Resp.stopped', Alt_Resp.tStopRefresh)
            # the Routine "Warning" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset() #reset, even though it wasn't used 
            
                 # ------Prepare to start Routine "Break"-------
            if trialCount == 104:
                continueRoutine = True
            else:
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
                    theseKeys = Endbreak.getKeys(keyList=['E', 'S', 's'], waitRelease=False)
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
            Reversal.addData('BreakText.started', BreakText.tStartRefresh)
            Reversal.addData('BreakText.stopped', BreakText.tStopRefresh)
            # check responses
            if Endbreak.keys in ['', [], None]:  # No response was made
                Endbreak.keys = None
            Reversal.addData('Endbreak.keys',Endbreak.keys)
            if Endbreak.keys != None:  # we had a response
                Condition_Loop.addData('Endbreak.rt', Endbreak.rt)
            Reversal.addData('Endbreak.started', Endbreak.tStartRefresh)
            Reversal.addData('Endbreak.stopped', Endbreak.tStopRefresh)
            # the Routine "Break" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
        # completed 1.0 repeats of 'Reversal'
        
    # completed 1.0 repeats of 'Condition_Loop'
    
# completed 1.0 repeats of 'Prac_or_live'


# ------Prepare to start Routine "Conclusion"-------
continueRoutine = True
# update component parameters for each repeat
thisExp.addData("globalClockTime", globalClock.getTime()) 

win.mouseVisible = True

#impath = 'FD\Intervals\Images\'
#textpath = 'FD\Intervals\Text\'

FILE_NAME_TEXT=('Intervals\Text\FD' + "_FrameIntervals_" + str(expInfo['participant']) + 'session_' + str(expInfo['session']) + '.log')
FILE_NAME_PNG = ('Intervals\Images\FD' + expName + "_FrameIntervals_" + str(expInfo['participant']) + 'session_' + str(expInfo['session']) + '.png')

import matplotlib.pyplot as plt

end_resp.keys = []
end_resp.rt = []
_end_resp_allKeys = []
#Calculate threshold over last five reversals
avRev = 6 #Average over how many reversals?

ST1Thresh = average(ST1RevVals[-avRev:-1])
ST2Thresh = average(ST2RevVals[-avRev:-1])
ST3Thresh = average(ST3RevVals[-avRev:-1])
ST4Thresh = average(ST4RevVals[-avRev:-1])

#Store threshold
thisExp.addData('ST1Thresh', ST1Thresh)
thisExp.addData('ST2Thresh', ST2Thresh)
thisExp.addData('ST3Thresh', ST3Thresh)
thisExp.addData('ST4Thresh', ST4Thresh)

#Store reversal values:
thisExp.addData('ST1RevVals', ST1RevVals)
thisExp.addData('ST2RevVals', ST2RevVals)
thisExp.addData('ST3RevVals', ST3RevVals)
thisExp.addData('ST4RevVals', ST4RevVals)
# keep track of which components have finished
ConclusionComponents = [EndText, end_resp]
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
    
    # *EndText* updates
    if EndText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        EndText.frameNStart = frameN  # exact frame index
        EndText.tStart = t  # local t and not account for scr refresh
        EndText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(EndText, 'tStartRefresh')  # time at next scr refresh
        EndText.setAutoDraw(True)
    
    # *end_resp* updates
    waitOnFlip = False
    if end_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_resp.frameNStart = frameN  # exact frame index
        end_resp.tStart = t  # local t and not account for scr refresh
        end_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_resp, 'tStartRefresh')  # time at next scr refresh
        end_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_resp.status == STARTED and not waitOnFlip:
        theseKeys = end_resp.getKeys(keyList=['i', 'space'], waitRelease=False)
        _end_resp_allKeys.extend(theseKeys)
        if len(_end_resp_allKeys):
            end_resp.keys = _end_resp_allKeys[-1].name  # just the last key pressed
            end_resp.rt = _end_resp_allKeys[-1].rt
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
## Save a plot of the intervals
if end_resp.keys == 'space':
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

thisExp.addData('EndText.started', EndText.tStartRefresh)
thisExp.addData('EndText.stopped', EndText.tStopRefresh)
# check responses
if end_resp.keys in ['', [], None]:  # No response was made
    end_resp.keys = None
thisExp.addData('end_resp.keys',end_resp.keys)
if end_resp.keys != None:  # we had a response
    thisExp.addData('end_resp.rt', end_resp.rt)
thisExp.addData('end_resp.started', end_resp.tStartRefresh)
thisExp.addData('end_resp.stopped', end_resp.tStopRefresh)
thisExp.nextEntry()
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
