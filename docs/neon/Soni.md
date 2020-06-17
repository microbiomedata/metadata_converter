
# Type: soni




URI: [neon:Soni](https://data.neonscience.org/Soni)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [diag16](diag16.md)  <sub>OPT</sub>
    * Description: Diagnostic value (diag), output as a 16-bit (16) integer Bit assignment according to NEONDOC000807 (L0 prime processing ATBD)
    * range: [Integer](types/Integer.md)
 * [tempArmBot](tempArmBot.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the arm (Arm) bottom (Bot) zone measured by platinum resistance thermometers (heated 3-D sonic anemometer only)
    * range: [Double](types/Double.md)
 * [tempArmTop](tempArmTop.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the arm (Arm) top zone (Top) measured by platinum resistance thermometers (heated 3-D sonic anemometer only)
    * range: [Double](types/Double.md)
 * [tempTranBot](tempTranBot.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the transducer (Tran) bottom zone (Bot) measured by platinum resistance thermometers (heated 3-D sonic anemometer only)
    * range: [Double](types/Double.md)
 * [tempTranTop](tempTranTop.md)  <sub>OPT</sub>
    * Description: Temperature (temp) of the transducer (Tran) top zone (Top) measured by platinum resistance thermometers (heated 3-D sonic anemometer only)
    * range: [Double](types/Double.md)

### Inherited from TAAT_L0prime:

 * [heaterFlag](heaterFlag.md)  <sub>OPT</sub>
    * Description: Heater flag indicating whether the heater was operational for a measurement period, (1 = on, no value = off)
    * range: [Integer](types/Integer.md)
 * [turbineSpeed](turbineSpeed.md)  <sub>OPT</sub>
    * Description: Turbine speed
    * range: [Double](types/Double.md)
    * inherited from: None

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

### Inherited from soni_L0prime:

 * [veloXaxs](veloXaxs.md)  <sub>OPT</sub>
    * Description: Linear velocity (velo) of wind in 3-D sonic anemometer along-axis direction (Xaxs), positive backward
    * range: [Double](types/Double.md)
 * [veloYaxs](veloYaxs.md)  <sub>OPT</sub>
    * Description: Linear velocity (velo) of wind in 3-D sonic anemometer cross-axis direction (Yaxs), positive right
    * range: [Double](types/Double.md)
 * [veloZaxs](veloZaxs.md)  <sub>OPT</sub>
    * Description: Linear velocity (velo) of wind in 3-D sonic anemometer vertical-axis direction (Zaxs), positive upwards
    * range: [Double](types/Double.md)
 * [veloSoni](veloSoni.md)  <sub>OPT</sub>
    * Description: Linear velocity (velo) of sound (Soni)
    * range: [Double](types/Double.md)
 * [tempSoni](tempSoni.md)  <sub>OPT</sub>
    * Description: Sonic temperature (TSONIC)
    * range: [String](types/String.md)
    * inherited from: None
 * [qfSoniCode](qfSoniCode.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o5: Wrong embedded sensor code)
    * range: [String](types/String.md)
    * inherited from: None
 * [voucherStatus](voucherStatus.md)  <sub>OPT</sub>
    * Description: Status of the specimen in an accessioning process
    * range: [String](types/String.md)
    * inherited from: None
 * [qfSoniSignalLow](qfSoniSignalLow.md)  <sub>OPT</sub>
    * Description: Sensor signal flag (QFSONIC s4 Low signal amplitude)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniUnrs](qfSoniUnrs.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o1: Sensor unresponsive)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniData](qfSoniData.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o2: No data available)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniTrig](qfSoniTrig.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o3: Sensor trigger source lost)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniComm](qfSoniComm.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o4: SDM communications error)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniTemp](qfSoniTemp.md)  <sub>OPT</sub>
    * Description: Sensor signal flag (QFSONIC,s1: Axes TSONIC difference > 4K)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniSignalPoor](qfSoniSignalPoor.md)  <sub>OPT</sub>
    * Description: Sensor signal flag (QFSONIC,s2: Poor signal lock)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniSignalHigh](qfSoniSignalHigh.md)  <sub>OPT</sub>
    * Description: Sensor signal flag (QFSONIC,s3: High signal amplitude)
    * range: [Integer](types/Integer.md)
    * inherited from: None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:soni |
| **In Subsets:** | | DP0.00007.001 |

