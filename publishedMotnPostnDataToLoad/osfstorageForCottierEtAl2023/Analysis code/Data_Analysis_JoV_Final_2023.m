%% Illusion effect table
% Written by Timothy Cottier, PhD student at the University of Melbourne
% The pre-processing and effect calculation for each illusion occurs in separate files.
% The current code simply imports the illusory effects, and calculates and
% plots correlations between illusions. 

%% Housekeeping
clear all;
close all;
clc;

if ispc
% Switch to the path 
try 
    cd('')
    addpath(genpath('\Function Folder'));

catch
    cd('')
    addpath(genpath('/Function Folder'));
    addpath('/Robust_Statistical_Toolbox-master')
end

%%%% Add function folder
addpath(genpath('*\OneDrive\Study 1\Analysis code\Function Folder'));
%addpath(genpath('*\OneDrive - The University of Melbourne\Study 1\Analysis code\Function Folder\Cbrewer2\cbrewer2'));

% Import ColorBrewer for Color coding the plots
addpath(genpath(['*' filesep 'Study 1' filesep 'Analysis code' filesep 'Function Folder' filesep 'Cbrewer2' filesep 'cbrewer2']));

elseif ismac
   addpath(genpath('/Users/timcottier/Library/CloudStorage/OneDrive-TheUniversityofMelbourne/Study 1/Analysis code/Function Folder'));
end

% Image format to save the images
fileFormat = '.tif';

%% Screen parameters for conversion to DVA
%From here: https://www.sr-research.com/eye-tracking-blog/background/visual-angle/
%Atan returns in radians; atand returns inverse tangent in degrees

%Specify in mms
Distance_Screen = 500; %Distance to the screen
Wrong_Screen_Width = 546; %I measured and put the screen width into PsychoPY at 54.6cms 
Actual_Screen_Width = 543.7; %The screen width is actuall 54.37 according to ASUS website
Screen_Width = Actual_Screen_Width; 
Screen_Height = 302.6; %30.26cms https://rog.asus.com/au/monitors/23-to-24-5-inches/rog-swift-pg258q-model/spec
DVA_Screen = 2*atand(Actual_Screen_Width/(2*Distance_Screen)); %Degrees of visual angle subtended by the screen

%Screen resolution, in pixels
Vert_Res = 1080;
Hor_rez = 1920;

%Pixel per mm
Pix_Horz_MM = Screen_Width/Hor_rez;
Vert_Pix_MM = Screen_Width/Hor_rez;

%% Initialise tables to store illusion effects 
%  Number of participants to import; we had 119 participants who did at least one session
NumParts = 119; % We will import all the participants that did not do the pilot, then exclude those that did a single session

