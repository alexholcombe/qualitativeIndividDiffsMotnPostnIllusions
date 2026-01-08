%% Flash Drag analysis code
%Created by Timothy Cottier, PhD Student University of Melbourne
%Based on materials from UoM ResCom services

%% Housekeeping
close all; clear all; clc;

% Monitor dimensions
HorRes = 1920;
VertRes = 1080;
refreshrate = 144; %It should have been ~60, screendim extracts this per part
frameDur = 1000/refreshrate; %How many ms per frame
AspectRat = HorRes/VertRes; %Aspect ratio = Width to height

%Add function folder to path; OS specific 
if ismac
    try 
        ImDir = ''; 
        addpath(''); 
    catch
        disp('External T7 SSD is not connected')
        ImDir = '';% Folder to save iamges in
    end
else %Must be PC
    ImDir = ''; 
end

QuicknDirty = 1; %If 1 save the images locally

% Plot graphs? 
PlotGraph = 0; % input('Do you want to plot each individuals staircase graph? 0 = No, 1 = Yes   '); %0 = No, 1 =Yes
OverallGraph = 0;%input('Do you want to plot the staircases overall? 0 = No; 1 = Yes:   ')

%% Define some experimental parameters
secDur = 2.3; %Duration of grating in seconds
GratingDur = secDur * refreshrate; % Grating duration in frames
flashOnList = [GratingDur - (refreshrate * (1200/1000)), GratingDur - (refreshrate * (900/1000)), ...
    GratingDur - (refreshrate * (600/1000)), GratingDur - (refreshrate * (300/1000))];  %Frame of flash onset (flashOnset)

%% Specify data import parameters
if ispc
    DataLocation = '';
elseif ismac
    DataLocation = ''; 
end
DataType = [filesep '*.csv']; %Import Csvs
addpath(DataLocation); % Add folder to import
FilesinDir = dir(strcat(DataLocation, DataType)); %Files in directory
DataFileNames = {FilesinDir.name}';
nFiles = length(DataFileNames); %How many datafiles are there to import

%% Initialise variables
%%% Initialise arrays for the reversal table and PSE
ReversalTable = []; %Each row is a participant; each column a stair
Reversal_Effect_Sess1 = []; %A single PSE value for each participant, calculated over the reversals; Each row a part
Reversal_Effect_Sess2 = [];

AllSubsPSE = []; %PSE for all subs; each row = part
AvOver = 20; %Average over this many trials for the PSE
PSEHist = cell2table(cell(0,5), 'VariableNames', {'Participant', 'Stair1Up', 'Stair2Up', 'Stair3_Down', 'Stair4_Down'}); 

%This will be the effect for each part; part in col 1; Effect = Col 2
FD_PSE_Effect_Sess1 = []; 
FD_PSE_Effect_Sess2 = []; 
NumParts = length(DataFileNames); %How many participants we have. Each file a unique part

%Store the date in this vector 
FD_Date_Sess1= {}; %Col 1 = part; Col 2 = Date
FD_Date_Sess2 = {}; 

%%Did they fail the attention check:
AttFailed = [];
NumFailed = []; %For each participant, store how many they failed

%% Initialise parameters to check that staircase convergence occurred 
% The right and left flash start 7 DVA apart.
    % One flash is 3.5Above, and the other is 3.5 below the horizontal meridian
Con_Threshold = 3.5; % If staircase's PSE is greater than 3.5, didn't converge
Not_Converged =[]; %Store  participants that did not converge; Col 1 = Part, Col 2 = session, Col 3 = Up difference, Col 4 = Down difference
One_key_List = []; %Initialise the list to store people who only press one key

