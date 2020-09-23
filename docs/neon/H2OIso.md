
# Type: H2OIso




URI: [neon:H2OIso](https://data.neonscience.org/H2OIso)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[H2OIso&#124;instStat:integer%20%3F;presCavi:double%20%3F;tempCavi:double%20%3F;tempDas:double%20%3F;tempEtal:double%20%3F;tempWarmBox:double%20%3F;posiMPV:double%20%3F;valvOutl:double%20%3F;fwMoleCH4:double%20%3F;valvMask:double%20%3F;ppmvFwMoleH2O:double%20%3F;N2Flag:double%20%3F;baseShift:double%20%3F;slopShift:double%20%3F;resiRMS:double%20%3F;d18OWater:double%20%3F;d2HWater:double%20%3F])

## Attributes


### Own

 * [N2Flag](N2Flag.md)  <sub>OPT</sub>
    * Description: Signal to indicate if the instrument is processing the data for N2 gas or background air. 0=air mode, 1=N2 mode
    * range: [Double](types/Double.md)
 * [baseShift](baseShift.md)  <sub>OPT</sub>
    * Description: Change in constant term of fitted baseline relative to the empty cavity baseline measured at the factory
    * range: [Double](types/Double.md)
 * [d18OWater](d18OWater.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 18O:16O in H2O, relative to the Vienna Standard Mean Ocean Water
    * range: [Double](types/Double.md)
 * [d2HWater](d2HWater.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 2H:1H in H2O, relative to the Vienna Standard Mean Ocean Water
    * range: [Double](types/Double.md)
 * [fwMoleCH4](fwMoleCH4.md)  <sub>OPT</sub>
    * Description: Total molar fraction of methane (CH4) in the air; used for correction of the isotopic CO2 measure for methane crosstalk
    * range: [Double](types/Double.md)
 * [instStat](instStat.md)  <sub>OPT</sub>
    * Description: Instrument status bit (963 = good, other values indicate either temperature or pressure is not stable)
    * range: [Integer](types/Integer.md)
 * [posiMPV](posiMPV.md)  <sub>OPT</sub>
    * Description: State of external rotary valve (if attached), 0-n for an n-port rotary valve
    * range: [Double](types/Double.md)
 * [ppmvFwMoleH2O](ppmvFwMoleH2O.md)  <sub>OPT</sub>
    * Description: Total wet mole fraction (fw) of water vapor (H2O) in the air
    * range: [Double](types/Double.md)
 * [presCavi](presCavi.md)  <sub>OPT</sub>
    * Description: Pressure of instrument cavity
    * range: [Double](types/Double.md)
 * [resiRMS](resiRMS.md)  <sub>OPT</sub>
    * Description: Root mean square (RMS) residuals of the least-squares fit
    * range: [Double](types/Double.md)
 * [slopShift](slopShift.md)  <sub>OPT</sub>
    * Description: Change in linear term of fitted baseline relative to the empty cavity baseline measured at the factory
    * range: [Double](types/Double.md)
 * [tempCavi](tempCavi.md)  <sub>OPT</sub>
    * Description: Temperature of instrument cavity
    * range: [Double](types/Double.md)
 * [tempDas](tempDas.md)  <sub>OPT</sub>
    * Description: Temperature inside chassis
    * range: [Double](types/Double.md)
 * [tempEtal](tempEtal.md)  <sub>OPT</sub>
    * Description: Temperature of Etalon
    * range: [Double](types/Double.md)
 * [tempWarmBox](tempWarmBox.md)  <sub>OPT</sub>
    * Description: Temperature of the warm box" - the temperature-controlled electronics and wavelength monitor chamber"
    * range: [Double](types/Double.md)
 * [valvMask](valvMask.md)  <sub>OPT</sub>
    * Description: State of external solenoid valves if attached, as a decimal representation of valves 1-6 where each valve is a binary bit (e.g., valve 1 = 1, valve 2 = 2, valve 3 = 4, etc. and the values are added)
    * range: [Double](types/Double.md)
 * [valvOutl](valvOutl.md)  <sub>OPT</sub>
    * Description: Digitizer value of outlet proportional valve, max open = 65000, closed = 0
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:H2OIso |
| **In Subsets:** | | DP0.00103.001 |

