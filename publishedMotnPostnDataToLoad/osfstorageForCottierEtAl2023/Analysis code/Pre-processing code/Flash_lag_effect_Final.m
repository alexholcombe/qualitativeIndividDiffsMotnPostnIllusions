%% TC Flash Lag effect analysis
%Written by Timothy Cottier, PhD student University of Melbourne
% This code will calculate the FLE, and save it into a mat file.

%% House keeping/setup
close all; clear all; clc;

%%%% Plot graphs? 
PlotGraph = 0; % 0 = False; 1 = True

%% Data import parameters
if ismac 
    dataLocation = '';
    DataType = '/*.csv'; 
    GraphDir = '';
    addpath(genpath('')); %Add function folder to path
elseif ispc
    dataLocation = '';
    DataType = '\*.csv'; 
    GraphDir = ''; %Save the graphs in this directory
end
addpath(dataLocation);
FilesinDir = dir(strcat(dataLocation, DataType)); % Locate files in directory
DataFileNames = {FilesinDir.name}'; % File names

%% Initialise variables
%--- Variables to store the PSE
AllsubsPSE = []; %One row per participant

AllSubsBroken = []; %Break up by onset time/orientation travelled, sanity check; Col 1 = 180, 2= 225, 3 = 270, 3 =315
AVOVER = 20; %How many trials to average over in calclating pse
NumParts = length(DataFileNames); % Number of participants

Stair_Length_Check = []; % Variable to store and check the length of staircases

%--- Variables to store the flash-lag effect
FLE_Sess1 = []; %Sess 1
FLE_Sess2 = []; %Session 2
FLE_Overall = []; %Overall (average of session 1 and 2)

%--- Variables to check if staircases did not converge
% Use difference between staircases within directions to explore convergence    
%Col 1 = Part; Col 2 = Session, Col 3 = CW Difference; Col 4 = CCW difference
CW_Diff = []; % Clockwise differences - Col 1 = Part, Col 2 = Value
CCW_Diff = []; % Counter clockwise
Questionable_Converge = []; % Staircases might not have converged
Not_Converged = []; % STaircases did not converge 
Questionable_Threshold = 10; % Threshold to say staircases possibly did not convert
Not_Converged_Thresh = 15; % Threshold to say convergence did not occur

%--- Pressed one-key
One_key_List = []; 

%% Specify parameters of the radial trajectory
Flash_Rad = 380; % Radius of the flash in pixels
Flash_Rad_DVA = TC_DVA(380); %Radius of the flash in DVA
Circumference = 2*pi*Flash_Rad_DVA; % Circumference - distance around the circle

%% Initialise the variables for the attention check, i.e, did they fail???
Att_Check = []; % Participant

%% IMPORT DATA LOOP
for N_file = 1:length(DataFileNames) %We want it to loop through the calculations for each participant 
    clear('FlTab', 'CurrentPart', 'CurrentSession'); %Clear variables to prevent issues
    FlTab = readtable(string(DataFileNames(N_file))); %Flash lag table
    CurrentPart = max(FlTab.participant);
    CurrentSession = max(FlTab.session);

    %-- Remove the practice trials
    FlTab(strcmp(FlTab.Prac, 'Yes'), :) = [];

    %--- Break data table up by staircases
    ST1 = FlTab(FlTab.StairNum == 1, :); % Stair 1
    ST2 = FlTab(FlTab.StairNum == 2, :); % Stair 2 
    ST3 = FlTab(FlTab.StairNum == 3, :); % Stair 3
    ST4 = FlTab(FlTab.StairNum == 4, :); % Stair 4
    
    %--- STORE THE NUMBER OF TRIAL COUNTS IN EACH STAIRCASE
    Stair_Length_Check(N_file, :) =  [max(ST1.ST1TC), max(ST2.ST2TC), max(ST3.ST3TC), max(ST4.ST4TC)];
     
    % --- Did they fail attcheck
    if sum(strcmp(FlTab.Failed_Att, 'True')) > 0
        Att_Check(length(Att_Check) + 1, 1) = CurrentPart; 
    end