%% DATA IMPORT LOOP
for N_file = 1:length(DataFileNames); %Loop through each participant
    clear('FDTab', 'CurrentSession'); %Clear variables to avoid overlap
    FDTab = readtable(string(DataFileNames(N_file))); % Import Flash-drag effect
    pt = N_file; % Current loop index
    CurrentPart = max(FDTab.participant); % Current participant
    CurrentSession = max(FDTab.session); %Which session? 
    FDTab(1, :) = []; % REMOVE THE FIRST ROW IT'S BLANK?
    FDTab((strcmp(FDTab.TypeFile, 'PracCond.xlsx')), :) = []; % Remove practice trials

    %% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%%%%%%%% ATTENTION CHECK %%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    AttFailed(N_file, 1) = max(FDTab.participant); %Inser the participant number into col 1
    UniqueFailedAtt = unique(FDTab.FailedAtt);
    UniqueFailedAtt(1) = []; 
    %zconvert to Numbers from STR
    UniqueFailedAtt(strcmp(UniqueFailedAtt, 'False')) = ({0});
    UniqueFailedAtt(strcmp(UniqueFailedAtt, 'True')) = ({1});
    UniqueFailedAtt = cell2mat(UniqueFailedAtt);
    AttFailed(N_file, 2) = max(UniqueFailedAtt); % Max, if 1, they failed Att
    clear('UniqueFailedAtt'); %Clear from memory to reduce resources
    
    %Did they pass or fail the attention checks
    AttCheck_Status = (FDTab.PassCheck(~cellfun('isempty', FDTab.PassCheck), :));
    AttCheck_Status((strcmp(AttCheck_Status, 'True'))) = ({1});
    AttCheck_Status((strcmp(AttCheck_Status, 'False'))) = ({0});
    AttCheck_Status = cell2mat(AttCheck_Status);
    NumFailed(N_file, 1) = max(FDTab.participant); %Inser the participant number into col 1
    NumFailed(N_file, 2) = sum(AttCheck_Status); %This will give us how many they passed
    FDTab(isnan(FDTab.ST1TC), :) = [];    %%% REMOVE ATTENTION CHECK ROWS STAIRCASE TRIALS

%% Variable information
%LeftG = Direction of left grating 
%RightG = Direction of right grating
%Reverse, was it part of the reversal sequence.
    %The reversal sequence, was the fact the grating immediately reversed the direction it just did
%Trialcount = Counter of trials, overall (includes practice)
%NormalStairTrialCount - counts the trials in this stair
%OffsetStairTrialCount - counts the trials in this stair
%resp_corr - > 1 = they pressed right; 0 = left
  
