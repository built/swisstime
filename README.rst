Swiss Time - A diagnostic code timer
=======================================
Swiss Time is a diagnostic tool for finding slow spots in code. It sits somewhere between a raw timer and a profiler.

<https://github.com/built/swisstime>

Once started, each call to tick() will record a time difference along a label that you provide.

In this way you build a timeline over the portion of code you are analyzing.

You can print a report of the results or gather report data to process your own way.

Usage
=====

Import and start the timer at the beginning of the code you want to analyze.

 >>> import swisstime
 >>> swisstime.start()

At the end of each section you want measured, call tick() with a description of that piece of code:

 >>> swisstime.tick("Load input image")

Do this after each section you are measuring:

 >>> action.tick("Build masks")

To display a report of your results, print the output of swisstime.report():

 >>> print( swisstime.report() )

Your output will look something like this:
::
--------------------------------------------------
Time in seconds
--------------------------------------------------
1.074243 | Startup
0.127297 | Load input image
0.024610 | Build masks
0.127521 | Populate layers
0.018821 | Build layers
0.022240 | Tone down green
0.100116 | Convert to floats
0.343161 | Resize
0.006000 | Image adjustments
0.052212 | Convert to bytes
0.969261 | Save as PNG


If you want the raw report data you can call:

>>> swisstime.data()

to get a list of label/time tuples.

Calling start() will reset all data and begin the analysis again.



