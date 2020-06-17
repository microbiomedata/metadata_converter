
# Type: ntr_internalLabBlanks_pub




URI: [neon:NtrInternalLabBlanksPub](https://data.neonscience.org/NtrInternalLabBlanksPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Inherited from cfc_chlorophyll_pub:

 * [extractionStartDate](extractionStartDate.md)  <sub>OPT</sub>
    * Description: The start date-time for an extraction event
    * range: [Time](types/Time.md)
 * [receivedCondition](receivedCondition.md)  <sub>OPT</sub>
    * Description: Condition of the sample on the date it was received
    * range: [String](types/String.md)
    * inherited from: None
 * [chlCarotWavelength1](chlCarotWavelength1.md)  <sub>OPT</sub>
    * Description: The first wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength1Abs](chlCarotWavelength1Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the first wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength2](chlCarotWavelength2.md)  <sub>OPT</sub>
    * Description: The second wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength2Abs](chlCarotWavelength2Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the second wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength3](chlCarotWavelength3.md)  <sub>OPT</sub>
    * Description: The third wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength3Abs](chlCarotWavelength3Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the third wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength4](chlCarotWavelength4.md)  <sub>OPT</sub>
    * Description: The fourth wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength4Abs](chlCarotWavelength4Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the fourth wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlorophyllSampleCode](chlorophyllSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a chlorophyll sample
    * range: [String](types/String.md)
    * inherited from: None
 * [chlorophyllSampleID](chlorophyllSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a chlorophyll sample
    * range: [String](types/String.md)
    * inherited from: None
 * [extractCarotConc](extractCarotConc.md)  <sub>OPT</sub>
    * Description: Calculated total carotenoid concentration of the extract solution, dilution-corrected as needed
    * range: [Double](types/Double.md)
    * inherited from: None
 * [extractChlAConc](extractChlAConc.md)  <sub>OPT</sub>
    * Description: Calculated chlorophyll A concentration of the extract solution, dilution-corrected as needed
    * range: [Double](types/Double.md)
    * inherited from: None
 * [extractChlBConc](extractChlBConc.md)  <sub>OPT</sub>
    * Description: Calculated chlorophyll B concentration of the extract solution, dilution-corrected as needed
    * range: [Double](types/Double.md)
    * inherited from: None
 * [extractionLength](extractionLength.md)  <sub>OPT</sub>
    * Description: The duration of an extraction event
    * range: [Double](types/Double.md)
    * inherited from: None
 * [handlingQF](handlingQF.md)  <sub>OPT</sub>
    * Description: Quality flag for sample handling
    * range: [String](types/String.md)
    * inherited from: None
 * [relativeAccuracyScale](relativeAccuracyScale.md)  <sub>OPT</sub>
    * Description: Indicator for the mean relative accuracy of standards analyzed as unknowns with a run of samples
    * range: [String](types/String.md)
    * inherited from: None
 * [solventVolume](solventVolume.md)  <sub>OPT</sub>
    * Description: Volume of solvent used in the extraction
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from csd_pressureGaugeRelationship_pub:

 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [namedLocation](namedLocation.md)  <sub>OPT</sub>
    * Description: Name of the measurement location in the NEON database
    * range: [String](types/String.md)
    * inherited from: None
 * [assetID](assetID.md)  <sub>OPT</sub>
    * Description: MxAssetID from the calibration file
    * range: [String](types/String.md)
    * inherited from: None
 * [calCertificateFile](calCertificateFile.md)  <sub>OPT</sub>
    * Description: Calibration certificate file
    * range: [String](types/String.md)
    * inherited from: None
 * [calculatedStage](calculatedStage.md)  <sub>OPT</sub>
    * Description: Stage calculated from the sum of the water column height and sensorStaffGaugeOffset
    * range: [Double](types/Double.md)
    * inherited from: None
 * [calcWaterColumnHeight](calcWaterColumnHeight.md)  <sub>OPT</sub>
    * Description: Calculated water column height based off of the calibratedPressMean
    * range: [Double](types/Double.md)
    * inherited from: None
 * [calibratedPressMean](calibratedPressMean.md)  <sub>OPT</sub>
    * Description: Mean calibrated surface water pressure
    * range: [Double](types/Double.md)
    * inherited from: None
 * [calibratedPressObsCount](calibratedPressObsCount.md)  <sub>OPT</sub>
    * Description: Number of observations included in the calibratedPressMean
    * range: [Double](types/Double.md)
    * inherited from: None
 * [calibratedPressStdDev](calibratedPressStdDev.md)  <sub>OPT</sub>
    * Description: Stanrdard deviation of calibrated surface water pressure
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gaugeHeight](gaugeHeight.md)  <sub>OPT</sub>
    * Description: Height of water at staff gauge
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sensorStaffGaugeOffset](sensorStaffGaugeOffset.md)  <sub>OPT</sub>
    * Description: Offset between the pressure sensor and the staff gauge; i.e. the staff gauge reading when the water level is just at a reading of 0 pressure
    * range: [Double](types/Double.md)
    * inherited from: None
 * [calibrationID](calibrationID.md)  <sub>OPT</sub>
    * Description: Calibration ID that corresponds to the ID assigned by CI to a set of calibration factors for a measurement stream
    * range: [String](types/String.md)
    * inherited from: None
 * [gaugeCollectDate](gaugeCollectDate.md)  <sub>OPT</sub>
    * Description: Date of the gauge height reading collection event
    * range: [String](types/String.md)
    * inherited from: None
 * [stationHorizontalID](stationHorizontalID.md)  <sub>OPT</sub>
    * Description: Horizontal code for station
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from ntr_internalLabBlanks_in:

 * [extractionEndDate](extractionEndDate.md)  <sub>OPT</sub>
    * Description: The end date-time for an extraction event
    * range: [Time](types/Time.md)
 * [kclBlank1Code](kclBlank1Code.md)  <sub>OPT</sub>
    * Description: Barcode of the first potassium chloride (KCl) blank reference sample
    * range: [String](types/String.md)
 * [kclBlank1Fate](kclBlank1Fate.md)  <sub>OPT</sub>
    * Description: Fate of the first potassium chloride (KCl) blank blank reference sample
    * range: [String](types/String.md)
    * inherited from: None
 * [kclBlank1ID](kclBlank1ID.md)  <sub>OPT</sub>
    * Description: Identifier for the first potassium chloride (KCl) blank reference sample
    * range: [String](types/String.md)
 * [kclBlank2Code](kclBlank2Code.md)  <sub>OPT</sub>
    * Description: Barcode of the second potassium chloride (KCl) blank reference sample
    * range: [String](types/String.md)
 * [kclBlank2Fate](kclBlank2Fate.md)  <sub>OPT</sub>
    * Description: Fate of the second potassium chloride (KCl) blank reference sample
    * range: [String](types/String.md)
    * inherited from: None
 * [kclBlank2ID](kclBlank2ID.md)  <sub>OPT</sub>
    * Description: Identifier for the second potassium chloride (KCl) blank reference sample
    * range: [String](types/String.md)
 * [kclBlank3Code](kclBlank3Code.md)  <sub>OPT</sub>
    * Description: Barcode of the third potassium chloride (KCl) blank reference sample
    * range: [String](types/String.md)
 * [kclBlank3Fate](kclBlank3Fate.md)  <sub>OPT</sub>
    * Description: Fate of the third potassium chloride (KCl) blank reference sample
    * range: [String](types/String.md)
    * inherited from: None
 * [kclBlank3ID](kclBlank3ID.md)  <sub>OPT</sub>
    * Description: Identifier for the third potassium chloride (KCl) blank reference sample
    * range: [String](types/String.md)
 * [kclReferenceCode](kclReferenceCode.md)  <sub>OPT</sub>
    * Description: Barcode of a potassium chloride (KCl) blank reference
    * range: [String](types/String.md)
    * inherited from: None
 * [kclReferenceFate](kclReferenceFate.md)  <sub>OPT</sub>
    * Description: Fate of a potassium chloride (KCl) blank reference
    * range: [String](types/String.md)
    * inherited from: None
 * [kclReferenceID](kclReferenceID.md)  <sub>OPT</sub>
    * Description: Identifier for a potassium chloride (KCl) blank reference
    * range: [String](types/String.md)