%StairNum:
    % 1 (flash ahead) and 2(flash behind staircases are assoicated with the grating moving up
    % 3 (flash behind) and 4(flash ahead)staircases are associated with the grating moving down
%% Split into separate staircases, then calculate effect
% the flash should be offset in the direction opposite motion. Up PSE (-); down PSE (+)

%Extract staircases into their own tables
Stair1Tab = FDTab(FDTab.CurrentStair == 1, :);
Stair2Tab = FDTab(FDTab.CurrentStair == 2, :);
Stair3Tab = FDTab(FDTab.CurrentStair == 3, :);
Stair4Tab = FDTab(FDTab.CurrentStair == 4, :);

%As a sanity check, check there's the same length of trials
StairSize = [size(Stair1Tab); size(Stair2Tab); size(Stair3Tab); size(Stair4Tab)]; 
StairTC = [length(Stair1Tab.ST1TC); length(Stair2Tab.ST2TC); length(Stair3Tab.ST3TC); length(Stair4Tab.ST4TC)];
if sum(StairTC == 52) ~= 4;
    for playbeep = 1:3; % Play beep three times to indicate staircase trialcount differs
        beep;
        pause(0.5); 
    end
    error('THE STAIRCASES ARE NOT THE SAME SIZE. REVIEW THE STAIRTC VARIABLE'); 
    return; %End the script early
end

%% Did the participant press the same key for 80% of the trails within a staircase    
    NumTrials = 52; %There were 52 trials per staircase
    Threshold_key = round(NumTrials * 0.8); % 80% of trials
    NumPresses = [sum(strcmp(Stair1Tab.resp_keys, 'right')) sum(strcmp(Stair1Tab.resp_keys, 'left'));...
        sum(strcmp(Stair2Tab.resp_keys, 'right')) sum(strcmp(Stair2Tab.resp_keys, 'left'));...
        sum(strcmp(Stair3Tab.resp_keys, 'right')) sum(strcmp(Stair3Tab.resp_keys, 'left'));...
       sum(strcmp(Stair4Tab.resp_keys, 'right')) sum(strcmp(Stair4Tab.resp_keys, 'left'))]; %Col 1 = Right, Col 2 = Leftt
    Failed_Key = 0; %Reset this variable - did they press the same key for >80% of trials?
    if sum(NumPresses>Threshold_key) >= 2; 
       KeyIdx = size(One_key_List, 1)+1; %Current row to put values into
       One_key_List(KeyIdx, :) = [CurrentPart, CurrentSession];
       Failed_Key = 1; %If true only presse one key for 80% of the trials in two staircase
    end

%% Calculate PSE
PSEHist.Participant(pt, :) = max(FDTab.participant);
% Assign the PSE tables to different variables for analysis
Stair1CH = Stair1Tab; % (Stair1Tab.participant == pt, :)
Stair2CH = Stair2Tab; %(Stair2Tab.participant == pt, :)
Stair3CH = Stair3Tab; %(Stair3Tab.participant == pt, :)
Stair4CH = Stair4Tab; %(Stair4Tab.participant == pt, :)

% Calculate PSE within each staircase
PSEHist.Stair1Up(pt, :) = mean(Stair1CH.ST1Fl(end-AvOver:end));
PSEHist.Stair2Up(pt, :) = mean(Stair2CH.ST2Fl(end-AvOver:end));
PSEHist.Stair3_Down(pt, :) = mean(Stair3CH.ST3Fl(end-AvOver:end));
PSEHist.Stair4_Down(pt, :) = mean(Stair4CH.ST4Fl(end-AvOver:end));

%Average PSE within direction of the grating
PSE_Up = mean([PSEHist.Stair1Up(pt, :) PSEHist.Stair2Up(pt, :)]);
PSE_Down = mean([PSEHist.Stair3_Down(pt, :) PSEHist.Stair4_Down(pt, :)]);

% Within grating direction, calculate the difference between staircase PSES
    % to check convergence
Up_Diff = (PSEHist.Stair1Up(pt, :) - PSEHist.Stair2Up(pt, :));
Down_Diff = (PSEHist.Stair3_Down(pt, :) - PSEHist.Stair4_Down(pt, :));

%Calculate the flash-drag effect
FD_Effect = (PSE_Down - PSE_Up)/2; 

%Use abs to get around negative values when checking threshold
if abs(Up_Diff) > Con_Threshold || abs(Down_Diff) > Con_Threshold
    Not_Converged(:, 1) = CurrentPart;
    Not_Converged(:, 2) = CurrentSession; 
    Not_Converged(:, 3) = Up_Diff;
    Not_Converged(:, 4) = Down_Diff; 
    FD_Effect = NaN; %Set to nan, because the staircases didn't converge.
end

% Store the flash-drag effect and date
if CurrentSession == 1
    FD_PSE_Effect_Sess1(pt, 1) = max(FDTab.participant);
    FD_PSE_Effect_Sess1(pt, 2) = FD_Effect;

    FD_Date_Sess1(pt, 1) = {CurrentPart};
    FD_Date_Sess1(pt, 2) = unique((FDTab.date));
else
    FD_PSE_Effect_Sess2(pt, 1) = max(FDTab.participant);
    FD_PSE_Effect_Sess2(pt, 2) = FD_Effect;

    FD_Date_Sess2(pt, 1) = {CurrentPart};
    FD_Date_Sess2(pt, 2) = unique((FDTab.date));   
end

%% Plot staircases
% % This plots the staircases for each individual participant
% if PlotGraph
%     fig = figure; %Open up figure window
%     fig.Position = [100 100 1600 1000]; %Resize window
% 
%     plot(Stair1CH.ST1TC, Stair1CH.ST1Fl, '-s','Color', [0 0.4470 0.7410], 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);
%     hold on
%     plot(Stair2CH.ST2TC, Stair2CH.ST2Fl, '-s', 'Color', [0.3010 0.7450 0.9330], 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);
%     plot(Stair3CH.ST3TC, Stair3CH.ST3Fl, '-s', 'Color', [0.8500 0.3250 0.0980], 'MarkerEdgeColor', 'red', 'MarkerFaceColor', [1 0 0]);
%     plot(Stair4CH.ST4TC, Stair4CH.ST4Fl, '-s', 'Color', [0.9290 0.6940 0.1250], 'MarkerEdgeColor', 'red', 'MarkerFaceColor', [1 0 0]);
%     hold off
%     lgd = legend({'Grating moving upwards, flash offset ahead', 'Grating moving upwards, flash offset behind', ...
%         'Grating moving downwards, flash offset ahead', 'Grating moving downwards, flash offset behind'}, 'Location', 'bestoutside')
%     title(({strcat("Participant: ", int2str(CurrentPart), " session: ", int2str(CurrentSession),', staircases'), 'Positive values means flash was above horizontal meridian, negative below'}))
%     xlabel('Trial Number');
%     ylabel({'Dva Height of flash relative to the horizontal meridian'}); 
%     saveas(gcf, fullfile(ImDir, strcat('Participant_', int2str(CurrentPart), "_session_", int2str(CurrentSession), '_staircase_plot.png')));
%     close(gcf) %Please close the window!!!
% end %End of plotgraph - > Individual staircases
% 
% if OverallGraph %Plot all participants on one graph
%     if N_file == 1
%         fig = figure; %Open up figure window
%         fig.Position = [100 100 1600 1000]; %Resize window
%     end 
%     plot(Stair1CH.ST1TC, Stair1CH.ST1Fl, '-s','Color', [0 0.4470 0.7410], 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0])
%     hold on
%     plot(Stair2CH.ST2TC, Stair2CH.ST2Fl, '-s', 'Color', [0.3010 0.7450 0.9330], 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0])
%     plot(Stair3CH.ST3TC, Stair3CH.ST3Fl, '-s', 'Color', [0.8500 0.3250 0.0980], 'MarkerEdgeColor', 'red', 'MarkerFaceColor', [1 0 0])
%     plot(Stair4CH.ST4TC, Stair4CH.ST4Fl, '-s', 'Color', [0.9290 0.6940 0.1250], 'MarkerEdgeColor', 'red', 'MarkerFaceColor', [1 0 0])
%     lgd = legend({'Grating moving upwards, flash offset ahead', 'Grating moving upwards, flash offset behind', ...
%         'Grating moving downwards, flash offset ahead', 'Grating moving downwards, flash offset behind'}, 'Location', 'bestoutside')
%     title(({strcat("All participants, across sessions, all staircases"), 'Positive values means flash was above horizontal meridian, negative below'}))
%     xlabel('Trial Number');
%     ylabel({'Dva Height of flash relative to the horizontal meridian'}); 
%     if N_file == length(DataFileNames)
%         hold off %only take the hold off on last trial
%         saveas(gcf, fullfile(ImDir, strcat('All_Participants_Staircases.png')));
%         close(gcf) %Please close the window!!!
%     end
% end % End of the overall graph if statement
end %END OF THE DATA IMPORT LOOP