[Session_1, Session_2]  = deal(nan(NumParts, 9)); %Session 1 and 2 table, should be same length and width
[Session_1(:, 1), Session_2(:, 1)] = deal((1:NumParts)'); %Make column 1 participant
Average_Array = []; %The Average_array stores the effect for each illusion, averaged across both sessions
 
 %% Create variables for each illusion, that stores the values for both sessions 
 FD_eff = [];
 FG_eff = [];
 FLE_eff = [];
 FLLUM_eff = [];
 Frohlich_eff = [];
 Gabor_eff = [];
 TG_eff = [];
 FJ_eff = [];
 
%% Load in all the files
addpath('Effect files'); %Add the folder with the files to the path 

load('FD_Values.mat'); %Flash-drag
load('FG_Values.mat'); %Flash-grab
load('FLE_Values.mat'); %Flash-lag effect
load('Luminance_Values.mat'); %Flash-lag luminance
load('Frohlich_Values.mat'); %Fröhlich 
load('Gabor_Values.mat'); %Motion induced position shift
load('TG_Values.mat'); %Twinkle-goes
load('FJ_Values.mat'); %Flash-Jump

%% INTERPRETING THE EFFECTS
% Positive values = an effect in the expected duration

%FD: the flash had to be offset in the opposite direction of motion
%FG: target displaced in the direction of reversal
%FLE: Degrees  flash had to be offset ahead of  target, to remove effect.
%FLLUM:  The effect is, that the darker should be darker (a larger number)
    %So a positive number = the effect, larger numbers = larger magnitude.
    %Positive number = the ramp becoming darker, was perceived darker 
%Fröhlich  = how many degrees did it have to start offset in the direction opposite motion
    %Positive = larger effect (it had to be offset more in the direction
        % opposite motion to cancel the effect)
%Gabor = effect = amount you had to offset in direction opposite of motion
        % For the gabors to be perceived as aligned
%Twinkle-goes the squares disappearance needs to be offset in the direction opposite motion
    %Negative = squares offset in direction of motion, no effect
%Flash-jump
    % Positive = changed height in direction opposite motion
    % Negative = changed height in direction of motion

%% Import the illusion effects into an array
%Column for each illusion:
    %1 = participant ID, 2 = FD (Flash-lag effect); 3 = FG (flash-grab effect); 4 = FLE (flash-lag effect), 5= FLLUM (flash-lag luminance)
    % 6 = Fröhlich , 7 = Motion induced position shift, 8 = Twinkle Goes (Dy-st), 9 = Flash Jump;
    % 10 = Static TG, 11 = Date the session was completed

Re_order_List = {'FLE', 'FLE-Lum', 'Fröhlich', 'FD', 'FG', 'Motion induced position shift', 'TG', 'FJ'};
Illusion_List = {'Flash-lag effect', 'Flash-lag Luminance', 'Fröhlich effect', ...
    'Flash-drag effect', 'Flash-grab effect', 'Motion induced position shift', 'Twinkle-goes effect', 'Flash-jump effect'};
    

for PartID = 1:NumParts; %For each row
     CurrentPart = Session_1(PartID, 1);
   %Col 2 contains the illusion effect 
    
  %Flash-lag - Col 2 = Polar angle, 3 = DVA
    try
        Session_1(PartID, 2) = FLE_Sess1(FLE_Sess1(:,1) == CurrentPart, 3);
    catch
        Session_1(PartID, 2) = nan;
    end

    try
        Session_2(PartID, 2) = FLE_Sess2(FLE_Sess2(:,1) == CurrentPart, 3);
    catch
        Session_2(PartID, 2) = nan;
    end
  
  %Flash lag Luminance
    try
        Session_1(PartID, 3) = Lum_Eff_S1(Lum_Eff_S1(:, 1) == CurrentPart, 2); 
    catch
        Session_1(PartID, 3) = nan;
    end
        
    try
        Session_2(PartID, 3) = Lum_Eff_S2(Lum_Eff_S2(:, 1) == CurrentPart, 2);
    catch 
        Session_2(PartID, 3) = nan; 
    end

    %Fröhlich  - Col 2 = Polar angle, 3 = DVA
    try
        Session_1(PartID, 4) = Frohlich_Sess1(Frohlich_Sess1(:, 1) == CurrentPart, 3);
    catch
        Session_1(PartID, 4) = nan;
    end
            
    try
        Session_2(PartID, 4) = Frohlich_Sess2(Frohlich_Sess2(:, 1) == CurrentPart, 3);
    catch
        Session_2(PartID, 4) = nan;
    end

    % Flash- Drag
   try % Not all participants did all the illusions in a session, so we use try and catch to stop erroring out
        Session_1(PartID, 5) = FD_PSE_Effect_Sess1(FD_PSE_Effect_Sess1(:, 1) == CurrentPart, 2);
   catch
       Session_1(PartID, 5) = nan;
   end
       
   try
       Session_2(PartID, 5) = FD_PSE_Effect_Sess2(FD_PSE_Effect_Sess2(:, 1) == CurrentPart, 2);
   catch %If it errors out just set to NaN
        Session_2(PartID, 5) = nan;         
   end
   
    %Flash-Grab Effect - Col 2 = Polar angle, 3 = DVA
    try
        Session_1(PartID, 6) = FG_Effect_S1(FG_Effect_S1(:, 1) == CurrentPart, 3);
    catch
         Session_1(PartID, 6) = nan;
    end
    try
        Session_2(PartID, 6) = FG_Effect_S2(FG_Effect_S2(:, 1) == CurrentPart, 3); 
    catch
        Session_2(PartID, 6) = nan;
    end 
 
    %Motion induced position shift (De Valois and Devalois) 'Gab_Eff_S1', 'Gab_Eff_S2'
    try
        Session_1(PartID, 7) = Gab_Eff_S1(Gab_Eff_S1(:, 1) == CurrentPart, 2);
    catch
        Session_1(PartID, 7) = nan;
    end
       
    try
        Session_2(PartID, 7) = Gab_Eff_S2(Gab_Eff_S2(:, 1) == CurrentPart, 2);
    catch
        Session_2(PartID, 7) = nan;
    end

    %Twinkle-goes
    try
        Session_1(PartID, 8) = TG_PSE_Effect_Sess1(TG_PSE_Effect_Sess1(:, 1) ==  CurrentPart, 2);
    catch
        Session_1(PartID, 8) = nan;    
    end
    
    try
        Session_2(PartID, 8) = TG_PSE_Effect_Sess2(TG_PSE_Effect_Sess2(:, 1) ==  CurrentPart, 2);
    catch
        Session_2(PartID, 8) = nan; 
    end

    %Flash Jump
    try
        Session_1(PartID, 9) = Cai_Eff_S1(Cai_Eff_S1(:, 1) == CurrentPart, 2); 
    catch
        Session_1(PartID, 9) = nan;       
    end
    try
        Session_2(PartID, 9) = Cai_Eff_S2(Cai_Eff_S2(:, 1) == CurrentPart, 2);
    catch
        Session_2(PartID, 9) = nan;
    end

end %End of the data import loop

%% Remove the following participants that did not complete a second session
    % These people should have already been removed
Pilot_Parts = [2, 4, 6]; % This is the pilot participants
Remove_Parts = [Pilot_Parts, 15, 39, 46, 47, 70, 74, 84, 88, 108, 119]; % 2, 4, 6 are pilots 

for RR = 1:length(Remove_Parts)
    CP = Remove_Parts(RR);%Current part to remove
    Rem_Idx_1 = Session_1(:, 1) == CP; %Row Index to remove people
    Rem_Idx_2 = Session_2(:, 1) == CP; %Row Index to remove people
    
    %Remove participant from both sessions
    Session_1(Rem_Idx_1, :) = [];  
    Session_2(Rem_Idx_2, :) = [];
end %End of the remove participant list

clear('RR', 'CP', 'Rem_Idx_1', 'Rem_Idx_2'); %Clean unnecessary variables from memory

%%% Check that the two sessions have the same number of participants
if size(Session_1, 1) ~= size(Session_2, 1) 
    error("Session 1 and 2 do not have the same number of participants!");
    return % stop code execution
end

%% Calculate an average effect for each participant for each illusion (Store this in average_array)
Average_Array = nan(size(Session_2)); 

%Loop through one participant at a time
for AA = 1:length(Session_2(:, 1)); % AA is for each row in session 2
    Curr_Participant = Session_2(AA, 1); % Current participant we are feeding into the average_array
        
    % Extract the participants illusory effect for each session
    S1_Idx = Session_1(:, 1) == Curr_Participant; % We only want the rows that belong to the participant
    S2_Idx = Session_2(:, 1) == Curr_Participant; 
    
    S1_effects = Session_1(S1_Idx, :);
    S2_effects = Session_2(S2_Idx, :);
    
    % Check the extracted rows belong to the same participant 
        % Column 1 is the participants index value
    if S1_effects(:, 1) ~= S2_effects(:, 1)
       beep; %Play the system beep error notice
       error('THE EXTRACTED ROWS DO NOT BELONG TO THE SAME PARTICIPANT'); 
       return; %Exit the script
    end
    
    %Calculate the average effect across both sessions
    Av_Effect = mean([S1_effects; S2_effects], 1); %Average across the rows
    Average_Array(AA, :) = Av_Effect; %Store the average effect
    
    %Clear the effect variables to not cause any lingering issues
    clear('S1_effects', 'S2_effects')
end

%% Now we have imported the participants, tell me how many ARE NOT nans in each illusion
    % This needs to be identical to the people not NaNs from the pre-processing.
for ill = 2:9
    disp([Illusion_List(ill-1) ' in session 1 had not nans totaling: ' int2str(sum(~isnan(Session_1(:, ill))))]);
    disp([Illusion_List(ill-1) ' in session 2 had not nans totaling: ' int2str(sum(~isnan(Session_2(:, ill))))]);
    disp([Illusion_List(ill-1) ' in the Average_Arrary had not nans totaling: ' int2str(sum(~isnan(Average_Array(:, ill))))]);
end

%% PLOT THE SCATTERPLOTS between SESSION 1 AND 2
Num_Scatters = 1; %Num of times to plot scatters
Loop_Count = 0; %Initialise a loop counter for the while loop
Rem_outliers = 0; % Remove outliers

Loop_Count = Loop_Count + 1;     
    
%Initialise the figure
LinFig = figure();
LinFig.Position = [100 100 1600 900];

% Select the colour scheme for the scatters
[cb] = cbrewer2('qual', 'Set3', 12, 'pchip'); %Value 3 (12), is the number of colours; Each row is a colour

%Dot Colours
Dot_Col = [cb(5,:)]; 

% Remove obvious outliers 
% Scatterplots indicate the presence of five outliers in session 1
        % Two participant had scores above 20 dva
        % One participant had a socre below -10 dva
        % Two participants had scores above 20DVA on both sessions
        % Remove these participants
       
% Find the outlier participants
Froh_Outliers = unique([Session_1(Session_1(:, 4) < -10, 1); Session_1(Session_1(:, 4) > 15, 1);...
    Session_2(Session_2(:, 4) < -10, 1); Session_2(Session_2(:, 4) > 15, 1)])

% Remove the outliers from this analysis
for outlier = 1:length(Froh_Outliers)
    Session_1(Session_1(:, 1) ==Froh_Outliers(outlier), 4) = nan;
    Session_2(Session_2(:, 1) == Froh_Outliers(outlier), 4) = nan;
    Average_Array(Average_Array(:, 1) == Froh_Outliers(outlier), 4) = nan;
end

%Use a loop to draw the plots
for scat_Count = 1:8
    
    subplot(2, 4, scat_Count) %Use this to select subplot location
    C_idx =  scat_Count + 1; %Correlation to select
    scatter(Session_1(:, C_idx), Session_2(:, C_idx), [], Dot_Col, 'filled')
    Line = lsline ; %Specify the least-squares line 
    
    try
        try
            Rho = table2array(Between_Session_Correlation(2, scat_Count))
        catch
            Rho = (Between_Session_Correlation(2, scat_Count))
        end

        Rho = strrep(sprintf('%.2f\n', Rho), '0.', '.');
        Txt = Rho; %num2str(table2array(Between_Session_Correlation(2, scat_Count))); % Corr_Idx
        PVal = Between_P(2, scat_Count); 
    end 
    
    if scat_Count == 1
        t = title(Illusion_List(scat_Count));    
        
        Txt_X =  -3;
        Txt_Y = 8;
        ylim([-4, 9])%([-3.5, 7])
        xlim([-4, 9])
        
    elseif scat_Count == 2
       t= title('Luminance flash-lag effect');
               
       Txt_X =  -0.32;
       Txt_Y = 0.5;
       xlabel('Session 1 luminance contrast (%)', 'FontSize', 14)
       ylabel('Session 2 luminance contrast (%)', 'FontSize', 14)
        
       ylim([-0.4, 0.6])
       xlim([-0.4, 0.6])

    elseif scat_Count == 3
        t = title(Illusion_List(scat_Count));
        
        Txt_X =  -3;
        Txt_Y = 7;
        ylim([-4, 8]) %([-3.5, 6])
        xlim([-4, 8])

 elseif scat_Count == 4
     
        xlim([-0.15, 0.3])
        t = title(Illusion_List(scat_Count)); 
        
        xlim([-0.2, 0.4])
        ylim([-0.2, 0.4]) %([-0.15, 0.4])
        
        %Specify x and y location of the correlation on the graph
        Txt_X =  -0.16;
        Txt_Y = 0.35;
        
    elseif scat_Count == 5
        t = title(Illusion_List(scat_Count));
        
       Txt_X = 1;
        Txt_Y = 9;
        ylim([0, 10]);
        xlim([0, 10]);
        
    elseif scat_Count == 6
        t = title(Illusion_List(scat_Count));
        
        Txt_X =  0.15;
        Txt_Y = 2.25;
        ylim([-0.2, 2.5])
        xlim([-0.2, 2.5])
            
    elseif scat_Count == 7
        t = title(Illusion_List(scat_Count));
        
        Txt_X =  -0.3;
        Txt_Y = 2.25;
        ylim([-0.5, 2.5])
        xlim([-0.5, 2.5])

    elseif scat_Count == 8
        t = title(Illusion_List(scat_Count)); 
        
        Txt_X = -0.82;
        Txt_Y = 1.7;
        ylim([-1, 2]) %([-0.6, 1.5])
        xlim([-1, 2])
    end % End of the if statement
    
    t.FontSize = 16; % SET THE FONT-SIZE OF THE SUBPLOT TITLES
  % xlabel('Session 1', 'FontWeight', 'bold', 'FontSize', 14)
  %  ylabel('Session 2', 'FontWeight', 'bold', 'FontSize', 14)

  try
   %  -------------- GET AND INITIALISE TEXT FOR THE SPEARMAN'S RHO ------
    SigTxt = 'significant'; % All were significant
    if PVal <.001
       PTxt = '<.001';
    else 
        PTxt = int2str(PVal);
        
        if PVal > .05
            SigTxt = 'non-significant';
        end
    end
    
    %%%% THIS ONE SHOWS P VALUES
    %Txt = append("{\itr}_s= ", Txt, ', {\itp} = ', PTxt) % ", {\itp} = ", PTxt)
    %%% AS ALL <0.001, just put ** 

    Txt = strcat("{\itr}_s= ", Txt, '^{**}') % ", {\itp} = ", PTxt)
    text(Txt_X, Txt_Y, Txt,'FontWeight','bold', 'FontSize', 16)