%% Variable information
%OritoTravel - orientation the target travels preceding the flash
%Original Flash Ori and FlashOri look identical
%FlashonOri - the flash is presented when the target reaches this orientation
%Flash ori, orientation of the flash, just keeps the ori 0-360
%Original flash ori goes into negatives, this wraps around
%Offset, tells us the stair it belonged to; stair could present the flash in
    %alignment or ahead or behind the moving target

%Staircases:
    % 1 (Rod ahead) and 2 (rod behind flash) were clockwise
    % 3 (Rod ahead of flash) and 4 (behind) were counterclockwise

%% CHECK HOW MANY TIMES PARTICIPANTS PRESS THE SAME KEY WITHIN EACH STAIRCASE
NumTrials = 40; %There are 40 trials per staircase
Threshold_key = 40 * 0.8; %How many total keypresses before I say they pressed one key
NumPresses = [sum(strcmp(ST1.resp_keys, 'i')) sum(strcmp(ST1.resp_keys, 'o'));...
    sum(strcmp(ST2.resp_keys, 'i')) sum(strcmp(ST2.resp_keys, 'o'));...
    sum(strcmp(ST3.resp_keys, 'i')) sum(strcmp(ST3.resp_keys, 'o'));...
sum(strcmp(ST4.resp_keys, 'i')) sum(strcmp(ST4.resp_keys, 'o'))]; %Col 1 = I responses, Col 2 = O responses

%Failed_Key = 1 means that one of the keys was
    % pressed over 80% of the time for two staircases
Failed_Key = 0; %Reset failed_key
if sum(NumPresses>Threshold_key) >= 2; 
   KeyIdx = size(One_key_List, 1)+1; %Current row to put values into
   One_key_List(KeyIdx, :) = [CurrentPart, CurrentSession];
   Failed_Key = 1; 
end

%% Calculate the Arc Length
%--- Convert each stair to radians
ST1.Stair1_Rad = deg2rad(ST1.Stair1);
ST2.Stair2_Rad = deg2rad(ST2.Stair2);
ST3.Stair3_Rad = deg2rad(ST3.Stair3);
ST4.Stair4_Rad = deg2rad(ST4.Stair4); 

%--- Caculate the arc length
% FGTab.ALength = TargRad * FGTab.Effect_Rad; 
ST1.Stair1_ALength = Flash_Rad * ST1.Stair1_Rad;
ST2.Stair2_ALength = Flash_Rad * ST2.Stair2_Rad;
ST3.Stair3_ALength = Flash_Rad * ST3.Stair3_Rad;
ST4.Stair4_ALength = Flash_Rad * ST4.Stair4_Rad;

% %-- Convert arc length from pixels to degrees of visual angle
% FGTab.Effect_Dva = TC_DVA(FGTab.ALength);
ST1.DVA = TC_DVA(ST1.Stair1_ALength);
ST2.DVA = TC_DVA(ST2.Stair2_ALength);
ST3.DVA = TC_DVA(ST3.Stair3_ALength);
ST4.DVA = TC_DVA(ST4.Stair4_ALength);

%% Calculcate the PSES here
% PSE in polar angle
ST1_PSE = mean(ST1.Stair1(end-AVOVER:end)); % Stair 1 PSE
ST2_PSE = mean(ST2.Stair2(end-AVOVER:end)); % Stair 2 PSE
ST3_PSE = mean(ST3.Stair3(end-AVOVER:end)); % Stair 3 PSE
ST4_PSE =  mean(ST4.Stair4(end-AVOVER:end)); % Stair 4 PSE

% PSE in DVA
ST1_DVA_PSE = mean(ST1.DVA(end-AVOVER:end)); 
ST2_DVA_PSE = mean(ST2.DVA(end-AVOVER:end)); 
ST3_DVA_PSE = mean(ST3.DVA(end-AVOVER:end)); 
ST4_DVA_PSE = mean(ST4.DVA(end-AVOVER:end)); 

% Store the PSES in a variable
AllsubsPSE(N_file, 1) = CurrentPart;
AllsubsPSE(N_file, 2) = ST1_PSE;
AllsubsPSE(N_file, 3) = ST2_PSE;
AllsubsPSE(N_file, 4) = ST3_PSE;
AllsubsPSE(N_file, 5) = ST4_PSE;