%% Clean the variables to save them
% No participant zeros, clean up the empty participant row in participant column
FD_PSE_Effect_Sess1(FD_PSE_Effect_Sess1(:, 1) == 0, :) = [];
FD_PSE_Effect_Sess2(FD_PSE_Effect_Sess2(:, 1) == 0, :) = [];
%Sort these variables, so it's chronological ascending for participant
FD_PSE_Effect_Sess1 = sortrows(FD_PSE_Effect_Sess1, 1, 'ascend');
FD_PSE_Effect_Sess2 = sortrows(FD_PSE_Effect_Sess2, 1, 'ascend'); 

%Which participants are missing
MissingParts = [];
for pcount = 1:119
    if ~ismember(pcount, FD_PSE_Effect_Sess1(:, 1))
       MissingParts(length(MissingParts) + 1, 1) = pcount
    end
end 

%% Calculate the change in effect from session 1 to 2
FD_PSE_Difference = []; % Difference in effect 
Sess1_Only = []; %Find participants that did Sess 1 but not sess 2 for this illusion (remove them from analysis)
Sess2_Only = []; % Find any participants that completed sess 2, but not sess 1 (to my awareness, this was none!)

for PartCounter = 1:length(FD_PSE_Effect_Sess2(:, 1));
   %Put participant in column 1
   FD_PSE_Difference(PartCounter, 1) = FD_PSE_Effect_Sess2(PartCounter, 1); %Give both the participant value
   FD_PSE_Difference(PartCounter, 2) = FD_PSE_Effect_Sess2(PartCounter, 2) - FD_PSE_Effect_Sess1(FD_PSE_Effect_Sess1(:, 1) == FD_PSE_Effect_Sess2(PartCounter, 1), 2); 
