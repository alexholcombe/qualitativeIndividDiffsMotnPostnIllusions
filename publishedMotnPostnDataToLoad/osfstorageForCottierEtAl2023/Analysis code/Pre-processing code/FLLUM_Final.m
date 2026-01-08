%% TC Flash Lag Lum pilot analysis
%Written by Timothy Cottier, PhD student University of Melbourne

%% Clean workspace
clear all; close all; clc;

%%% DO YOU WANNA GRAPH THE PLOTS (staircases for each participant?)
PlotGraph = 0; %input('Do you want to plotgraphs, 1 = Yes; 0 = No: '); %0(False); 1(True)
PlotOverall = 0; %THIS IS NOT HELPFUL AT ALL; %input('Do you want to play all the participants on a single graph? 1 = Yes, 0 = No: ' )
PlotInv = 1; % 1 = Yes, plot individuals.

%% Data import parameters

if ismac
    DataLocation = '';
    Stair_Folder = ''; %Folder to save staircase in
elseif ispc
    DataLocation = '';
    Stair_Folder = ''
end
DataType = [filesep '*.csv'];
addpath(DataLocation); %Add data to path

%Get files
FilesinDir = dir(strcat(DataLocation, DataType));
DataFileNames = {FilesinDir.name}';

%% Initialise variables
%--- Average over this many of the last trials to calculate PSE
AvOver = 20; 

%--- Variables to store PSE 
%Col_1 = Part; Col_2= Sess; Col_3 = ST1Thresh; Col_4 = ST2Thresh; Col_5 = ST3Thresh; Col_6 = ST4Thresh
AllSubs_PSE = []; % STORE THE PSE FOR EACH PARTICIPANT AVERAGED ACROSS BOTH SESSIONS; each participant is a row
TrialCheck = []; % CHECK NUM TRIALS

