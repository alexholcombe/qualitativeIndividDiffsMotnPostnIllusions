%% Flash Jump effect analysis
%Written by Timothy Cottier, A/Prof Dr Hinze Hogendoorn, and Dr William Turner

%% Clean up workspace
clear all; close all; clc;

% --- Do you want to plot graphs
PlotGraph = 0; % 1 = yes; 0 = no

%% Initialise variables to store the effect
    % Effect will be averaged within height change (e.g., shrinking or  increasing)
Cai_Eff_S1 = [0 0]; %Col 1 = participant; Col 2 = effect
Cai_Eff_S2 = [0 0];
Cai_Eff_Overall = [0 0];

%% Data importation parameters
if ispc 
    DataLocation = ''; 
    ImDir = '';
    addpath('\Function Folder'); %Add function folder to path
elseif ismac
    DataLocation = '';
    ImDir = '';
    addpath('/Function Folder'); %Add function folder to path
end

DataType = [filesep '*.csv']; 
addpath(DataLocation); % Add data location
FilesinDir = dir(strcat(DataLocation, DataType));
DataFileNames = {FilesinDir.name}';
SampleSize = length(DataFileNames); %This will be how many participants participated; 1 file per participant

% For trouble-shooting why p117 has two effects, lets just store fileNames
Analysed_Files = {}; 

%% Initialise storage parameters
%%% FOR PLOTTING, LETS STORE ALL THE INCREASING AND DECREASING VALUES
Increasing_Vals = []; % Increasing values
Decreasing_Vals = []; % Shrinking values

%--- Initialise a variable for how many check trials they failed
Checks_Passed = []; % C1 = Part; C2 = Session; C3 = Num passed; C4 = Pass Checks?

%--- Initialise variables to store how many outliers trials per participant
Num_Outliers = []; %Col 1 = Part; Col 2 = Sess; Col 3 = Height increasing outliers; Col 4= Height decreasing outliers

%% Data importation loop
for fileNum = 1:length(DataFileNames);
    clear("FJData", "Increasing_Effect", "Shrinking_Effect", 'CurrentPart', 'CurrentSession'); %Stop variables from lingering over
    FJData = readtable(string(DataFileNames(fileNum))); % Data table
    CurrentPart = max(FJData.participant); %Current participant
    CurrentSession = max(FJData.session); %Current session 

    % Store file for troubleshooting
    Analysed_Files{fileNum, 1} = string(DataFileNames(fileNum)); 

    %% Remove practice trials and attention checks
    FJData(strcmp(FJData.condFile, 'FJPrac.xlsx'), :) = []; % Remove practice trials
    CP = sum(strcmp(FJData.CheckPass, 'True')); %Number of checks passed
    FJData(strcmp(FJData.CheckTrials, 'True'), :) = []; % Remove the three attention checks
    Failed_Att = false; %Did they fail the attention check - if passed zero trials, then yes

    if CP == 0 %They did not pass any checks
        Failed_Att = true; 
    end
    Checks_Passed(fileNum, :) = [CurrentPart CurrentSession CP Failed_Att]; %Store how many checks were passed by each participant

%% Recode sidetoadjustis variables
%SidetoAdjustis saves on every iteration of the loop
%Sidesave only saves the side to be adjusted at the END of the trial.
    %With the FJ effect. So this is the row we want to extract.

    for elephant = 1:length(FJData.SidetoAdjustis);
        if strcmp(FJData.SideAdjust(elephant, :), '');
            FJData.SideAdjust(elephant, :) = FJData.SideSave(elephant, :);
        end
    end
    FJData.SidetoAdjustis = FJData.SideSave; %
    FJData = removevars(FJData, 'SideSave'); 

%% Variable information
%BarAdjustmentAmount is the final amount of adjustment the participant applied  to the bar
    %height. 
%FinalCaieffect = reported bar height - actual bar height at time of flash
%Adjustedbarheight- Is the bar's reported (adjusted) height at time of flash
%OriginalSize - is the bar's height of the br, at the time of the flash, excluding
    %adjustments