### Inherited from zoo_dnaRawDataFiles_pub:

 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [domainID](domainID.md)  <sub>OPT</sub>
    * Description: Unique identifier of the NEON domain
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
    * inherited from: None
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
    * inherited from: None
 * [processedDate](processedDate.md)  <sub>OPT</sub>
    * Description: Date or date and time of processing event
    * range: [Time](types/Time.md)
    * inherited from: None
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
    * inherited from: None
 * [internalLabID](internalLabID.md)  <sub>OPT</sub>
    * Description: Internal identifier used by the external facility
    * range: [String](types/String.md)
    * inherited from: None
 * [dnaSampleID](dnaSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for DNA sample
    * range: [String](types/String.md)
    * inherited from: None
 * [dnaSampleCode](dnaSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a DNA sample
    * range: [String](types/String.md)
    * inherited from: None
 * [sequencerRunID](sequencerRunID.md)  <sub>OPT</sub>
    * Description: Identifier for the sequencing run
    * range: [String](types/String.md)
    * inherited from: None
 * [rawDataFileName](rawDataFileName.md)  <sub>OPT</sub>
    * Description: Name of file or folder containing raw data, including file extension
    * range: [String](types/String.md)
    * inherited from: None
 * [rawDataFilePath](rawDataFilePath.md)  <sub>OPT</sub>
    * Description: The system path identifying the raw data file location
    * range: [String](types/String.md)
    * inherited from: None
 * [sequencingFacilityID](sequencingFacilityID.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is sequencing samples
    * range: [String](types/String.md)
    * inherited from: None
 * [rawDataFileDescription](rawDataFileDescription.md)  <sub>OPT</sub>
    * Description: Description of the contents and type of file
    * range: [String](types/String.md)
    * inherited from: None

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:ntr_internalLabBlanks_pub |

