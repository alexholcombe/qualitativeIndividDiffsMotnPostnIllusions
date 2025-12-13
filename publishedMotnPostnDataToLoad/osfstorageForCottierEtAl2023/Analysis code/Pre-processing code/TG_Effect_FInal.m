 %% Twinkle Goes analysis
%Written by Timothy Cottier, PhD student University of Melbourne

%% House keeping/setup
close all; clear all; clc;

% Monitor dimensions
HorRes = 1920;
VertRes = 1080;
AspectRat = HorRes/VertRes; %Ratio of width to height

addpath ''; %Add function path to library

%%% Do you want to plot the graph?
PlotGraph = 0; %
Plot_Eff = 0;%input("Do you want to plot the effect graphs for each stair? 1 = Yes")

%% %%%%%%%%%%%%%%%%
%%% IMPORT DATA PARAMETERS %%%
%%%%%%%%%%%%%%%%%%%
if ismac == 1
    DataLocation = '';
    ImDir = ''; %Save the images in this folder
elseif ispc
    DataLocation = '';
    ImDir = '';
end
DataType = [filesep '*.csv']; 
addpath(DataLocation);

%Get files
FilesinDir = dir(strcat(DataLocation, DataType));
DataFileNames = {FilesinDir.name}';

%% Initialise PSE storage variables
% Store PSE - Row = participant;
PSESubs_Sess1 = []; %Session 1
PSESubs_Sess2 = []; %Session 2

NumTrials = 40; % Number of trials per staircase

%How many trials to average over to get the PSE
AvOver = 10; %Because there's only 40 trials, I find that some people are very noisy upto about ~30
Stair_Trial_Check = []; %AS A SANITY CHECK, just store the MAXIMUM Trial count for each stair

% INITIALISE VARIABLES TO STORE THE PSE effects (Col 1 = part; Col 2 = effect)
    % TG effect = Dynamic - static staircase
TG_PSE_Effect_Sess1 = []; %Session 1 
TG_PSE_Effect_Sess2 = []; %Session 2

% Static only
ST_Effects_Sess1 = []; 
ST_Effects_Sess2 = [];

%Dynamic only -(Col 1 = Part; Col 2 = Dynamic)
DY_Effects_Sess1 = [];
DY_Effects_Sess2 = []; 

%Reversal effects
TG_Rev_Effect_Sess1 = [];
TG_Rev_Effect_Sess2 = [];

%% Initialise variables to check staircase convergence
%Initialise parameters to check if convergence occurred
    %Col 1 = Part; Col 2 = Sess;
     % Col 3 ST right to left; Col 4 ST Left to right, 
     % Col 5 DY right to left;  Col 6 DY left ro right
Con_Storage = []; 
Quest_Storage = [];
Not_Converged = [];

%Threshold when we decide if something is questionable or not converged
Quest_Thresh = 30; %Questionable/possibly didn't converge
Not_Con_Thresh = 50; %Definitely did not converge

% Pressed one-key - Store if participants pressed mostly one key during the staircase
One_key_List = [];

