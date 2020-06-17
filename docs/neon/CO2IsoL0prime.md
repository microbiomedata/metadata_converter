
# Type: CO2Iso_L0prime




URI: [neon:CO2IsoL0prime](https://data.neonscience.org/CO2IsoL0prime)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [idGas](idGas.md)  <sub>OPT</sub>
    * Description: Gas spectrum ID
    * range: [Integer](types/Integer.md)

### Inherited from CO2Iso:

 * [valvSol](valvSol.md)  <sub>OPT</sub>
    * Description: State of external solenoid valves (if attached)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [specID](specID.md)  <sub>OPT</sub>
    * Description: Identity of the spectrum being collected at a point in time; used to identify gas species being analyzed
    * range: [Double](types/Double.md)
    * inherited from: None
 * [fwMoleCO2](fwMoleCO2.md)  <sub>OPT</sub>
    * Description: Total wet mole fraction (fw) of CO2 in the air
    * range: [Double](types/Double.md)
 * [fwMole12CO2](fwMole12CO2.md)  <sub>OPT</sub>
    * Description: Total wet mole fraction (fw) of 12CO2 in the air
    * range: [Double](types/Double.md)
 * [fwMole13CO2](fwMole13CO2.md)  <sub>OPT</sub>
    * Description: Total wet mole fraction (fw) of 13CO2 in the air
    * range: [Double](types/Double.md)
 * [2Mind13CO2](2Mind13CO2.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 13C:12C in CO2, relative to the Vienna Pee Dee Belemnite with 2 minute box averaging
    * range: [Double](types/Double.md)
    * inherited from: None
 * [30Secd13CO2](30Secd13CO2.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 13C:12C in CO2, relative to the Vienna Pee Dee Belemnite with 30 second box averaging
    * range: [Double](types/Double.md)
    * inherited from: None
 * [5Mind13CO2](5Mind13CO2.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 13C:12C in CO2, relative to the Vienna Pee Dee Belemnite with 5 minute box averaging
    * range: [Double](types/Double.md)
    * inherited from: None
 * [percentFwMoleH2O](percentFwMoleH2O.md)  <sub>OPT</sub>
    * Description: Total wet mole fraction (fw) in percent of water vapor (H2O) in the air
    * range: [Double](types/Double.md)
 * [2MinCO2IsoRatio](2MinCO2IsoRatio.md)  <sub>OPT</sub>
    * Description: The isotopic ratio of 13CO2/12CO2 with 2 minute box averaging
    * range: [Double](types/Double.md)
    * inherited from: None
 * [30SecCO2IsoRatio](30SecCO2IsoRatio.md)  <sub>OPT</sub>
    * Description: The isotopic ratio of 13CO2/12CO2 with 30 seconds box averaging
    * range: [Double](types/Double.md)
    * inherited from: None
 * [5MinCO2IsoRatio](5MinCO2IsoRatio.md)  <sub>OPT</sub>
    * Description: The isotopic ratio of 13CO2/12CO2 with 5 minute box averaging
    * range: [Double](types/Double.md)
    * inherited from: None
 * [CO2IsoRatio](CO2IsoRatio.md)  <sub>OPT</sub>
    * Description: The isotopic ratio of 13CO2/12CO2 without any averaging
    * range: [Double](types/Double.md)
    * inherited from: None
 * [fdMoleCH4](fdMoleCH4.md)  <sub>OPT</sub>
    * Description: Dry molar fraction of methane (CH4) in the air
    * range: [Double](types/Double.md)
    * inherited from: None
 * [fwMoleHPCH4](fwMoleHPCH4.md)  <sub>OPT</sub>
    * Description: High precision total molar fraction of methane (CH4) in the air based on the 12CH4 peak
    * range: [Double](types/Double.md)
    * inherited from: None
 * [fdMoleHPCH4](fdMoleHPCH4.md)  <sub>OPT</sub>
    * Description: High precision dry molar fraction of methane (CH4) in the air based on the 12CH4 peak
    * range: [Double](types/Double.md)
    * inherited from: None
 * [peakHeigH2O](peakHeigH2O.md)  <sub>OPT</sub>
    * Description: Peak height of H2O line, peak height of the H2O feature used for the H2O concentration
    * range: [Double](types/Double.md)
    * inherited from: None
 * [spliFitCH4](spliFitCH4.md)  <sub>OPT</sub>
    * Description: Maximum of the spline fit to the CH4 line, used to calculate methane concentration
    * range: [Double](types/Double.md)
    * inherited from: None
 * [peakHeig12C](peakHeig12C.md)  <sub>OPT</sub>
    * Description: Peak height of 12C line
    * range: [Double](types/Double.md)
    * inherited from: None
 * [peakHeig13C](peakHeig13C.md)  <sub>OPT</sub>
    * Description: Peak height of 13C line
    * range: [Double](types/Double.md)
    * inherited from: None

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
    * inherited from: None
 * [ppmvFwMoleH2O](ppmvFwMoleH2O.md)  <sub>OPT</sub>
    * Description: Total wet mole fraction (fw) of water vapor (H2O) in the air
    * range: [Double](types/Double.md)
    * inherited from: None
 * [N2Flag](N2Flag.md)  <sub>OPT</sub>
    * Description: Signal to indicate if the instrument is processing the data for N2 gas or background air. 0=air mode, 1=N2 mode
    * range: [Double](types/Double.md)
    * inherited from: None
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
    * inherited from: None
 * [d2HWater](d2HWater.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 2H:1H in H2O, relative to the Vienna Standard Mean Ocean Water
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from H2OIso_L0prime:

 * [fdMoleH2O](fdMoleH2O.md)  <sub>OPT</sub>
    * Description: Dry mole fraction (fd) on molar basis (Mole) of water vapor (H2O), synonymous with mixing ratio
    * range: [Double](types/Double.md)
 * [qfSensStatus](qfSensStatus.md)  <sub>OPT</sub>
    * Description: Instrument status flag  (1=fail, 0=pass, -1=NA (i.e, could not be run))
    * range: [Integer](types/Integer.md)
 * [qfStusN2](qfStusN2.md)  <sub>OPT</sub>
    * Description: Flag to indicate if the N2Flag is correctly set to air mode (0 = pass, 1 = fail)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfLowRtioMoleWetH2O](qfLowRtioMoleWetH2O.md)  <sub>OPT</sub>
    * Description: Flag to indicate the humidity in the air measured by PICARRO L2130-I is below 5000 ppm
    * range: [Integer](types/Integer.md)
    * inherited from: None

### Inherited from profGasCyl_L2prime:

 * [fdMoleCO2](fdMoleCO2.md)  <sub>OPT</sub>
    * Description: Dry mole fraction (fd) on molar basis (Mole) of carbondioxide (CO2), synonymous with mixing ratio
    * range: [Double](types/Double.md)
 * [fdMole12CO2](fdMole12CO2.md)  <sub>OPT</sub>
    * Description: Dry molar fraction (fd) of 12CO2 in the air
    * range: [Double](types/Double.md)
 * [fdMole13CO2](fdMole13CO2.md)  <sub>OPT</sub>
    * Description: Dry molar fraction (fd) of 13CO2 in the air
    * range: [Double](types/Double.md)
 * [d13CO2](d13CO2.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 13C:12C in CO2, relative to the Vienna Pee Dee Belemnite
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:CO2Iso_L0prime |
| **In Subsets:** | | IP0.00102.001 |

