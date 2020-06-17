
# Type: soniAmrs




URI: [neon:SoniAmrs](https://data.neonscience.org/SoniAmrs)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Inherited from irga_L0prime:

 * [idx](idx.md)  <sub>OPT</sub>
    * Description: Index value (idx)
    * range: [Integer](types/Integer.md)
 * [diag](diag.md)  <sub>OPT</sub>
    * Description: Diagnostic value (diag), output as a 32 bit integer Bit assignment according to NEONDOC000807 (L0 prime processing ATBD)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [tempBloc](tempBloc.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the instrument block (Bloc)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempCellIn](tempCellIn.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the optical cell (Cell) inlet (In) thermocouple
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempCellOut](tempCellOut.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the optical cell (Cell) outlet (Out) thermocouple
    * range: [Double](types/Double.md)
    * inherited from: None
 * [presAtmBox](presAtmBox.md)  <sub>OPT</sub>
    * Description: Pressure (pres), measured as atmospheric (Atm) pressure of the control box (Box), synonymous with absolute pressure or total pressure (at sea level the standard atmospheric pressure is 101.325 kPa)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [presGageCell](presGageCell.md)  <sub>OPT</sub>
    * Description: Pressure (pres), measured as differential against ambient pressure, synonymous with gage (Gage) pressure (at sea level the gage pressure equals total pressure minus 101.325 kPa), between the optical cell (Cell) and the control box
    * range: [Double](types/Double.md)
    * inherited from: None
 * [pwrH2OSamp](pwrH2OSamp.md)  <sub>OPT</sub>
    * Description: Power (pwr) of the water vapor (H2O) signal in the absorption band used for sampling (Samp)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [pwrH2ORef](pwrH2ORef.md)  <sub>OPT</sub>
    * Description: Power (pwr) of the water vapor (H2O) signal in the absorption band used for reference (Ref)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [rhoMoleH2O](rhoMoleH2O.md)  <sub>OPT</sub>
    * Description: Density (rho) on molar basis (Mole) of water vapor (H2O), synonymous with number density
    * range: [Double](types/Double.md)
    * inherited from: None
 * [pwrCO2Samp](pwrCO2Samp.md)  <sub>OPT</sub>
    * Description: Power (pwr) of the carbondioxide (CO2) signal in the absorption band used for sampling (Samp)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [pwrCO2Ref](pwrCO2Ref.md)  <sub>OPT</sub>
    * Description: Power (pwr) of the carbondioxide (CO2) signal in the absorption band used for reference (Ref)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [rhoMoleCO2](rhoMoleCO2.md)  <sub>OPT</sub>
    * Description: Density (rho) on molar basis (Mole) of carbondioxide (CO2), synonymous with number density
    * range: [Double](types/Double.md)
    * inherited from: None
 * [diag2](diag2.md)  <sub>OPT</sub>
    * Description: Diagnostic value (diag) number 2 (2; sync clocks)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [poteCool](poteCool.md)  <sub>OPT</sub>
    * Description: Electric potential (pote) at the cooler (Cool)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ssiCO2](ssiCO2.md)  <sub>OPT</sub>
    * Description: Signal strength indicator (ssi) for the carbondioxide (CO2) absorption band
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ssiH2O](ssiH2O.md)  <sub>OPT</sub>
    * Description: Signal strength indicator (ssi) for the water vapor (H2O) absorption band
    * range: [Double](types/Double.md)
    * inherited from: None
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