%% Data importation loop
for N_file = 1:length(DataFileNames) %We want it to loop through the calculations for each participant 
    % Clear variables between loop calls to minimise errors
    clear('CurrentPart', 'CurrentSession', 'TGTab', 'ST1', 'ST2', 'ST3', 'ST4', 'ST5', 'ST6', 'ST7', 'ST8');
    TGTab = readtable(string(DataFileNames(N_file))); %For each file, read in the table 
    CurrentPart = max(TGTab.participant); %The current participant
    CurrentSession = max(TGTab.session);% Current sesion
    
    %% Split the table into staircases

    %- STAIRCAE INFORMATION:
        %Odd Number staircases = top square moved right to left
        %Even number staircases = top square moved left to right

    %%%% STATIC NOISE TABLES
    ST1 =  TGTab(TGTab.StairNoEx == 1, :);
    ST2 =  TGTab(TGTab.StairNoEx == 2, :);
    ST3 =  TGTab(TGTab.StairNoEx == 3, :);
    ST4 =  TGTab(TGTab.StairNoEx == 4, :);
   
    %%%% DYNAMIC NOISE TABLES    
    ST5 =  TGTab(TGTab.StairNoEx == 5, :);
    ST6 =  TGTab(TGTab.StairNoEx == 6, :);
    ST7 =  TGTab(TGTab.StairNoEx == 7, :);
    ST8 =  TGTab(TGTab.StairNoEx == 8, :);
    
    %%% CHECK THE STAIRCASES TRIAL COUNTS ARE EQUAL TO 40
    Stair_Trial_Check(N_file, :) = [max(TGTab.Stair1TC), max(TGTab.Stair2TC), max(TGTab.Stair3TC), max(TGTab.Stair4TC), ...
        max(TGTab.Stair5TC), max(TGTab.Stair6TC), max(TGTab.Stair7TC), max(TGTab.Stair8TC)];
    
    if sum(Stair_Trial_Check(1, :) == NumTrials) ~= 8
        error('!!!WARNING THE TRIAL COUNTS ARE NOT EQUAL!!!');
        disp(strcat('Participant: ', int2str(CurrentPart), '_Session', int2str(CurrentSession), 'does not have equal trialcount for each staircase!!!'));
        return %Exit the script
    end
    
    %% Check if the participant pressed a single key for 80% of a single staircase
    Threshold_key = NumTrials * 0.8; % Pressing a single-key for 80% of the trials
    NumPresses = [sum(strcmp(ST1.Resp_keys, 'right')) sum(strcmp(ST1.Resp_keys, 'left'));...
        sum(strcmp(ST2.Resp_keys, 'right')) sum(strcmp(ST2.Resp_keys, 'left'));...
        sum(strcmp(ST3.Resp_keys, 'right')) sum(strcmp(ST3.Resp_keys, 'left'));...
        sum(strcmp(ST4.Resp_keys, 'right')) sum(strcmp(ST4.Resp_keys, 'left'));...
        sum(strcmp(ST5.Resp_keys, 'right')) sum(strcmp(ST5.Resp_keys, 'left'));...
        sum(strcmp(ST6.Resp_keys, 'right')) sum(strcmp(ST6.Resp_keys, 'left'));...
        sum(strcmp(ST7.Resp_keys, 'right')) sum(strcmp(ST7.Resp_keys, 'left'));...
        sum(strcmp(ST8.Resp_keys, 'right')) sum(strcmp(ST8.Resp_keys, 'left'))]; %Col 1 = Number of Right responses, Col 2 = Left
    
    % Identify if one of the keys was pressed over 80% of the time for two staircases
    Failed_Key = 0; %Reset variable to store if they failed the key-press check
    if sum(NumPresses>Threshold_key) >= 2; 
       KeyIdx = size(One_key_List, 1)+1; %Current row to store the values into 
       One_key_List(KeyIdx, :) = [CurrentPart, CurrentSession];
       Failed_Key = 1; %If true only pressed one key 80% of the time for at least two staircases
    end

    %% Calculate PSE by averaging over last 10 trials for each staircase
    ST1_PSE = mean(ST1.Stair1(end-AvOver:end, :));
    ST2_PSE = mean(ST2.Stair2(end-AvOver:end, :));
    ST3_PSE = mean(ST3.Stair3(end-AvOver:end, :));
    ST4_PSE = mean(ST4.Stair4(end-AvOver:end, :));
    ST5_PSE = mean(ST5.Stair5(end-AvOver:end, :));
    ST6_PSE = mean(ST6.Stair6(end-AvOver:end, :));  
    ST7_PSE = mean(ST7.Stair7(end-AvOver:end, :));
    ST8_PSE = mean(ST8.Stair8(end-AvOver:end, :));      

    %Calculate the effect here, Average across staircases within direction
    %%% STATIC NOISE EFFECT
    ST_RtL = mean([ST1_PSE ST3_PSE]);
    ST_LtR = mean([ST2_PSE ST4_PSE]);
    ST_effect = (ST_RtL - ST_LtR)/2;
    
    %%% DYNAMIC NOISE EFFECT
    DY_RtL = mean([ST5_PSE ST7_PSE]);
    DY_LtR = mean([ST6_PSE ST8_PSE]);
    DY_effect = (DY_RtL - DY_LtR)/2;

    %%% TWINKLE-GOES EFFECT
    TG_Effect = (DY_effect - ST_effect);
      
