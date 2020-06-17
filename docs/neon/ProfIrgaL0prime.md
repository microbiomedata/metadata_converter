
# Type: profIrga_L0prime




URI: [neon:ProfIrgaL0prime](https://data.neonscience.org/ProfIrgaL0prime)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [asrpCO2](asrpCO2.md)  <sub>OPT</sub>
    * Description: Electromagnetic absorptance (asrp) in the carbondioxide (CO2) absorption band
    * range: [Double](types/Double.md)
 * [asrpH2O](asrpH2O.md)  <sub>OPT</sub>
    * Description: Electromagnetic absorptance (asrp) in the water vapor (H2O) absorption band
    * range: [Double](types/Double.md)
 * [fwMoleH2O](fwMoleH2O.md)  <sub>OPT</sub>
    * Description: Total wet mole fraction (fw) of water vapor (H2O) in the air
    * range: [Double](types/Double.md)
 * [presCell](presCell.md)  <sub>OPT</sub>
    * Description: Pressure (pres) of the optical cell
    * range: [Double](types/Double.md)
 * [tempCell](tempCell.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the optical cell
    * range: [Double](types/Double.md)

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
    * inherited from: None
 * [fwMole13CO2](fwMole13CO2.md)  <sub>OPT</sub>
    * Description: Total wet mole fraction (fw) of 13CO2 in the air
    * range: [Double](types/Double.md)
    * inherited from: None
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
    * inherited from: None
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

### Inherited from H2OIso_L0prime:

 * [fdMoleH2O](fdMoleH2O.md)  <sub>OPT</sub>
    * Description: Dry mole fraction (fd) on molar basis (Mole) of water vapor (H2O), synonymous with mixing ratio
    * range: [Double](types/Double.md)
 * [qfSensStatus](qfSensStatus.md)  <sub>OPT</sub>
    * Description: Instrument status flag  (1=fail, 0=pass, -1=NA (i.e, could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
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
    * inherited from: None
 * [fdMole13CO2](fdMole13CO2.md)  <sub>OPT</sub>
    * Description: Dry molar fraction (fd) of 13CO2 in the air
    * range: [Double](types/Double.md)
    * inherited from: None
 * [d13CO2](d13CO2.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 13C:12C in CO2, relative to the Vienna Pee Dee Belemnite
    * range: [Double](types/Double.md)
    * inherited from: None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:profIrga_L0prime |
| **In Subsets:** | | IP0.00105.001 |

