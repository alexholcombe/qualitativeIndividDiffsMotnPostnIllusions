For individual-differences paper

On 18 December I went through all the below 

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

I would have thought that allowing for a spike at zero would reduce the Bayes factor to no longer favor the negative participants as much? Because probably most of the negative participants don't have a miniscule probability under the assumption of zero effect. I think you addressed this in your email but I wasn't sure I understood.