%% CHECK IF THE STARICASES CONVERGED
    Con_Av = 6; %Check that convergence occurred over the last 6 trials 
    ST1_Con = mean(ST1.Stair1(end-Con_Av:end, :));
    ST2_Con = mean(ST2.Stair2(end-Con_Av:end, :));
    ST3_Con = mean(ST3.Stair3(end-Con_Av:end, :));
    ST4_Con = mean(ST4.Stair4(end-Con_Av:end, :));
    ST5_Con = mean(ST5.Stair5(end-Con_Av:end, :));
    ST6_Con = mean(ST6.Stair6(end-Con_Av:end, :)); 
    ST7_Con = mean(ST7.Stair7(end-Con_Av:end, :));
    ST8_Con = mean(ST8.Stair8(end-Con_Av:end, :));  
    
    %Check the difference within directions 
        %Use abs(), because we are just interested in absolute difference
    RtL_ST = abs(ST3_Con - ST1_Con); % static - right to left
    LtR_ST = abs(ST4_Con - ST2_Con); % Static - Left to right
    RtL_DY = abs(ST7_Con - ST5_Con); % Dynamic - right to left
    LtR_DY = abs(ST8_Con - ST6_Con); % Dynamic - left to rigt
    
    % Store the absolute difference with the convergence
    Con_Storage(N_file, 1:6) = [CurrentPart, CurrentSession, RtL_ST, LtR_ST, RtL_DY, LtR_DY]; 
    % Reset variables
    Not_Converge = false; %Did not converge
    Quest_Converge = false; %Possibly did not converge

    %Within static and dynamic, explore if convergence did not occur
    %%% Static
    if RtL_ST > Quest_Thresh || LtR_ST > Quest_Thresh % Are they greater than questionable convergence
        if RtL_ST > Not_Con_Thresh || LtR_ST > Not_Con_Thresh % Did not converge
            %ST_effect = NaN;
            Not_Converge = true; %Didn't converge
        else
            Quest_Converge = true; %Possibly didn't converge - check
        end
    end
        
    %%% Dynamic
    if RtL_DY > Quest_Thresh || LtR_DY > Quest_Thresh 
        if  RtL_DY > Not_Con_Thresh || LtR_DY > Not_Con_Thresh
            %DY_effect = NaN; %Set to NaN - convergence threshold breached
            Not_Converge = true;
        else
            Quest_Converge = true;
        end
    end

    %%% Store the states of convergence
    if Not_Converge == true; % Did not converge
            Not_Converged(N_file, 1:6) = [CurrentPart, CurrentSession, RtL_ST, LtR_ST, RtL_DY, LtR_DY]; 
            %TG_Effect = NaN; %Give NaNs to effecets that don't converge
    elseif Quest_Converge == true; % Possibly didn't converge
            Quest_Storage(N_file, 1:6) = [CurrentPart, CurrentSession, RtL_ST, LtR_ST, RtL_DY, LtR_DY]; 
    end
    
    %% Store the PSE and effects 
        % Each row is a separate participant
        % Col1 = Participant ID, Col 2-9 = PSE for staircase 
    if CurrentSession == 1  % Current session is 1 
        PSESubs_Sess1(N_file, 1:9)= [CurrentPart, ST1_PSE, ST2_PSE, ST3_PSE, ST4_PSE, ST5_PSE, ST6_PSE, ST7_PSE, ST8_PSE]; %Store PSEs
        TG_PSE_Effect_Sess1(N_file, 1:2) = [CurrentPart, TG_Effect]; % Store Twinkle-goes effect
        ST_Effects_Sess1(N_file, 1:2) = [CurrentPart, ST_effect]; %Store the static effect
        DY_Effects_Sess1(N_file, 1:2) = [CurrentPart, DY_effect]; %Store the dynamic effect
    elseif CurrentSession == 2 % Currently session 2
        PSESubs_Sess2(N_file, 1:9)= [CurrentPart, ST1_PSE, ST2_PSE, ST3_PSE, ST4_PSE, ST5_PSE, ST6_PSE, ST7_PSE, ST8_PSE]; %Store PSE
        TG_PSE_Effect_Sess2(N_file, 1:2) = [CurrentPart, TG_Effect]; %Store Twinkle-goes effect
        ST_Effects_Sess2(N_file, 1:2) = [CurrentPart, ST_effect]; %Store the static effect
        DY_Effects_Sess2(N_file, 1:2) = [CurrentPart, DY_effect]; %Store the dynamic effect
    end
        
