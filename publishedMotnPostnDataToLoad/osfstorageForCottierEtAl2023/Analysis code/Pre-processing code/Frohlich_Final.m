%% Frohlich effect analysis code
%Created by Timothy Cottier, PhD Student University of Melbourne

%% House keeping
close all; clear all; clc;

SkipGraphs = 1; %'Do you want to plot graphs? 0 = Yes, 1 = No:   ');
PlotOverall = 0; % Do you want to plot the staircases individually (0 = No) or overall on a single plot (1 = Yes); 

%% Data import parameters
DataType = [filesep '*.csv'];
if ispc
    dataLocation = '';
    Imdir = [''];
elseif ismac 
    dataLocation = '';
    Imdir = '';
    addpath(genpath('')); %Add function folder to path
end
addpath(dataLocation); 

FilesinDir = dir(strcat(dataLocation, DataType)); % Identify the files in the directory
DataFileNames = {FilesinDir.name}';
NumParts = length(DataFileNames); %This will be how many participants participated; 1 file per participant

%% Initiate arrays to store variables
allsubs_Sess1 = zeros(3,NumParts,NumParts); % Session 1  
allsubs_Sess2 = zeros(3,NumParts, NumParts); %Session 2
allsubs =  zeros(3,NumParts, NumParts); %Not split by session
ParticipantArray = num2cell([(1:100)', zeros(100, 1)]); %Col 1, participant number, col 2, participant name)
PartCount = 0; %This counts what participant we are on. 

%% PSE Parameters
NumTrials = 40; %There are 40 trials per staircase
AvOver = 10; % Average over this many trials to get PSE 
PSEAv = [];
DVA_PSEAv = []; % The PSE in Degrees of Visual Angle
%Col 1 = part; Col 2 = effect
Frohlich_Sess1 = []; %Frohlich effect Session 1
Frohlich_Sess2 = []; %Frohlich effect Session 2

%% STAIRCASE AND VARIABLE INFORMATION
% Behind - > Offset (45 degrees) in direction opposite motion
% Ahead - > Offset (45 degrees) in the direction of motion
% Stair 1 - Clockwise, starts behind (- 45)
% Stair 2 - Counterclockwise, starts ahead (- 45)
% Stair 3 - Clockwise, starts ahead (+ 45)
% Stair 4 - counterclockwise, starts behind (+ 45)

%Resp_corr == 1, means they responded to the arrow key corresponding to the direction of motion
%StartingRodOri = the starting orientation of the rod

%--- specify parameters of the radial trajectory
% We want to calculate the arc length
Line_Rad = 330; %Radius of the radial trajectory
Line_Rad_Dva = TC_DVA(Line_Rad); % Line radius in dva
Dia = Line_Rad * 2; %Diameter
Circumference = 2*pi*Line_Rad; % Circumference - distance around the circle

%% INITIALISE VARIABLES TO CHECK CONVERGENCE
%Col 1 = Part; Col = Session; Col 3 = Value
Store_CWDIFF = []; % Clockwise values
Store_CCWDiff = []; % Counterclockwise values

%Col 1 = Part; Col 2 = Session  Col 3 = CW; Col 4 = CCW
Questionable_Converge = []; % Possibly did not converge
Not_Converged = []; % Definitely did not convert
Questionable_Thresh = 20; % In degrees of polar angle
Not_Converged_Thresh = 45; % In degrees of polar angle

%% Keep track of anyone excluded for having an effect greater than 90 deg of polar angle
Eff_Greater_90 = [];

%% Initialise variables to check if one key was pressed for the majority of a staircase
One_key_List = []; %Col 1 = Part; Col 2 = Session

%% Attention check initialisation
Att_Check = []; % Participant
Num_AttChecks = 8;
Failed_Att_Check = 8 * 0.5; % Criteria applied to say people failed attention check (50%)

%%  Data import loop
for fileNum = 1:length(DataFileNames);
    clear("FRETab", "CurrentPart", "CurrentSession", "CurrentFile") %Clear variables  to reduce contamination
    CurrentFile = string(DataFileNames(fileNum));
    FRETab = readtable(CurrentFile); % Frohlich effec table
    CurrentParticipant = max(FRETab.participant);
    CurrentSession = max(FRETab.session); 
        
    % Did they pass attention check:
    if FRETab.NumFails >= Failed_Att_Check
        Att_Check = CurrentPart; 
    end
    
    %%%Remove attention check trials
    FRETab(~ismissing(FRETab.PassCheck), :) = []; 

%% Split the table by staircases
ST1 = FRETab((FRETab.StairNumber==1), :); % Rod was rotating clockwise
ST2 = FRETab((FRETab.StairNumber==2), :); % Rod was rotating counterclockwise
ST3 = FRETab((FRETab.StairNumber==3), :); % Rod was rotating clockwise
ST4 = FRETab((FRETab.StairNumber==4), :); % Rod was rotating counterclockwise

%% Check if participants pressed a single key
%Each Row = part | Col 1 = Left, Col 2 = Right
Threshold_key = NumTrials * 0.8; %How many total keypresses before I say they pressed one key
NumPresses = [sum(strcmp(ST1.resp_keys, 'right')) sum(strcmp(ST1.resp_keys, 'left'));...
    sum(strcmp(ST2.resp_keys, 'right')) sum(strcmp(ST2.resp_keys, 'left'));...
    sum(strcmp(ST3.resp_keys, 'right')) sum(strcmp(ST3.resp_keys, 'left'));...
    sum(strcmp(ST4.resp_keys, 'right')) sum(strcmp(ST4.resp_keys, 'left'))]; %Col 1 = Right keypresses, Col 2 = Left keypresses

% One of the keys was pressed over 80% of the time for two staircases
    Failed_Key = 0; %Reset failed_key
    if sum(NumPresses>Threshold_key) >= 2; 
       KeyIdx = size(One_key_List, 1)+1; %Current row to store values in
       One_key_List(KeyIdx, :) = [CurrentParticipant, CurrentSession]; 
       Failed_Key = 1; %If true only pressed one key for 80% of trials
    end

%% Convert from polar angle to degrees of visual angle
%--- Firstly, convert from degrees to radians
ST1.Stair1_Rad = deg2rad(ST1.Stair1);
ST2.Stair2_Rad = deg2rad(ST2.Stair2);
ST3.Stair3_Rad = deg2rad(ST3.Stair3);
ST4.Stair4_Rad = deg2rad(ST4.Stair4);

%--- Calculate arc length
ST1.ALength_Rad = Line_Rad * ST1.Stair1_Rad;
ST2.ALength_Rad = Line_Rad * ST2.Stair2_Rad; 
ST3.ALength_Rad = Line_Rad * ST3.Stair3_Rad;
ST4.ALength_Rad = Line_Rad * ST4.Stair4_Rad;

%--- Convert arc length to degrees of visual angle
ST1.DVA = TC_DVA(ST1.ALength_Rad);
ST2.DVA = TC_DVA(ST2.ALength_Rad);
ST3.DVA = TC_DVA(ST3.ALength_Rad);
ST4.DVA = TC_DVA(ST4.ALength_Rad);

%% Calculate the PSE for each staircase
%%% EFFECT INTERPRETATION:
    %Positive (we observed expected effect) - Rod needed to be displaced in direction opposite motion
    %Negative (opposite of expected effect) - Rod had to be displaced in direction of motion
    %C1(Column1) = Stair(ST) 1, C2 = ST2, C3 = ST3, C4 = ST4, C5 = Participant ID
    %PSEAv variable to store the PSE
    PSEAv(fileNum, 1:5) = [mean(ST1.Stair1(end-AvOver:end, :)), mean(ST2.Stair2(end-AvOver:end, :)), mean(ST3.Stair3(end-AvOver:end, :)),...
        mean(ST4.Stair4(end-AvOver:end, :)), CurrentParticipant];  
    PSE_CW = mean([PSEAv(fileNum, 1) PSEAv(fileNum, 3)]); % Average PSE together for Rod's clockwise motion
    PSE_CCW = mean([PSEAv(fileNum, 2) PSEAv(fileNum, 4)]); % Average PSE together for Rod's counterclockwise motion
    
    % Calculate the DVA for PSE
    DVA_PSEAv(fileNum, 1:5) =  [mean(ST1.DVA(end-AvOver:end, :)), mean(ST2.DVA(end-AvOver:end, :)), ...
        mean(ST3.DVA(end-AvOver:end, :)), mean(ST4.DVA(end-AvOver:end, :)), CurrentParticipant];
    PSE_DVA_CW = mean([DVA_PSEAv(fileNum, 1) DVA_PSEAv(fileNum, 3)]);
    PSE_DVA_CCW = mean([DVA_PSEAv(fileNum, 2) DVA_PSEAv(fileNum, 4)]);

%% Calculate the frohlich effect
Frohlich_Eff = (PSE_CCW - PSE_CW)/2; % 
DVA_Eff = (PSE_DVA_CCW - PSE_DVA_CW)/2; 

if Failed_Key % If they failed a key press
    Frohlich_Eff = NaN; 
    DVA_Eff = NaN;
end

%-- If frohlich effect is greater than 90 bin that participant
if Frohlich_Eff > 90
%     Frohlich_Eff = NaN;
%     DVA_Eff = NaN;
    Eff_Greater_90(fileNum)= CurrentParticipant; 
end 

%% Check if the staircases converged
Con_av = 6; % Average over this many trials, to check if convergence occurred
Con_PSE_ST1 = mean(ST1.Stair1(end-Con_av:end, :)); %Stair 1
Con_PSE_ST2 = mean(ST2.Stair2(end-Con_av:end, :)); %Stair 2
Con_PSE_ST3 = mean(ST3.Stair3(end-Con_av:end, :)); %Stair 3
Con_PSE_ST4 = mean(ST4.Stair4(end-Con_av:end, :)); %Stair 4

% Within direction, check the distance between stairs
CW_Diff = Con_PSE_ST3 - Con_PSE_ST1;
CCW_Diff = Con_PSE_ST2 - Con_PSE_ST4;
    
% Store the difference in a list
Store_CWDIFF(fileNum, 1:3) = [CurrentParticipant, CurrentSession, CW_Diff]; %Clockwise list
Store_CCWDiff(fileNum, 1:3) = [CurrentParticipant, CurrentSession, CCW_Diff]; %Counterclockwise list
    
if CW_Diff > Questionable_Thresh || CCW_Diff > Questionable_Thresh
  if CW_Diff > Not_Converged_Thresh || CCW_Diff > Not_Converged_Thresh
      Not_Converged(fileNum, 1) = CurrentParticipant;
      Not_Converged(fileNum, 2) = CurrentSession;
      Not_Converged(fileNum, 3) = CW_Diff;
      Not_Converged(fileNum, 4) = CCW_Diff;
      Frohlich_Eff = nan; % Staircases did not converge, so nullify effect
      DVA_Eff = nan;
  else % Possibly did not converge
      Questionable_Converge(fileNum, 1:4) = [CurrentParticipant, CurrentSession, CW_Diff, CCW_Diff]; 
  end 
end
        
%% Store the illusory effect 
    %CCW positive = had to be start offset in the direction opposite motion
    %CW negative = had to be offset in the direction opposite motion
    if CurrentSession == 1
        Frohlich_Sess1(fileNum, 1) = CurrentParticipant; % Current participant
        Frohlich_Sess1(fileNum, 2) = Frohlich_Eff; %Session 1 effect - Polar angle
        Frohlich_Sess1(fileNum, 3) = DVA_Eff;
    elseif CurrentSession == 2
        Frohlich_Sess2(fileNum, 1) = CurrentParticipant; % Current participant
        Frohlich_Sess2(fileNum, 2) = Frohlich_Eff; %Session 2 effect
        Frohlich_Sess2(fileNum, 3) = DVA_Eff;
    end
    
%% Plot the staircases for each participant
if ~SkipGraphs
    STfig = figure;
    STfig.Position = [100 100 1300 900];   
    t = tiledlayout(2, 1, 'TileSpacing', 'compact');
    nexttile
    %Plot clockwise staircases on top
    plot(ST1.Stair1TC, ST1.Stair1, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);
    hold on;
    plot(ST3.Stair3TC, ST3.Stair3, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);
    xlabel("Trial Number"); 
    yline(0, '- r');
    title('Clockwise staircases plotted over 40 trials, beginning offset ahead or behind');
    aleg = legend({'Behind', 'Ahead', 'No effect'}, 'Location', 'bestoutside');
    title(aleg, 'Offset Direction');
    hold off;

    % Plot counterclockwise staircases on bottom
    nexttile;
    plot(ST2.Stair2TC, ST2.Stair2, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);
    hold on;
    plot(ST4.Stair4TC, ST4.Stair4, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0]);
    xlabel({"Trial Number", strcat('Participant: ', int2str(max(ST4.participant)))}); 
    yline(0, '- r');
    title('CounterClockwise staircases plotted over 40 trials, beginning offset ahead or behind');
    aleg = legend({'Behind', 'Ahead', 'No effect'}, 'Location', 'bestoutside');
    title(aleg, 'Offset Direction');
    hold off;
    saveas(gcf, fullfile(Imdir, strcat('Staircases_Participant_', int2str(max(FRETab.participant)), '_Sess_', int2str(CurrentSession), '.png')));
    close(gcf); %STOP THE IMAGES GOING OUT OF CONTROL
end %End of the skipgraphs if statement

end %%% END OF THE DATA IMPORT LOOP

%% Clean the effect variables:
% There is no participant zero, so remove these empty rows
Frohlich_Sess1(Frohlich_Sess1(:, 1) == 0, :) = []; %Session 1
Frohlich_Sess2(Frohlich_Sess2(:, 1) == 0, :) = [];  %Session 2
% 
% %Remove > 90 degree effects, unlikely to be true effects
Frohlich_Sess1(abs(Frohlich_Sess1(:, 2)) >= 90, 2) = NaN; 
Frohlich_Sess2(abs(Frohlich_Sess2(:, 2)) >= 90, 2) = NaN; %Use abs to grab any negative effects < -90

%Sort participants by ascending
Frohlich_Sess1 = sortrows(Frohlich_Sess1, 1, 'ascend');
Frohlich_Sess2 = sortrows(Frohlich_Sess2, 1, 'ascend');

% Remove the zeroes in the Eff_Greater_90
Eff_Greater_90(Eff_Greater_90 == 0) = [];

%% Identify participants that only completed a single session
Sess1_only = []; %Variable to store participants that only did sess 1
Sess2_only = []; %Store participants that only did Sess 2

for PC1 = 1:length(Frohlich_Sess1)
    if sum(Frohlich_Sess1(PC1, 1) == Frohlich_Sess2(:, 1)) ~= 1;
        Sess1_Only(PC1, 1) = Frohlich_Sess1(PC1, 1);
    end
 
    if PC1 <= length(Frohlich_Sess2)
        if sum(Frohlich_Sess2(PC1, 1) == Frohlich_Sess1(:, 1)) ~= 1;
            Sess2_Only(PC1, 1) = Frohlich_Sess2(PC1, 1);
        end
    end
end

% Remove rows == zero
Sess1_Only(Sess1_Only == 0) = [];
Sess2_Only(Sess2_Only == 0) = [];

%% Remove the following participants that did not complete a second session, did not converge their staircases, or pressed one key

%FIRSTLY, WE JUST WANT TO REMOVE PARTICIPANTS WHO DID ONLY ONE SESSION
Remove_Parts = [2, 4, 6, 15, 39, 46, 47, 70, 74, 84, 88, 108, 119 Sess1_Only', Sess2_Only'];
Remove_Parts = unique(Remove_Parts); %Use unique to remove any ID's listed multiple times in Remove_Parts

for RR = 1:length(Remove_Parts)
    CP = Remove_Parts(RR);%Current part to remove
    Rem_Idx_1 = Frohlich_Sess1(:, 1) == CP; %Row Index to remove session 1 people
    Rem_Idx_2 = Frohlich_Sess2(:, 1) == CP; % Row index to remove session 2 people
    %Remove participant from both sessions
    Frohlich_Sess1(Rem_Idx_1, :) = [];  
    Frohlich_Sess2(Rem_Idx_2, :) = [];
end %End of the remove participant list

% Now tell me how many people did this illusion
if length(Frohlich_Sess1) ~= length(Frohlich_Sess2)
    error('!!! THERE IS NOT AN EQUAL NUMBER OF PEOPLE IN EACH SESSION, PLEASE REVIEW YOUR CODE !!!')
end

% Sample size
Sample_Size = length(Frohlich_Sess1); 
disp([int2str(length(Frohlich_Sess1)) 'completed session 1 and ' int2str(length(Frohlich_Sess2)) ' completed session 2']);
A = input('Press enter to continue!')

% NOW, WE REMOVE PARTICIPANTS WHO PRESSED ONE KEY
 %One_key_List = unique(One_key_List); 
for Remove_P = 1:length(One_key_List(:, 1))
    CP = One_key_List(Remove_P, 1);%Current part to remove
    Rem_Idx_1 = Frohlich_Sess1(:, 1) == CP; %Row Index to remove session 1 people
    Rem_Idx_2 = Frohlich_Sess2(:, 1) == CP; % Row index to remove session 2 people
    %Remove participant from both sessions
    Frohlich_Sess1(Rem_Idx_1, :) = [];  
    Frohlich_Sess2(Rem_Idx_2, :) = [];
end %End of the remove participant list

% Now tell me how many people did this
if length(Frohlich_Sess1) ~= length(Frohlich_Sess2)
    error('!!! THERE IS NOT AN EQUAL NUMBER OF PEOPLE IN EACH SESSION, PLEASE REVIEW YOUR CODE !!!')
end

Sample_Size(:, 2) = [length(Frohlich_Sess1)];

 % NOW WE WANT TO REMOVE PARTICIPANTS THAT HAD STAIRCASES THAT DID NOT CONVERT 

for Remove_P = 1:length(Not_Converged(:, 1))
    CP = Not_Converged(Remove_P, 1);%Current part to remove
    Rem_Idx_1 = Frohlich_Sess1(:, 1) == CP; %Row Index to remove session 1 people
    Rem_Idx_2 = Frohlich_Sess2(:, 1) == CP; % Row index to remove session 2 people
    
    %Remove participant from both sessions
    Frohlich_Sess1(Rem_Idx_1, :) = [];  
    Frohlich_Sess2(Rem_Idx_2, :) = [];
end %End of the remove participant list

% Now tell me how many people did this
if length(Frohlich_Sess1) ~= length(Frohlich_Sess2)
    error('!!! THERE IS NOT AN EQUAL NUMBER OF PEOPLE IN EACH SESSION, PLEASE REVIEW YOUR CODE !!!')
end

Sample_Size(:, 3) = length(Frohlich_Sess1);

%% NOW WE REMOVE EFFECTS GREATER THAN 90
sum(Frohlich_Sess1(:, 2:3) > 90)
sum(Frohlich_Sess2(:, 2:3) > 90)

%% Check before we save the variables that participants are still sequentially ordered
A = 0; % Proxy variables to double check something
for P_Count = 1:length(Frohlich_Sess1)
    if Frohlich_Sess1(P_Count, 1) == Frohlich_Sess2(P_Count, 1)
        A = A+1;
    end
end

if A ~= length(Frohlich_Sess1);
    error('After you removed some variables, Frohlich effect session variables no longer have participants in the same order');
    return; %Leave script early
end
clear('RR', 'A', 'CP', 'Rem_Idx_1', 'Rem_Idx_2'); %Clean unnecessary variables from memory

%% Clean the convergence variables
% Remove the zeros from the converging lists
Not_Converged = Not_Converged(Not_Converged(:, 1) ~= 0, :);
Questionable_Converge = Questionable_Converge(Questionable_Converge(:, 1) ~= 0, :);
disp(strcat(int2str(length(unique(Not_Converged(:,1)))), ' participants had a staircase that did not converge'));
disp(strcat('There is a total of: ', {' '}, int2str(sum(isnan(Frohlich_Sess1(:, 2)))), ' NaNs in Session 1, and a total of ', {' '}, ...
    int2str(sum(isnan(Frohlich_Sess2(:,2)))), ' NaNs in session 2'));

%% Calculate the difference in effect between session 1 and 2
Froh_Eff_Difference = [];
Frohlich_Effect = []; %Overall effect   

for PartCounter = 1:length(Frohlich_Sess2)
    %Allocate participant
    Froh_Eff_Difference(PartCounter, 1) = Frohlich_Sess2(PartCounter, 1); 
    Froh_Eff_Difference(PartCounter, 2) = Frohlich_Sess2(PartCounter, 2) - Frohlich_Sess1(Frohlich_Sess1(:, 1) == Frohlich_Sess2(PartCounter, 1), 2);
    
    %%% Overall effect
    Frohlich_Effect(PartCounter, 1) = Frohlich_Sess2(PartCounter, 1);
    Frohlich_Effect(PartCounter, 2) = mean([Frohlich_Sess2(PartCounter, 2)  Frohlich_Sess1(Frohlich_Sess1(:, 1) == Frohlich_Sess2(PartCounter, 1), 2)]);
end

%% Identify effects with z-scores > 3. Don't remove, could be a genuine effect?
%Session 1 outliers?
Z_Sess1 = [Frohlich_Sess1(:, 1) normalize(Frohlich_Sess1(:, 2), 'zscore')]; % Convert scores to z-score
Z_Idx_S1 = abs(Z_Sess1(:, 2)) > 3; %Use absolute, to just raw find z-scores > or < +/- 3
Outliers_S1 = Frohlich_Sess1(Z_Idx_S1, :); %Outliers in session 1 
Z_S2 = [Frohlich_Sess2(:, 1) normalize(Frohlich_Sess2(:, 2), 'zscore')]; % Convert session 2 to z
Z_Idx_S2 = abs(Z_S2(:, 2)) > 3; %Use absolute, to just raw find z-scores > or < +/- 3
Outliers_S2 = Frohlich_Sess2(Z_Idx_S2, :); %Session 2 outliers
%Leave outliers in right now. 

%% Remove these participants (Most of these should have been picked up by the rule)
% P7 only pressed one buttn the whole time
% P8 did not converge
% P15, stairs went in opposite direction
% P22, only pressed one button
% P23_S1, seems to have only pressed one button
% p24, appears to have pressed only one button
% P33 - Staircaes do not converge
% 
% Remove_List = [7, 8, 15, 22, 24, 33, 42

%% Save effect file
save('Frohlich_Values.mat', 'Frohlich_Sess1', 'Frohlich_Sess2', 'Frohlich_Effect'); 
disp(['There is a total of ' int2str(sum(isnan(Frohlich_Sess1(:, 2)))) ' nans in the Frohlich effect']);
