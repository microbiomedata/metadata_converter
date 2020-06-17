
# Type: H2OIso_L0prime




URI: [neon:H2OIsoL0prime](https://data.neonscience.org/H2OIsoL0prime)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [fdMoleH2O](fdMoleH2O.md)  <sub>OPT</sub>
    * Description: Dry mole fraction (fd) on molar basis (Mole) of water vapor (H2O), synonymous with mixing ratio
    * range: [Double](types/Double.md)
 * [qfLowRtioMoleWetH2O](qfLowRtioMoleWetH2O.md)  <sub>OPT</sub>
    * Description: Flag to indicate the humidity in the air measured by PICARRO L2130-I is below 5000 ppm
    * range: [Integer](types/Integer.md)
 * [qfSensStatus](qfSensStatus.md)  <sub>OPT</sub>
    * Description: Instrument status flag  (1=fail, 0=pass, -1=NA (i.e, could not be run))
    * range: [Integer](types/Integer.md)
 * [qfStusN2](qfStusN2.md)  <sub>OPT</sub>
    * Description: Flag to indicate if the N2Flag is correctly set to air mode (0 = pass, 1 = fail)
    * range: [Integer](types/Integer.md)

### Inherited from H2OIso:

 * [instStat](instStat.md)  <sub>OPT</sub>
    * Description: Instrument status bit (963 = good, other values indicate either temperature or pressure is not stable)
    * range: [Integer](types/Integer.md)
 * [presCavi](presCavi.md)  <sub>OPT</sub>
    * Description: Pressure of instrument cavity
    * range: [Double](types/Double.md)
 * [tempCavi](tempCavi.md)  <sub>OPT</sub>
    * Description: Temperature of instrument cavity
    * range: [Double](types/Double.md)
 * [tempDas](tempDas.md)  <sub>OPT</sub>
    * Description: Temperature inside chassis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempEtal](tempEtal.md)  <sub>OPT</sub>
    * Description: Temperature of Etalon
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempWarmBox](tempWarmBox.md)  <sub>OPT</sub>
    * Description: Temperature of the warm box" - the temperature-controlled electronics and wavelength monitor chamber"
    * range: [Double](types/Double.md)
 * [posiMPV](posiMPV.md)  <sub>OPT</sub>
    * Description: State of external rotary valve (if attached), 0-n for an n-port rotary valve
    * range: [Double](types/Double.md)
    * inherited from: None
 * [valvOutl](valvOutl.md)  <sub>OPT</sub>
    * Description: Digitizer value of outlet proportional valve, max open = 65000, closed = 0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [fwMoleCH4](fwMoleCH4.md)  <sub>OPT</sub>
    * Description: Total molar fraction of methane (CH4) in the air; used for correction of the isotopic CO2 measure for methane crosstalk
    * range: [Double](types/Double.md)
    * inherited from: None
 * [valvMask](valvMask.md)  <sub>OPT</sub>
    * Description: State of external solenoid valves if attached, as a decimal representation of valves 1-6 where each valve is a binary bit (e.g., valve 1 = 1, valve 2 = 2, valve 3 = 4, etc. and the values are added)
    * range: [Double](types/Double.md)
 * [ppmvFwMoleH2O](ppmvFwMoleH2O.md)  <sub>OPT</sub>
    * Description: Total wet mole fraction (fw) of water vapor (H2O) in the air
    * range: [Double](types/Double.md)
 * [N2Flag](N2Flag.md)  <sub>OPT</sub>
    * Description: Signal to indicate if the instrument is processing the data for N2 gas or background air. 0=air mode, 1=N2 mode
    * range: [Double](types/Double.md)
 * [baseShift](baseShift.md)  <sub>OPT</sub>
    * Description: Change in constant term of fitted baseline relative to the empty cavity baseline measured at the factory
    * range: [Double](types/Double.md)
    * inherited from: None
 * [slopShift](slopShift.md)  <sub>OPT</sub>
    * Description: Change in linear term of fitted baseline relative to the empty cavity baseline measured at the factory
    * range: [Double](types/Double.md)
    * inherited from: None
 * [resiRMS](resiRMS.md)  <sub>OPT</sub>
    * Description: Root mean square (RMS) residuals of the least-squares fit
    * range: [Double](types/Double.md)
    * inherited from: None
 * [d18OWater](d18OWater.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 18O:16O in H2O, relative to the Vienna Standard Mean Ocean Water
    * range: [Double](types/Double.md)
 * [d2HWater](d2HWater.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 2H:1H in H2O, relative to the Vienna Standard Mean Ocean Water
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:H2OIso_L0prime |
| **In Subsets:** | | IP0.00103.001 |