%% Plot the staircase per participant - Not in publication
    %On iteration 1, plot individual staircases
%     %On iteration 2, plot static stair
%     %On iteration 3, plot dynamic stair
% if PlotGraph %If true, will plot
%     for pNum = 1:3
%         if pNum == 1    %Plot stairs individually
%             Ind_Fig = figure;
%             Ind_Fig.Position = [100 100 1300 900];   
%             t = tiledlayout(2, 1, 'TileSpacing', 'compact')
%             nexttile
%         elseif pNum == 2 %Plot every part on one graph, only initialise the figure once
%             if N_file == 1 
%                 STfig = figure('Name', 'Static staircases all participants');
%                 STfig.Position = [100 100 1300 900];   
%             end
%             figure(STfig); hold on; %Call this figure - should be open already?
%         elseif pNum == 3    
%             if N_file == 1
%                 DYfig = figure('Name', 'Dynamic staircases all participants')
%                 DYfig.Position = [100 100 1300 900];   
%             end
%             figure(DYfig); %Same logic as above
%             hold on;  %We use hold on to draw all participants on one figure
%         end
%     if pNum <3 %Only plot the static staircases for loop iteration 1 and 2
%         plot(ST1.Stair1TC, ST1.Stair1, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0])
%         hold on
%         plot(ST2.Stair2TC, ST2.Stair2, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0])
%         plot(ST3.Stair3TC, ST3.Stair3, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0])
%         plot(ST4.Stair4TC, ST4.Stair4, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0])
%         xlabel("Trial Number"); 
%         %ylabel({"Positive values: Squares are displaced in the direction of motion", "Negative: Displaced in the direction opposite motion"});
%         xlim([0, 45])
%         yline(0, '- r')
%         % ylim([(min(ToPlot.SqOffset) - 0.01), (max(ToPlot.SqOffset) + 0.01)]);
%         title('Static staircases');
%         aleg = legend({'RtL Dynamic, AHead', 'LtR Dynamic, Ahead', 'RtL Dynamic, Behind', 'LtR Dynamic, Behind'}, 'Location', 'bestoutside');
%         title(aleg, 'Staircase');
%     end 
%     if pNum == 1
%         hold off;
%         nexttile;
%     end
%     
%     if pNum == 1 || pNum == 3 %Don't plot dynamic staircases for the static stair
%         plot(ST5.Stair5TC, ST5.Stair5, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0])
%         hold on
%         plot(ST6.Stair6TC, ST6.Stair6, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0])
%         plot(ST7.Stair7TC, ST7.Stair7, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0])
%         plot(ST8.Stair8TC, ST8.Stair8, '-s', 'MarkerEdgeColor', 'black', 'MarkerFaceColor', [0 0 0])
% 
%         hold off
%         xlabel("Trial Number"); 
%         %ylabel({"Positive values: Squares are displaced in the direction of motion", "Negative: Displaced in the direction opposite motion"});
%         xlim([0, 45])
%         % ylim([(min(ToPlot.SqOffset) - 0.01), (max(ToPlot.SqOffset) + 0.01)]);
%         title('Dynamic staircases');
%         yline(0, '- r');
%         aleg = legend({'RtL Dynamic, AHead', 'LtR Dynamic, Ahead', 'RtL Dynamic, Behind', 'LtR Dynamic, Behind'}, 'Location', 'bestoutside');
%         title(aleg, 'Staircase');
%         sgtitle(['Participant: ' int2str(CurrentPart) ', Session: ' int2str(CurrentSession)])
%     
%     if pNum == 1
%         saveas(Ind_Fig, fullfile(ImDir, strcat('Stairs_P', int2str(CurrentPart),'_S', int2str(CurrentSession), '.png')));
%         close(Ind_Fig) %Close the window to stop heaps of images 
%         
%     elseif pNum == 3
%         if N_file == length(DataFileNames)
%             saveas(STfig, 'ST_Stair_All_Parts.png');
%             saveas(DYfig, 'DY_Stair_All_Parts.png');
%         end       
%     end
%     
%     end
%     end % End of the pnum for loop
%end %End of plotting loop
end %%% END OF DATA IMPORT LOOP

