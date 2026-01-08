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

