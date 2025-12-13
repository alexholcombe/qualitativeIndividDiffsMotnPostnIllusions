%% Gabor analysis
%Written by Timothy Cottier, PhD student University of Melbourne

%% House keeping/setup
close all; clear all; clc;
ShowGraph = 0; %input('Do you want to plot graphs? 0 = No, 1 = Yes.

%% Data import parameters
%-- What PC are  you on
if ismac
    ImDir = ''; %Directory to save images in
    dataLocation = '';
    addpath('/Function Folder'); %Add function folder to path
elseif ispc
    ImDir = '';
    dataLocation = '';
    addpath('\Function Folder'); %Add function folder top path
end

DataType = [filesep '*.csv'];
addpath(dataLocation);

%Get files
FilesinDir = dir(strcat(dataLocation, DataType));
DataFileNames = {FilesinDir.name}';

%% Initialise variables for effect calculation
% Left side is right * -1. Thus, all calculations focus on right side.
%Effect is difference between right top and bottom gabor's / 2
    % Negative - Top was more inwards (Closer to fixation)
    % Positive - Top was more outwards (Further from fixation)

% STORE THE EFFECT SPLIT BY THE ROTATION DIRECTION OF THE TOP GABORS
Eff_in = []; % Top gabors were rotating inwards
Eff_out = []; % Top gabors were rotating outwards

%Split by offset of the top and bottom gabors
Eff_off_in = [];
Eff_off_out = [];

% An array to store all participants, regardless of offset
AllSubs_In = [];
AllSubs_Out = [];

%Variables to store the effect (Col 1 = Participant, Col 2 = effect)
Gab_Eff_S1 = []; % Session 1
Gab_Eff_S2 = []; % Session 2
Eff_Table = []; % As we run through each part, we will store the effect in here

EFF_Table_Offset = []; %In this table, we will split the effect by offset
Overall_GabTab = []; %Create a table to just STORE ALL OF THE PARTICIPANTS IN ONE MEGA TABLE

%Initialise the offset matrixes. Store the offset for each direction of motion
Offset_In = [];
Offset_Out = [];

%%% CHECK THAT EACH CONDITION HAD THE SAME NUMBER OF TRIALS
Trial_Check = []; 

%%% Breahed DVA Threshold
Thresh_Violated = []; %DVA threshold breached

%%% Create a variable to store how many trials were removed
    % Participant; Session; Num Trials removed (for each part)
Outlier_Storage = [];

%% Data import loop
for N_file = 1:length(DataFileNames) %We want it to loop through the calculations for each participant 
    clear('GabTab', 'CurrentPart', 'CurrentSession'); %Clear the previous table and variables to avoid errors
    GabTab = readtable(string(DataFileNames(N_file))); %For each file, read this in as a table     
    CurrentPart = max(GabTab.participant);
    CurrentSession = max(GabTab.session);

    %% As a safety precaution, we will calculate the gabors effect here in matlab and compare it to that from psychopy
    GabTab(1, :) = []; % We need to delete the first row because it's just the instructions routine row
    GabTab(61, :) = []; %Delete the last row cause it's values from the end routine we don't analyse
    GabTab.SanityEffect = (GabTab.FinalTopRight - GabTab.FinalBotRight)/2; %Effect we will calculate in matlab

    %AvEff is the eff calculated in py
    SumCheck = [];
    for Eff_i = 1:length(GabTab.AvEff);
        GabTab.AvEff(Eff_i);
        GabTab.SanityEffect(Eff_i);
        SumCheck(Eff_i) = (GabTab.AvEff(Eff_i) ~= GabTab.SanityEffect(Eff_i)); %Identify where the matlab calculation and python are NOT identical
        sum(SumCheck); %Tell me how many cases that are NOT identical; fine if last row, as that's just the end routine finishing :)
    end 
     
   %Is there a difference between the python and mat calculations
   if  sum(SumCheck) ~= 0;
       disp('!!! WARNING !!!');
       disp('THERE IS A DIFFERENCE BETWEEN ONE OF THE PSYCHOPY AND MATLAB EFFECTS, THEY ARE NOT EQUAL');
       disp(strcat('Part:', int2str(CurrentPart)))
       return %Stop executing the code
   end
   
   %% Convert the effect to DVA from pixels
    GabTab.pixeff = GabTab.AvEff; %Make the original pixel effect it's own variable
    GabTab.AvEff = TC_DVA(GabTab.AvEff); % Convert AvEff to DVA
    
    %% REMOVE OUTLIERS - Double-check this
    %If the DVA is greater than 10 or less than 10, it's probably an
        %outlier
    Dva_Thresh = 10; %Dva threshold
    
    % How many trials exceed the DVA_thresh
    Num_Trials_Exceed = sum(GabTab.AvEff > Dva_Thresh) + sum(GabTab.AvEff < -Dva_Thresh);

    Outlier_Storage(length(Outlier_Storage) + 1, :) = [CurrentPart CurrentSession Num_Trials_Exceed];

    GabTab(GabTab.AvEff < -Dva_Thresh, :) = []; %Exclude those less than
    GabTab(GabTab.AvEff > Dva_Thresh, :) = []; %Exclude those greater than
        
%% Split the table by the direction the top gabors was moving in
        %Bottom gabors always rotated in the opposite direction
    InTable = GabTab(strcmp(GabTab.TopGabDir, 'In'), :); %Top gabors rotated towards fixation
    OutTable = GabTab(strcmp(GabTab.TopGabDir, 'Out'), :); %Top gabors rotated to edge of screen

%% Calculate the average effect for each motion direction
    % This is not splitting the gabors by alignment       
    MeanEff_Dir = groupsummary(GabTab, {'participant', 'TopGabDir', 'BotGabDir'}, {'sum', 'mean', 'std'}, {'AvEff'});
    MeanEff_Dir = removevars(MeanEff_Dir, 'GroupCount'); %Remove this variable to clean up

    %Separate the tables based on the direction of motion of the top gabors (In or outwards)
    AvAcrss_In = MeanEff_Dir(strcmp(MeanEff_Dir.TopGabDir, 'In'), :);
    AvAcrss_Out = MeanEff_Dir(strcmp(MeanEff_Dir.TopGabDir, 'Out'), :);
    
    %Remove the TopGabDir/BotGabDir to enable the join function to work (uniqueness requirement)
    AvAcrss_In = removevars(AvAcrss_In, {'TopGabDir', 'BotGabDir'});
    AvAcrss_Out = removevars(AvAcrss_Out, {'TopGabDir', 'BotGabDir'});

    %%% CALCULATE A SINGLE EFFECT VALUE
    mean_In = AvAcrss_In.mean_AvEff;
    mean_Out = AvAcrss_Out.mean_AvEff;
      
    % Effect Mean_in - mean_out:
        %positive = larger effect, offset in direction opposite of motion
        %Negative = opposite of effect, offset in direction of motion
    Gabors_Effect = (mean_In - mean_Out)/2;
    
    if CurrentSession == 1
        Gab_Eff_S1(N_file, 1) = CurrentPart; %Current participant
        Gab_Eff_S1(N_file, 2) = Gabors_Effect; %Session 1
    elseif CurrentSession == 2
        Gab_Eff_S2(N_file, 1) = CurrentPart; %Current participant
        Gab_Eff_S2(N_file, 2) = Gabors_Effect; %Session 2
    end
    
    %FOR ALL PARTICIPANTS, STORE THE EFFECT IN AN ARRAY FOR ALL PARTICIPANTS
    %C1 = participant; C2 = Session; C3 = mean_AvEff; C4 = std_AvEff,
    AllSubs_In(N_file, 1:4) = [AvAcrss_In.participant, CurrentSession, AvAcrss_In.mean_AvEff, AvAcrss_In.std_AvEff]; % Top gabors moving inwards
    AllSubs_Out(N_file, 1:4) = [AvAcrss_Out.participant, CurrentSession, AvAcrss_Out.mean_AvEff, AvAcrss_Out.std_AvEff]; %Top gabors moving outwards
   
end %%% END OF DATA IMPORT LOOP

%% Clean the most important variables:
%There is no participant zero, clean up empty rows
Gab_Eff_S1(Gab_Eff_S1(:, 1) ==0, :) = [];
Gab_Eff_S2(Gab_Eff_S2(:, 1) == 0, :) = [];

%Sort the rows chronologically ascending for participants
Gab_Eff_S1 = sortrows(Gab_Eff_S1, 1, 'ascend');
Gab_Eff_S2 = sortrows(Gab_Eff_S2, 1, 'ascend');

Outlier_Storage = sortrows(Outlier_Storage, 'ascend');

% How many participants had more than one trial removed?
disp(['A total of ' int2str(sum(Outlier_Storage(:, 3) > 1)) ' participants had more than 1  trial removed'])

% How many participants had one trial removed
Num_Part_One_T_Removed = sum(Outlier_Storage(:, 3))

%% Identify participants that only completed a single session
Sess1_only = []; %Variable to store participants that only did sess 1
Sess2_only = []; %Store participants that only did Sess 2
for PC1 = 1:length(Gab_Eff_S1)
    if sum(Gab_Eff_S1(PC1, 1) == Gab_Eff_S2(:, 1)) ~= 1;
        Sess1_Only(PC1, 1) = Gab_Eff_S1(PC1, 1);
    end
 
    if PC1 <= length(Gab_Eff_S2)
        if sum(Gab_Eff_S2(PC1, 1) == Gab_Eff_S1(:, 1)) ~= 1;
            Sess2_Only(PC1, 1) = Gab_Eff_S2(PC1, 1);
        end
    end
end
%Zero rows
Sess1_Only(Sess1_Only == 0) = [];
Sess2_Only(Sess2_Only == 0) = [];

%% Remove the following participants that did not complete a second session, or failed attention checks
Remove_Parts = [2, 4, 6, 15, 39, 46, 47, 70, 74, 84, 88, 108, 119, Sess1_Only', Sess2_Only'];
Remove_Parts = unique(Remove_Parts); %Use unique to remove any ID's listed multiple times in Remove_Parts

for RR = 1:length(Remove_Parts)
    CP = Remove_Parts(RR); %Current part to remove
    Rem_Idx_1 = Gab_Eff_S1(:, 1) == CP; %Row Index to remove session 1 people
    Rem_Idx_2 = Gab_Eff_S2(:, 1) == CP; % Row index to remove session 2 people
    %Remove participant from both sessions
    Gab_Eff_S1(Rem_Idx_1, :) = [];  
    Gab_Eff_S2(Rem_Idx_2, :) = [];
end %End of the remove participant list

%% Check before we save the variables that participants are still sequentially ordered
A = 0; % Proxy variables to double check something
for P_Count = 1:length(Gab_Eff_S1)
    if Gab_Eff_S1(P_Count, 1) == Gab_Eff_S2(P_Count, 1)
        A = A+1;
    end
end
if A ~= length(Gab_Eff_S1);
    error('After you removed some variables, FG_Effect session variables no longer have participants in the same order');
    return; %Leave script early
end
clear('RR', 'A', 'CP', 'Rem_Idx_1', 'Rem_Idx_2'); %Clean unnecessary variables from memory

%% Plot the effect for each participant on a bar graph
NumParts = length(Gab_Eff_S1); %How many participants participated in this study

AllSubs_In(AllSubs_In(:, 1) == 0, :) = [];  %Remove rows with zero participant ID's
if ShowGraph == 1
    %%%% HERE WE ARE JUST PLOTTING THE RAW SCORE FOR EACH PARTICIPANT ACROSS BOTH SESSIONS (we can
    %%%% eyeball for any that clearly misunderstood the instructions)
    %open figure window
    fig = figure;
    fig.Position = [100 100 1600 1000];
    %Plot the inwards first, plot each participant 
    avx = 1:length(AllSubs_In); 
    avy = [(AllSubs_In(:, 3))]; % Col 2 = mean
    bar(avx, avy)
    hold on
    bar((NumParts+1:NumParts * 2), AllSubs_Out(:, 3))
    xlabel({('Direction of the top gabor'), ('Bottom Gabor moved in the opposite direction')})
    xticks(1:NumParts*2) %We do x2 because there will be two data points for each participant
    legend({'Gabor moving inwards', 'Gabor moving outwards'})
    ylabel('Pixel difference between the top and bottom gabor')
    title({'Mean effect for each participant'});
    hold off
    saveas(gcf, 'Mean_effect_per_part.png'); 
end

%% Plot the AVERAGe aggregate effect for INWARDS AND OUTWARDS MOTION - averaged across participants and sessions
if ShowGraph == 1
    fig = figure;
    fig.Position = [100 100 1600 1000];
    %Plot the inwards first, plot each participant 
    avx = 1;
    avy = (AllSubs_In(:, 3));
    %We calculate the standard error for each bar INDIVIDUALLY now
    sems = std(avy)/sqrt(size(avy, 1));
    AvErr = sems; %[AvStandardErr(1), AvStandardErr(2)]
    YBar = mean(avy);
    bar(avx, YBar)
    hold on
    errorbar(avx, YBar, AvErr, 's'); 

    avx = 2;
    avy = (AllSubs_Out(:, 3));
    sems = std(avy)/sqrt(size(avy, 1));
    AvErr = sems; %[AvStandardErr(1), AvStandardErr(2)]
    YBar = mean(avy);
    bar(avx, YBar);
    errorbar(avx, YBar, AvErr, 's'); 

    xlabel({('Direction of the top gabor'), ('Bottom Gabor moved in the opposite direction')});
    xticklabels({'Top moving inward', 'Top moving outward'});
    legend({'Gabor moving inwards', 'Gabor moving outwards'});
    ylabel('DVA difference between the top and bottom gabor');
    title({'Mean difference across subjects between the top and bottom gabors', 'Error bars represent SEM'});
    hold off
    saveas(gcf,'Av_Eff_Across_offsets_All_parts.png');      
end

%% Save the effect for the correlation table
Gab_Overall = [] %The average of the two sessions
Gab_Difference = []; % 

for PartCounter = 1:length(Gab_Eff_S2(:, 1))
    %Allocate participants
    Gab_Overall(PartCounter, 1) =  Gab_Eff_S2(PartCounter, 1);
    Gab_Difference(PartCounter, 1) = Gab_Eff_S2(PartCounter, 1); 
    % Allocate effect value
    Gab_Overall(PartCounter, 2) = mean([Gab_Eff_S2(PartCounter, 2) Gab_Eff_S1(Gab_Eff_S1(:, 1) == Gab_Eff_S2(PartCounter, 1), 2)]);
    Gab_Difference(PartCounter, 2)= Gab_Eff_S2(PartCounter, 2) - Gab_Eff_S1(Gab_Eff_S1(:, 1) == Gab_Eff_S2(PartCounter, 1), 2);
end

save('Gabor_Values.mat', 'Gab_Eff_S1', 'Gab_Eff_S2', 'Gab_Overall', 'Gab_Sess_Corr', 'Gab_Sess_P');

%How many NaNs are there?
disp(strcat('There is a total of: ', {' '}, int2str(sum(isnan(Gab_Eff_S1(:, 2)))), ' NaNs in Session 1, and a total of ', {' '}, ...
    int2str(sum(isnan(Gab_Eff_S2(:,2)))), ' NaNs in session 2'))