%% DOUBLE-CHECK THAT THE TRIAL COUNTS ARE THE SAME
if mean(mean(Stair_Trial_Check)) ~= 40
    disp('!!!WARNING!!!!');
    disp('STAIR TRIAL COUNTS ARE NOT IDENTICAL');
    return %Exit the script, as not all participants did the same trialcounts
end

%% Clean the variables
%Remove zeros from the convergence storage
Not_Converged(Not_Converged(:, 1) == 0, :) = [];
Quest_Storage(Quest_Storage(:, 1) == 0, :) = [];

%Remove participant zero rows
TG_PSE_Effect_Sess1(TG_PSE_Effect_Sess1(:, 1) == 0, :) = [];
TG_PSE_Effect_Sess2(TG_PSE_Effect_Sess2(:, 1) == 0, :) = [];
ST_Effects_Sess1(ST_Effects_Sess1(:,1) == 0, :) = [];
ST_Effects_Sess2(ST_Effects_Sess2(:,1) == 0, :) = [];
DY_Effects_Sess1(DY_Effects_Sess1(:, 1) == 0, :) = [];
DY_Effects_Sess2(DY_Effects_Sess2(:, 1) == 0, :) = [];

%Sort participants by ascending
TG_PSE_Effect_Sess1 = sortrows(TG_PSE_Effect_Sess1, 1, 'ascend');
TG_PSE_Effect_Sess2 = sortrows(TG_PSE_Effect_Sess2, 1, 'ascend');
ST_Effects_Sess1 = sortrows(ST_Effects_Sess1, 1, 'ascend');
ST_Effects_Sess2 = sortrows(ST_Effects_Sess2, 1, 'ascend'); 
DY_Effects_Sess1 = sortrows(DY_Effects_Sess1, 1, 'ascend');
DY_Effects_Sess2 = sortrows(DY_Effects_Sess2, 1, 'ascend'); 

%% Tell me which participants didn't do a TG session
No_Sess1 = [];
No_Sess2 = [];
for el = 1:116
    if sum(el == TG_PSE_Effect_Sess1(:, 1)) < 1
        No_Sess1(length(No_Sess1) + 1, :) = [el]
    end

    if sum(el == TG_PSE_Effect_Sess2(:, 1)) <1
        No_Sess2(length(No_Sess1) + 1, :) = [el]
    end
end

%% Identify participants that only completed a single session
Sess1_only = []; %Variable to store participants that only did sess 1
Sess2_only = []; %Store participants that only did Sess 2
for PC1 = 1:length(TG_PSE_Effect_Sess1)
    if sum(TG_PSE_Effect_Sess1(PC1, 1) == TG_PSE_Effect_Sess2(:, 1)) ~= 1;
        Sess1_Only(PC1, 1) = TG_PSE_Effect_Sess1(PC1, 1);
    end
 
if PC1 <= length(TG_PSE_Effect_Sess2)
    if sum(TG_PSE_Effect_Sess2(PC1, 1) == TG_PSE_Effect_Sess1(:, 1)) ~= 1;
        Sess2_Only(PC1, 1) = TG_PSE_Effect_Sess2(PC1, 1);
    end
end
end

% Remove rows == zero
Sess1_Only(Sess1_Only == 0) = [];
Sess2_Only(Sess2_Only == 0) = [];

%% Remove the following participants that did not complete a second session, or failed attention checks
Pilot_Parts = [2, 4, 6]; % These participants only participated in the pilot.
Remove_Parts = [2, 4, 6, 15, 39, 46, 47, 70, 74, 84, 88, 108, 119, Sess1_Only', Sess2_Only'];
Remove_Parts = unique(Remove_Parts); %Use unique to remove any participants listed multiple times in Remove_Parts

