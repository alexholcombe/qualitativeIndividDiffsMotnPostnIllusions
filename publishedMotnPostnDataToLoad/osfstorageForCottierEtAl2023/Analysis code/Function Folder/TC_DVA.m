%% This code converts from pixels to DVA
% Created by Tim Cottier
% Uses the specifications for the ASUS PG258Q
% Code was obtained from: https://imaging.mrc-cbu.cam.ac.uk/imaging/TransformingVisualAngleAndPixelSize
% Changes to code were made based upon this post: https://www.sr-research.com/eye-tracking-blog/background/visual-angle/

%% Input parameters
% XCoord = Distance of the object from the centre (0, 0)
% Pixel_Width = The width of the pixels in mm
% Screen_Distance = Distance of the screen from the participant

%% Function code
function [VisAngleX, VisAngleY] = TC_DVA(XCoord, YCoord, Pixel_Width, Screen_Distance)

%--- SPECIFY THE MONITOR PARAMETERS
%Based on the ASUS 258Q parameters specified here: 
    % https://rog.asus.com/au/monitors/23-to-24-5-inches/rog-swift-pg258q-model/spec/
Screen_Width = 543.7; % In MM
Screen_height = 302.6; % In MM
Resolution = [1920, 1080]; % Resolution of screen 

if nargin <4 %This means a Screen_Distance was not provided
    Screen_Distance = 500; % Distance from screen to participant in MMs (~50cms)
    if nargin <3 % This means a Pixel_width was not provided
        Pixel_Width = Screen_Width/Resolution(1); % How wide each pixel is in MM
    end
end

if ~isempty(XCoord) %They provided an xcoord
    VisAngleX = atand((XCoord * Pixel_Width)/Screen_Distance); % Degrees of visual angle
else % They did nt provide an xcoord
    VisAngleX = nan;
end

if nargin == 2 && ~isempty(YCoord) % This means a YCoord was provided
    Pixel_Height = Screen_height/Resolution(2);
    VisAngleY = atand((YCoord * Pixel_Height)/Screen_Distance); %Vertical degrees of visual angle
else
    VisAngleY = NaN;

end % End of Y coordinate nargin
end % End of function statement