end
end %Stop drawing the scatterplots     

%%% Save the correlation scatters
Out_Status = ['-without-outliers' fileFormat]; %Status on outliers

% Add the x and y labels
han = axes(LinFig, 'visible', 'off');
han.XLabel.Visible = 'on';
han.YLabel.Visible='on';
ylabel(han, 'Session 2 illusion magnitude (dva)', 'FontSize', 20, 'FontWeight','bold');
xlabel(han, 'Session 1 illusion magnitude (dva)', 'FontSize', 20, 'FontWeight','bold');

saveas(LinFig, ['Test-retest', Out_Status]); 
% close(LinFig)

%% Normality assumption checks
    %Loop iteration 1, look at session 1
    %Loop iteration 2, look at session 2
    % Loop iteration 3, look at average effect 

% Create a folder to solve the normality check outputs
if ~(isfolder('Normality_Check'));
   mkdir('Normality_Check');
end

Normality = {'Normal', 'Non-normal'};

% Sample size
SampSize = [sum(~isnan(Session_1(:, 2:end))); sum(~isnan(Session_2(:, 2:end))); sum(~isnan(Average_Array(:, 2:end)))];  % Exclude nans in sample size
DF = SampSize - 1; % Degrees of freedom

for sn = 1:3 
    %Histograms
    Norm_fig = figure;
    Norm_fig.Position = [100 100 1600 900];

    if sn == 1;
        toplot = Session_1;
        str = 'Session 1';
        hstr = 'S1';
    elseif sn == 2
        toplot = Session_2;
        str = 'Session 2';
        hstr = 'S2'
    elseif sn == 3
        toplot = Average_Array;
        str = 'average effect';
        hstr = 'av';
    end
        
    for NP = 1:2 %Loops through what to plot 
                % Iteration 1, plot histograms
                % Iteration 2, plot qq-plots
    for SP = 1:8 %Loop through the subplot position on the figure
        CI = SP+1; %Correlation_index
        if NP == 1 %Plot histograms
            subplot(2, 5, SP);
            histfit(toplot(:, CI));
            ylabel('Density'); 
        end
%         elseif NP == 2
%             subplot(2, 5, SP);
%             probplot(toplot(:, CI));  %qqplot(toplot(:, CI));
%         end 

        xlabel(Illusion_List{SP}, 'FontWeight', 'bold'); %Put the illusion on the x axis

        % https://osf.io/2ngdk > Code is based on this by Grzeckowski et al. (2017) 
        % Conduct kolmogorov-smirnov test for each illusion
        [h,p,ksstat,cv] = kstest(toplot(:, CI));
        fprintf(1, '\nKSTest showed illusion %s distribution was %s for %s, K-S stat = %0.2f, df = %0.2f, p = %0.2f', Illusion_List{SP}, Normality{h+1}, str, ksstat, DF(sn, SP), p);
        
        %Put the K-S statistic on the subplot
        if p < 0.001
            pval = '< 0.001';
        else
            pval = num2str(round(0, 4));
        end
        
        Txt = append("{\itK-S} = ", num2str(ksstat), '{\it, p} = ', (pval)); % ", {\itp} = ", PTxt)
        title(Txt);
    end % End of the subplot loop
    fprintf(''); %Please put a space between each session
    
    try
    if NP == 1
        %Save the histogram and close the histogram window
        sgtitle(['Histograms for ', str], 'FontWeight', 'bold');
        saveas(Norm_fig, ['Normality_Check' filesep 'Histograms' filesep 'Normality_Hists_', hstr, Out_Status]);
     %   close(Norm_fig);   
    elseif NP == 2
        sgtitle(['PP-Plots for ', str], 'FontWeight', 'bold');
        if ~isfolder(['Normality_Check', filesep, 'PP'])
           mkdir(['Normality_Check', filesep, 'PP'])
        end
        saveas(Norm_fig, ['Normality_Check' filesep 'PP' filesep 'PP-Plots_', hstr, Out_Status]);
 %       close(Norm_fig);
    end
    end
    end % End of the choose histogram or QQ Plot
