%% Flash Grab Analysis
%Written by Timothy Cottier, PhD student at University of Melbourne. 
    % Assistance provided by A/Prof Dr Hinze Hogendoorn and Dr. Will Turner

%% Housekeeping
close all; clear all; clc;

%%% Plot graphs?
GraphPlot = 0; %0 = False; 1 = True

RefreshRate = 144; 
FrameDur = 1000/RefreshRate; %Duration in MS

%% Data importation paramaters
if ispc
    dataLocation = '';
    ImDir = '';
    addpath(genpath('')); %Add function folder to path
elseif ismac
    dataLocation = '';
    ImDir = ''; 
    addpath(genpath('Function Folder')); %Add function folder to path
end

addpath(dataLocation); %Add data location to path
DataType = [filesep '*.csv'];

FilesinDir = dir(strcat(dataLocation, DataType)); % Files currently in directory
DataFileNames = {FilesinDir.name}'; % The names of the data files
NumParts = length(DataFileNames); %Sample size (total number of files)

CW_IMDIR = [ImDir, filesep 'CW_Trials']; % Folder for clockwise images
CCW_IMDIR = [ImDir filesep 'CCW_Trials']; %Folder for counter-clockwise images
if ~isfolder(CW_IMDIR) % If folder doesn't currently exist
    mkdir(CW_IMDIR); % Make folder
end
if ~isfolder(CCW_IMDIR)
    mkdir(CCW_IMDIR);
end

%% Initialise variables to store the effect
%%% Split effect by direction
CW_S1 = []; % Session 1 Clockwise
CCW_S1 = []; % Session 1 counterclockwise
%Session 2
CW_S2 = []; %Session 2 clockwise
CCW_S2 = []; %Session 2 counterclockwise

%For the CW and CCW store their pre-effect values
Raw_Storage_S1 = []; %Col 1 = part; Col 2 = CW; Col 3 = CCW
Raw_Storage_S2 = []; %Col 1 = part; Col 2 = CW; Col 3 = CCW

%--- Variable that stores the FG effect --- 
FG_Effect_S1 = [];
FG_Effect_S2 = [];
FG_Effect_Overall = [];

%-- Variable to store date (in column 3)
FG_Date_S1 ={};
FG_Date_S2 = {}; 

%%%%% Initialise variable to store outliers
%Col 1 = Part; Col 2 = ID
CW_Outliers = [];
CCW_Outliers = [];
Outlier_List_CW = [];
Outlier_List_CCW = [];
Num_Outliers = []; %Num of outliers per participant [Part, Session, CW, CCW]

%Initialise index variables for CW and CCW
CW_IDX = [];
CCW_IDX = [];

%%% Equal amount of trials? Store the group count of each condition for each participant
TrialCount_Check = []; %Each row is a separate participant, each page is a separate session

%- Initialise variable to store effect by inducer duration
Inducer_Part = []; %P1=CW; P2=CCW; C1=SubID; C2=700; C3=800; C4=900; C5=1000; C6=1100; C7=1200

%% Rules for excluding participants
%%%% Invalid responses (click fixation, not target)
NumTrials = 180; % N trials completed
Percent_Invalid = 10; % Percentage of total trials that can be invalid before participants are excluded.
Invalid_Thresh = NumTrials * (Percent_Invalid/100); % If more than this many trials is invalid, exclude
Invalid_Idx = 0; % This is an index to choose which row to store the particpant in, if they exceed threshold
Invalid_Responses = []; % Participants with too many invalid trials; Col 1 = Part, Col 2 = Sess; Col 3 = Num invalid responses
All_InvalidResps = []; % Store Num of Invalid trials per participant

% Define the dimension of the circle used to remove trials
Circle_Rad = 200; %Radius of the exclusive zone in pixels

%%%% Miss/fail catch trials
% PassCheck did they pass the CatchCond? To pass, mouse had to be within 50
    % pixels of the x and y coordinate.