%%  Assign the flash-jump effect values
% Cai effect - > Is the x coordinate cai that is corrected for shrinking
    % E.g., any positive effect = extrapolation in direction of motion
FJData.FinalCaieff = FJData.CoordsX_FinalCaieff; %Use this variable - does not correct for shrinking
FJData.OffsetDir = FJData.OffsetDirBack;

%How much adjustment was applied to the bar (not the effect)
FJData.AdjustmentApplied = FJData.XCoord_AdjustedBarHeight - FJData.OriginalSize;

%--- Remove NaNs - There are rows with nan values because the trials repeat untill participants press space
FJData(isnan(FJData.FinalCaieff), :) = []; 

%% Convert cai effect from pixels to DVA 
FJData.Cai_Pixels = FJData.FinalCaieff; % Precaution - store the pixel effect    
[a, FJData.FinalCaieff] = TC_DVA([], FJData.FinalCaieff); %[X, Y]

%% Split the table by the height change pattern of the bar (was the bar growing or shrinking in height)
FJ_Increasing = FJData(strcmp(FJData.SidetoAdjustis, 'Increasing'), :); % Bar was increasing in height
FJ_Shrinking = FJData(strcmp(FJData.SidetoAdjustis, 'Shrinking'), :); %Bar was shrinking in height
Increase_Eff = FJ_Increasing.FinalCaieff; % Increasing cai effect 
Decrease_Eff = FJ_Shrinking.FinalCaieff; % Shrinking cai effect

%--- Store the cai effect height change by direction
Increasing_Vals = [Increasing_Vals; Increase_Eff]; % Store by height was increasing
Decreasing_Vals = [Decreasing_Vals; Decrease_Eff]; % Store by height was decreasing

%% Find outlier trials - for each participant
%For the first 46 participants, sometimes the adjustment variable broke
    % As a consequence, the adjustment was continuously applied on each
    % frame. Even in the absence of a keypress. 

%%%% REMOVE ANY TRIALS WITH Z-SCORES ABOVE OR BELOW THRESHOLD
Z_Cai_inc = zscore(FJ_Increasing.FinalCaieff); % Z-scores when height increasing
Z_Cai_Shrink =  zscore(FJ_Shrinking.FinalCaieff); % Z-scores when height shrinking
Z_threshold = 3; % We will remove trials with z-scores > or < than this
Inc_Outliers = abs(Z_Cai_inc) >= Z_threshold; % Increasing trials above threshold
Shr_Outliers = abs(Z_Cai_Shrink) >= Z_threshold; %Shrinking trials above threshold

% -- For each participant
N_Inc_Out = sum(Inc_Outliers); %Number of increasing outliers
N_Shrink_Out = sum(Shr_Outliers); % Number of shrinking outliers
Num_Outliers(fileNum, :) = [CurrentPart, CurrentSession, N_Inc_Out N_Shrink_Out]; %Store the number of outliers for each participant

% %Remove outliers trials
FJData(Inc_Outliers, :) = [];
FJData(Shr_Outliers, :) = []; 

%% Calculate the effect
%Split the table by the height changes of the bar they are adjustng (Adjustsideis)
%Within each growth pattern, the effect is just the average across trials
Increasing_Effect = mean(FJ_Increasing.FinalCaieff); % Average - increasing height
Shrinking_Effect = mean(FJ_Shrinking.FinalCaieff); % Average - Shrinking height

%--- Interpreting the effect:
    %Positive = Effect, changed height in direction opposite motion
    %Negaitve = No effect, changed height in direction of motion
Cai_Eff = (Shrinking_Effect - Increasing_Effect)/2; %Calculate the effect