end %End of the normality assumption check loop. 

%----- Remove outliers I have identified via histagrams
% Participant 80 was -25 on Session 1, and then -75 on session 2, seems
Num_Scatters = 0

%% Test-retest reliability; correlations of session 1 to session 2 (within illusion correlations)
[Between_Session_Correlation, Between_P, Between_Partial, Partial_P, Part_Booth, Booth_P, Part_Corr, Part_P] = deal(zeros(1,8)); %There is 8 illusions

%Rows in Session 2 with NaNs
S2_NaNs = Session_2(sum(isnan(Session_2), 2) > 0, :);

%%%% CORRELATIONS
for Corr_Idx = 2:9 %There's 8 correlations; Col 1 = part
    Idx = Corr_Idx-1; %This is the index for the orws
    
    %We will make line the session 1, does session 1 predict session 2
    S1 = Session_1(:, Corr_Idx); %Session 1
    S2 = Session_2(:, Corr_Idx); %Session 2
   
    %%%% REGULAR CORRELATION
    %Pearson's r in Row 1
    [Between_Session_Correlation(1, Idx), Between_P(1, Idx)] = (corr(S1, S2, 'Rows', 'complete'));
    
    %Spearman's in Row 2
    [Between_Session_Correlation(2, Idx), Between_P(2, Idx)] = (corr(S1, S2, 'Type', 'Spearman', 'Rows', 'complete'));

%     try
%         %%%% PARTIAL CORRELATION - controlling for numbers of day between
%         %%%% sessions
%         [Between_Partial(1, Idx), Partial_P(1, Idx)] = partialcorr(S1, S2, Final_Days(:, 2), 'Type', 'Spearman', 'Rows', 'complete');
% 
%         %%% Partial correlation - controlling for computer booth
%         [Part_Booth(1, Idx), Booth_P(1, Idx)] = partialcorr(S1, S2, Final_Days(:, 3), 'Type', 'Spearman', 'Rows', 'complete');
% 
%         %Partial correlation - controlling for numbers of days between sessions
%                 %and booth
%         [Part_Corr(1, Idx), Part_P(1, Idx)] = partialcorr(S1, S2, Final_Days(:, 2:3), 'Type', 'Spearman', 'Rows', 'complete');
%     end
end

Between_Session_Correlation = round(Between_Session_Correlation, 4);
Between_Partial = round(Between_Partial, 4);

%%% Put these into tables
Between_Session_Correlation = array2table(Between_Session_Correlation, 'VariableNames', ...
    {'FLE', 'FLE-Lum', 'FE', 'FD', 'FG', 'Motion induced position shift', 'TG', 'Fj'}, ...
    'RowNames', {'Pearsons', 'Spearmans'});

% try %The ssd may not be connected
% 
% Between_Partial = array2table(Between_Partial, 'VariableNames', ...
%     {'FD', 'FG', 'FLE', 'FLLUM', 'Fröhlich ', 'Motion induced position shift', 'TG', 'FJ', 'RM'}, ...
%     'RowNames', {'Spearmans'});
% 
% Part_Booth = array2table(Part_Booth, 'VariableNames', ...
%     {'FD', 'FG', 'FLE', 'FLLUM', 'Fröhlich ', 'Motion induced position shift', 'TG', 'FJ', 'RM'}, ...
%     'RowNames', {'Spearmans'});
% 
% Part_Corr = array2table(Part_Corr, 'VariableNames', ...
%     {'FD', 'FG', 'FLE', 'FLLUM', 'Fröhlich ', 'Motion induced position shift', 'TG', 'FJ', 'RM'}, ...
%     'RowNames', {'Spearmans'});
% end

%% Get the sample size that went into each illusion
Sess_1_Samp = sum(~isnan(Session_1(:, 2:end))); 
Sess_2_Samp = sum(~isnan(Session_2(:, 2:end)));

%% Descriptive statistics
% Mean
Sess1_Mean = mean(Session_1(:, 2:end), 'omitnan'); % Mean for session 1 for each illusion
Sess2_Mean = mean(Session_2(:, 2:end), 'omitnan'); % Mean for session 2 for each illusion
Av_mean = mean(Average_Array(:, 2:end), 'omitnan');  % Mean for the average effect for each illusion

%Standard deviation
Sess1_SD = std(Session_1(:, 2:end), 'omitnan');
Sess2_SD = std(Session_2(:, 2:end), 'omitnan');  
Av_SD = std(Average_Array(:, 2:end), 'omitnan'); 

%% PURGE ALL THE IMAGES BEFORE RAINCLOUD PLOTS
close all;

%% Rain cloud plots
% Code originally from here: https://github.com/RainCloudPlots/RainCloudPlots 
% This is based upon the paper: "Allen, M., Poggiali, D., & Whittaker et al. (2009).
    %Raincloud Plots: A multi-platform tool for robust data visualation.

%--- Specify parameters of the raincloud plot
%Select colour scheme for raincloud plots
[cb] = cbrewer2('qual', 'Set3', 12, 'pchip'); %Value 3 (12), is the number of colours; Each row is a colour

%Set the colours of the rainplots for each session
Rain_Col_S1 = cb(5,:);
Rain_Col_S2 = cb(4,:);

%Size of the rain drops
DotSize = 50; %220

% Y axis lower bound
Lower_Bound = 1.3; %Default = 1

% Difference in Y Coordinates for the dots between session 1 and 2
Dot_Y_Diff = 0.15; 

%Boxplot line width - > This has been setup to not affect the clouds line width
Box_line_width = 2; %6;

%--- Density type
Dens_Type = 'ks'; %Default is matlab's ksdentsity.  

% ---- HIDE THE AXIS VALUES (The ticks)
Hide_Ax = 1; 

% -- DO YOU WANT THE BLACK DASHED LINE IN THE CENTRE OF EACH PLOT TO LINE UP    
Cent_Line = 1; % 0 = false; 1 = true

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%% --- Start the loop to make 9 rain cloud plots

for Plot_idx = 1:2 %Individual or overall loop
    % Plot_idx == 1 means plot the raincloud plot as a separate figure
    % Plot_idx == 2, plot all the raincloud plots on a single figure

for Illusion_Idx = 2:9 %Illusion loop
    
Corr_Idx = Illusion_Idx - 1; %Index used to select the between-session correlation
%--- Speciy the parameters for each illusions plot

%What illusion is it, and what units are the effects in
if Illusion_Idx == 6
    Which_Illusion = 'FG'; %'Flash-grab';
    Eff_units = 'Degrees of visual angle';
    YLimits = [-0.25 0.31];

    Subplot_Loc = 1; % Where to put the illusions subplot

    show_x = 0; %Don't show x axis

    %Parameters for the overlapping raincloud plots
    Dot_Dodge_S1 = 0.55; %Dot position
    Dot_Dodge_S2 = 0.55; %Dot position
    Box_Dodge_S1 = 0.125;
    Box_Dodge_S2 = 0.34; 

    DotY_S1 = [-0.17];
    DotY_S2 = [-0.22];
  
    Txt_Y = 0.22;
    Ill_Y = 0.22;

    if Cent_Line
        XLimits = [-6 10];


        %-- Where to put the correlations on the graph
        Txt_X = 5.75;
        
        %Where you put the illusion name on the graph
        Ill_X = -4.1;
    else
        XLimits = [-10 10];

        %-- Where to put the correlations on the graph
        Txt_X = 27;
        
        %Where you put the illusion name on the graph
        Ill_X = 2;
    end