%--- A variable to store the passchecks for all participant
    % Col 1 = Part, Col 2 = Sess, Col 3 = Proportion of checks passed
NumCatch = 20; % How many catch trials was there total (4 catch trials for every loop; 5 repeats)
PassCheck_All = [];
PassCheck_Failed = []; %Failed because they missed 20% of the attention checks
PassCheck_Idx = 0;  %Use this index to store participant's sequentially
Pass_Thresh = 0.8 * NumCatch; %Exceed this threshold to pass the attention check

%% Response storage - parameters
%--- Store the coordinates of each response
Coords_MouseReps=[]; % C1 = Part, C2 = Sess, C3 = mouseResp_Y, C4= MouseResp_X
%--- Store the coordinates of the target
Targs_Coords=[]; %C1 = Part, C2 = Sess, C3 = mouseResp_Y, C4= MouseResp_X
%--- Store the response for each type X coordinate location of the target
Resp_Split_Targ = []; 
%----- Split by direction
Resp_Split_CW = [];
Resp_Split_CCW = [];

%% Specify radial trajectory parameters
TargRad = 450; % Radius of the target in pixels

%% Data import loop
for N_file = 1:length(DataFileNames) %We want it to loop through the calculations for each participant 
    clear('FGTab'); %To minimise errors from the previous iteration, clear variables
    FGTab = readtable(string(DataFileNames(N_file))); %For each file, read in the table 
    CurrentPart = max(FGTab.participant); %Current participant
    CurrentSession = max(FGTab.session); %Current session

    %% Catch/attention check trials
    NumPass = sum(strcmp(FGTab.PassCheck, 'True')); %Catch trials passed? 
    FGTab = FGTab(strcmp(FGTab.CatchCond, 'No'), :); %Remove catch trials for analysis
    PassCheck_All(N_file, :) = [CurrentPart CurrentSession NumPass];
    Failed_AttCheck = false; %Reset to false
    
    if NumPass < Pass_Thresh %Have to get 80% of catch trials to pass
        Failed_AttCheck = true;
        PassCheck_Idx = PassCheck_Idx + 1;
        PassCheck_Failed(PassCheck_Idx,:) = [CurrentPart CurrentSession NumPass];
    end
    
    %% Remove people with too many invalid responses
    %-- Firstly, need  to identify how many invalid responses they made
    %Calculate the distance for each response from origin
    Distance = sqrt((FGTab.mouseResp_x).^2 + (FGTab.mouseResp_y).^2); %From origin
    Num_InvalidResp = sum(Distance<Circle_Rad); %An invalid response, and then one within the circle
    All_InvalidResps(N_file, 1:3) = [CurrentPart, CurrentSession, Num_InvalidResp]; % Store number of invalid responses
    
    %Does the number of valid responses exceed the threshold?
    if Num_InvalidResp > Invalid_Thresh
        Exceeded_Invalid_Thresh = true;
        Invalid_Idx = Invalid_Idx + 1; 
        Invalid_Responses(Invalid_Idx, 1:3) = [CurrentPart, CurrentSession, Num_InvalidResp];
    else
        Exceeded_Invalid_Thresh = false;
    end

    %% Split by inducer duration (Ms_Travelled)
    FGTab.Ms_Travelled = FGTab.OriSTOP * FrameDur; %Convert from frames to MS

%% Store the y coordinates of each response for each participant
CArray = [FGTab.participant, FGTab.session, FGTab.mouseResp_y, FGTab.mouseResp_x]; %Resp array
[G, ID] = findgroups(FGTab.DegTargX); %Targ coordinates array - > Left, Centre, and Right groups

% Use G (group number) as the page index - Each page represents a different position (e.g., left, right) of the target
for i = 1:3;
    Group_IDX = G == i;
    %-- Split FGTab by group idx and direction
    Split_FG = FGTab(Group_IDX, :);
    RST(:, :, i) = [Split_FG.participant, Split_FG.session, Split_FG.mouseResp_x, Split_FG.mouseResp_y];