% PSETABLE WILL STORE THE MEAN THRESHOLD VALUES FOR EACH RAMP
% PSE RAW STORES THE THRESHOLD FOR EACH STAIR 
[PSETable, PSERawTable] = deal((table((1:length(DataFileNames))')));
PSETable.Properties.VariableNames{1} = 'participant';
PSERawTable.Properties.VariableNames{1} = 'participant';
[PSETable.Brighter_S1_STDErr, PSETable.Darker_S1_STDErr,PSETable.Brighter_S2_STDErr, PSETable.Darker_S2_STDErr] = ...
    deal(zeros(length(DataFileNames), 1));
% PSETableSum = groupsummary(FLLum, {'PartID', 'session', 'StairNum', FLLum.Fla[end-20:end]}, {'mean', 'std', 'range'}, 'FlashLuminance')

%--- Initialise variables to calculate an effect
%Col 1 = Participant; Col 2 = effect
Lum_Eff_S1 = []; % Luminance effect on Session 1
Lum_Eff_S2 = []; % Luminance effect - Session 2
Lum_Eff_Overall = []; % Luminance effect - effect averaged across sessions

%--- Initialise variables to check if convergence occurred
Quest_Thresh = 0.2; % If this threshold is breached - > Likely didn't converge
None_Con_Thresh = 0.3; % If this threshold is breached - > Definitely didn't converge

% Col 1 = PartID; Col 2 = Session; Col 3  = Brighter Ramp; Col 4 = Darker ramp 
Questionable_Converge = []; % May not have converged, manually check
Not_Converged = []; % Staircase definitely did not converge, reject participant

%Store the differences between the brighter and darker
% Col 1 = Part; Col 2 = Value
Br_Diff = [];
Dim_Dif = [];

%---- Did participants predominantly only press one key 
One_key_List = [];

%% Attention check failed
Att_Check = []; %Participant FailedAtt

%% IMPORT DATA FILE LOOP
for N_file = 1:length(DataFileNames) % Read in each file
    clear('Check_FLLum', 'Check_FLLum', 'CurrentPart', 'CurrentSession'); %Clean the variables between participants
    [Check_FLLum,FLLum] =  deal(readtable(string(DataFileNames(N_file)))); % Data table
    CurrentPart = max(FLLum.participant); % Current participant 
    CurrentSession = max(FLLum.session); % Current sessions

    % REMOVE PRACTICE TRIALS
    FLLum(strcmp(FLLum.WasPractice, 'True'), :) = []; 

    % Break the stable up into separate tables per staircase 
    Stair1 = FLLum(FLLum.StairNum == 1, :);
    Stair2 = FLLum(FLLum.StairNum == 2, :); 
    Stair3 = FLLum(FLLum.StairNum == 3, :); 
    Stair4 = FLLum(FLLum.StairNum == 4, :); 

    % --- As a precaution, store how many trials participants completed in each staircase 
    TrialCheck(N_file, :) = [max(Stair1.ST1TC), max(Stair2.ST2TC), max(Stair3.ST3TC), max(Stair4.ST4TC)]; 

    % Did they fail attention check
    if sum(strcmp(FLLum.FailedAtt, 'True')) > 0
        Att_Check(length(Att_Check) + 1, 1) = CurrentPart; 
    end

    %% Calculate the PSE within each staircase
    ST1PSE = mean(Stair1.ST1Opa(end-AvOver:end)); % Stair 1 PSE 
    ST2PSE = mean(Stair2.ST2Opa(end-AvOver:end)); % Stair 2 PSE
    ST3PSE = mean(Stair3.ST3Opa(end-AvOver:end)); % Stair 3 PSE
    ST4PSE = mean(Stair4.ST4Opa(end-AvOver:end)); % Stair 4 PSE

    %% Calculate the effect
    %%% Average within brighter and dimmer ramps 
    Brighter_Av = mean([ST1PSE ST2PSE]); % Brighter effect
    Dimmer_Av = mean([ST3PSE ST4PSE]); % Dimmer effect
    FLLUM_Effect = (Dimmer_Av-Brighter_Av)/2; % Flash-lag luminance effect 
  
%% Check percentage of single keypresses
    NumTrials = 60; %There are 60 trials per staircase
    Threshold_key = NumTrials * 0.8; %How many total keypresses before I say they pressed one key
    NumPresses = [sum(strcmp(Stair1.resp_keys, 'up')) sum(strcmp(Stair1.resp_keys, 'down'));...
        sum(strcmp(Stair2.resp_keys, 'up')) sum(strcmp(Stair2.resp_keys, 'down'));...
        sum(strcmp(Stair3.resp_keys, 'up')) sum(strcmp(Stair3.resp_keys, 'down'));...
        sum(strcmp(Stair4.resp_keys, 'up')) sum(strcmp(Stair4.resp_keys, 'down'))]; %Records how many up and down keypresses
    
    Failed_Key = 0; %Reset failed_key 
    if sum(NumPresses>Threshold_key) >= 2; % Breached the keypress threshold in 2 staircases
       KeyIdx = size(One_key_List, 1)+1; %Current row to put values into
       One_key_List(KeyIdx, :) = [CurrentPart, CurrentSession]; %Store number of single keypresses
       Failed_Key = 1; %If true only pressed one key
    end

%% Check staircase convergence
    Con_Trials = 6; % Average over this trials to check convergence
    ST1_Con = mean(Stair1.ST1Opa(end-Con_Trials:end)); % Stair 1 convergence 
    ST2_Con = mean(Stair2.ST2Opa(end-Con_Trials:end)); % Stair 2 convergence
    ST3_Con = mean(Stair3.ST3Opa(end-Con_Trials:end)); % Stair 3 Convergence
    ST4_Con = mean(Stair4.ST4Opa(end-Con_Trials:end)); % Stair 4 convergence

    % Calculate the difference within the brighter and dimmer staircases
    Brighter_Diff = abs(ST1_Con - ST2_Con); % Use abs cause we are looking at absolute difference
    Dimmer_Diff = abs(ST3_Con - ST4_Con); %Dimmer staircases

    % Store the difference
    Br_Diff(N_file, 1:2) = [CurrentPart, Brighter_Diff]; % Brighter difference
    Dim_Dif(N_file, 1:2) = [CurrentPart, Dimmer_Diff]; % Dimmer difference
    
    % Are the staircase differences greater than convergence thresholds?
    if Brighter_Diff > Quest_Thresh || Dimmer_Diff > Quest_Thresh % Possibly breach threshold
       if Brighter_Diff > None_Con_Thresh || Dimmer_Diff > None_Con_Thresh % Definitely breaches threshold
            Not_Converged(N_file, 1:4) = [CurrentPart, CurrentSession, Brighter_Diff, Dimmer_Diff]; 
            FLLUM_Effect = NaN; %Set the value as NaN, as convergence breached
       else % May have breached convergence thresholds
           Questionable_Converge(N_file, 1:4) = [CurrentPart, CurrentSession, Brighter_Diff, Dimmer_Diff];
       end 
    end

%% Store the Flash-lag Luminance effect and PSE
if CurrentSession == 1; % Session 1 file
    PSERawTable.ST1Sesh1PSE(N_file) = ST1PSE;
    PSERawTable.ST2Sesh1PSE(N_file) = ST2PSE;
    PSERawTable.ST3Sesh1PSE(N_file) = ST3PSE;
    PSERawTable.ST4Sesh1PSE(N_file) = ST4PSE;
    PSETable.Brighter_Sess1_PSE(N_file) =  Brighter_Av;
    PSETable.Dimmer_Sess1_PSE(N_file) = Dimmer_Av;
    Lum_Eff_S1(N_file, 1:2) = [CurrentPart, FLLUM_Effect];
elseif CurrentSession == 2; % Session 2 file
    PSERawTable.ST1Sesh2PSE(N_file) = ST1PSE;
    PSERawTable.ST2Sesh2PSE(N_file) = ST2PSE;
    PSERawTable.ST3Sesh2PSE(N_file) = ST3PSE;
    PSERawTable.ST4Sesh2PSE(N_file) = ST4PSE;
    PSETable.Brighter_Sess2_PSE(N_file) = Brighter_Av;
    PSETable.Dimmer_Sess2_PSE(N_file)= Dimmer_Av;
    Lum_Eff_S2(N_file, 1:2) = [CurrentPart, FLLUM_Effect]; 
end 
   
%% Plot each individual's staircases 
if PlotGraph
    fig = figure; %If not subplot, plot each individually
    fig.Position = [100 100 1300 900];
    subplot(2, 1, 1)
    plot(Stair1.ST1TC, Stair1.ST1Opa, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);
    hold on;
    plot(Stair2.ST2TC, Stair2.ST2Opa, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);
    hold off;
    xlabel("Trial Number"); 
    ylabel("Opacity of the flash (1 = darker, 0 = brighter)");
    legend('Starts brighter', 'Starts Dimmer');
    title('Ramp going brighter');
    sgtitle(strcat("Part: ", int2str(CurrentPart), ', Session ', int2str(CurrentSession))); 

    subplot(2, 1, 2)
    plot(Stair3.ST3TC, Stair3.ST3Opa, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);
    hold on
    plot(Stair4.ST4TC, Stair4.ST4Opa, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);
    hold off
    ylabel("Opacity of the flash (1 = darker, 0 = brighter)")
    legend('Starts brighter', 'Starts Dimmer');
    title('Ramp going darker');
    saveas(gcf, fullfile(Stair_Folder, ['Stairs_P: ' , CurrentPart, ', S: ', CurrentSession, '.png'])); % Savefile 
    close(gcf)
end % End of the plotting loop
end % End of data import loop

%% Clean effect variables:
%Remove zeros, as there is no participant zero
Lum_Eff_S1(Lum_Eff_S1(:, 1) == 0, :) = []; %Session 1
Lum_Eff_S2(Lum_Eff_S2(:, 1) == 0, :) = []; %Session 2

%Remove the zeros
Not_Converged = Not_Converged(Not_Converged(:, 1) ~= 0, :)
Questionable_Converge = Questionable_Converge(Questionable_Converge(:, 1) ~= 0, :);
disp(strcat(int2str(length(unique(Not_Converged(:,1)))), ' participants had a staircase that did not converge'))

%Sort participants by ascending
Lum_Eff_S1 = sortrows(Lum_Eff_S1, 1, 'ascend');
Lum_Eff_S2 = sortrows(Lum_Eff_S2, 1, 'ascend');

%% Identify participants that only completed a single session
Sess1_only = []; %Variable to store participants that only did sess 1
Sess2_only = []; %Store participants that only did Sess 2
for PC1 = 1:length(Lum_Eff_S1)
    if sum(Lum_Eff_S1(PC1, 1) == Lum_Eff_S2(:, 1)) ~= 1;
        Sess1_Only(PC1, 1) = Lum_Eff_S1(PC1, 1);
    end
 
    if PC1 <= length(Lum_Eff_S2)
        if sum(Lum_Eff_S2(PC1, 1) == Lum_Eff_S1(:, 1)) ~= 1;
            Sess2_Only(PC1, 1) = Lum_Eff_S2(PC1, 1);
        end
    end
end

% Remove rows == zero
Sess1_Only(Sess1_Only == 0) = [];
Sess2_Only(Sess2_Only == 0) = [];

%% Remove the following participants that did not complete a second session, did not converge their staircases, or pressed one key
Pilot_Parts = [2, 4, 6];

Remove_Parts = [Pilot_Parts, 15, 39, 46, 47, 70, 74, 84, 88, 108, 119, Sess1_Only', Sess2_Only', Not_Converged(:, 1)'];
Remove_Parts = unique(Remove_Parts); %Use unique to remove any ID's listed multiple times in Remove_Parts

Only_not_converged = unique(Not_Converged([~ismember(Not_Converged(:, 1), [2, 4, 6, 15, 39, 46, 47, 70, 74, 84, 88, 108, 119, Sess1_Only', Sess2_Only'])], 1));

for RR = 1:length(Remove_Parts)
    CP = Remove_Parts(RR);%Current part to remove
    Rem_Idx_1 = Lum_Eff_S1(:, 1) == CP; %Row Index to remove session 1 people
    Rem_Idx_2 = Lum_Eff_S2(:, 1) == CP; % Row index to remove session 2 people
    %Remove participant from both sessions
    Lum_Eff_S1(Rem_Idx_1, :) = [];  
    Lum_Eff_S2(Rem_Idx_2, :) = [];
end %End of the remove participant list

%% How many people uniquely failed the attention check
Att_Check(Att_Check > 119) = [];
Att_Check = unique(Att_Check); 

Only_AttCheck = unique(Att_Check([~ismember(Att_Check(:, 1), [2, 4, 6, 15, 39, 46, 47, 70, 74, 84, 88, 108, 119, Sess1_Only', Sess2_Only'])], 1));
length(Only_AttCheck);

%% Check before we save the variables that participants are still sequentially ordered
A = 0; % Proxy variables to double check something
for P_Count = 1:length(Lum_Eff_S1)
    if Lum_Eff_S1(P_Count, 1) == Lum_Eff_S2(P_Count, 1)
        A = A+1;
    end
end
if A ~= length(Lum_Eff_S1);
    error('After you removed some variables, the FLLUM effect session variables no longer have participants in the same order');
    return; %Leave script early
end
clear('RR', 'A', 'CP', 'Rem_Idx_1', 'Rem_Idx_2'); %Clean unnecessary variables from memory

% Check the lengths of the two effects are the same
if length(Lum_Eff_S1) ~= length(Lum_Eff_S2)
    error("THE TWO EFFECT VARIABLES ARE NOT THE SAME SIZE"); % Display an error statement 
    return; % Stop executing the script
end

%% Check the staircases had an equal number of trials
if mean(mean(TrialCheck)) ~= 60
    disp('!!!WARNING!!!')
    disp('STAIRCASE TRIALS ARE NOT THE SAME')
end

%% Calculate an overall and difference effect
%Differece value between the two sessions
PSE_Difference = [];
FLLUM_Overall = [];

for PartCounter = 1:length(Lum_Eff_S2)
    PSE_Difference(PartCounter, 1) = Lum_Eff_S2(PartCounter, 1); %Add participant ID
    PSE_Difference(PartCounter, 2) = Lum_Eff_S2(PartCounter, 2) - Lum_Eff_S1(Lum_Eff_S1(:, 1) == Lum_Eff_S2(PartCounter, 1), 2);
end

%%  Identify outliers (Participants with z-scores above 3)
Z_S1 = [Lum_Eff_S1(:, 1) normalize(Lum_Eff_S1(:, 2), 'zscore')]; % Session 1 z-scores
Z_S2 = [Lum_Eff_S2(:, 1) normalize(Lum_Eff_S2(:, 2), 'zscore')]; % Session 2 z-scores
S1_Idx = abs(Z_S1(:, 2)) > 3; 
S2_Idx = abs(Z_S2(:, 2)) > 3; 
Outliers_S1 = Lum_Eff_S1(S1_Idx, :); % Store session 1 outliers
Outliers_S2 = Lum_Eff_S2(S2_Idx, :); % Store session 2 outliers
    
%% Save file
save('Luminance_Values.mat', "Lum_Eff_S1", "Lum_Eff_S2", "PSE_Difference");

disp(strcat('There is a total of: ', {' '}, int2str(sum(isnan(Lum_Eff_S1(:, 2)))), ' NaNs in Session 1, and a total of ', {' '}, ...
    int2str(sum(isnan(Lum_Eff_S2(:,2)))), ' NaNs in session 2'));