elseif Illusion_Idx == 7
    Which_Illusion = 'MIPS'; %'Motion induced position shift';
    Eff_units = 'Degrees of Visual Angle'; 
    YLimits = [-1.8 2];

    Subplot_Loc = 5;
    show_x = 0; %Don't show x axis

    Lower_Bound = 1; %Default = 1
    
    %Parameters for the overlapping raincloud plots
    Dot_Dodge_S1 = 0.6; %Dot position
    Dot_Dodge_S2 = 0.6; %Dot position 
    Box_Dodge_S1 = 0.125;
    Box_Dodge_S2 = 0.3;

    DotY_S1 = [-1];
    DotY_S2 = [-1.4];
  
    Txt_Y = 1.70;
    Ill_Y = 1.70;

    if Cent_Line
        XLimits = [-1.5 2.2]

        %-- Where to put the correlations name on the graph
        Txt_X = 0.875;
    
        %Where you put the illusion name on the graph
        Ill_X = -1.2;

    else
        XLimits = [-0.6, 2.2];

        %-- Where to put the correlations name on the graph
        Txt_X = 1.25;
    
        %Where you put the illusion name on the graph
        Ill_X = -0.58;

    end
    
elseif Illusion_Idx == 8
    Which_Illusion =  'TG';%'Twinkle-goes';
    Eff_units = 'Degrees of Visual Angle'; 
    YLimits = [-2 2.5];

    Subplot_Loc = 2; 
    show_x = 0; % Don't show x axis

    Lower_Bound = 1.3; %Default = 1

    %Parameters for the overlapping raincloud plots
    Dot_Dodge_S1 = 0.65; %Dot position
    Dot_Dodge_S2 = 0.55; %Dot position 
    Box_Dodge_S1 = 0.125;
    Box_Dodge_S2 = 0.28;

    DotY_S1 = [-1.22];
    DotY_S2 = [-1.62];

    Txt_Y = 2.1;
    Ill_Y = 2.1;

    if Cent_Line 
        XLimits = [-1.5 2.2]

        %-- Where to put the Correatlions name on the graph
        Txt_X = 0.65;
    
        %Where you put the illusion name on the graph
        Ill_X = -1.2;

    else
        XLimits = [-0.5 2];

        %-- Where to put the Correatlions name on the graph
        Txt_X = 1.1;
    
        %Where you put the illusion name on the graph
        Ill_X = -0.475;
    
    end


elseif Illusion_Idx == 5
     Which_Illusion = 'FD'; %'Flash-drag';
    Eff_units = 'Degrees of Visual Angle'; 
    YLimits = [-8 9];
    
    Subplot_Loc = 6;
    show_x = 1; % Show x ais

    %Parameters for the overlapping raincloud plots
    Dot_Dodge_S1 = 0.55; %Dot position
    Dot_Dodge_S2 = 0.55; %Dot position
    Box_Dodge_S1 = 0.125; %Box 1 position
    Box_Dodge_S2 = 0.4; %Box two position

    % 1 = Lower bound; 2 = Upper bound
    DotY_S1 = [-5];
    DotY_S2 = [-6.5];

    Txt_Y = 7;
    Ill_Y = 7;

    if Cent_Line % We want to centre line 

        XLimits = [-0.5 0.5]
        %-- Where to put the correlations on the graph
        Txt_X = 0.16;
    
        %Where you put the illusion name on the graph
        Ill_X = -0.4;

    else
        XLimits = [-0.21, 0.4];

        %-- Where to put the correlations on the graph
        Txt_X = 0.2;
    
        %Where you put the illusion name on the graph
        Ill_X = -0.17

    end   

elseif Illusion_Idx == 4
    Which_Illusion = 'FE'; %'Fröhlich';
    Eff_units = 'Degrees of visual angle';
    YLimits = [-0.36 0.31];
    
    Subplot_Loc = 4;
    show_x = 0; % Don't show x 

    Lower_Bound = 1.3; %Default = 1
   
    %Parameters for the overlapping raincloud plots
    Dot_Dodge_S1 = 0.7; %Dot position
    Dot_Dodge_S2 = 0.6; %Dot position 
    Box_Dodge_S1 = 0.17;
    Box_Dodge_S2 = 0.4;

    DotY_S1 = [-0.2];
    DotY_S2 = [-0.3];
    
    Txt_Y = 0.22;
    Ill_Y = 0.22;

    if Cent_Line
        XLimits = [-6 10];

       %-- Where to put the correlations name on the graph
        Txt_X = 3;
        
        %Where you put the illusion name on the grah
        Ill_X = -4.1;

    else
        XLimits = [-4 10];

        %-- Where to put the correlations name on the graph
        Txt_X = 16;
        
        %Where you put the illusion name on the graph
        Ill_X = -65;    
    end
    

elseif Illusion_Idx == 2
    Which_Illusion = 'FLE'; %'Flash-lag effect';
    Eff_units = 'Degrees of visual angle';
    YLimits = [-0.2 0.2];

    Subplot_Loc = 7; 
    show_x = 1; %Show the x axis
        
    %Parameters for the overlapping raincloud plots
    Dot_Dodge_S1 = 0.55; %Dot position
    Dot_Dodge_S2 = 0.55; %Dot position
    Box_Dodge_S1 = 0.15;
    Box_Dodge_S2 = 0.4;

    DotY_S1 = [-0.12];
    DotY_S2 = [-0.16];

    Txt_Y = 0.15;
    Ill_Y = 0.15;

    if Cent_Line
        XLimits = [-6 10];

        %-- Where to put the correlations name on the graph
        Txt_X = 4.5;
    
        %Where you put the illusion name on the graph
        Ill_X = -4.1;
  
    else
        XLimits = [-4 10];

        %-- Where to put the correlations name on the graph
        Txt_X = 17;
        
        %Where you put the illusion name on the graph
        Ill_X = -30;
    end

elseif Illusion_Idx == 3
    Which_Illusion = 'LUM-FLE'; %'Luminance flash-lag';
    Eff_units = 'PsychoPY opacity (%)';
    YLimits = [-3.5 3.5];

    Subplot_Loc = 9;
    show_x = 1; % Don't show the x axis
        
    Lower_Bound = 1; %Default = 1
    
    %Parameters for the overlapping raincloud plots
    Dot_Dodge_S1 = 0.70; %Dot position
    Dot_Dodge_S2 = 0.8; %Dot position 
    Box_Dodge_S1 = 0.15;
    Box_Dodge_S2 = 0.40;

    DotY_S1 = [-1.9];
    DotY_S2 = [-2.5];

    Txt_Y = 2.5;
    Ill_Y = 2.5;

    if Cent_Line
        XLimits = [-0.5 0.5]

        %-- Where to put the correlations name on the graph
        Txt_X = 0.18;
    
        %Where you put the illusion name on the graph
        Ill_X = -0.4;
  
    else
        XLimits = [-0.62 0.75];

        %-- Where to put the correlations name on the graph
        Txt_X = 0.25;
    
        %Where you put the illusion name on the graph
        Ill_X = -0.58;
      end