end

T_Array = [FGTab.participant, FGTab.session, FGTab.DegTargY, FGTab.DegTargX]; %Temporary array for target coordinates

if N_file == 1 % On file one, just initialise the variable with the array
    Resp_Split_Targ = RST; 
    Coords_MouseReps = CArray;
    Targs_Coords = [T_Array];
else
    Resp_Split_Targ = [Resp_Split_Targ; RST]; %After file 1, just append array to existing Resp_Split_Targ
    Coords_MouseReps = [Coords_MouseReps; CArray];
    Targs_Coords = [Targs_Coords; T_Array];
end

%% Convert from polar angle to arc length
%-- Start off by converting the effect into radians
FGTab.Effect_Rad = deg2rad(FGTab.FlashGrabEffect);

%-- Caculate the arc length
FGTab.ALength = TargRad * FGTab.Effect_Rad; 

%-- Convert arc length from pixels to degrees of visual angle
FGTab.Effect_Dva = TC_DVA(FGTab.ALength);

%% SPLIT FG TABLE BY REVERSAL DIRECTION
    FGTab_CW = FGTab(strcmp(FGTab.RevDir, 'CW'), :);
    FGTab_CCW = FGTab(strcmp(FGTab.RevDir, 'CCW'), :);

%Extract the illusion effect, trial by trial
    CW_FGE = [FGTab_CW.FlashGrabEffect];
    CCW_FGE = [FGTab_CCW.FlashGrabEffect];

    CW_DVA = [FGTab_CW.Effect_Dva];
    CCW_DVA = [FGTab_CCW.Effect_Dva]; 

%% Split store the responses split by the target position, split by direction
    [GCW, CW_ID] = findgroups(FGTab_CW.DegTargX); %CW -Clockwise
    [GCCW, CCW_ID] = findgroups(FGTab_CCW.DegTargX); %CCW
    
    for ii = 1:3;
        CW_IDX = GCW == ii; % Use GCW or GCCW as the page index
        CCW_IDX = GCCW == ii;
    
        %-- Split FGTab by group idx
        Split_FG_CW = FGTab_CW(CW_IDX, :); % CW
        Split_FG_CCW = FGTab_CCW(CCW_IDX, :); %CCW
    
        % For each participant get the three target position split by direction(CW, CCW)
        RST_CW(:, :,ii) = [Split_FG_CW.participant, Split_FG_CW.session, Split_FG_CW.mouseResp_x, Split_FG_CW.mouseResp_y];
        RST_CCW(:, :, ii) = [Split_FG_CCW.participant, Split_FG_CCW.session, Split_FG_CCW.mouseResp_x, Split_FG_CCW.mouseResp_y];
    end

    if N_file == 1 % Again, if file 1, just initialise variable with the arrays
        Resp_Split_CW = RST_CW;
        Resp_Split_CCW = RST_CCW;
    else
        Resp_Split_CW = [Resp_Split_CW; RST_CW];
        Resp_Split_CCW = [Resp_Split_CCW; RST_CCW];
    end