end

% Identify parts in session 1 that did not do session 2
for PC1 = 1:length(FD_PSE_Effect_Sess1(:, 1));
   if sum(FD_PSE_Effect_Sess1(PC1, 1) == FD_PSE_Effect_Sess2(:, 1)) ~= 1;
        Sess1_Only(PC1, 1) = FD_PSE_Effect_Sess1(PC1, 1);
   end
end

for PC2 = 1:length(FD_PSE_Effect_Sess2(:, 1)); 
    if sum(FD_PSE_Effect_Sess2(PC2, 1) == FD_PSE_Effect_Sess1(:, 1)) ~= 1;
        Sess2_Only(PC2, 1) = FD_PSE_Effect_Sess2(PC2, 1);
    end
end

% Remove zero rows
Sess1_Only(Sess1_Only == 0) = [];
Sess2_Only(Sess2_Only == 0) = [];

%% Remove the following participants that did not complete a second session (Overall, and for FD)
% 2, 4, 6, 15, 39, 46, 47, 70, 74, 84, 88, 107, 108, 119,
Pilot_Parts = [2, 4, 6];
Remove_Parts = [Pilot_Parts, Sess1_Only' Sess2_Only', 15, 39, 46, 47, 70, 74, 84, 88, 107, 108, 119];

for RR = 1:length(Remove_Parts)
    CP = Remove_Parts(RR);%Current part to remove
    Rem_Idx_1 = FD_PSE_Effect_Sess1(:, 1) == CP; %Row Index to remove people    
    %Remove participant from both sessions
    FD_PSE_Effect_Sess1(Rem_Idx_1, :) = [];  
end %End of the remove participant list
clear('RR', 'CP', 'Rem_Idx_1', 'Rem_Idx_2'); %Clean unnecessary variables from memory

%% GIVE ME A HISTOGRAM OF THE EFFECTS
%Put the effect in histograms - sep for each session
for apricot = 1:2
    close(gcf) %Purge the old images off the screen
    subplot(1, 2, 1);
    hist([FD_PSE_Effect_Sess1(:,2)]);
    ylabel('Effect in DVA, (+) = expected effect', 'FontSize', 16);
    xlabel('Frequency', 'FontSize', 16);
    title('Session 1', 'FontSize', 16);

    subplot(1, 2, 2);
    hist(FD_PSE_Effect_Sess2(:, 2));
    ylabel('Effect in DVA. (+) = effect ', 'FontSize', 16);
    xlabel('Frequency', 'FontSize', 16);
    title('Session 2', 'FontSize', 16);
    
    if apricot == 1
        sgtitle('Outliers included - FD magnitude');
        saveas(gcf, 'Histogram_FD.png');
    elseif apricot == 2
        sgtitle('Outliers excluded - FD Magnitude')'
        saveas(gcf, 'Histogram_FD_outliersexcluded.png');
    end
    %IDENTIFY OUTLIERS FROM THIS
    %Part 33 sess 1 is clear outlier with -1.8 - > one of their stairs did not
        %converge in both sessions so lets just remove them
    FD_PSE_Effect_Sess1(FD_PSE_Effect_Sess1(:, 1) == 33, 2) = nan;
    FD_PSE_Effect_Sess2(FD_PSE_Effect_Sess2(:, 1) == 33, 2) = nan; 
end

%% save effect
    %%%% POSITIVE VALUES INDICATE AN OFFSET IN THE DIRECTION OPPOSITE MOTION;
    %%%% NEGATIVE IS AN OFFSET IN THE DIRECTION OF MOTION
save('FD_Values.mat', 'FD_PSE_Effect_Sess1', 'FD_PSE_Effect_Sess2','FD_PSE_Difference'); % 'FD_Date_Sess1', 'FD_Date_Sess2');
disp(strcat('There is a total of: ', {' '}, int2str(sum(isnan(FD_PSE_Effect_Sess1(:, 2)))), ' NaNs in Session 1, and a total of ', {' '}, ...
    int2str(sum(isnan(FD_PSE_Effect_Sess2(:,2)))), ' NaNs in session 2')); % Participant 33 is nan - THis staircase did not converge