elseif Illusion_Idx == 9
    Which_Illusion = 'FJ'; %'Flash-jump';
    Eff_units = 'Degrees of Visual Angle'; 
    YLimits = [-0.85 1];
    
    Subplot_Loc = 8; 
    show_x = 1; % We want to show the x axis for this one

    Lower_Bound = 0.8; %Default = 1

    %Parameters for the overlapping raincloud plots
    Dot_Dodge_S1 = 0.55; %Dot position
    Dot_Dodge_S2 = 0.55; %Dot position 
    Box_Dodge_S1 = 0.125;
    Box_Dodge_S2 = 0.325;

    DotY_S1 = [-0.5];
    DotY_S2 = [-0.68]; %DotY_S1 - Dot_Y_Diff/20

    %-- The Y stays constant, regardless of cent or not centered line
    Ill_Y = 0.8;
    Txt_Y = 0.8;

    if Cent_Line % This means we want the dashed line aligned across figures
        XLimits = [-1.5 2.2]

        Txt_X = 0.82;
        Ill_X = -1.2;

    else %Don't align dashed lines
        %-- Where to put the correlations on the graph
        Txt_X = 0.85;
        
        %Where you put the illusion name on the graph
        Ill_X = -0.8;

        XLimits = [-1  1.85]
    end
end 

%1 = plot the raincloud plots individually for each illusion, but overlapping for each session
%2 = plot the illusions as a subplot

if Plot_idx == 1 %Plot the rainclouds overlapping 
    Rain_Figs = figure('Position', [100 100 1900 900]);
elseif Plot_idx == 2 % Plot the raincloud plots as subplots
    Which_plot = Illusion_Idx - 1; 
    if Which_plot == 1 %Only initialise a new figure window for the first subplot
        Rain_Figs = figure('Position', [100 100 1900 900]);
        % Try a tiled layout
        t = tiledlayout(3,3);
    end 
    nexttile(Subplot_Loc); %Move to the next tile in the layout

end
    %Draw x line first to avoid issues
    xline(0, '--', 'color', [0 0 0 0.2], 'LineWidth', 4); hold on; % Put an x-line at zero
    
    [h1, u1, S1_DropsY] = raincloud_plot(Session_1(:, Illusion_Idx), 'box_on', 1, 'box_dodge', 1, 'box_dodge_amount', ...
        Box_Dodge_S1, 'color', Rain_Col_S1, 'alpha', 0.6, 'cloud_edge_col',Rain_Col_S1, ...
        'dot_dodge_amount', Dot_Dodge_S1, 'line_width', Box_line_width, 'box_col_match', 1, 'lwr_bnd', Lower_Bound, 'DotSize', DotSize, 'Dot_Edge', 1); 
%     hold on;
    
    [h2, u2, S2_DropsY] = raincloud_plot(Session_2(:, Illusion_Idx), 'box_on', 1, 'box_dodge', 1, 'box_dodge_amount', ...
        Box_Dodge_S2, 'color', Rain_Col_S2, 'alpha', 0.6, 'cloud_edge_col', Rain_Col_S2, 'dot_dodge_amount', ...
        Dot_Dodge_S2, 'box_col_match', 1, 'line_width', Box_line_width,  'lwr_bnd', Lower_Bound, 'DotSize', DotSize, 'Dot_Edge', 1); 

    %---- FORMAT THE CURRENT FIGURE WINDOW
%     if Illusion_Idx ~= 9
        set(gca, 'XLim', (XLimits));
        set(gca, 'YLim', (YLimits));
%     end
       %--- HIDE THE AXES TICK VALUES
%         if Hide_Ax
          if ~show_x
             xticks([])
          % Show the ticks for these illusions
          else
           if Illusion_Idx == 9
               xticks([-1.5, -1, -0.5, 0, 0.5, 1 1.5, 2]);
           elseif Illusion_Idx == 7
               xticks([-6, -4, -2, 0, 2, 4, 6, 8, 10]);
           elseif Illusion_Idx == 5 || Illusion_Idx == 3
               xticks([-0.5, -0.3, -0.1, 0, 0.1, 0.3, 0.5]);
               if Illusion_Idx == 3
                    xticklabels({'-50', '-30', '-10', '0', '10', '30', '50'});
               end
           elseif Illusion_Idx == 2
               xticks([-6, -4, -2, 0, 2, 4, 6, 8, 10]);
           end %End statement for specify xticks
          end 
             yticks([]) %Hide y ticks, as the distribution density values are not meaningful

        %- BOLD THE AXES LINEWIDTH
        set(gca,'linewidth',4)

    %--- Put the mean for each session as an x line
    S1_mean = mean(Session_1(:, Illusion_Idx), 'omitnan');
    S2_mean = mean(Session_2(:, Illusion_Idx), 'omitnan');

    % Draw a line 
    %S1 mean line
    mean_line_1 = line([S1_mean S1_mean], [0 YLimits(2)], 'LineStyle', '-', 'Color', Rain_Col_S1, 'LineWidth', 6); hold on; % Put an x-line at zero

    %S2 mean line
    mean_line_2 = line([S2_mean S2_mean], [0 YLimits(2)], 'LineStyle', '-', 'Color', Rain_Col_S2, 'LineWidth', 6); hold on; % Put an x-line at zero

    box off; 
     
    % FLLUM needs its own xlabel
    if Subplot_Loc == 9
        xlabel('Illusion magnitude % luminance contrast')
    end

    % Put the Y data in a single row
    n = length(Session_1); 
    h1{2}.YData = repmat(DotY_S1, n, 1); %Value to repeat, num rows, num cols (always 1)

    n = length(Session_2); 
    h2{2}.YData = repmat(DotY_S2, n, 1);

    % Plot lines between the markers
    RC_x = [(Session_1(:, Illusion_Idx))'; Session_2(:, Illusion_Idx)'];
    RC_y = [h1{2}.YData; h2{2}.YData];
    lh = plot(RC_x, RC_y, '-', 'Color', [0 0 0 0.5], 'LineWidth', 1, 'MarkerSize', DotSize);
    hold off
    
    set(gca, 'FontSize', 20)% Change the xtick size
    % This puts which illusion it is in the top left
    text(Ill_X, Ill_Y, Which_Illusion, 'FontSize', 24, 'FontWeight', 'bold');
end

% overarching x and y label 
han = axes(Rain_Figs, 'visible', 'off');
han.Title.Visible = 'on';
han.XLabel.Visible = 'on';
han.YLabel.Visible = 'on'; 
Label_Size = 26;

try % This will only work for the tiled layout
    ylabel(t, 'Distribution density', 'FontSize', Label_Size, 'FontWeight', 'bold')
    xlabel(t, 'Illusory magnitude (dva)', 'FontSize', Label_Size, 'FontWeight', 'bold'); 
    % Minimise the white space
    t.TileSpacing = 'compact';
    t.Padding = 'compact'; 

catch
    ylh = ylabel(han, 'Distribution density', 'FontSize', Label_Size, 'FontWeight', 'bold');
    xlh = xlabel(han, 'Illusory effect', 'FontSize', Label_Size); %xlh = x label handle
    %Change location of the x label - This moves it down by 10%:
    xlh.Position(2) =  xlh.Position(2) - abs(xlh.Position(2) * 1.6); 
    % Move the y label to the left
    ylh.Position(1) = ylh.Position(1) - abs(ylh.Position(1) * 0.8); 
end

lgd = legend([h1{2} h2{2} mean_line_1 mean_line_2], ...
    {'Session 1 participant scores', 'Session 2 participant scores', 'Session 1 mean', 'Session 2 mean'}, ...
    'Location', 'northeastoutside');