if CurrentSession == 1
    if sum(Cai_Eff_S1(:, 1) == CurrentPart) >= 1
        error(['PARTICIPANT: ' int2str(CurrentPart) 'IS ALREADY IN CAI_EFF_S1'])
    else
        Cai_Eff_S1(fileNum, 1:2) =[CurrentPart, Cai_Eff];% Col 1 = participant; 2 = effect
    end

elseif CurrentSession == 2
    if sum(Cai_Eff_S2(:, 1) == CurrentPart) >= 1
        error(['PARTICIPANT: ' int2str(CurrentPart) 'IS ALREADY IN Cai_Eff_S2'])
    else
        Cai_Eff_S2(fileNum, 1:2) = [CurrentPart, Cai_Eff];
    end
end

%% Plot each trial on a histogram, split by growth pattern
if PlotGraph == 1 %If yes, will plot
    NumBins = 14; %nbins - default is 7
    SP1 = subplot(1, 2, 1); % Increasing plot 
    histogram(FJ_Increasing.FinalCaieff, NumBins); % Increasing histogram
    title('Bar to be adjusted is increasing in height'); % Increasing 
    xlabel({"DVA difference between the target and reference bar's height", '(-) = made bar shorter'}); 
    ylabel('Frequency'); 

    subplot(1, 2, 2); % Shrinking plot 
    histogram(FJ_Shrinking.FinalCaieff, NumBins); % Shrinking histogram 
    title('Bar to be adjusted is decreasing in height'); % Bar is shrinking in height
    xlabel({"DVA difference between the target and reference bar's height", '(+) = made bar longer'}); 
    ylabel('Frequency'); 
    sgtitle({'Flash-jump effect', ['P', 'int2str(CurrentPart)', ', session: ', int2str(CurrentSession)]}); 
    saveas(Ifig, fullfile(ImDir, strcat('FJ_Trials_', 'P', int2str(CurrentPart), '_session', int2str(CurrentSession), '.png'))); % Save as figure
    close(Ifig) %Close figure handle
end %Plot graph

%% Split the effect by the offset of the reference bar
    % E.g., was the bar they were trying to height match, smaller, taller or equal in height 
LargerIDX = zeros(length(FJData.OffsetDir), 1); % Reference bar was larger
SmallerIDX = zeros(length(FJData.OffsetDir), 1); % Reference bar was smaller

% The reference bar (the one they were not adjusting was offset)
for el = 1:length(FJData.OffsetDir);
    if strcmp(FJData.OffsetDir(el, :), 'BotLrg') | strcmp(FJData.OffsetDir(el, :), 'TopLRG'); 
        LargerIDX(el, :) = 1;
    end
    if strcmp(FJData.OffsetDir(el, :), 'TopSML') | strcmp(FJData.OffsetDir(el, :), 'BotSml');
        SmallerIDX(el, :) = 1;
    end
end

% Split the offset into groups:
% --- 10 = Height was equal | 20 = Larger | 30 = Smaller
FJData.ReferenceGroups = zeros(length(FJData.OffsetDirBack), 1);
FJData.ReferenceGroups(:,:) = 10; % Equal in height
FJData.ReferenceGroups(logical(LargerIDX), :) = 20; % Reference bar was taller
FJData.ReferenceGroups(logical(SmallerIDX), :) = 30; % REference bar was shorter

LargerTab = FJData(logical(LargerIDX), :);
SmallerTab = FJData(logical(SmallerIDX), :);
IdenticalTab =FJData(strcmp(FJData.OffsetDir, 'NA'), :);

%Check that the size was equal
SizeCheck(fileNum, :) = [size(IdenticalTab, 1), size(LargerTab, 1), size(SmallerTab, 1)];

%% Descriptive statics split by the different reference bar sizes
%Calculate aggregate mean across all sessions
DescriptiveTab = groupsummary(FJData, {'participant', 'session', 'ReferenceGroups', 'SidetoAdjustis'}, {'mean', 'std'}, ...
    {'FinalCaieff', 'AdjustmentApplied'});
