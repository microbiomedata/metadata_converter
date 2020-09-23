
# Type: csd_continuousDischarge_pub




URI: [neon:CsdContinuousDischargePub](https://data.neonscience.org/CsdContinuousDischargePub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[CsdContinuousDischargePub&#124;siteID:string%20%3F;startDate:time%20%3F;endDate:time%20%3F;namedLocation:string%20%3F;assetID:string%20%3F;calCertificateFile:string%20%3F;calibratedPressure:double%20%3F;curveID:string%20%3F;dischargeAlphaQF:integer%20%3F;dischargeBetaQF:integer%20%3F;dischargeConsistQF:integer%20%3F;dischargeFinalQF:integer%20%3F;dischargeFinalQFSciRvw:string%20%3F;dischargeGapQF:integer%20%3F;dischargeNullQF:integer%20%3F;dischargePersistQF:integer%20%3F;dischargeRangeQF:integer%20%3F;dischargeSpikeQF:integer%20%3F;dischargeStepQF:integer%20%3F;dischargeSuspectCalQF:integer%20%3F;dischargeValidCalQF:integer%20%3F;equivalentStage:double%20%3F;maxpostDischarge:double%20%3F;nonSystematicUnc:double%20%3F;stageUnc:double%20%3F;systematicUnc:double%20%3F;withParaUncQlower1Std:double%20%3F;withParaUncQlower2Std:double%20%3F;withParaUncQMean:double%20%3F;withParaUncQMedian:double%20%3F;withParaUncQStdDev:double%20%3F;withParaUncQupper1Std:double%20%3F;withParaUncQupper2Std:double%20%3F;withRemnUncQlower1Std:double%20%3F;withRemnUncQlower2Std:double%20%3F;withRemnUncQMean:double%20%3F;withRemnUncQMedian:double%20%3F;withRemnUncQStdDev:double%20%3F;withRemnUncQupper1Std:double%20%3F;withRemnUncQUpper2Std:double%20%3F;calibrationID:string%20%3F;stationHorizontalID:string%20%3F])

## Attributes


### Own

 * [assetID](assetID.md)  <sub>OPT</sub>
    * Description: MxAssetID from the calibration file
    * range: [String](types/String.md)
 * [calCertificateFile](calCertificateFile.md)  <sub>OPT</sub>
    * Description: Calibration certificate file
    * range: [String](types/String.md)
 * [calibratedPressure](calibratedPressure.md)  <sub>OPT</sub>
    * Description: Calibrated surface water pressure
    * range: [Double](types/Double.md)
 * [calibrationID](calibrationID.md)  <sub>OPT</sub>
    * Description: Calibration ID that corresponds to the ID assigned by CI to a set of calibration factors for a measurement stream
    * range: [String](types/String.md)
 * [curveID](curveID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the curve fit to gauge and discharge measurements
    * range: [String](types/String.md)
 * [dischargeAlphaQF](dischargeAlphaQF.md)  <sub>OPT</sub>
    * Description: Discharge quality assurance and quality control report for the alpha quality flag that indicates if one or more quality analysis failed for a datum detailed in NEON.DOC.001113 (1=fail; 0=pass; -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
 * [dischargeBetaQF](dischargeBetaQF.md)  <sub>OPT</sub>
    * Description: Discharge quality assurance and quality control report for the beta quality flag which indicates if one or more quality analysis could not be run for a datum detailed in NEON.DOC.001113 (1=fail; 0=pass; -1=NA (i.e could not be run))
    * range: [Integer](types/Integer.md)
 * [dischargeConsistQF](dischargeConsistQF.md)  <sub>OPT</sub>
    * Description: Discharge quality flag for the consistency test detailed in NEON.DOC.011081 (1=fail; 0=pass; -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
 * [dischargeFinalQF](dischargeFinalQF.md)  <sub>OPT</sub>
    * Description: Discharge final quality flag indicating whether a data product has passed or failed an overall assessment of its quality; detailed in ATBD (1=fail; 0=pass)
    * range: [Integer](types/Integer.md)
 * [dischargeFinalQFSciRvw](dischargeFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Discharge final quality flag indicating whether a data product has failed a science review of its quality detailed in NEON.DOC.001113 (1=fail; 0=pass/not-reviewed)
    * range: [String](types/String.md)
 * [dischargeGapQF](dischargeGapQF.md)  <sub>OPT</sub>
    * Description: Discharge quality flag for the gap test detailed in NEON.DOC.011081 (1=fail; 0=pass; -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
 * [dischargeNullQF](dischargeNullQF.md)  <sub>OPT</sub>
    * Description: Discharge quality flag for the null test detailed in NEON.DOC.011081 (1=fail; 0=pass; -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
 * [dischargePersistQF](dischargePersistQF.md)  <sub>OPT</sub>
    * Description: Discharge quality flag for the persistence test detailed in NEON.DOC.011081 (1=fail; 0=pass; -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
 * [dischargeRangeQF](dischargeRangeQF.md)  <sub>OPT</sub>
    * Description: Discharge quality flag for the range test detailed in NEON.DOC.011081 (1=fail; 0=pass; -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
 * [dischargeSpikeQF](dischargeSpikeQF.md)  <sub>OPT</sub>
    * Description: Discharge quality flag for the spike test detailed in NEON.DOC.011081 (1=fail; 0=pass; -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [dischargeStepQF](dischargeStepQF.md)  <sub>OPT</sub>
    * Description: Discharge quality flag for the step test detailed in NEON.DOC.011081 (1=fail; 0=pass; -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
 * [dischargeSuspectCalQF](dischargeSuspectCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the suspect calibration check of discharge detailed in NEON.DOC.011081 (1=fail; 0=pass; -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
 * [dischargeValidCalQF](dischargeValidCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check of discharge detailed in NEON.DOC.011081 (1=fail; 0=pass; -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [equivalentStage](equivalentStage.md)  <sub>OPT</sub>
    * Description: Stage equivalent to the observed surface water pressure
    * range: [Double](types/Double.md)
 * [maxpostDischarge](maxpostDischarge.md)  <sub>OPT</sub>
    * Description: Total stream or river discharge
    * range: [Double](types/Double.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
 * [nonSystematicUnc](nonSystematicUnc.md)  <sub>OPT</sub>
    * Description: Uncertainty associated with instrumental noise and free surface fluctuations; sensor repeatability
    * range: [Double](types/Double.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [stageUnc](stageUnc.md)  <sub>OPT</sub>
    * Description: Uncertainty associated with the stage timeseries data; the sum of nonSystematicUnc and systematicUnc
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationHorizontalID](stationHorizontalID.md)  <sub>OPT</sub>
    * Description: Horizontal code for station
    * range: [String](types/String.md)
 * [systematicUnc](systematicUnc.md)  <sub>OPT</sub>
    * Description: Uncertainty associated with the relationship between water column height and staff gauge readings; quantified by the difference between calculatedStage and recorded gaugeHeight
    * range: [Double](types/Double.md)
 * [withParaUncQMean](withParaUncQMean.md)  <sub>OPT</sub>
    * Description: Mean discharge including parametric error associated with the rating curve fit
    * range: [Double](types/Double.md)
 * [withParaUncQMedian](withParaUncQMedian.md)  <sub>OPT</sub>
    * Description: Median discharge including parametric error associated with the rating curve fit
    * range: [Double](types/Double.md)
 * [withParaUncQStdDev](withParaUncQStdDev.md)  <sub>OPT</sub>
    * Description: Standard deviation of discharge including parametric error associated with the rating curve fit
    * range: [Double](types/Double.md)
 * [withParaUncQlower1Std](withParaUncQlower1Std.md)  <sub>OPT</sub>
    * Description: Lower bound of one standard deviation for discharge including parametric error associated with the rating curve fit
    * range: [Double](types/Double.md)
 * [withParaUncQlower2Std](withParaUncQlower2Std.md)  <sub>OPT</sub>
    * Description: Lower bound of the 95 % confidence interval for discharge including parametric error associated with the rating curve fit
    * range: [Double](types/Double.md)
 * [withParaUncQupper1Std](withParaUncQupper1Std.md)  <sub>OPT</sub>
    * Description: Upper bound of one standard deviation for discharge including parametric error associated with the rating curve fit
    * range: [Double](types/Double.md)
 * [withParaUncQupper2Std](withParaUncQupper2Std.md)  <sub>OPT</sub>
    * Description: Upper bound of the 95 % confidence interval for discharge including parametric error associated with the rating curve fit
    * range: [Double](types/Double.md)
 * [withRemnUncQMean](withRemnUncQMean.md)  <sub>OPT</sub>
    * Description: Mean discharge including parametric and remnant error associated with the rating curve fit
    * range: [Double](types/Double.md)
 * [withRemnUncQMedian](withRemnUncQMedian.md)  <sub>OPT</sub>
    * Description: Median discharge including parametric and remnant error associated with the rating curve fit
    * range: [Double](types/Double.md)
 * [withRemnUncQStdDev](withRemnUncQStdDev.md)  <sub>OPT</sub>
    * Description: Standard deviation of discharge including parametric and remnant error associated with the rating curve fit
    * range: [Double](types/Double.md)
 * [withRemnUncQUpper2Std](withRemnUncQUpper2Std.md)  <sub>OPT</sub>
    * Description: Upper bound of the 95 % confidence interval for discharge including parametric and remnant error associated with the rating curve fit
    * range: [Double](types/Double.md)
 * [withRemnUncQlower1Std](withRemnUncQlower1Std.md)  <sub>OPT</sub>
    * Description: Lower bound of one standard deviation for discharge including parametric and remnant error associated with the rating curve fit
    * range: [Double](types/Double.md)
 * [withRemnUncQlower2Std](withRemnUncQlower2Std.md)  <sub>OPT</sub>
    * Description: Lower bound of the 95 % confidence interval for discharge including parametric and remnant error associated with the rating curve fit
    * range: [Double](types/Double.md)
 * [withRemnUncQupper1Std](withRemnUncQupper1Std.md)  <sub>OPT</sub>
    * Description: Upper bound of one standard deviation for discharge including parametric and remnant error associated with the rating curve fit
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:csd_continuousDischarge_pub |
| **In Subsets:** | | DP4.00130.001 |