%% Calculate the flash-lag effect
% Calculating the direction effect, by averaging within staircases
CW_Eff = (ST1_PSE+ST2_PSE)/2; % Clockwise effect
CCW_Eff = (ST3_PSE+ST4_PSE)/2; % Counterclockwise effect

% DVA effect 
CW_DVA_Eff = (ST1_DVA_PSE + ST2_DVA_PSE)/2; % Clockwise DVA effect
CCW_DVA_Eff = (ST3_DVA_PSE + ST4_DVA_PSE)/2; % Counterclockwise DVA effect

if Failed_Key == 0 
    Pse_Eff = (CW_Eff-CCW_Eff)/2;
    DVA_PSE = (CW_DVA_Eff-CCW_DVA_Eff)/2;

elseif Failed_Key == 1 % Partipants pressed one key for the majority of the trials
    Pse_Eff = NaN;
    DVA_PSE = NaN;
end

%% Check staircase convergence
Diff_Thresh = 6; % Check if convergence happened over this many trials for each staircase
ST1_Diff = mean(ST1.Stair1(end-Diff_Thresh:end)); % Stair 1 
ST2_Diff = mean(ST2.Stair2(end-Diff_Thresh:end));
ST3_Diff = mean(ST3.Stair3(end-Diff_Thresh:end));
ST4_Diff = mean(ST4.Stair4(end-Diff_Thresh:end));

CW_Difference =  abs(ST1_Diff - ST2_Diff); % Clockwise difference. Abs (absolute difference)
CCW_Difference = abs(ST3_Diff - ST4_Diff);

% Store the difference value
CW_Diff(N_file, 1:2) = [CurrentPart, CW_Difference]; 
CCW_Diff(N_file, 1:2) = [CurrentPart, CCW_Difference];

%If the staircases did not converge, don't give it an effect
if CW_Difference >= Questionable_Threshold || CCW_Difference >= Questionable_Threshold % Possibly did not converge
    if CW_Difference >= Not_Converged_Thresh || CCW_Difference >= Not_Converged_Thresh % Staircases definitely did not converge
        Not_Converged(N_file, 1:4) = [CurrentPart, CurrentSession, CW_Difference, CCW_Difference];
        %I have checked these participants staircases, and they nearly
             %converged, so they are fine, don't exclude
        if CurrentPart ~= 68
             Pse_Eff = NaN; %Allocate not a number because did not converge
        end
    else % Staircases possibly did not converge
        Questionable_Converge(N_file, 1:4) = [CurrentPart, CurrentSession, CW_Difference, CCW_Difference];
    end
else % They did converge - so allocate zero values
    Not_Converged(N_file, 1:3) = 0;
    Questionable_Converge(N_file, 1:3) = 0;
end
    
%% Store the flash-lag effect 
if CurrentSession == 1
    FLE_Sess1(N_file, 1) = CurrentPart; %Sess 1
    FLE_Sess1(N_file, 2) = Pse_Eff; %Sess 1
    FLE_Sess1(N_file, 3) = DVA_PSE; % DVA
elseif CurrentSession == 2
    FLE_Sess2(N_file, 1) = CurrentPart; %Sess 2
    FLE_Sess2(N_file, 2) = Pse_Eff; %Sess 2
    FLE_Sess2(N_file, 3) = DVA_PSE; % DVA
end

%% Plot the staircases
if PlotGraph 
    %Plot the staircases - CW on top, CCW on bottom
    STfig = figure;
    STfig.Position = [100 100 1300 900];   
    t = tiledlayout(2, 1, 'TileSpacing', 'compact')
    nexttile
    %Clockwise
    plot(ST1.ST1TC, ST1.Stair1, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);
    hold on
    plot(ST2.ST2TC, ST2.Stair2, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);
    xlabel("Trial Number"); 
    yline(0, '- r')
    title('Clockwise staircases plotted over 40 trials. Flash begins offsets ahead or behind the target');
    aleg = legend({'Ahead', 'Behind', 'No effect'}, 'Location', 'bestoutside');
    title(aleg, 'Offset Direction');
    hold off

    nexttile;
    plot(ST3.ST3TC, ST3.Stair3, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);
    hold on
    plot(ST4.ST4TC, ST4.Stair4, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);

    xlabel("Trial Number"); 
    yline(0, '- r')
    title('Counterclockwise staircases plotted over 40 trials. Flash begins offsets ahead or behind the target');
    aleg = legend({'Ahead', 'Behind', 'No effect'}, 'Location', 'bestoutside');
    
    sgtitle(['Participant: ' num2str(CurrentPart) ', session ' num2str(CurrentSession)])
    title(aleg, 'Offset Direction');
    hold off
    saveas(gcf, fullfile(GraphDir, strcat('Staircases_Participant_', int2str(CurrentPart),'_session_', int2str(CurrentSession), '.png')));
    close(gcf)