lgd.Position = lgd.Position + [0 0 0.14 0.158]

if Plot_idx == 1
    FileName = ([Which_Illusion '_Combined_Rains.jpg']);
elseif Plot_idx == 2
    FileName = ([Which_Illusion '_Single_Plot.jpg']);
end

Rain_Dir = '/Users/timcottier/Documents/2022/Study 1/Raincloud Plots';

saveas(Rain_Figs, fullfile(Rain_Dir, FileName))

end %Individual or overall loop

%% Correlation between llusions - average magnitude

%----- CLEAN UP THE DATA
Zero_Idx = (Average_Array(:, 1) == 0);%Get an index of zero rows to remove - just remove those with zero in the participant
Average_Array(logical(Zero_Idx), :) = []; %This will remove participant IDs that are zero (not possible to have a zero id)

% From here, set any zero values to nan
Average_Array(Average_Array == 0) = nan; 

%---- SAMPLE SIZE SANITY CHECKS
% %%% Average_array sample size - > this should be the same as before
AA_SampSize = sum(~isnan(Average_Array(:, 2:end)), 1)

% --- Check Average_array has the same participants as those in session 1 and session 2
for aaa = 1:length(Average_Array)
    %CheckList Col 1 = sess 1; Col 2 = Sess 2
    CheckList(aaa, 1) = sum(Average_Array(aaa, 1) == Session_1(:, 1));
    CheckList(aaa, 2) = sum(Average_Array(aaa, 1) == Session_2(:, 1));
end

SumCheck = sum(CheckList);
if SumCheck(1) ~= length(Session_1)
    error('SAMPLE SIZES ARE DIFFERENT BETWEEN AVERAGE ARRAY AND SAMPLE 1')
    return
end

if SumCheck(2) ~= length(Session_2)
    error('SAMPLE SIZES ARE DIFFERENT BETWEEN AVERAGE ARRAY AND SAMPLE 2')
    return
end

% %%%%%%%%%%%%%%%%%
%---- PAIRWISE CORRELATIONS
[Pear_Pair_Overall, Pear_Pair_P] = corr(Average_Array(:, 2:end), 'Type', 'Pearson', 'Rows', 'pairwise') %Pearon's's
[Pair_Overall, Pair_P] = corr(Average_Array(:, 2:end), 'Type', 'Spearman', 'Rows', 'pairwise') %Spearman's

Alpha = 0.05; 
Num_Correlations = 7 + 6 + 5 + 4 +3 + 2 +1; 
Bon_Corr = Alpha/Num_Correlations;

%Round the correlations
Pair_Overall = round(Pair_Overall, 4);
Pear_Pair_Overall = round(Pear_Pair_Overall, 4);

%%% Bootstrapped confidence intervals spearman's
% Create a function;
scorr = @(a) corr(a, 'Type', 'Spearman', 'Rows', 'pairwise'); % Spearman's function to feed into bootstrap
% The bootstrapped CI's go column to column
[spear_boot_CI, boot_rho] = bootci(1000, {scorr, Average_Array(:, 2:end)}, 'Type', 'bca', 'Alpha', 0.05); % 95%Bootstrapped confidence intervals for Spearman's Rho
spear_boot_CI = round(spear_boot_CI, 3) % Round the bootstrapped confidence intervals to 3 decimal points

%%% Bootstrapped confidence intervals pearson's
pcorr = @(a) corr(a, 'Type', 'Pearson', 'Rows', 'pairwise'); % Pearson's function to feed into bootstrap
P_boot_CI = bootci(1000, {pcorr, Average_Array(:, 2:end)}, 'Type', 'bca', 'Alpha', 0.05); % Pearson's 95% bootstrap CI
P_boot_CI = round(P_boot_CI, 3)

% To clean the presentation, zero out a heap of correlation and p values
for zz = 1:length(Pair_Overall)
    Pair_Overall(zz, zz:end) = 0; % Blank out on correlation atrix
    Pair_P(zz, zz:end) = 99; 
end


%% What was the final sample size for the significant correlations
Samp = sum(~isnan(Average_Array(:, 2:end))) 

%% Visualise correlations as a heatmap
fig = figure;
Corr_Heatmap = imagesc(Pair_Overall(2:end, 1:end-1)); %Image SC turns data into images
set(gca, 'XTick', 1:7); set(gca, 'YTick', 1:7);
set(gca, 'XTickLabel', {'FLE', 'LUM-FLE', 'FE', 'FD', 'FG', 'Motion induced position shift', 'TG'}, 'fontsize', 18); 
set(gca, 'YTickLabel', {'LUM-FLE', 'FE', 'FD', 'FG', 'Motion induced position shift', 'TG', 'FJ'}, 'fontsize', 18); 

colorcet('D1A') % Or D1
set(gca, 'clim', [-1, 1])
CB = colorbar()
CB.Label.String = "Spearman's rho"
CB.Label.FontWeight = "bold"
CB.Label.FontSize = 20
%title({'Correlations between illusions', 'Illusory magnitude averaged across sessions'}, 'FontSize', 18)
saveas(gcf,'Corr_Map_Overall_Pairwise.tif')

%--- Put these values in a table, highlighting bonferonni sig correlations
Overall_Table = array2table(Pair_Overall(2:end, 1:end-1), 'VariableNames', {'FLE', 'LUM-FLE', 'FE', 'FD', 'FG', 'Gab', 'TG'}, ...
    'RowNames', {'LUM-FLE', 'FE', 'FD', 'FG', 'Gab', 'TG', 'FJ'}) 

%Bonferoni corrected p values, there was 28 correlations
Alpha = 0.05; 
Bon_P = Alpha/28; % / Num comparisons
Overall_Table.Properties.DimensionNames(1) = {'Illusions'}; %Rename the first columns headr

% %%% SAVE THIS TABLE AS A TEXT FILE
writetable(Overall_Table, 'Pair_Overall_Correlations.csv', 'WriteRowNames', true)
fig = uifigure('Position',[500 500 760 360]);
uit = uitable(fig, 'Data', Overall_Table)
uit.Position = [20 20 720 320]

% ---- Colour the significant c orrelations red
styleIndices = Pair_P(:, :) < Bon_P %.05;
[row, col] = find(styleIndices)
s = uistyle('BackgroundColor', [1 0.6 0.6])
addStyle(uit, s, 'cell', [row, col])

% %%%%%% HERE, MAKE SURE YOU SAVE THE TABLE 
 exportapp(fig, 'Overall_Pair_Correlations.jpg')

%% Disattentuated (relaibility corrected) correlation coefficients
try
    Between_Session_Correlation = table2array(Between_Session_Correlation);
end

Disattentuated_Correlation = []; %Initialise array 
for Row_Idx = 1:size(Pair_Overall, 1) %For each row
    for Col_Idx = 1:7    % For each column
        Disattentuated_Correlation(Row_Idx, Col_Idx) = Pair_Overall(Row_Idx, Col_Idx)/sqrt(Between_Session_Correlation(2, Col_Idx) * Between_Session_Correlation(2, Col_Idx+1))
    end
end 

Disattentuated_Correlation(Disattentuated_Correlation > 1) = 1; % Cannot have spearman's above 1. So cap at 1

% To clean the presentation, zero out a heap of correlation and p values
for zz = 1:length(Disattentuated_Correlation)
    Disattentuated_Correlation(zz, zz:end) = 0; % Blank out on correlation atrix