for RR = 1:length(Remove_Parts)
    CP = Remove_Parts(RR);%Current part to remove
    Rem_Idx_1 = TG_PSE_Effect_Sess1(:, 1) == CP; %Row Index to remove people  
    Rem_Idx_2 = TG_PSE_Effect_Sess2(:, 1) == CP; 
    Rem_Idx_ST1 = ST_Effects_Sess1(:, 1) == CP; %Remove those from difference scores
    Rem_Idx_ST2 = ST_Effects_Sess2(:, 1) == CP; %Remove those from difference scores
    Rem_Idx_DY1 = DY_Effects_Sess1(:, 1) == CP; %Remove from overall effect calculation
    Rem_Idx_DY2 = DY_Effects_Sess2(:, 1) == CP; %Remove from overall effect calculation
    
    %Remove participant from both sessions
    TG_PSE_Effect_Sess1(Rem_Idx_1, :) = [];  
    TG_PSE_Effect_Sess2(Rem_Idx_2, :) = [];
    ST_Effects_Sess1(Rem_Idx_ST1, :) = [];
    ST_Effects_Sess2(Rem_Idx_ST2, :) = []; 
    DY_Effects_Sess1(Rem_Idx_DY1, :) = []; 
    DY_Effects_Sess2(Rem_Idx_DY2, :) = [];

end %End of the remove participant list

% Sample size after completing the two sessions:
if length(TG_PSE_Effect_Sess1) ~= length(TG_PSE_Effect_Sess2)
    error('THE LENGTH OF SESSION 1 AND 2 ARE NOT THE SAME, PLEASE CHECK')
end

Sample_Size(:, 1) = length(TG_PSE_Effect_Sess1);

%% Remove participants that did not converge

for RR = 1:length(Not_Converged(:, 1) )
    CP = Not_Converged(RR, 1);%Current part to remove
    Rem_Idx_1 = TG_PSE_Effect_Sess1(:, 1) == CP; %Row Index to remove people  
    Rem_Idx_2 = TG_PSE_Effect_Sess2(:, 1) == CP; 
    Rem_Idx_ST1 = ST_Effects_Sess1(:, 1) == CP; %Remove those from difference scores
    Rem_Idx_ST2 = ST_Effects_Sess2(:, 1) == CP; %Remove those from difference scores
    Rem_Idx_DY1 = DY_Effects_Sess1(:, 1) == CP; %Remove from overall effect calculation
    Rem_Idx_DY2 = DY_Effects_Sess2(:, 1) == CP; %Remove from overall effect calculation
    
    %Remove participant from both sessions
    TG_PSE_Effect_Sess1(Rem_Idx_1, :) = [];  
    TG_PSE_Effect_Sess2(Rem_Idx_2, :) = [];
    ST_Effects_Sess1(Rem_Idx_ST1, :) = [];
    ST_Effects_Sess2(Rem_Idx_ST2, :) = []; 
    DY_Effects_Sess1(Rem_Idx_DY1, :) = []; 
    DY_Effects_Sess2(Rem_Idx_DY2, :) = [];

end %End of the remove participant list

% Sample size after completing the two sessions:
if length(TG_PSE_Effect_Sess1) ~= length(TG_PSE_Effect_Sess2)
    error('THE LENGTH OF SESSION 1 AND 2 ARE NOT THE SAME, PLEASE CHECK')
end

Sample_Size(:, 2) = length(TG_PSE_Effect_Sess1);

%% Remove participants that failed one key 
for OKL = 1:length(One_key_List(:, 1))
    CP = One_key_List(OKL, 1);%Current part to remove
    Rem_Idx_1 = TG_PSE_Effect_Sess1(:, 1) == CP; %Row Index to remove people  
    Rem_Idx_2 = TG_PSE_Effect_Sess2(:, 1) == CP; 
    Rem_Idx_ST1 = ST_Effects_Sess1(:, 1) == CP; %Remove those from difference scores
    Rem_Idx_ST2 = ST_Effects_Sess2(:, 1) == CP; %Remove those from difference scores
    Rem_Idx_DY1 = DY_Effects_Sess1(:, 1) == CP; %Remove from overall effectr calculation
    Rem_Idx_DY2 = DY_Effects_Sess2(:, 1) == CP; %Remove from overall effectr calculation
    
    %Remove participant from both sessions
    TG_PSE_Effect_Sess1(Rem_Idx_1, :) = [];  
    TG_PSE_Effect_Sess2(Rem_Idx_2, :) = [];
    ST_Effects_Sess1(Rem_Idx_ST1, :) = [];
    ST_Effects_Sess2(Rem_Idx_ST2, :) = []; 
    DY_Effects_Sess1(Rem_Idx_DY1, :) = []; 
    DY_Effects_Sess2(Rem_Idx_DY2, :) = [];
