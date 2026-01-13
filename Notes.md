For individual-differences paper

## Motivation

This picture that the vast majority of recent papers provide, that extrapolation is the only live candidate explanation of the FLE, likely has negative consequences for other researchers, including applied researchers that don’t venture deeply into the basic literature. As an illustration of this, we point to a paper by clinical vision researchers that was published in 2025. For this paper, the researchers chose the FLE as a measure of the visual system’s extrapolation ability and concluded that amblyopes have impaired cortical extrapolation processing, on the basis of finding that the FLE was smaller in the amblyopes than in controls (Wang et al., 2025).

## Getting/checking the data of the largest study to date, Tim Cottier et al. JoV

On 18 December I went through all the below of Tim's OSF posting of the JoV data, but I think he's fixed it all since

TG has both Effects.Sess1 and PSE.Effect.Sess1, why is that?
For now, assume we want PSE, so delete Effects.Sess1

#### Discrepancy between published FD scale 

Published graphs go from 0 to around 10, but in the MATLAB files, 

mean(mm$FD.PSE.Effect.Sess1,na.rm=T)
[1] 30.46481

mean(mm$FD.PSE.Effect.Sess2,na.rm=T)
[1] 30.45448

#### Missing data for at least one session

FDE:  Datafiles has 104 participants, consistent with paper saying "The final sample size for this illusion comprised 104 participants." But participant 33 has missing values for FDE for both session 1 and session 2.	

Frohlich: there are 88 participants in the data file, consistent with the paper which says "The final sample size for this illusion comprised 88 participants." But participant 34 has missing values for both sessions, while 21 and 61 have missing values for just one session.

#### Outlier data not in the published paper figure

| illusion | participant | session | value      |
| -------- | ----------- | ------- | ---------- |
| Frohlich | 80          | 1       | -25.409091 |
| Frohlich | 80          | 2       | -74.772727 |
| Frohlich | 99          | 1       | -61.659091 |
| Frohlich | 99          | 2       | -2.204545  |


### Test for negative-effect participants

### Quantify temporal imprecision of each illusion

- trial-to-trial FLE variability: My prediction is that it'd be at least 50 ms in all participants (although random chance could result in some having a smaller value despite their true value being larger than 50).  Tim hadn't yet posted individual-trial data but he will later.

- Collect data for more severe test of qualitative differences (idea emerged with Frederik). E.g. use overlap FLE configuration, which seems to reduce size of effect because has to violate the shape cue

### Report what temporal magnitude (ms) is of each illusion

### Modeling non-responders (people who have exactly zero effect)

From email with Frederik 9-01-26: About the specifics of not using the Gaussian assumption, you mentioned "possibly with a spike at 0 for non-responders".  In the case of these motion and position illusions, I don't think it's as plausible as in the Stroop effect that there would be non-responders. In the case of the Stroop effect, one could be a "non-responder" for either of two reasons that I can think of. One is that they simply didn't do the task, or did it incorrectly, and no screening / outlier filtering was in place to exclude those participants. A second reason is that the participant can't read, or is such a bad reader that the reading isn't automatic ,so that their Stroop effect is zero. 
In the case of the motion and position illusions, Tim did do some filtering of outliers, which it would be good to remind ourselves of, as that may affect exactly how we think about the possibility of zero-effect people. Another possibility is that a person could be motion-blind (analogous to not being able to read), but that is so rare that there's probably less than 8 cases in the entire neuropsychological literature, and probably almost all of them had a major brain injury.  A third possibility is that the participant cheated by holding their fingers up to the screen or something to check the location of the object. Tim, what do you reckon is the chance of that? 
Perhaps we should assign a number to the proportion of participants that we think plausibly could be non-responders for one of these three reasons. I'm going to say that less than 8% would be like this, and I like to think that's generous.

Tim Cottier says: "I think it is very unlikely participants would have held their finger up to the screen. A lot of the stimulus was very fast paced with 2afc, and we told them to respond as quickly as possible. By the time participants went to put their finger on the screen, the stimulus would have disappeared. Stimulus durations were usually less than <50ms. The one exemption to this, is the motion-induced position shift. There was no time limits for a trial, and it did use an adjustment method. Therefore, participants theoretically could hold their finger up to the screen to align the gabors. That said, for participants that did this, we would expect to observe zero to no illusory effect. If I recall correctly, all participants experienced a motion-induced position shift illusion. However, participants did complete the illusion in a booth with no experimenter present, so it is still possible they did this. "

I would have thought that allowing for a spike at zero would reduce the Bayes factor to no longer favor the negative participants as much? Because probably most of the negative participants don't have a miniscule probability under the assumption of zero effect. I think you addressed this in your email but I wasn't sure I understood.