%% Identify responses that could be outliers
Z_CW = zscore(CW_FGE); % %Col 1 = part; Col 2 = Z-scoree
Z_CCW = zscore(CCW_FGE);
Z_Threshold = 3; %Z's above this are likely an outlier
CW_IDX = logical((abs(Z_CW) > 3)');
CCW_IDX = logical((abs(Z_CCW) > 3)');

CWOutliers = Z_CW(CW_IDX, 1);
CCWOutliers = Z_CCW(CCW_IDX, 1);

Num_CW_Out = sum(CW_IDX); %Number of CW Outliers
Num_CCW_Out = sum(CCW_IDX); %Number of CCW outlier
Num_Outliers(N_file, :) = [CurrentPart CurrentSession Num_CW_Out Num_CCW_Out];

%%% This notes if there was an outlier trial
if ~isempty(CWOutliers) %if either of these lists is NOT EMPTY, there's an outlier
    Outlier_List_CW(N_file, :) = CurrentPart;   
end
if ~isempty(CCWOutliers)
    Outlier_List_CCW(N_file, :) = CurrentPart;   
end

%% Illusory effect (FlashGrabEffect)
%The effect = difference between the final mouse position and the target
%%% Interpretation:
        %(+) = Target reported displaced in direction of reversal
        %(-) = Target reported displaced direction opposite reversal
        %NaN = Catch trials

%Create an average for each direction
CW_Effect = mean(FGTab_CW.FlashGrabEffect); 
CCW_Effect = mean(FGTab_CCW.FlashGrabEffect);

CW_FGE = [FGTab_CW.FlashGrabEffect];
CCW_FGE = [FGTab_CCW.FlashGrabEffect];

DVA_CW = mean(FGTab_CW.Effect_Dva);
DVA_CCW = mean(FGTab_CCW.Effect_Dva);

FG_Effect = mean([CW_Effect CCW_Effect]); %In PsychoPY I correct for direction differences 

DVA_Effect = mean([DVA_CW DVA_CCW]); % Flash-Grab effect in DVA

%If exceeded threshold for invalid responses, FG_Effect will be NaN
if Exceeded_Invalid_Thresh || Failed_AttCheck
    FG_Effect = nan; 
    DVA_Effect = nan; 
end

%Create an average for each direction
if CurrentSession == 1 %Store pre-effect values
    Raw_Storage_S1(N_file, 1:3) = [CurrentPart CW_Effect CCW_Effect]; 

    FG_Effect_S1(N_file, 1) = CurrentPart; %Col 1 = participant
    FG_Effect_S1(N_file, 2) = FG_Effect; %Col 2 = Polar Angle Effect
    FG_Effect_S1(N_file, 3) = DVA_Effect; %Col 3 = DVA effect

    FG_Date_S1(N_file, 1)= {CurrentPart};
    FG_Date_S1(N_file, 2)= unique(FGTab.date);

elseif CurrentSession == 2 %Session 2
    Raw_Storage_S2(N_file, 1:3) = [CurrentPart CW_Effect CCW_Effect];

    FG_Effect_S2(N_file, 1) = CurrentPart; %Col 1 = participant
    FG_Effect_S2(N_file, 2) = FG_Effect; %Col 2 = Effect
    FG_Effect_S2(N_file, 3) = DVA_Effect; %Col 3 = DVA effect

    FG_Date_S2(N_file, 1)=  {CurrentPart}; 
    FG_Date_S2(N_file, 2)=  unique(FGTab.date); 
end

%% GRAPHING
if GraphPlot
    %% SPLIT BY TARGETS OFFSET; Columns(1 = None, 2 = Right, 3 = Left)
    %USE DIFFRENT VARIABLES AS THEY COULD BE DIFFERENT LENGTHS 
    CW_Resp_1 = FGTab_CW.RespPolarAngle(strcmp(FGTab_CW.OffDir, 'None'), :);
    CW_Resp_2 = FGTab_CW.RespPolarAngle(strcmp(FGTab_CW.OffDir, 'Right'), :);
    CW_Resp_3 = FGTab_CW.RespPolarAngle(strcmp(FGTab_CW.OffDir, 'Left'), :);
    
    CCW_Resp_1 = FGTab_CCW.RespPolarAngle(strcmp(FGTab_CCW.OffDir, 'None'), :);
    CCW_Resp_2 = FGTab_CCW.RespPolarAngle(strcmp(FGTab_CCW.OffDir, 'Right'), :);
    CCW_Resp_3 = FGTab_CCW.RespPolarAngle(strcmp(FGTab_CCW.OffDir, 'Left'), :);
    
    %Subplot raincloud plots (Left subplot = CCW; Right sub = CW)
    
    %Split by inducer duration and direction
    OvEffPart_Temp = groupsummary(FGTab, {'participant', 'RevDir', 'Ms_Travelled', 'PyCond'}, {'mean', 'std'}, 'FlashGrabEffect'); %OffDir - 'session' , {'mean', 'std'}, 'FlashGrabEffect'

    % Check there is an equal amount of trials
    if length (unique(OvEffPart_Temp.GroupCount)) ~= 1;
       for playbeep = 1:3 %Play a warning beep 3 times
           beep;
           pause(0.5); %500ms break between beeps
       end
       error("THERE IS NOT AN EQUAL AMOUNT OF TRIALS PER CONDITION"); %Play an error message
    end
    
  Inducer_Part(N_file, :, 1) = [CurrentPart, CurrentSession, OvEffPart_Temp.mean_FlashGrabEffect(OvEffPart_Temp.PyCond == 1, :), ...
      OvEffPart_Temp.mean_FlashGrabEffect(OvEffPart_Temp.PyCond == 2, :) ...
    OvEffPart_Temp.mean_FlashGrabEffect(OvEffPart_Temp.PyCond == 3, :), OvEffPart_Temp.mean_FlashGrabEffect(OvEffPart_Temp.PyCond==4, :), ...
    OvEffPart_Temp.mean_FlashGrabEffect(OvEffPart_Temp.PyCond==5, :), OvEffPart_Temp.mean_FlashGrabEffect(OvEffPart_Temp.PyCond==6,:)]; %P1=CW; P2=CCW; C1=SubID; C2=700; C3=800; C4=900; C5=1000; C6=1100; C7=1200
  Inducer_Part(N_file, :, 2) = [CurrentPart, CurrentSession, OvEffPart_Temp.mean_FlashGrabEffect(OvEffPart_Temp.PyCond == 11, :), ...
      OvEffPart_Temp.mean_FlashGrabEffect(OvEffPart_Temp.PyCond == 22, :) ...
    OvEffPart_Temp.mean_FlashGrabEffect(OvEffPart_Temp.PyCond == 33, :), OvEffPart_Temp.mean_FlashGrabEffect(OvEffPart_Temp.PyCond==44, :), ...
    OvEffPart_Temp.mean_FlashGrabEffect(OvEffPart_Temp.PyCond==55, :), OvEffPart_Temp.mean_FlashGrabEffect(OvEffPart_Temp.PyCond==66,:)]; %P1=CW; P2=CCW; C1=SubID; C2=700; C3=800; C4=900; C5=1000; C6=1100; C7=1200

end %End of the graph-plot if statement
end % END OF THE Data Import  LOOP

%% Clean the effect variables
%Remove participant rows with the value of zero, you cannot have a participant of zero
FG_Effect_S1(FG_Effect_S1(:, 1) == 0, :) = [];
FG_Effect_S2(FG_Effect_S2(:, 1) ==0, :) = [];

%Sort participants by ascending
FG_Effect_S1 = sortrows(FG_Effect_S1, 1, "ascend");
FG_Effect_S2 = sortrows(FG_Effect_S2, 1, "ascend");

%% Calculate the difference in effect from session 2 to 1
FG_EFF_Difference = []; 

for PartCounter = 1:length(FG_Effect_S2(:, 1))
    FG_EFF_Difference(PartCounter, 1) = FG_Effect_S2(PartCounter, 1); %Col 1 = Participant
    
    if FG_Effect_S2(PartCounter, 1) == 59 || FG_Effect_S2(PartCounter, 1) == 68; %Part 59 and 68 did not do session 1. Everyone else did.
        FG_EFF_Difference(PartCounter, 2) =  nan; %So there is no difference value
        FG_Effect_Overall(PartCounter, 2) =  nan; %Exclude participants that did not do both sessions
    else 
        FG_EFF_Difference(PartCounter, 2) = FG_Effect_S2(PartCounter, 2) - FG_Effect_S1(FG_Effect_S1(:, 1) == FG_Effect_S2(PartCounter, 1), 2); %...
        FG_Effect_Overall(PartCounter, 2) = mean([FG_Effect_S2(PartCounter,2)  FG_Effect_S1(FG_Effect_S1(:, 1) == FG_Effect_S2(PartCounter, 1), 2)]);
        %Remember, not all part's have completed sess 1 an 2. 
    end

    %Calculate overall effect
    FG_Effect_Overall(PartCounter, 1) = FG_Effect_S2(PartCounter, 1); %Participant
end

%% Identify participants that only completed a single session
Sess1_only = []; %Variable to store participants that only did sess 1
Sess2_only = []; %Store participants that only did Sess 2
for PC1 = 1:length(FG_Effect_S1)
    if sum(FG_Effect_S1(PC1, 1) == FG_Effect_S2(:, 1)) ~= 1;
        Sess1_Only(PC1, 1) = FG_Effect_S1(PC1, 1);
    end
 
    if PC1 <= length(FG_Effect_S2)
        if sum(FG_Effect_S2(PC1, 1) == FG_Effect_S1(:, 1)) ~= 1;
            Sess2_Only(PC1, 1) = FG_Effect_S2(PC1, 1);
        end
    end
end
%Zero rows
Sess1_Only(Sess1_Only == 0) = [];
Sess2_Only(Sess2_Only == 0) = [];

%% Remove the following participants that did not complete a second session, or failed attention checks
Remove_Parts = [2, 4, 6, 15, 39, 46, 47, 70, 74, 84, 88, 108, 119, Sess1_Only', Sess2_Only', PassCheck_Failed(:, 1)', Invalid_Responses(:, 1)'];
Remove_Parts = unique(Remove_Parts); %Use unique to remove any ID's listed multiple times in Remove_Parts

for RR = 1:length(Remove_Parts)
    CP = Remove_Parts(RR);%Current part to remove
    Rem_Idx_1 = FG_Effect_S1(:, 1) == CP; %Row Index to remove people  
    Rem_Idx_2 = FG_Effect_S2(:, 1) == CP; 
    Rem_Idx_Diff = FG_EFF_Difference(:, 1) == CP; %Remove those from difference scores
    Rem_Idx_Ov = FG_Effect_Overall(:, 1) == CP; %Remove from overall effectr calculation
    %Remove participant from both sessions
    FG_Effect_S1(Rem_Idx_1, :) = [];  
    FG_Effect_S2(Rem_Idx_2, :) = [];
    FG_EFF_Difference(Rem_Idx_Diff, :) = [];
    FG_Effect_Overall(Rem_Idx_Ov, :) =[]; 
end %End of the remove participant list
clear('RR', 'CP', 'Rem_Idx_1', 'Rem_Idx_2'); %Clean unnecessary variables from memory

%% Check before we save the variables that participants are still sequentially ordered
A = 0; % Proxy variables to double check something
for P_Count = 1:length(FG_Effect_S1)
    if FG_Effect_S1(P_Count, 1) == FG_Effect_S2(P_Count, 1) && FG_Effect_S1(P_Count, 1) == FG_EFF_Difference(P_Count, 1)
        A = A+1;
    end
end
if A ~= length(FG_Effect_S1);
    error('After you removed some variables, FG_Effect session variables no longer have participants in the same order');
    return; %Leave script early
end
clear('A');

%% SAVE VALUES FOR ILLUSION TABLE
save('FG_Values.mat', "FG_Effect_S1", "FG_Effect_S2", "FG_EFF_Difference", "FG_Effect_Overall")

%Display number of NaNS 
disp(strcat('There is a total of: ', {' '}, int2str(sum(isnan(FG_Effect_S1(:, 2)))), ' NaNs in Session 1, and a total of ', {' '}, ...
    int2str(sum(isnan(FG_Effect_S2(:,2)))), ' NaNs in session 2'));

%% Parameters of the annulus image:
Win_Height = 1080;
Size = [1.05 1] * Win_Height; %W & H - Dimensions relative to window size, not screen
Im_X = [-0.5 0.5] * Size(1); %Image X coordinates
