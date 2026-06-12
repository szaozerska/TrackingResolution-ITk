This project is an extension of `TrackingResolution` (F. Chen, V. M. Cairo, C. Young; https://doi.org/10.5281/zenodo.11199209) that can be used for calculating the resolution of the track parameters for different detectors. The present repository focuses on comparing Run 3 Inner Detector (ID) and Inner Tracker (ITk) ATLAS configurations (see `id3_vs_itk.ipynb`), and estimating the improvement in resolution when the first layer of the ITk is positioned closer to the beam pipe (see `compare_ITks.ipynb`).
Written in Python 3.6.8. 

### Input format for detector description
The supported layer configuration is solenoidal geometry (i.e. cylinder layers), with origin set at its center. 
xy plane denotes the transverse plane. z-direction is in the direction of the cylinder axis.
All layers are assumed to be infinitely long along z-axis.
Particle is assumed to be of unit charge e.

- Comment by starting the line with `#`.
- Each non-comment line must contain exactly four whitespace-separated values:
    1) material thickness in radiation lengths (X0)
    2) xy measurement resolution (m)
    3) z measurement resolution (m)
    4) layer position (m)
- Layers may be listed in any order, but duplicate positions are not allowed.

An example input file is provided in `example.txt`. 
Alternatively, you can define a `Detector` object directly in the code — see examples in `ATLAS.py` and `ITk.py`.

### Running the code

**In Jupyter Notebook:**
```bash
%run trackingerror.py
```
For notebook examples, see `example.ipynb`.

**In terminal:**
```bash
python3 trackingerror.py [-h] [-f filename] [-p momentum] [-m mass] [-B MagneticField][-eta pseudorapidity][-verbose v]
```

Example, where `example.txt` describes detector layers:
```bash
python3 trackingerror.py -f example.txt
```

To see the available options and defaults, use:
```bash
python3 trackingerror.py -h
```

Command-line options supported by `trackingerror.py`:
- `-f`, `--foo`            input file path containing detector layer configuration
- `-p`, `--p`              particle momentum in GeV/c (default: 1)
- `-m`, `--m`              particle mass in GeV/c^2 (default: 0.106)
- `-B`, `--B`              magnetic field in T (default: 2)
- `-eta`, `--eta`          pseudorapidity (default: 0)
- `-verbose`, `--verbose`  set to 1 to print the layer configuration (default: 0)

The script calculates tracking resolutions using Gluckstern-based formulas and prints:

```text
sigma(pt)/pt : dimensionless
sigma(d)     : micrometers
sigma(phi)   : radians
sigma(z)     : micrometers
sigma(theta) : radians
```

When you run the `trackingerror.py`, it performs the command-line calculation and then opens any Matplotlib plots created by `plot_fixedeta()` or `plot_fixedp()` (see below).

### Plotting functions
Plotting functions are available in `trackingerror.py`:
- `plot_fixedeta(source, var, B=2, eta=0, m=0.106, input_mode='file', label=None)` — plots a selected resolution variable versus pT at fixed pseudorapidity.
- `plot_fixedp(source, var, B=2, p=1, m=0.106, input_mode='file', label=None, eta_max=2.5)` — plots a selected resolution variable versus pseudorapidity at fixed pT.

These functions accept either:
    - `input_mode='file'` with `source` as the filename with the description of a detector, or
    - `input_mode='detector'` with `source` as a `Detector` object.

Supported plot variables: `sigma(d), sigma(z), sigma(phi), sigma(theta), sigma(pt)/pt`.

### Notes

Caveat: at least three layers are needed for a stable fit and reasonable output.