### Inherited from soniAmrs_L0prime:

 * [acceXaxs](acceXaxs.md)  <sub>OPT</sub>
    * Description: Linear acceleration (acce) in attitude and motion reference system along-axis direction (Xaxs), positive forward
    * range: [Double](types/Double.md)
 * [acceYaxs](acceYaxs.md)  <sub>OPT</sub>
    * Description: Linear acceleration (acce) in attitude and motion reference system cross-axis direction (Yaxs), positive left
    * range: [Double](types/Double.md)
 * [acceZaxs](acceZaxs.md)  <sub>OPT</sub>
    * Description: Linear acceleration (acce) in attitude and motion reference system vertical-axis direction (Zaxs), positive upwards
    * range: [Double](types/Double.md)
 * [acceXaxsFree](acceXaxsFree.md)  <sub>OPT</sub>
    * Description: Linear acceleration (acce) in attitude and motion reference system along-axis direction (Xaxs), positive forward, after subtraction of acceleration due to earth's gravity (free)
    * range: [Double](types/Double.md)
 * [acceYaxsFree](acceYaxsFree.md)  <sub>OPT</sub>
    * Description: Linear acceleration (acce) in attitude and motion reference system cross-axis direction (Yaxs), positive left, after subtraction of acceleration due to earth's gravity (free)
    * range: [Double](types/Double.md)
 * [acceZaxsFree](acceZaxsFree.md)  <sub>OPT</sub>
    * Description: Linear acceleration (acce) in attitude and motion reference system vertical-axis direction (Zaxs), positive upwards, after subtraction of acceleration due to earth's gravity (free)
    * range: [Double](types/Double.md)
 * [omegYaxs](omegYaxs.md)  <sub>OPT</sub>
    * Description: Angular velocity (omeg) around the attitude and motion reference system cross-axis (Yaxs), positive in clockwise direction, synonymous with pitch rate
    * range: [Double](types/Double.md)
 * [omegXaxs](omegXaxs.md)  <sub>OPT</sub>
    * Description: Angular velocity (omeg) around the attitude and motion reference system along-axis (Xaxs), positive in clockwise direction, synonymous with roll rate
    * range: [Double](types/Double.md)
 * [omegZaxs](omegZaxs.md)  <sub>OPT</sub>
    * Description: Angular velocity (omeg) around the attitude and motion reference system vertical-axis (Zaxs), positive in clockwise direction, synonymous with yaw rate
    * range: [Double](types/Double.md)
 * [thetYaxs](thetYaxs.md)  <sub>OPT</sub>
    * Description: Angle (thet) around the attitude and motion reference system cross-axis (Yaxs), positive in clockwise direction, synonymous with pitch angle
    * range: [Double](types/Double.md)
 * [thetXaxs](thetXaxs.md)  <sub>OPT</sub>
    * Description: Angle (thet) around the attitude and motion reference system along-axis (Xaxs), positive in clockwise direction, synonymous with roll angle
    * range: [Double](types/Double.md)
 * [thetZaxs](thetZaxs.md)  <sub>OPT</sub>
    * Description: Angle (thet) around the attitude and motion reference system vertical-axis (Zaxs), positive in clockwise direction, synonymous with yaw angle
    * range: [Double](types/Double.md)
 * [diag32](diag32.md)  <sub>OPT</sub>
    * Description: Diagnostic value (diag), output as a 32-bit (32) integer Bit assignment according to NEONDOC000807 (L0 prime processing ATBD)
    * range: [Integer](types/Integer.md)
 * [qfAmrsVal](qfAmrsVal.md)  <sub>OPT</sub>
    * Description: Sensor signal flag: Selftest (gives the result of the last manually ran self-test)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfAmrsFilt](qfAmrsFilt.md)  <sub>OPT</sub>
    * Description: Sensor signal flag: Filter Valid (indicates if input into filter orientation filter is reliable and or complete)(1=pass, 0=fail, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfAmrsVelo](qfAmrsVelo.md)  <sub>OPT</sub>
    * Description: Sensor signal flag: NoVelocityUpdate status
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfAmrsRng](qfAmrsRng.md)  <sub>OPT</sub>
    * Description: Sensor signal flag: Clipping indication
    * range: [Integer](types/Integer.md)
    * inherited from: None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:soniAmrs |
| **In Subsets:** | | DP0.00010.001 |

