#SOX Formulas

#Example - SOX - 23.98 to 24 for DCP
sox left.wav sound/left.wav speed 1.001


#LOOP - enter folder and run on wav files.
for name in *.wav; do sox "$name"  "${name%.*}_24.wav" speed 1.001; done