end %End of plotting if statement
 
end %%% End of the data import loop!!!!!! 

%% Clean effect variables:
% Remove the zeros from the CW and CCW_difference
Not_Converged = Not_Converged(Not_Converged(:, 1) ~= 0, :);
Questionable_Converge = Questionable_Converge(Questionable_Converge(:, 1) ~= 0, :);
disp(strcat(int2str(length(unique(Not_Converged(:,1)))), ' participants had a staircase that did not converge'));

%Remove the zeoes, as there is no participant zero
FLE_Sess1(FLE_Sess1(:, 1) == 0, :) = []; %Sess 1
FLE_Sess2(FLE_Sess2(:, 1) == 0, :) = []; %Session 2

%Sorrt by ascending participants
FLE_Sess1 = sortrows(FLE_Sess1, 1, 'ascend');
FLE_Sess2 = sortrows(FLE_Sess2, 1, 'ascend');

%% Identify participants that only completed a single session
Sess1_only = []; %Variable to store participants that only did sess 1
Sess2_only = []; %Store participants that only did Sess 2

for PC1 = 1:length(FLE_Sess1)
    if sum(FLE_Sess1(PC1, 1) == FLE_Sess2(:, 1)) ~= 1;
        Sess1_Only(PC1, 1) = FLE_Sess1(PC1, 1);
    end
 
    if PC1 <= length(FLE_Sess2)
        if sum(FLE_Sess2(PC1, 1) == FLE_Sess1(:, 1)) ~= 1;
            Sess2_Only(PC1, 1) = FLE_Sess2(PC1, 1);
        end
    end
end

% Remove rows == zero
Sess1_Only(Sess1_Only == 0) = [];
Sess2_Only(Sess2_Only == 0) = [];

%% Remove the following participants that did not complete a second session, did not converge their staircases, or pressed one key
%Single Session, how many participants only did 1 session
Single_Sess = [Sess1_Only', Sess2_Only']; 
Pilot_Parts = [2,4,6]; % Participant that only did pilot
 
%Participants we want to remove
Remove_Parts = [Pilot_Parts, 15, 39, 46, 47, 70, 74, 84, 88, 108, 119, Single_Sess]; % Not_Converged(:, 1)'];
Remove_Parts = unique(Remove_Parts); %Use unique to remove any ID's listed multiple times in Remove_Parts