end

% Sample size after completing the two sessions:
if length(TG_PSE_Effect_Sess1) ~= length(TG_PSE_Effect_Sess2)
    error('THE LENGTH OF SESSION 1 AND 2 ARE NOT THE SAME, PLEASE CHECK')
end

Sample_Size(:, 3) = length(TG_PSE_Effect_Sess1);

%% Outliers 
%Remove the rows where participant is equal to zero
PSESubs_Sess1(PSESubs_Sess1(:, 1) == 0, :) = [];
PSESubs_Sess2(PSESubs_Sess2(:, 1) == 0, :) = [];

Z_Outliers = 3; % Threshold - Z-scores above this value are going to be considered outliers
Outlier_List = []; %Store outliers in here

Z_PSESubs_Sess1 = PSESubs_Sess1; %Assign this variable the PSE values
Z_PSESubs_Sess2 = PSESubs_Sess2;
Z_PSESubs_Sess1(:, 2:end) = normalize(Z_PSESubs_Sess1(:, 2:end), 'zscore'); %Convert PSE values to z-scores
Z_PSESubs_Sess2(:, 2:end) = normalize(Z_PSESubs_Sess2(:, 2:end), 'zscore');

% Identify participants with Z-scores > 3 
Z_S1_IDX = max(Z_PSESubs_Sess1(:, 2:end) > 3, [], 2);
Z_S2_IDX = max(Z_PSESubs_Sess2(:, 2:end) > 3, [], 2);
Outlier_List_S1 = PSESubs_Sess1(Z_S1_IDX, :); %C1 = Part, C2 = Session, C3:10 = PSEs
Outlier_List_S2 = PSESubs_Sess2(Z_S2_IDX, :); %C1 = Part, C2 = Session, C3:10 = PSEs
    
% Store list of outliers to end the of existing list
Outlier_List = [Outlier_List; Outlier_List_S1; Outlier_List_S2];

% Exclude outliers from both sessions
for out = 1:length(Outlier_List(:, 1))
    CP = Outlier_List(out, 1);
    Rem_Idx_1 = TG_PSE_Effect_Sess1(:, 1) == CP; %Row Index to remove people  
    Rem_Idx_2 = TG_PSE_Effect_Sess2(:, 1) == CP; 
    Rem_Idx_ST1 = ST_Effects_Sess1(:, 1) == CP; %Remove those from difference scores
    Rem_Idx_ST2 = ST_Effects_Sess2(:, 1) == CP; %Remove those from difference scores
    Rem_Idx_DY1 = DY_Effects_Sess1(:, 1) == CP; %Remove from overall effect calculation
    Rem_Idx_DY2 = DY_Effects_Sess2(:, 1) == CP; %Remove from overall effect calculation
    
    %Remove participant from both sessions
    TG_PSE_Effect_Sess1(Rem_Idx_1, :) = [];  
    TG_PSE_Effect_Sess2(Rem_Idx_2, :) = [];
    ST_Effects_Sess1(Rem_Idx_ST1, :) = [];
    ST_Effects_Sess2(Rem_Idx_ST2, :) = []; 
    DY_Effects_Sess1(Rem_Idx_DY1, :) = []; 
    DY_Effects_Sess2(Rem_Idx_DY2, :) = [];

end

% Sample size after completing the two sessions:
if length(TG_PSE_Effect_Sess1) ~= length(TG_PSE_Effect_Sess2)
    error('THE LENGTH OF SESSION 1 AND 2 ARE NOT THE SAME, PLEASE CHECK')
end

Sample_Size(:, 4) = length(TG_PSE_Effect_Sess1);

% Looks like no additional outliers are removed

% Now we removed the first few outliers, plot histograms for each session
if ~exist('Outlier_Hists')
    mkdir('Outlier_Hists')
end

