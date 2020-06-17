
# Type: WSDBuoy_2min




URI: [neon:WSDBuoy2min](https://data.neonscience.org/WSDBuoy2min)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [buoyCompGapQAQCRpt](buoyCompGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy compass quality assurance and quality control report for the gap test, which indicates that the datum is missing and is a part of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [buoyCompNullQAQCRpt](buoyCompNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy compass quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyCompPersistenceQAQCRpt](buoyCompPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy compass QAQC report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a designated period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyCompRangeQAQCRpt](buoyCompRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy compass quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyCompSpikeQAQCRpt](buoyCompSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy compass quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyCompStepQAQCRpt](buoyCompStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy compass quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindDirAlphaQAQCRpt](buoyWindDirAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindDirBetaQAQCRpt](buoyWindDirBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindDirCalmWindQAQCRpt](buoyWindDirCalmWindQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality assurance and quality control report for the calm wind test, which indicates whether or not Buoy wind direction measurements were made during calm winds, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindDirConsistencyQAQCRpt](buoyWindDirConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindDirDeadZoneQAQCRpt](buoyWindDirDeadZoneQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality assurance and quality control report for the dead band test, which indicates whether or not Buoy wind direction measurements were made in the dead band zone of the sensor, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindDirGapQAQCRpt](buoyWindDirGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [buoyWindDirNullQAQCRpt](buoyWindDirNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindDirPersistenceQAQCRpt](buoyWindDirPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a time period, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindDirRangeQAQCRpt](buoyWindDirRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindDirSpikeQAQCRpt](buoyWindDirSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindDirStepQAQCRpt](buoyWindDirStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindDirValidCalQAQCRpt](buoyWindDirValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind direction QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindSpeedAlphaQAQCRpt](buoyWindSpeedAlphaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality assurance and quality control report for the alpha quality flag, which indicates if one or more quality analysis failed for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindSpeedBetaQAQCRpt](buoyWindSpeedBetaQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality assurance and quality control report for the beta quality flag, which indicates if one or more quality analysis could not be run for a datum, detailed in NEON.DOC.001113 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindSpeedConsistencyQAQCRpt](buoyWindSpeedConsistencyQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality assurance and quality control report for the consistency test, which indicates whether or not measurements are consistent with co-located measurements, (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindSpeedGapQAQCRpt](buoyWindSpeedGapQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality assurance and quality control report for the gap test, which indicates that the datum is missing and is apart of a prolonged period of missing data, detailed in NEON.DOC.011081 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [buoyWindSpeedNullQAQCRpt](buoyWindSpeedNullQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality assurance and quality control report for the null test, which indicates a missing datum, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindSpeedPersistenceQAQCRpt](buoyWindSpeedPersistenceQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality assurance and quality control report for the persistence test, which indicates  whether there is a realistic fluctuation of values over a  period of time, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindSpeedRangeQAQCRpt](buoyWindSpeedRangeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality assurance and quality control report for the range test, which indicates whether a datum exceeds a realistic value, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindSpeedSpikeQAQCRpt](buoyWindSpeedSpikeQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality assurance and quality control report for the spike test, which indicates whether or not a datum has been identified as a spike, detailed in NEON.DOC.000783 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindSpeedStepQAQCRpt](buoyWindSpeedStepQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality assurance and quality control report for the step test, which indicates whether unusual jumps in the data exist, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)
 * [buoyWindSpeedValidCalQAQCRpt](buoyWindSpeedValidCalQAQCRpt.md)  <sub>OPT</sub>
    * Description: Buoy wind speed QAQC report for the valid calibration check, which indicates whether the measurements are within the valid calibration date range, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [String](types/String.md)

### Inherited from SCGW_5_minute:

 * [endDateTime](endDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is completed
    * range: [Time](types/Time.md)
 * [groundwaterSpecCond](groundwaterSpecCond.md)  <sub>OPT</sub>
    * Description: Specific conductivity in groundwater in microsiemens per centimeter
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterSpecCondExpUncert](groundwaterSpecCondExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for Specific Conductivity in groundwater in degrees celsius
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groundwaterSpecCondRangeQF](groundwaterSpecCondRangeQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the range test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterSpecCondPersistQF](groundwaterSpecCondPersistQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the persistence test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterSpecCondStepQF](groundwaterSpecCondStepQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the step test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterSpecCondNullQF](groundwaterSpecCondNullQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the null test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterSpecCondGapQF](groundwaterSpecCondGapQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the gap test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterSpecCondConsistQF](groundwaterSpecCondConsistQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the consistency test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [groundwaterSpecCondSpikeQF](groundwaterSpecCondSpikeQF.md)  <sub>OPT</sub>
    * Description: Specific Conductivity in groundwater quality flag for the spike test, detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [validCalQF](validCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check detailed in NEON.DOC.011081 (1=fail, 0=pass, -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [sciRvwQF](sciRvwQF.md)  <sub>OPT</sub>
    * Description: Stand-alone quality flag (does not interact with final quality flag) indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from TSD_1_min:

 * [startDateTime](startDateTime.md)  <sub>OPT</sub>
    * Description: Date and time at which a sampling is initiated
    * range: [Time](types/Time.md)
 * [thermistorDepth](thermistorDepth.md)  <sub>OPT</sub>
    * Description: Depth of the temperature sensor (thermistor) from water surface in lakes and rivers
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tsdWaterTemp](tsdWaterTemp.md)  <sub>OPT</sub>
    * Description: Temperature of surface water at specific depths in lakes and rivers
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tsdWaterTempConsistQF](tsdWaterTempConsistQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the consistency test of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [tsdWaterTempExpUncert](tsdWaterTempExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for tsdWaterTemp
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tsdWaterTempGapQF](tsdWaterTempGapQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the gap test of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [tsdWaterTempNullQF](tsdWaterTempNullQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the null test of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [tsdWaterTempRangeQF](tsdWaterTempRangeQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the range test of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [tsdWaterTempSpikeQF](tsdWaterTempSpikeQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the spike test of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [tsdWaterTempStepQF](tsdWaterTempStepQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the step test of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [tsdWaterTempValidCalQF](tsdWaterTempValidCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check of tsdWaterTemp. Detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None

### Inherited from WSDBuoy_30min:

 * [buoyCompGapFailQM](buoyCompGapFailQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompGapNAQM](buoyCompGapNAQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompGapPassQM](buoyCompGapPassQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompNullFailQM](buoyCompNullFailQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompNullNAQM](buoyCompNullNAQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompNullPassQM](buoyCompNullPassQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompPersistenceFailQM](buoyCompPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompPersistenceNAQM](buoyCompPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompPersistencePassQM](buoyCompPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompRangeFailQM](buoyCompRangeFailQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompRangeNAQM](buoyCompRangeNAQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompRangePassQM](buoyCompRangePassQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompSpikeFailQM](buoyCompSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompSpikeNAQM](buoyCompSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompSpikePassQM](buoyCompSpikePassQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompStepFailQM](buoyCompStepFailQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompStepNAQM](buoyCompStepNAQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyCompStepPassQM](buoyCompStepPassQM.md)  <sub>OPT</sub>
    * Description: Buoy compass quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirAlphaQM](buoyWindDirAlphaQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [buoyWindDirBetaQM](buoyWindDirBetaQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [buoyWindDirCalmWindFailQM](buoyWindDirCalmWindFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the failed outcomes of the calm wind test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirCalmWindNAQM](buoyWindDirCalmWindNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes when the calm wind test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirCalmWindPassQM](buoyWindDirCalmWindPassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the passed outcomes of the calm wind test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirConsistencyFailQM](buoyWindDirConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirConsistencyNAQM](buoyWindDirConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirConsistencyPassQM](buoyWindDirConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirDeadZoneFailQM](buoyWindDirDeadZoneFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the failed outcomes of the dead band test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirDeadZoneNAQM](buoyWindDirDeadZoneNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes when the dead band test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirDeadZonePassQM](buoyWindDirDeadZonePassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the passed outcomes of the dead band test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirExpUncert](buoyWindDirExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for wind direction on buoy
    * range: [Double](types/Double.md)
 * [buoyWindDirFinalQF](buoyWindDirFinalQF.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [buoyWindDirFinalQFSciRvw](buoyWindDirFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [buoyWindDirGapFailQM](buoyWindDirGapFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirGapNAQM](buoyWindDirGapNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirGapPassQM](buoyWindDirGapPassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirMean](buoyWindDirMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of wind direction on buoy
    * range: [Double](types/Double.md)
 * [buoyWindDirNullFailQM](buoyWindDirNullFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirNullNAQM](buoyWindDirNullNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirNullPassQM](buoyWindDirNullPassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirNumPts](buoyWindDirNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of wind direction on buoy
    * range: [Double](types/Double.md)
 * [buoyWindDirPersistenceFailQM](buoyWindDirPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirPersistenceNAQM](buoyWindDirPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirPersistencePassQM](buoyWindDirPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirRangeFailQM](buoyWindDirRangeFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirRangeNAQM](buoyWindDirRangeNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirRangePassQM](buoyWindDirRangePassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirSpikeFailQM](buoyWindDirSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirSpikeNAQM](buoyWindDirSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirSpikePassQM](buoyWindDirSpikePassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirStdErMean](buoyWindDirStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for wind direction on buoy
    * range: [Double](types/Double.md)
 * [buoyWindDirStepFailQM](buoyWindDirStepFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirStepNAQM](buoyWindDirStepNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirStepPassQM](buoyWindDirStepPassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirValidCalFailQM](buoyWindDirValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirValidCalNAQM](buoyWindDirValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirValidCalPassQM](buoyWindDirValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind direction quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindDirVariance](buoyWindDirVariance.md)  <sub>OPT</sub>
    * Description: Variance in wind direction on buoy
    * range: [Double](types/Double.md)
 * [buoyWindSpeedAlphaQM](buoyWindSpeedAlphaQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric detailing the outcomes of the alpha quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [buoyWindSpeedBetaQM](buoyWindSpeedBetaQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric detailing the outcomes of the beta quality flag over the averaging period, as a percent and detailed in NEON.DOC.001113
    * range: [Double](types/Double.md)
 * [buoyWindSpeedConsistencyFailQM](buoyWindSpeedConsistencyFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the failed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedConsistencyNAQM](buoyWindSpeedConsistencyNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes when the consistency test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedConsistencyPassQM](buoyWindSpeedConsistencyPassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the passed outcomes of the consistency test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedExpUncert](buoyWindSpeedExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for wind speed on buoy
    * range: [Double](types/Double.md)
 * [buoyWindSpeedFinalQF](buoyWindSpeedFinalQF.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality flag indicating whether a data product has passed or failed an overall assessment of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [buoyWindSpeedFinalQFSciRvw](buoyWindSpeedFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [buoyWindSpeedGapFailQM](buoyWindSpeedGapFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the failed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedGapNAQM](buoyWindSpeedGapNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes when the gap test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedGapPassQM](buoyWindSpeedGapPassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the passed outcomes of the gap test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedMaximum](buoyWindSpeedMaximum.md)  <sub>OPT</sub>
    * Description: Maximum wind speed on buoy
    * range: [Double](types/Double.md)
 * [buoyWindSpeedMean](buoyWindSpeedMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of wind speed on buoy
    * range: [Double](types/Double.md)
 * [buoyWindSpeedMinimum](buoyWindSpeedMinimum.md)  <sub>OPT</sub>
    * Description: Minimum wind speed on buoy
    * range: [Double](types/Double.md)
 * [buoyWindSpeedNullFailQM](buoyWindSpeedNullFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the failed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedNullNAQM](buoyWindSpeedNullNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes when the null test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedNullPassQM](buoyWindSpeedNullPassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the passed outcomes of the null test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedNumPts](buoyWindSpeedNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of wind speed on buoy
    * range: [Double](types/Double.md)
 * [buoyWindSpeedPersistenceFailQM](buoyWindSpeedPersistenceFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes  the failed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedPersistenceNAQM](buoyWindSpeedPersistenceNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes when the persistence test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedPersistencePassQM](buoyWindSpeedPersistencePassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the passed outcomes of the persistence test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedRangeFailQM](buoyWindSpeedRangeFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the failed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedRangeNAQM](buoyWindSpeedRangeNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes when the range test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedRangePassQM](buoyWindSpeedRangePassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the passed outcomes of the range test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedSpikeFailQM](buoyWindSpeedSpikeFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the failed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedSpikeNAQM](buoyWindSpeedSpikeNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes when the spike test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedSpikePassQM](buoyWindSpeedSpikePassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the passed outcomes of the spike test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedStdErMean](buoyWindSpeedStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for wind speed on buoy
    * range: [Double](types/Double.md)
 * [buoyWindSpeedStepFailQM](buoyWindSpeedStepFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the failed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedStepNAQM](buoyWindSpeedStepNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes when the step test could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedStepPassQM](buoyWindSpeedStepPassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the passed outcomes of the step test over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedValidCalFailQM](buoyWindSpeedValidCalFailQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the failed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedValidCalNAQM](buoyWindSpeedValidCalNAQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes when the valid calibration check could not be run over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedValidCalPassQM](buoyWindSpeedValidCalPassQM.md)  <sub>OPT</sub>
    * Description: Buoy wind speed quality metric that summarizes the passed outcomes of the valid calibration check over the averaging period, as a percent
    * range: [Double](types/Double.md)
 * [buoyWindSpeedVariance](buoyWindSpeedVariance.md)  <sub>OPT</sub>
    * Description: Variance in wind speed on buoy
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:WSDBuoy_2min |
| **In Subsets:** | | DP1.20059.001 |

