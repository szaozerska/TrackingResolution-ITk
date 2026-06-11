# Reference for the resolutions and position data:
# Full report (May 2026)               - https://arxiv.org/pdf/2605.07585
# The corresponding ATLAS results page - https://atlas.web.cern.ch/Atlas/GROUPS/PHYSICS/PAPERS/IDTR-2021-01/
# Radial data specifically: Fig. 1 of the report

# Radiation length taken from ATLAS.txt, which relies on 
# https://cds.cern.ch/record/2669540 (30 Mar 2019)
# Verification and adjustments can be done.
#
# The full paper on technical configurations of the ATLAS detector for Run 3:
# https://iopscience.iop.org/article/10.1088/1748-0221/19/05/P05063/pdf
#
# Note that only barrel layers are included!

from math import sqrt
from trackingerror import Layer, Detector

def ATLAS_PhaseII():
    # Used for Run 3
    # Barrel: "The majority of the pixel detector uses planar sensors with a pitch (in the 𝜙 
    # and 𝜂 directions resp.) of 50×400µm2; the IBL uses planar sensors with 50×250µm2 pixel pitch"
    # (from the ATLAS report, May 2026)
    
    # TODO should it be a different value for the pixel resolution? I am taking it
    # similarly to pitch/sqrt(12) as was done in the initial version of the package, but
    # I am unsure if that's precise enough. Leaving as is for now
    Pixel1=Layer(0.019, 5.0e-5/sqrt(12), 2.5e-5/sqrt(12), 0.03325)   # IBL layer
    Pixel2=Layer(0.028, 5.0e-5/sqrt(12), 40e-5/sqrt(12), 0.0505)    # B-layer
    Pixel3=Layer(0.028, 5.0e-5/sqrt(12), 40e-5/sqrt(12), 0.0885)    # Layer 1
    Pixel4=Layer(0.028, 5.0e-5/sqrt(12), 40e-5/sqrt(12), 0.1225)    # Layer 2
    # 4 layers total, not 5!
    # The radiation length is concerningly big, but it seems like that is the value in the report
    
    Strip1=Layer(0.0875, 8.0e-5/sqrt(12), 8.0e-5/sqrt(12), 0.299)
    Strip2=Layer(0.0875, 8.0e-5/sqrt(12), 8.0e-5/sqrt(12), 0.371)
    Strip3=Layer(0.0875, 8.0e-5/sqrt(12), 8.0e-5/sqrt(12), 0.443)
    Strip4=Layer(0.0875, 8.0e-5/sqrt(12), 8.0e-5/sqrt(12), 0.514)
    
    detector=Detector()
    detector.addlayer2(Pixel1)
    detector.addlayer2(Pixel2)
    detector.addlayer2(Pixel3)
    detector.addlayer2(Pixel4)
    detector.addlayer2(Strip1)
    detector.addlayer2(Strip2)
    detector.addlayer2(Strip3)
    detector.addlayer2(Strip4)
    
    return detector