if PlotGraph
    %Plot histograms for each stair
    %Session 1
    for Ctr = 2:9
        Curr_Stair = Ctr - 1;
        subplot(2, 4, Curr_Stair);
        hist(PSESubs_Sess1(:, Ctr));
        title(strcat('Stair ', {' '}, int2str(Curr_Stair)'));
    end
        sgtitle('PSE over last 20 trials for each staircase, in Session 1');
        saveas(gcf, strcat('Outlier_Hists\PSE_Sess1_Wave_', int2str(Z_Count),'.png'));
        close(gcf);
        
    %Session 2
    for Ctr = 2:9
        Curr_Stair = Ctr - 1;
        subplot(2, 4, Curr_Stair);
        hist(PSESubs_Sess2(:, Ctr));
        title(strcat('Stair ', {' '}, int2str(Curr_Stair)'));
    end
        sgtitle('PSE over last 20 trials for each staircase, in Session 2');
        saveas(gcf, strcat('Outlier_Hists\PSE_Sess2_Wave_', int2str(Z_Count), '.png'));
        close(gcf);
    end 

%% Tidy up the workspace by deleting some variables:
clear('RR', 'CP', 'Rem_Idx_1', 'Rem_Idx_2', 'Rem_Idx_ST1', 'Rem_Idx_2', 'Rem_Idx_ST1', 'Rem_Idx_ST2', 'Rem_Idx_DY1', 'Rem_Idx_DY2'); %Clean unnecessary variables from memory

%% Check before we save the variables that participants are still sequentially ordered
A = 0; % Proxy variables to double check something
for P_Count = 1:length(TG_PSE_Effect_Sess1)
    if TG_PSE_Effect_Sess1(P_Count, 1) == TG_PSE_Effect_Sess2(P_Count, 1) && ST_Effects_Sess1(P_Count, 1) == ST_Effects_Sess2(P_Count, 1) && DY_Effects_Sess1(P_Count, 1) == DY_Effects_Sess2(P_Count, 1)
        A = A+1;
    end
end
if A ~= length(TG_PSE_Effect_Sess1);
    error('After you removed some variables, TG_PSE_Effect_Sess1 session variables no longer have participants in the same order');
    return; %Leave script early
end
clear('A');

%% Convert pixels to DVA % - > Are you converting participant ID here (col 1)
ST_Effects_Sess1(:, 2) = TC_DVA(ST_Effects_Sess1(:,2)); 
ST_Effects_Sess2(:, 2) = TC_DVA(ST_Effects_Sess2(:,2));
DY_Effects_Sess1(:, 2) = TC_DVA(DY_Effects_Sess1(:, 2));
DY_Effects_Sess2(:, 2) = TC_DVA(DY_Effects_Sess2(:, 2)); 
TG_PSE_Effect_Sess1(:, 2) = TC_DVA(TG_PSE_Effect_Sess1(:, 2));
TG_PSE_Effect_Sess2(:, 2) = TC_DVA(TG_PSE_Effect_Sess2(:, 2)); 

%% Calculate the difference in illusory effect from session 1 to 2
%Difference value between the two sessions
    %Positive = increase in effect
    %Negative = decrease in effect
TG_PSE_Difference = []; %Initialise variable

for PartCounter = 1:length(TG_PSE_Effect_Sess2)
   TG_PSE_Difference(PartCounter, 1) = TG_PSE_Effect_Sess2(PartCounter, 1); %Allocate participant value
   TG_PSE_Difference(PartCounter, 2)= TG_PSE_Effect_Sess2(PartCounter, 2) - TG_PSE_Effect_Sess1(TG_PSE_Effect_Sess1(:, 1) == TG_PSE_Effect_Sess2(PartCounter, 1), 2); %Difference value 
end 

%% Save data
save('TG_Values.mat', 'ST_Effects_Sess1', 'ST_Effects_Sess2', 'TG_PSE_Effect_Sess1', ...
    'TG_PSE_Effect_Sess2');

disp(strcat('There is a total of: ', {' '}, int2str(sum(isnan(TG_PSE_Effect_Sess1(:, 2)))), ' NaNs in Session 1, and a total of ', {' '}, ...
    int2str(sum(isnan(TG_PSE_Effect_Sess2(:,2)))), ' NaNs in session 2'));