end

% Put the correlation values on the correlation matrix
    % Based on code from here: https://au.mathworks.com/matlabcentral/fileexchange/15877-heat-maps-with-text

% Remove first row if abs(sum) > 0
if sum(abs(Disattentuated_Correlation(1, :))) <= 0
    Disattentuated_Correlation(1, :) = []
end

[rows,cols] = size(Disattentuated_Correlation);

for i = 1:rows
    for j = 1:i
                 textHandles(j,i) = text(j,i,num2str(round(Disattentuated_Correlation(i,j), 2)),...
                'horizontalAlignment','center', 'FontSize', 14, 'FontWeight', 'bold');
    end
end

%%% Write the table
%--- Put these values in a table, highlighting significant correlations
    % Use bonferonni correction
% Dis_Table = array2table(Disattentuated_Correlation(2:end, :), 'VariableNames', {'FG', 'Gab', 'TG', 'FD', 'Froh', 'FLE', 'Lum'}, ...
%     'RowNames', {'Gab', 'TG', 'FD', 'Froh', 'FLE', 'Lum', 'Fj'}) %'RM'}) 

Dis_Table.Properties.DimensionNames(1) = {'Illusions'}; %Rename the first columns headr

% % %%% SAVE THIS TABLE AS A TEXT FILE
% try
%     writetable(Dis_Table, 'Disattentuated_Correlations.csv', 'WriteRowNames', true)
%     fig = uifigure('Position',[500 500 760 360]);
%     uit = uitable(fig, 'Data', Dis_Table)
%     uit.Position = [20 20 720 320]
% end
%% Add the test-retest reliability and disattentuated correlations to the attenuated heatmaps
    % make a single heatmap Add the test re-test reliability values here
Between_Sess_Spear = (Between_Session_Correlation(2, :));

for TRT_Corr = 1:8
    Pair_Overall(TRT_Corr, TRT_Corr) = Between_Sess_Spear(TRT_Corr)
end

% Add the disattentuated values here
for Add_Corr = 1:7
    Pair_Overall(Add_Corr, Add_Corr+1:end) =  Disattentuated_Correlation(Add_Corr:end, Add_Corr)
end

Pair_Overall = round(Pair_Overall, 2)

%%% Visualise correlations on map
fig = figure; %fig.Position = [100 100 900 900]
Corr_Heatmap = imagesc(Pair_Overall()); %Image SC turns data into images
%make the interrater relaibility gray
for reset_Cdata = 1:8
    Corr_Heatmap.CData(reset_Cdata, reset_Cdata) = 0.5
end

set(gca, 'XTick', 1:8);
set(gca, 'YTick', 1:8);
set(gca, 'XTickLabel', {'FLE', 'LUM-FLE', 'FE', 'FD', 'FG', 'MIPS', 'TG', 'FJ'}, 'fontsize', 18, 'FontWeight', 'bold');
set(gca, 'YTickLabel', {'FLE', 'LUM-FLE', 'FE', 'FD', 'FG', 'MIPS', 'TG', 'FJ'}, 'fontsize', 18, 'FontWeight', 'bold'); 
colorcet('D1A'); % Or D1; %colormap('jet') % Matlab's yucky default
Corr_Heatmap.AlphaData = .8; %Reduce the transparency

set(gca, 'clim', [-1, 1]);
CB = colorbar()
CB.Label.String = "Spearman's rho"
CB.Label.FontWeight = "bold"
CB.Label.FontSize = 20

%Add numbers to the heatmap.rounded to two decimal points, no 0 in front. 
[rows,cols] = size(Pair_Overall);

Text_Size = 18; 

for j = 1:cols
    for i = 1:rows

        if j == i %& j~=3 & j ~=7
                textHandles(j,i) = text(j,i,strcat(strrep(num2str(round(Pair_Overall(i,j), 2)), '0.', '.'), '*'),...
                'horizontalAlignment','center', 'FontSize', Text_Size, 'FontWeight', 'bold', 'Color', [1, 1, 1]);

        elseif j == 3 & i == 4
                textHandles(j,i) = text(j,i,strcat(strrep(num2str(round(Pair_Overall(i,j), 2)), '0.', '.'), '*'),...
                'horizontalAlignment','center', 'FontSize', Text_Size, 'FontWeight', 'bold');
           
        elseif j == 5 & i == 6
                textHandles(j,i) = text(j,i,strcat(strrep(num2str(round(Pair_Overall(i,j), 2)), '0.', '.'), '*'),...
                'horizontalAlignment','center', 'FontSize', Text_Size, 'FontWeight', 'bold');

        elseif j == 5 & i == 7
                textHandles(j,i) = text(j,i,strcat(strrep(num2str(round(Pair_Overall(i,j), 2)), '0.', '.'), '*'),...
                'horizontalAlignment','center', 'FontSize', Text_Size, 'FontWeight', 'bold');
       
        elseif j == 6 & i == 7
                textHandles(j,i) = text(j,i,strcat(strrep(num2str(round(Pair_Overall(i,j), 2)), '0.', '.'), '*'),...
                'horizontalAlignment','center', 'FontSize', Text_Size, 'FontWeight', 'bold');

        else
                 textHandles(j,i) = text(j,i,strrep(num2str(round(Pair_Overall(i,j), 2)), '0.', '.'),...
                'horizontalAlignment','center', 'FontSize', Text_Size, 'FontWeight', 'bold');

        end
    end
end


%% Sample size in each illusion - excluding NaNs
S1_SampSize = sum(~isnan(Session_1(:, 2:end)), 1)
S2_SampSize = sum(~isnan(Session_2(:, 2:end)), 1)
Average_Array_SampleSize = sum(~isnan(Average_Array(:, 2:end)), 1)

%% Look at the correlations between sessions
% Look at pairwise correlations for each illusion between sess 1 and 2

[Between_Sess_Corr, Between_Sess_p] = corr(Session_1(:, 2:end), Session_2(:, 2:end), 'Type', 'Spearman', 'Rows', 'pairwise'); 

% Round to three
Between_Sess_Corr = round(Between_Sess_Corr, 3);
Between_Sess_p = round(Between_Sess_p, 3);

%--- Put these values in a table, highlighting bonferonni sig correlations
Between_Sess_Tab = array2table(Between_Sess_Corr, 'VariableNames', {'FLE', 'LUM-FLE', 'FE', 'FD', 'FG', 'Gab', 'TG', 'FJ'}, ...
    'RowNames', {'FLE', 'LUM-FLE', 'FE', 'FD', 'FG', 'Gab', 'TG', 'FJ'}) 
Between_Sess_Tab.Properties.DimensionNames(1) = {'Illusions'}; %Rename the first columns headr

% % %%% SAVE THIS TABLE AS A TEXT FILE
% writetable(Between_Sess_Tab, 'Pair_Overall_Correlations.csv', 'WriteRowNames', true)
% fig = uifigure('Position',[500 500 760 360]);
% uit = uitable(fig, 'Data', Between_Sess_Tab)
% uit.Position = [20 20 720 320]
% 
% % ---- Colour the significant correlations red
% styleIndices = Between_Sess_p(:, :) < Bon_P %.05;
% [row, col] = find(styleIndices)
% s = uistyle('BackgroundColor', [1 0.6 0.6])
% addStyle(uit, s, 'cell', [row, col])

%% Save Average effect for each participant.
writematrix(Average_Array, 'Average_Array.csv');
