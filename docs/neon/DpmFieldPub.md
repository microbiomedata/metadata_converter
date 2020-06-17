
# Type: dpm_field_pub




URI: [neon:DpmFieldPub](https://data.neonscience.org/DpmFieldPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Inherited from asi_fieldSuperParent_pub:

 * [waterTemp](waterTemp.md)  <sub>OPT</sub>
    * Description: Temperature of water (C)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [aCollectedBy](aCollectedBy.md)  <sub>OPT</sub>
    * Description: Primary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [bCollectedBy](bCollectedBy.md)  <sub>OPT</sub>
    * Description: Secondary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [altLocation](altLocation.md)  <sub>OPT</sub>
    * Description: Alternate Sampling Location description
    * range: [String](types/String.md)
    * inherited from: None
 * [maxDepth](maxDepth.md)  <sub>OPT</sub>
    * Description: Maximum depth
    * range: [Double](types/Double.md)
    * inherited from: None
 * [upperSegmentDepth](upperSegmentDepth.md)  <sub>OPT</sub>
    * Description: Depth at top of stratified lake segment
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lowerSegmentDepth](lowerSegmentDepth.md)  <sub>OPT</sub>
    * Description: Depth at bottom of stratified lake segment
    * range: [Double](types/Double.md)
    * inherited from: None
 * [wellWaterDepth](wellWaterDepth.md)  <sub>OPT</sub>
    * Description: Depth of water in well from top of well casing
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sampleDepth](sampleDepth.md)  <sub>OPT</sub>
    * Description: Depth sample was collected
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sampleExtractionMethod](sampleExtractionMethod.md)  <sub>OPT</sub>
    * Description: Method used to extract the sample
    * range: [String](types/String.md)
    * inherited from: None
 * [wellVolumePurged](wellVolumePurged.md)  <sub>OPT</sub>
    * Description: Total volume removed from the well, prior to sampling
    * range: [Double](types/Double.md)
    * inherited from: None
 * [samplerType](samplerType.md)  <sub>OPT</sub>
    * Description: Type of sampler used to collect the sample
    * range: [String](types/String.md)
    * inherited from: None
 * [parentSampleID](parentSampleID.md)  <sub>OPT</sub>
    * Description: Parent sampleID of sample being processed
    * range: [String](types/String.md)
    * inherited from: None
 * [lakeSampleDepth1](lakeSampleDepth1.md)  <sub>OPT</sub>
    * Description: Sample depth of a single lake sample collected below the surface; the sample depth of the upper sample for a composite lake sample collected below the surface
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lakeSampleDepth2](lakeSampleDepth2.md)  <sub>OPT</sub>
    * Description: Sample depth of the lower sample for a composite lake sample collected below the surface
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sdgSamplingProtocolVersion](sdgSamplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version of the dissolved gas protocol where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
    * inherited from: None
 * [asiSamplingProtocolVersion](asiSamplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version of the aquatic stable isotopes protocol where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
    * inherited from: None
 * [aquaticSiteType](aquaticSiteType.md)  <sub>OPT</sub>
    * Description: Type of aquatic site, includes lake, river or stream
    * range: [String](types/String.md)
    * inherited from: None
 * [parentSampleCode](parentSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a parent sample
    * range: [String](types/String.md)
    * inherited from: None
 * [fieldDataQF](fieldDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for field data
    * range: [String](types/String.md)
    * inherited from: None
 * [samplingImpractical](samplingImpractical.md)  <sub>OPT</sub>
    * Description: Samples and/or measurements were not collected due to the indicated circumstance
    * range: [String](types/String.md)
    * inherited from: None
 * [additionalCoordUncertainty](additionalCoordUncertainty.md)  <sub>OPT</sub>
    * Description: Additional uncertainty to be added to the coordinate uncertainty at all sites
    * range: [Double](types/Double.md)
    * inherited from: None
 * [amcSamplingProtocolVersion](amcSamplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version of the aquatic microbes protocol where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
    * inherited from: None
 * [swcSamplingProtocolVersion](swcSamplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version of the water chemistry protocol where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
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

### Inherited from dpm_fieldData_in:

 * [aSetBy](aSetBy.md)  <sub>OPT</sub>
    * Description: Primary NEON technician username who set the collector
    * range: [String](types/String.md)
 * [bSetBy](bSetBy.md)  <sub>OPT</sub>
    * Description: Secondary NEON technician username who set the collector
    * range: [String](types/String.md)
 * [fieldFilterCondition](fieldFilterCondition.md)  <sub>OPT</sub>
    * Description: Condition of the filter reported in the field
    * range: [String](types/String.md)
 * [fieldFilterConditionRemarks](fieldFilterConditionRemarks.md)  <sub>OPT</sub>
    * Description: Additional description of the field filter condition
    * range: [String](types/String.md)
 * [fieldFilterDamage](fieldFilterDamage.md)  <sub>OPT</sub>
    * Description: Field description of how the filter is damaged, if at all
    * range: [String](types/String.md)
 * [fieldFilterDamageRemarks](fieldFilterDamageRemarks.md)  <sub>OPT</sub>
    * Description: Additional description of possible field damages, e.g., tear, hole, piece missing
    * range: [String](types/String.md)
 * [filterID](filterID.md)  <sub>OPT</sub>
    * Description: The non-repeating manufacturer-generated ID of each filter
    * range: [String](types/String.md)
 * [filterWet](filterWet.md)  <sub>OPT</sub>
    * Description: Percentage of the filter area that is wet
    * range: [Double](types/Double.md)
 * [equipCondition](equipCondition.md)  <sub>OPT</sub>
    * Description: Condition of the equipment
    * range: [String](types/String.md)
 * [equipConditionDesc](equipConditionDesc.md)  <sub>OPT</sub>
    * Description: Description of problems with the equipment
    * range: [String](types/String.md)
 * [filterCode](filterCode.md)  <sub>OPT</sub>
    * Description: Barcode of the filter
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from inv_pervial_pub:

 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [slideID](slideID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with each slide per sampleID or subsampleID
    * range: [String](types/String.md)
    * inherited from: None
 * [referenceCount](referenceCount.md)  <sub>OPT</sub>
    * Description: Number of individuals removed from this sample and placed in reference collection
    * range: [String](types/String.md)
    * inherited from: None
 * [referenceID](referenceID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with the reference collection
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [slideCode](slideCode.md)  <sub>OPT</sub>
    * Description: Barcode of a slide
    * range: [String](types/String.md)
    * inherited from: None
 * [referenceCode](referenceCode.md)  <sub>OPT</sub>
    * Description: Barcode of a reference sample
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from mam_voucher_pub:

 * [tagID](tagID.md)  <sub>OPT</sub>
    * Description: Domain-level unique identifier of tag used to mark the individual
    * range: [String](types/String.md)
    * inherited from: None
 * [voucherSampleID](voucherSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the voucher sample
    * range: [String](types/String.md)
    * inherited from: None
 * [decimalLatitude](decimalLatitude.md)  <sub>OPT</sub>
    * Description: The geographic latitude (in decimal degrees, WGS84) of the geographic center of the reference area
    * range: [Double](types/Double.md)
 * [decimalLongitude](decimalLongitude.md)  <sub>OPT</sub>
    * Description: The geographic longitude (in decimal degrees, WGS84) of the geographic center of the reference area
    * range: [Double](types/Double.md)
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
 * [coordinateUncertainty](coordinateUncertainty.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the Location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
 * [elevation](elevation.md)  <sub>OPT</sub>
    * Description: Elevation (in meters) above sea level
    * range: [Double](types/Double.md)
 * [elevationUncertainty](elevationUncertainty.md)  <sub>OPT</sub>
    * Description: Uncertainty in elevation values (in meters)
    * range: [Double](types/Double.md)
 * [morphospeciesID](morphospeciesID.md)  <sub>OPT</sub>
    * Description: Identifier for morphospecies
    * range: [String](types/String.md)
    * inherited from: None
 * [identifiedBy](identifiedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who identified the specimen
    * range: [String](types/String.md)
    * inherited from: None
 * [taxonIDRemarks](taxonIDRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes about the specific taxon; free text comments accompanying the record
    * range: [String](types/String.md)
    * inherited from: None
 * [morphospeciesIDRemarks](morphospeciesIDRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes about the morphospecies; free text comments accompanying the record
    * range: [String](types/String.md)
    * inherited from: None
 * [altLongitude](altLongitude.md)  <sub>OPT</sub>
    * Description: Alternate Sampling Location coordinate - longitude
    * range: [Double](types/Double.md)
    * inherited from: None
 * [altLatitude](altLatitude.md)  <sub>OPT</sub>
    * Description: Alternate Sampling Location coordinate - latitude
    * range: [Double](types/Double.md)
    * inherited from: None
 * [collectedBy](collectedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who collected the sample or specimen
    * range: [String](types/String.md)
    * inherited from: None
 * [altCoordinateUncertainty](altCoordinateUncertainty.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given altLatitude and altLongitude describing the smallest circle containing the whole of the Location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
    * inherited from: None
 * [altGeodeticDatum](altGeodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth for alternate location coordinate
    * range: [String](types/String.md)
    * inherited from: None
 * [nativeStatusCode](nativeStatusCode.md)  <sub>OPT</sub>
    * Description: The process by which the taxon became established in the location
    * range: [String](types/String.md)
    * inherited from: None
 * [altCoordinateSource](altCoordinateSource.md)  <sub>OPT</sub>
    * Description: Alternate method used to collect or create spatial information
    * range: [String](types/String.md)
    * inherited from: None
 * [altElevation](altElevation.md)  <sub>OPT</sub>
    * Description: Alternate elevation (in meters) above sea level
    * range: [Double](types/Double.md)
    * inherited from: None
 * [altElevationUncertainty](altElevationUncertainty.md)  <sub>OPT</sub>
    * Description: Alternate uncertainty in elevation values (in meters)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [habitatDescription](habitatDescription.md)  <sub>OPT</sub>
    * Description: Description of the habitat in which the event occurred
    * range: [String](types/String.md)
    * inherited from: None
 * [tagCode](tagCode.md)  <sub>OPT</sub>
    * Description: Code of domain-level unique identifier used to mark the individual
    * range: [String](types/String.md)
    * inherited from: None
 * [voucherSampleCode](voucherSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a voucher sample
    * range: [String](types/String.md)
    * inherited from: None

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
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
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
| **Mappings:** | | neon:dpm_field_pub |
| **In Subsets:** | | DP1.00101.001 |

