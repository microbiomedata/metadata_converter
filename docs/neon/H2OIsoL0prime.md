
# Type: H2OIso_L0prime




URI: [neon:H2OIsoL0prime](https://data.neonscience.org/H2OIsoL0prime)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[H2OIsoL0prime&#124;fdMoleH2O:double%20%3F;instStat:integer%20%3F;presCavi:double%20%3F;tempCavi:double%20%3F;tempWarmBox:double%20%3F;valvMask:double%20%3F;ppmvFwMoleH2O:double%20%3F;N2Flag:double%20%3F;d18OWater:double%20%3F;d2HWater:double%20%3F;qfSensStatus:integer%20%3F;qfStusN2:integer%20%3F;qfLowRtioMoleWetH2O:integer%20%3F])

## Attributes


### Own

 * [N2Flag](N2Flag.md)  <sub>OPT</sub>
    * Description: Signal to indicate if the instrument is processing the data for N2 gas or background air. 0=air mode, 1=N2 mode
    * range: [Double](types/Double.md)
 * [d18OWater](d18OWater.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 18O:16O in H2O, relative to the Vienna Standard Mean Ocean Water
    * range: [Double](types/Double.md)
 * [d2HWater](d2HWater.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of stable isotopes 2H:1H in H2O, relative to the Vienna Standard Mean Ocean Water
    * range: [Double](types/Double.md)
 * [fdMoleH2O](fdMoleH2O.md)  <sub>OPT</sub>
    * Description: Dry mole fraction (fd) on molar basis (Mole) of water vapor (H2O), synonymous with mixing ratio
    * range: [Double](types/Double.md)
 * [instStat](instStat.md)  <sub>OPT</sub>
    * Description: Instrument status bit (963 = good, other values indicate either temperature or pressure is not stable)
    * range: [Integer](types/Integer.md)
 * [ppmvFwMoleH2O](ppmvFwMoleH2O.md)  <sub>OPT</sub>
    * Description: Total wet mole fraction (fw) of water vapor (H2O) in the air
    * range: [Double](types/Double.md)
 * [presCavi](presCavi.md)  <sub>OPT</sub>
    * Description: Pressure of instrument cavity
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
 * [tempCavi](tempCavi.md)  <sub>OPT</sub>
    * Description: Temperature of instrument cavity
    * range: [Double](types/Double.md)
 * [tempWarmBox](tempWarmBox.md)  <sub>OPT</sub>
    * Description: Temperature of the warm box" - the temperature-controlled electronics and wavelength monitor chamber"
    * range: [Double](types/Double.md)
 * [valvMask](valvMask.md)  <sub>OPT</sub>
    * Description: State of external solenoid valves if attached, as a decimal representation of valves 1-6 where each valve is a binary bit (e.g., valve 1 = 1, valve 2 = 2, valve 3 = 4, etc. and the values are added)
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:H2OIso_L0prime |
| **In Subsets:** | | IP0.00103.001 |

