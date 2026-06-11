# Radial position data taken from https://arxiv.org/pdf/2412.15090, 25 Feb 2025
# The latest (as of June 2026) expected performance report for the ITk

# Radiation length taken from ATLAS.txt, which relies on 
# https://cds.cern.ch/record/2669540 "Expected Tracking Performance of the ATLAS Inner Tracker at the HL-LHC" (30 Mar 2019)
# Verification and adjustments could be made (more precise estimates layer-by-layer).

# Note that only barrel layers are included!

from math import sqrt
from trackingerror import Layer, Detector

def ITk():
    # TODO update radiation length?
    Pixel1=Layer(0.0174, 2.5e-5/sqrt(12), 10.0e-5/sqrt(12), 0.034)
    Pixel2=Layer(0.0174, 5.0e-5/sqrt(12), 5.0e-5/sqrt(12), 0.099)
    Pixel3=Layer(0.0174, 5.0e-5/sqrt(12), 5.0e-5/sqrt(12), 0.16)
    Pixel4=Layer(0.0174, 5.0e-5/sqrt(12), 5.0e-5/sqrt(12), 0.228)
    Pixel5=Layer(0.0174, 5.0e-5/sqrt(12), 5.0e-5/sqrt(12), 0.291)
    
    # TODO update radiation length?
    # 0.0675 = Radiation length taken as 0.27/4 from the figures in https://iopscience.iop.org/article/10.1088/1748-0221/20/02/P02018/pdf
    Strip1=Layer(0.0505, 8.0e-5/sqrt(12), 8.0e-5/sqrt(12), 0.399)
    Strip2=Layer(0.0505, 8.0e-5/sqrt(12), 8.0e-5/sqrt(12), 0.562)
    Strip3=Layer(0.0505, 8.0e-5/sqrt(12), 8.0e-5/sqrt(12), 0.762)
    Strip4=Layer(0.0505, 8.0e-5/sqrt(12), 8.0e-5/sqrt(12), 1)
    
    detector=Detector()
    detector.addlayer2(Pixel1)
    detector.addlayer2(Pixel2)
    detector.addlayer2(Pixel3)
    detector.addlayer2(Pixel4)
    detector.addlayer2(Pixel5)
    detector.addlayer2(Strip1)
    detector.addlayer2(Strip2)
    detector.addlayer2(Strip3)
    detector.addlayer2(Strip4)
    
    return detector