DescriptiveTab.StandardError_Cai = DescriptiveTab.std_FinalCaieff/(sqrt(max(SampleSize))); % Calculate standard error for the effect
DescriptiveTab.StandardErrorAdjustment = DescriptiveTab.std_AdjustmentApplied/(sqrt(max(SampleSize))); % STD error for adjustment applied

%Split descriptive tab by increasing and decreasing
DescripIncrease = DescriptiveTab(strcmp(DescriptiveTab.SidetoAdjustis, 'Increasing'), :);
DescripShrink = DescriptiveTab(strcmp(DescriptiveTab.SidetoAdjustis, 'Shrinking'), :);
 
%For the different growth patterns it gives you the mean effect for each offset
    %Col 1 = Increasing; Col 2 = Shrinking
AverageEffect = [DescripIncrease.mean_FinalCaieff  DescripShrink.mean_FinalCaieff]; 

end %OF THE DATA IMPORT LOOP

%% Clean the effect variables
% There is no participant zero, so remove these participants
Cai_Eff_S1(Cai_Eff_S1(:,1) == 0, :) = [];
Cai_Eff_S2(Cai_Eff_S2(:, 1) == 0, :) = [];

% Sort participants by ascending
Cai_Eff_S1 = sortrows(Cai_Eff_S1, 1, 'ascend');
Cai_Eff_S2 = sortrows(Cai_Eff_S2, 1, "ascend");

%% Tell how me how many are not nans
Cai_Eff_S1(isnan(Cai_Eff_S1(:, 2)), 1)
Cai_Eff_S2(isnan(Cai_Eff_S2(:, 2)), 1)

%% Identify participants that only completed a single session
Sess1_only = []; %Variable to store participants that only did sess 1
Sess2_only = []; %Store participants that only did Sess 2
for PC1 = 1:length(Cai_Eff_S1)
    if sum(Cai_Eff_S1(PC1, 1) == Cai_Eff_S2(:, 1)) ~= 1;
        Sess1_Only(PC1, 1) = Cai_Eff_S1(PC1, 1);
    end
 
    if PC1 <= length(Cai_Eff_S2)
        if sum(Cai_Eff_S2(PC1, 1) == Cai_Eff_S1(:, 1)) ~= 1;
            Sess2_Only(PC1, 1) = Cai_Eff_S2(PC1, 1);
        end
    end
end

% Remove rows == zero
Sess1_Only(Sess1_Only == 0) = [];
Sess2_Only(Sess2_Only == 0) = [];

Sample_Size(:, 1) = length(Cai_Eff_S1);

%% Remove the following participants that did not complete a second session
Pilot_parts = [2, 4, 6];
Remove_Parts = [Pilot_parts, 15, 39, 46, 47, 70, 74, 84, 88, 108, 119, Sess1_Only', Sess2_Only'];
Remove_Parts = unique(Remove_Parts); %Use unique to remove any ID's listed multiple times in Remove_Parts

for RR = 1:length(Remove_Parts)
    CP = Remove_Parts(RR);%Current part to remove
    Rem_Idx_1 = Cai_Eff_S1(:, 1) == CP; %Row Index to remove session 1 people
    Rem_Idx_2 = Cai_Eff_S2(:, 1) == CP; % Row index to remove session 2 people
    %Remove participant from both sessions
    Cai_Eff_S1(Rem_Idx_1, :) = [];  
    Cai_Eff_S2(Rem_Idx_2, :) = [];
end %End of the remove participant list

% Sample size after completing the two sessions:
if length(Cai_Eff_S1) ~= length(Cai_Eff_S2)
    error('THE LENGTH OF SESSION 1 AND 2 ARE NOT THE SAME, PLEASE CHECK')
end

Sample_Size(:, 2) = length(Cai_Eff_S1);

%% Remove participants that failed the attention checks

% Just get poarticipants that failed the attention checks
Failed_Att = Checks_Passed(Checks_Passed(:, 4) == 1, 1)

