[![gprMax Geometry Visual Check](https://github.com/pratiktech28/gprmax_geometry_check/actions/workflows/geometry.yml/badge.svg)](https://github.com/pratiktech28/gprmax_geometry_check/actions/workflows/geometry.yml)

![images](https://github.com/user-attachments/assets/50e360df-19a1-43eb-9f86-ffafd530985d)         <img width="200" height="200" alt="download" src="https://github.com/user-attachments/assets/6a03ea57-b70e-420e-9295-742808096b96" />     

![download](https://github.com/user-attachments/assets/6cecd15f-c44a-4f41-9601-36e26c5231df)       <img width="412" height="122" alt="download" src="https://github.com/user-attachments/assets/ee5d60ef-e1fb-4a8f-aaed-2dbf427fb4f3" />


**🛰️ gprMax Spatia
l Fidelity & Geometry Validator**
**Automated Geometric Integrity Testing for Physics-Based Electromagnetic Simulation***
**📖 Overview**
In computational electromagnetics, specifically within gprMax, spatial accuracy is the foundation of numerical validity. A single coordinate error in the .in file can lead to hours of wasted compute resources on a flawed model.
This repository implements an Automated Geometry Validation Pipeline. It parses simulation input files, extracts spatial configurations (Antennas, Targets, PML boundaries), and validates their alignment against the intended physical model—all within a CI/CD environment.

---
**🛠️ Technical Execution & Proof**

Attribute,Indicator,Status / Value
Pipeline Core,geometry.yml,✅ PASSED
Verification Speed,⚡ High Velocity,27 Seconds
Coordinate Precision,🎯 Sub-Millimeter,±0.001 m
Environment Check,🛡️ Spatial Fidelity,VERIFIED

**🖼️ Spatial Interpretation & Visualization**

The pipeline generates a Simulation Domain Preview to ensure that the engine correctly interprets the spatial configuration. This visual proof confirms that the antenna source and buried targets are localized with absolute precision.

<div align="center">
<img src="geometry_preview.png" width="550" alt="gprMax Geometry Visual Check">


<p><i><b>Figure 1:</b> Automated Spatial Alignment Verification.


<font color="blue">🔵 Blue Circle:</font> Antenna Source Location | <font color="red">🔴 Red Square:</font> Buried Target (Box) Model.</i></p>
</div>

**⚙️ How it Works: The "Trident" Logic**
The validation process is divided into three critical stages:
Parsing Engine: A custom-built script scans the user_model.in for #box and #cylinder directives.
Geometric Mapping: Converts raw simulation coordinates into a visual coordinate system, ensuring that PML (Perfectly Matched Layer) boundaries do not intersect with active sources.
CI/CD Gatekeeping: The GitHub Action fails the build if any geometric overlap or out-of-bounds error is detected, preventing resource leakage.


**🚀 Deployment & Local Usage**
To verify geometry locally before pushing to the cloud:

```
# Clone the validator
git clone https://github.com/pratiktech28/gprmax_geometry_check.git

# Install lightweight dependencies
pip install matplotlib

# Run the validation script
python <img width="800" height="600" alt="geometry_preview" src="https://github.com/user-attachments/assets/58ba7b79-507f-43d0-87ea-0e57a2dfe443" />
check_geometry.py --input simulation_model.in
---



**👨‍💻 Contributor Insights**
"Beyond numerical accuracy, the integrity of the spatial domain is non-negotiable. This tool ensures that the physics engine is fed a geometrically perfect model, every single time."
Repository
https://github.com/pratiktech28/gprmax_ge
ometry_check.git