% How many parts did not converge, without being removed for only doing one session
Only_not_converged = unique(Not_Converged([~ismember(Not_Converged(:, 1), [2, 4, 6, 15, 39, 46, 47, 70, 74, 84, 88, 108, 119, Sess1_Only', Sess2_Only'])], 1));
Remove_Parts = unique([Remove_Parts'; Only_not_converged])

for RR = 1:length(Remove_Parts)
    CP = Remove_Parts(RR);%Current part to remove
    Rem_Idx_1 = FLE_Sess1(:, 1) == CP; %Row Index to remove  people from session 1
    Rem_Idx_2 = FLE_Sess2(:, 1) == CP; % Row index to remove people from session 2
    %Remove participant from both sessions
    FLE_Sess1(Rem_Idx_1, :) = [];  
    FLE_Sess2(Rem_Idx_2, :) = [];
end %End of the remove participant list

%% How many people uniquely failed the attention check
Att_Check(Att_Check > 119) = [];
Att_Check = unique(Att_Check); 

Only_AttCheck = unique(Att_Check([~ismember(Att_Check(:, 1), [2, 4, 6, 15, 39, 46, 47, 70, 74, 84, 88, 108, 119, Sess1_Only', Sess2_Only'])], 1));
length(Only_AttCheck);

%% Check before we save the variables that participants are still sequentially ordered
A = 0; % Proxy variables to double check something
for P_Count = 1:length(FLE_Sess1)
    if FLE_Sess1(P_Count, 1) == FLE_Sess2(P_Count, 1)
        A = A+1;
    end
end
if A ~= length(FLE_Sess1);
    error('After you removed some variables, the FLLUM effect session variables no longer have participants in the same order');
    return; %Leave script early
end
clear('RR', 'A', 'CP', 'Rem_Idx_1', 'Rem_Idx_2'); %Clean unnecessary variables from memory

% Check the lengths of the two effects are teh same
if length(FLE_Sess1) ~= length(FLE_Sess2)
    error("THE TWO EFFECT VARIABLES ARE NOT THE SAME SIZE"); % Display an error statement 
    return; % Stop executing the script
end

%% CHECK THE STAIRCASES HAVE THE SAME NUMBER OF TRIALS
if mean(mean(Stair_Length_Check)) ~= 40
    disp('!!! WARNING !!!')
    error('THE STAIRCASES DO NOT HAVE THE SAME TRIALCOUNT!')
    return % Exit the script
end

%% Calculate the difference in effect from session 1 to 2
%%% FOR INTEREST CONVERT THE EFFECT INTO MS
Speed = 180; %Speed per second was 180
FLE_MS_S1 = FLE_Sess1;
FLE_MS_S1(:, 2) = (FLE_MS_S1(:, 2) / Speed) * 1000; %We want in ms
FLE_MS_S2 = FLE_Sess2;
FLE_MS_S2(:, 2) = (FLE_Sess2(:, 2) / Speed) * 1000;%We want in ms

PSE_Difference = []; %(+) = increase an effect

for PartCounter = 1:length(FLE_Sess2)
    %Put participant number in column 1
    PSE_Difference(PartCounter, 1) = FLE_Sess2(PartCounter, 1);
    PSE_Difference(PartCounter, 2) = FLE_Sess2(PartCounter, 2) -  FLE_Sess1(FLE_Sess1(:, 1) == FLE_Sess2(PartCounter, 1), 2);
    FLE_Overall(PartCounter, 1) = FLE_Sess2(PartCounter, 1);
    FLE_Overall(PartCounter, 2) = mean([FLE_Sess2(PartCounter, 2), FLE_Sess1(FLE_Sess1(:, 1) == FLE_Sess2(PartCounter, 1), 2)]);
end

%% Check for any effects greater than Z-score of 3 (maybe didn't understand instructions?)
Z_S1 = [FLE_Sess1(:, 1) normalize(FLE_Sess1(:, 2), 'zscore')];
Z_S2 = [FLE_Sess2(:, 1) normalize(FLE_Sess2(:, 2), 'zscore')];
Z1_Idx = abs(Z_S1(:, 2)) > 3;
Z2_Idx = abs(Z_S2(:, 2)) > 3;
Outliers_S1 = FLE_Sess1(Z1_Idx, :); % Outliers in session 1 
Outliers_S2 = FLE_Sess2(Z2_Idx, :); % Outliers in sesssion 2

%% Save the effect file
%Save the effect values for the correlation table
save('FLE_Values.mat','FLE_Sess1', 'FLE_Sess2', 'FLE_Overall', 'PSE_Difference')
disp(strcat('There is a total of: ', {' '}, int2str(sum(isnan(FLE_Sess1(:, 2)))), ' NaNs in Session 1, and a total of ', {' '}, ...
    int2str(sum(isnan(FLE_Sess2(:,2)))), ' NaNs in session 2'));

% Check participants are in sequential order:
Check = [FLE_Sess1(:, 1) FLE_Sess2(:, 1)];
CheckSum = sum(Check(:, 1) == Check(:, 2));
if CheckSum ~= length(FLE_Sess2)
    error('ERROR, THE PARTICIPANTS ARE NOT SEQUENTIALLY ORDERED');
    return; % Exit the script
end