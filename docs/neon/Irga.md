
# Type: irga




URI: [neon:Irga](https://data.neonscience.org/Irga)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


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

### Inherited from irga_L0prime:

 * [idx](idx.md)  <sub>OPT</sub>
    * Description: Index value (idx)
    * range: [Integer](types/Integer.md)
 * [diag](diag.md)  <sub>OPT</sub>
    * Description: Diagnostic value (diag), output as a 32 bit integer Bit assignment according to NEONDOC000807 (L0 prime processing ATBD)
    * range: [Integer](types/Integer.md)
 * [tempBloc](tempBloc.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the instrument block (Bloc)
    * range: [Double](types/Double.md)
 * [tempCellIn](tempCellIn.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the optical cell (Cell) inlet (In) thermocouple
    * range: [Double](types/Double.md)
 * [tempCellOut](tempCellOut.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the optical cell (Cell) outlet (Out) thermocouple
    * range: [Double](types/Double.md)
 * [presAtmBox](presAtmBox.md)  <sub>OPT</sub>
    * Description: Pressure (pres), measured as atmospheric (Atm) pressure of the control box (Box), synonymous with absolute pressure or total pressure (at sea level the standard atmospheric pressure is 101.325 kPa)
    * range: [Double](types/Double.md)
 * [presGageCell](presGageCell.md)  <sub>OPT</sub>
    * Description: Pressure (pres), measured as differential against ambient pressure, synonymous with gage (Gage) pressure (at sea level the gage pressure equals total pressure minus 101.325 kPa), between the optical cell (Cell) and the control box
    * range: [Double](types/Double.md)
 * [pwrH2OSamp](pwrH2OSamp.md)  <sub>OPT</sub>
    * Description: Power (pwr) of the water vapor (H2O) signal in the absorption band used for sampling (Samp)
    * range: [Double](types/Double.md)
 * [pwrH2ORef](pwrH2ORef.md)  <sub>OPT</sub>
    * Description: Power (pwr) of the water vapor (H2O) signal in the absorption band used for reference (Ref)
    * range: [Double](types/Double.md)
 * [rhoMoleH2O](rhoMoleH2O.md)  <sub>OPT</sub>
    * Description: Density (rho) on molar basis (Mole) of water vapor (H2O), synonymous with number density
    * range: [Double](types/Double.md)
 * [pwrCO2Samp](pwrCO2Samp.md)  <sub>OPT</sub>
    * Description: Power (pwr) of the carbondioxide (CO2) signal in the absorption band used for sampling (Samp)
    * range: [Double](types/Double.md)
 * [pwrCO2Ref](pwrCO2Ref.md)  <sub>OPT</sub>
    * Description: Power (pwr) of the carbondioxide (CO2) signal in the absorption band used for reference (Ref)
    * range: [Double](types/Double.md)
 * [rhoMoleCO2](rhoMoleCO2.md)  <sub>OPT</sub>
    * Description: Density (rho) on molar basis (Mole) of carbondioxide (CO2), synonymous with number density
    * range: [Double](types/Double.md)
 * [diag2](diag2.md)  <sub>OPT</sub>
    * Description: Diagnostic value (diag) number 2 (2; sync clocks)
    * range: [Integer](types/Integer.md)
 * [poteCool](poteCool.md)  <sub>OPT</sub>
    * Description: Electric potential (pote) at the cooler (Cool)
    * range: [Double](types/Double.md)
 * [ssiCO2](ssiCO2.md)  <sub>OPT</sub>
    * Description: Signal strength indicator (ssi) for the carbondioxide (CO2) absorption band
    * range: [Double](types/Double.md)
 * [ssiH2O](ssiH2O.md)  <sub>OPT</sub>
    * Description: Signal strength indicator (ssi) for the water vapor (H2O) absorption band
    * range: [Double](types/Double.md)
 * [tempMean](tempMean.md)  <sub>OPT</sub>
    * Description: Cell temperature (weighted average of head inlet and outlet temperature)
    * range: [String](types/String.md)
    * inherited from: None
 * [presSum](presSum.md)  <sub>OPT</sub>
    * Description: Total pressure (LI-7550 box pressure + head pressure)
    * range: [String](types/String.md)
    * inherited from: None
 * [qfIrgaHead](qfIrgaHead.md)  <sub>OPT</sub>
    * Description: Sensor flag (fL01: Head detect)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfIrgaTempOut](qfIrgaTempOut.md)  <sub>OPT</sub>
    * Description: Sensor flag (fL02: Outlet temperature)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfIrgaTempIn](qfIrgaTempIn.md)  <sub>OPT</sub>
    * Description: Sensor flag (fL03: Inlet temperature)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfIrgaAux](qfIrgaAux.md)  <sub>OPT</sub>
    * Description: Sensor flag (fL04: Aux input)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfIrgaPres](qfIrgaPres.md)  <sub>OPT</sub>
    * Description: Sensor flag (fL05: Differential pressure)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfIrgaChop](qfIrgaChop.md)  <sub>OPT</sub>
    * Description: Sensor flag (fL06: Chopper)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfIrgaDetc](qfIrgaDetc.md)  <sub>OPT</sub>
    * Description: Sensor flag (fL07: Detector)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfIrgaPll](qfIrgaPll.md)  <sub>OPT</sub>
    * Description: Sensor flag (fL08: PLL)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfIrgaSync](qfIrgaSync.md)  <sub>OPT</sub>
    * Description: Sensor flag (fL09: Sync)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfIrgaAgc](qfIrgaAgc.md)  <sub>OPT</sub>
    * Description: Sensor flag (fL10: AGC)
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

### Inherited from profIrga_L0prime:

 * [asrpH2O](asrpH2O.md)  <sub>OPT</sub>
    * Description: Electromagnetic absorptance (asrp) in the water vapor (H2O) absorption band
    * range: [Double](types/Double.md)
 * [asrpCO2](asrpCO2.md)  <sub>OPT</sub>
    * Description: Electromagnetic absorptance (asrp) in the carbondioxide (CO2) absorption band
    * range: [Double](types/Double.md)
 * [fwMoleH2O](fwMoleH2O.md)  <sub>OPT</sub>
    * Description: Total wet mole fraction (fw) of water vapor (H2O) in the air
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempCell](tempCell.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the optical cell
    * range: [Double](types/Double.md)
    * inherited from: None
 * [presCell](presCell.md)  <sub>OPT</sub>
    * Description: Pressure (pres) of the optical cell
    * range: [Double](types/Double.md)
    * inherited from: None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:irga |
| **In Subsets:** | | DP0.00016.001 |

