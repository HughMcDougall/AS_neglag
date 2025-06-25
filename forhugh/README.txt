File is formatted like a javelin input file except for the first line.

First line of the file contains the parameters used to generate the light curve: DRW damping timescale, DRW structure function, redshift, apparent magnitude, amplitude ratio, short lag (disk continuum lag), |long negative lag|

The most important parameters are the last three. The amplitude ratio is the ratio of the amplitude of the long lag to the short lag (always <0.3 for these examples). 

The second row of the file says the number of light curves (2 for these examples). The third row says the length of the first light curve. Then I give the time, mag, and mag error of that light curve in the three columns that follow. After the first light curve is another row that gives the length of the second light curve. Then the second light curve follows with the same columns.