for FA = 1:length(Failed_Att(:, 1))
    CP = Failed_Att(FA, 1);%Current part to remove
    Rem_Idx_1 = Cai_Eff_S1(:, 1) == CP; %Row Index to remove session 1 people
    Rem_Idx_2 = Cai_Eff_S2(:, 1) == CP; % Row index to remove session 2 people
    %Remove participant from both sessions
    Cai_Eff_S1(Rem_Idx_1, :) = [];  
    Cai_Eff_S2(Rem_Idx_2, :) = [];
end %End of the remove participant list

% Sample size after completing the two sessions:
if length(Cai_Eff_S1) ~= length(Cai_Eff_S2)
    error('THE LENGTH OF SESSION 1 AND 2 ARE NOT THE SAME, PLEASE CHECK')
end

Sample_Size(:, 3) = length(Cai_Eff_S1);

%% Finally tell me how many outliers trials are in each session
Num_Outliers(:, 5) = sum(Num_Outliers(:, 3:4), 2)
S1_Outliers = Num_Outliers(Num_Outliers(:, 2) == 1, :);
S2_Outliers = Num_Outliers(Num_Outliers(:, 2) == 2, :);

% Tell me how many above 1 trials were excluded
P_Trials_More_1=  Num_Outliers(Num_Outliers(:, 5) > 1, :);

% 1 trial that was an outlier 
OneTrial_Out = Num_Outliers(Num_Outliers(:, 5) == 1, :);
Num_1_Trial_Out = length(OneTrial_Out); 
%% Check the sessions are the same length
if length(Cai_Eff_S1) ~= length(Cai_Eff_S2);
    error('THE CAI EFFECT ON SESSION 1 IS NOT THE SAME LENGTH AS THE CAI EFFECT ON SESSION 2');
    return %Exit the script
end 

%% Check before we save the variables that participants are still sequentially ordered
A = 0; % Proxy variables to double check something
for P_Count = 1:length(Cai_Eff_S1)
    if Cai_Eff_S1(P_Count, 1) == Cai_Eff_S2(P_Count, 1)
        A = A+1;
    end
end
if A ~= length(Cai_Eff_S1);
    error('After you removed some variables, Frohlich effect session variables no longer have participants in the same order');
    return; %Leave script early
end
clear('RR', 'A', 'CP', 'Rem_Idx_1', 'Rem_Idx_2'); %Clean unnecessary variables from memory
%% CHECK THE SAMPLE SIZE
try
    if mean(mean(SizeCheck)) ~= 16
        disp('THERE WAS NOT EQUAL AMOUNT OF TRIALS IN EACH CONDITION')
    end
end

%% Calculate the difference in effect from session 1 to 2
Eff_Difference = []; % Variable to store effect

for PartCounter = 1:length(Cai_Eff_S2(:, 1))
    % Col 1 = Participant | Col 2 = Effect value
    Eff_Difference(PartCounter, 1:2) = [Cai_Eff_S2(PartCounter, 1), Cai_Eff_S2(PartCounter, 2) - Cai_Eff_S1(Cai_Eff_S1(:, 1) == Cai_Eff_S2(PartCounter, 1), 2)]; %Participant
    Cai_Eff_Overall(PartCounter,1:2) =  [Cai_Eff_S2(PartCounter, 1), mean([Cai_Eff_S2(PartCounter, 2) Cai_Eff_S1(Cai_Eff_S1(:, 1) == Cai_Eff_S2(PartCounter, 1), 2)])]; %Participant
end

%% Save Data
save('FJ_Values.mat', 'Cai_Eff_S1', 'Cai_Eff_S2', 'Cai_Eff_Overall', 'Eff_Difference')
disp(strcat('There is a total of: ', {' '}, int2str(sum(isnan(Cai_Eff_S1(:, 2)))), ' NaNs in Session 1, and a total of ', {' '}, ...
    int2str(sum(isnan(Cai_Eff_S2(:,2)))), ' NaNs in session 2'));