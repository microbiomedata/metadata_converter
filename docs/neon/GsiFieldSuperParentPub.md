
# Type: gsi_fieldSuperParent_pub




URI: [neon:GsiFieldSuperParentPub](https://data.neonscience.org/GsiFieldSuperParentPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Inherited from asi_fieldSuperParent_pub:

 * [waterTemp](waterTemp.md)  <sub>OPT</sub>
    * Description: Temperature of water (C)
    * range: [Double](types/Double.md)
 * [aCollectedBy](aCollectedBy.md)  <sub>OPT</sub>
    * Description: Primary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [bCollectedBy](bCollectedBy.md)  <sub>OPT</sub>
    * Description: Secondary NEON technician username who collected the data
    * range: [String](types/String.md)
 * [altLocation](altLocation.md)  <sub>OPT</sub>
    * Description: Alternate Sampling Location description
    * range: [String](types/String.md)
 * [maxDepth](maxDepth.md)  <sub>OPT</sub>
    * Description: Maximum depth
    * range: [Double](types/Double.md)
 * [upperSegmentDepth](upperSegmentDepth.md)  <sub>OPT</sub>
    * Description: Depth at top of stratified lake segment
    * range: [Double](types/Double.md)
 * [lowerSegmentDepth](lowerSegmentDepth.md)  <sub>OPT</sub>
    * Description: Depth at bottom of stratified lake segment
    * range: [Double](types/Double.md)
 * [wellWaterDepth](wellWaterDepth.md)  <sub>OPT</sub>
    * Description: Depth of water in well from top of well casing
    * range: [Double](types/Double.md)
 * [sampleDepth](sampleDepth.md)  <sub>OPT</sub>
    * Description: Depth sample was collected
    * range: [Double](types/Double.md)
 * [sampleExtractionMethod](sampleExtractionMethod.md)  <sub>OPT</sub>
    * Description: Method used to extract the sample
    * range: [String](types/String.md)
 * [wellVolumePurged](wellVolumePurged.md)  <sub>OPT</sub>
    * Description: Total volume removed from the well, prior to sampling
    * range: [Double](types/Double.md)
 * [samplerType](samplerType.md)  <sub>OPT</sub>
    * Description: Type of sampler used to collect the sample
    * range: [String](types/String.md)
 * [parentSampleID](parentSampleID.md)  <sub>OPT</sub>
    * Description: Parent sampleID of sample being processed
    * range: [String](types/String.md)
 * [lakeSampleDepth1](lakeSampleDepth1.md)  <sub>OPT</sub>
    * Description: Sample depth of a single lake sample collected below the surface; the sample depth of the upper sample for a composite lake sample collected below the surface
    * range: [Double](types/Double.md)
 * [lakeSampleDepth2](lakeSampleDepth2.md)  <sub>OPT</sub>
    * Description: Sample depth of the lower sample for a composite lake sample collected below the surface
    * range: [Double](types/Double.md)
 * [sdgSamplingProtocolVersion](sdgSamplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version of the dissolved gas protocol where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [asiSamplingProtocolVersion](asiSamplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version of the aquatic stable isotopes protocol where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [aquaticSiteType](aquaticSiteType.md)  <sub>OPT</sub>
    * Description: Type of aquatic site, includes lake, river or stream
    * range: [String](types/String.md)
 * [parentSampleCode](parentSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a parent sample
    * range: [String](types/String.md)
 * [fieldDataQF](fieldDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for field data
    * range: [String](types/String.md)
 * [samplingImpractical](samplingImpractical.md)  <sub>OPT</sub>
    * Description: Samples and/or measurements were not collected due to the indicated circumstance
    * range: [String](types/String.md)
 * [additionalCoordUncertainty](additionalCoordUncertainty.md)  <sub>OPT</sub>
    * Description: Additional uncertainty to be added to the coordinate uncertainty at all sites
    * range: [Double](types/Double.md)
    * inherited from: None
 * [amcSamplingProtocolVersion](amcSamplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version of the aquatic microbes protocol where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)
 * [swcSamplingProtocolVersion](swcSamplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version of the water chemistry protocol where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)

### Inherited from csd_pressureGaugeRelationship_pub:

 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
    * inherited from: None
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

### Inherited from gag_fieldData_pub:

 * [endStageHeight](endStageHeight.md)  <sub>OPT</sub>
    * Description: End stage (m)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [precipDescrip](precipDescrip.md)  <sub>OPT</sub>
    * Description: Qualitative description of precipitation levels
    * range: [String](types/String.md)
    * inherited from: None
 * [previousRain](previousRain.md)  <sub>OPT</sub>
    * Description: Previous Rain event within 48 hours (Yes/No)
    * range: [String](types/String.md)
    * inherited from: None
 * [waterColorDescrip](waterColorDescrip.md)  <sub>OPT</sub>
    * Description: Qualitative description of water color and clarity
    * range: [String](types/String.md)
 * [riparianPhenologyDescrip](riparianPhenologyDescrip.md)  <sub>OPT</sub>
    * Description: Qualitative description of riparian phenology status
    * range: [String](types/String.md)
    * inherited from: None
 * [icePresent](icePresent.md)  <sub>OPT</sub>
    * Description: Indication of the presence of ice
    * range: [String](types/String.md)
    * inherited from: None
 * [beaufortScaleWind](beaufortScaleWind.md)  <sub>OPT</sub>
    * Description: Qualitative description of wind conditions based on the beaufort scale
    * range: [String](types/String.md)
    * inherited from: None
 * [algaePresence](algaePresence.md)  <sub>OPT</sub>
    * Description: Presence of algae
    * range: [String](types/String.md)
    * inherited from: None
 * [leafLitterPresence](leafLitterPresence.md)  <sub>OPT</sub>
    * Description: Presence of leaf litter
    * range: [String](types/String.md)
    * inherited from: None
 * [macrophytePresence](macrophytePresence.md)  <sub>OPT</sub>
    * Description: Presence of macrophytes
    * range: [String](types/String.md)
    * inherited from: None
 * [nominalCloudCover](nominalCloudCover.md)  <sub>OPT</sub>
    * Description: Sky Condition, estimate of cloud cover percent
    * range: [String](types/String.md)
    * inherited from: None
 * [oilsPresence](oilsPresence.md)  <sub>OPT</sub>
    * Description: Presence of oils
    * range: [String](types/String.md)
    * inherited from: None
 * [pollenPresence](pollenPresence.md)  <sub>OPT</sub>
    * Description: Presence of pollen as film, foam, or deposit
    * range: [String](types/String.md)
    * inherited from: None
 * [trashPresent](trashPresent.md)  <sub>OPT</sub>
    * Description: Presence of trash
    * range: [String](types/String.md)
    * inherited from: None
 * [waterClarityDescrip](waterClarityDescrip.md)  <sub>OPT</sub>
    * Description: Qualitative description of water clarity
    * range: [String](types/String.md)
 * [woodyDebrisPresence](woodyDebrisPresence.md)  <sub>OPT</sub>
    * Description: Presence of woody debris
    * range: [String](types/String.md)
    * inherited from: None
 * [dscTempHydroCond](dscTempHydroCond.md)  <sub>OPT</sub>
    * Description: Type of temporary hydrologic condition present at the discharge transect
    * range: [String](types/String.md)
    * inherited from: None
 * [dscTempHydroCondLoc](dscTempHydroCondLoc.md)  <sub>OPT</sub>
    * Description: Location of the temporary hydrologic condition present at the discharge transect
    * range: [String](types/String.md)
    * inherited from: None
 * [gaugeTempHydroCond](gaugeTempHydroCond.md)  <sub>OPT</sub>
    * Description: Type of temporary hydrologic condition present at the staff gauge
    * range: [String](types/String.md)
    * inherited from: None
 * [gaugeTempHydroCondLoc](gaugeTempHydroCondLoc.md)  <sub>OPT</sub>
    * Description: Location of the temporary hydrologic condition present at the staff gauge
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
 * [altLatitude](altLatitude.md)  <sub>OPT</sub>
    * Description: Alternate Sampling Location coordinate - latitude
    * range: [Double](types/Double.md)
 * [collectedBy](collectedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who collected the sample or specimen
    * range: [String](types/String.md)
    * inherited from: None
 * [altCoordinateUncertainty](altCoordinateUncertainty.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given altLatitude and altLongitude describing the smallest circle containing the whole of the Location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
 * [altGeodeticDatum](altGeodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth for alternate location coordinate
    * range: [String](types/String.md)
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

### Inherited from vst_shrubgroup_pub:

 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
    * inherited from: None
 * [identificationReferences](identificationReferences.md)  <sub>OPT</sub>
    * Description: A list of sources (concatenated and semicolon separated) used to derive the specific taxon concept; including field guide editions, books, or versions of NEON keys used
    * range: [String](types/String.md)
    * inherited from: None
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
    * inherited from: None
 * [identificationQualifier](identificationQualifier.md)  <sub>OPT</sub>
    * Description: A standard term to express the determiner's doubts about the Identification
    * range: [String](types/String.md)
    * inherited from: None
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
    * inherited from: None
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
    * inherited from: None
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
 * [scientificName](scientificName.md)  <sub>OPT</sub>
    * Description: Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined
    * range: [String](types/String.md)
    * inherited from: None
 * [taxonRank](taxonRank.md)  <sub>OPT</sub>
    * Description: The lowest level taxonomic rank that can be determined for the individual or specimen
    * range: [String](types/String.md)
    * inherited from: None
 * [subplotID](subplotID.md)  <sub>OPT</sub>
    * Description: Identifier for the NEON subplot
    * range: [String](types/String.md)
    * inherited from: None
 * [canopyArea](canopyArea.md)  <sub>OPT</sub>
    * Description: Area of the group canopy
    * range: [Double](types/Double.md)
    * inherited from: None
 * [deadPercent](deadPercent.md)  <sub>OPT</sub>
    * Description: Percent of a given species, within a group, that is dead
    * range: [Double](types/Double.md)
    * inherited from: None
 * [groupID](groupID.md)  <sub>OPT</sub>
    * Description: Identifier for a group of individuals being measured
    * range: [String](types/String.md)
    * inherited from: None
 * [livePercent](livePercent.md)  <sub>OPT</sub>
    * Description: Percent of a given species, within a group, that is alive
    * range: [Double](types/Double.md)
    * inherited from: None
 * [meanHeight](meanHeight.md)  <sub>OPT</sub>
    * Description: The mean of multiple height measurements
    * range: [Double](types/Double.md)
    * inherited from: None
 * [nestedSubplotID](nestedSubplotID.md)  <sub>OPT</sub>
    * Description: Numeric identifier for nested subplot ID within a subplotID
    * range: [String](types/String.md)
    * inherited from: None
 * [volumePercent](volumePercent.md)  <sub>OPT</sub>
    * Description: Percent of the total volume of a group attributed to a particular species
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from waq_instantaneous_pub:

 * [specificConductance](specificConductance.md)  <sub>OPT</sub>
    * Description: Conductivity auto-corrected to 25 degrees C
    * range: [Double](types/Double.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
    * inherited from: None
 * [dissolvedOxygen](dissolvedOxygen.md)  <sub>OPT</sub>
    * Description: Dissolved Oxygen Concentration
    * range: [Double](types/Double.md)
 * [dissolvedOxygenSaturation](dissolvedOxygenSaturation.md)  <sub>OPT</sub>
    * Description: Dissolved Oxygen Percent Saturation
    * range: [Double](types/Double.md)
 * [pH](pH.md)  <sub>OPT</sub>
    * Description: Measurement of pH in sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlorophyll](chlorophyll.md)  <sub>OPT</sub>
    * Description: Chlorophyll a concentration in water
    * range: [Double](types/Double.md)
    * inherited from: None
 * [fDOM](fDOM.md)  <sub>OPT</sub>
    * Description: Fluorescent dissolved organic matter concentration as quinine sulfate equivalents
    * range: [Double](types/Double.md)
    * inherited from: None
 * [turbidity](turbidity.md)  <sub>OPT</sub>
    * Description: Turbidity of water as FNU
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sensorDepth](sensorDepth.md)  <sub>OPT</sub>
    * Description: Water depth of measurement
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sensorDepthValidCalQF](sensorDepthValidCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check of sensor depth detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [specificConductanceValidCalQF](specificConductanceValidCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check of specific conductance detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [buoyNAFlag](buoyNAFlag.md)  <sub>OPT</sub>
    * Description: Flag indicating that data could not be published due to an error on the buoy (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [chlorophyllAlphaQF](chlorophyllAlphaQF.md)  <sub>OPT</sub>
    * Description: Chlorophyll a quality assurance and quality control report for the alchlorophyll aa quality flag that indicates if one or more quality analysis failed for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [chlorophyllBetaQF](chlorophyllBetaQF.md)  <sub>OPT</sub>
    * Description: Chlorophyll a quality assurance and quality control report for the beta quality flag which indicates if one or more quality analysis could not be run for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [chlorophyllConsistQF](chlorophyllConsistQF.md)  <sub>OPT</sub>
    * Description: Chlorophyll a quality flag for the consistency test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [chlorophyllExpUncert](chlorophyllExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for chlorophyll a
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlorophyllFinalQF](chlorophyllFinalQF.md)  <sub>OPT</sub>
    * Description: Chlorophyll a final quality flag indicating whether a data product has passed or failed an overall assessment of its quality; detailed in ATBD (1=fail; 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [chlorophyllFinalQFSciRvw](chlorophyllFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Chlorophyll a final quality flag indicating whether a data product has failed a science review of its quality detailed in NEON.DOC.001113 (1=fail; 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [chlorophyllGapQF](chlorophyllGapQF.md)  <sub>OPT</sub>
    * Description: Chlorophyll a quality flag for the gap test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [chlorophyllNullQF](chlorophyllNullQF.md)  <sub>OPT</sub>
    * Description: Chlorophyll a quality flag for the null test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [chlorophyllPersistenceQF](chlorophyllPersistenceQF.md)  <sub>OPT</sub>
    * Description: Chlorophyll a quality flag for the persistence test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [chlorophyllRangeQF](chlorophyllRangeQF.md)  <sub>OPT</sub>
    * Description: Chlorophyll a quality flag for the range test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [chlorophyllSpikeQF](chlorophyllSpikeQF.md)  <sub>OPT</sub>
    * Description: Chlorophyll a quality flag for the spike test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [chlorophyllStepQF](chlorophyllStepQF.md)  <sub>OPT</sub>
    * Description: Chlorophyll a quality flag for the step test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [chlorophyllValidCalQF](chlorophyllValidCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check of chlorophyll a detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenAlphaQF](dissolvedOxygenAlphaQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen quality assurance and quality control report for the alpha quality flag that indicates if one or more quality analysis failed for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenBetaQF](dissolvedOxygenBetaQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen quality assurance and quality control report for the beta quality flag which indicates if one or more quality analysis could not be run for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenConsistQF](dissolvedOxygenConsistQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen quality flag for the consistency test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenExpUncert](dissolvedOxygenExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for dissolved oxygen
    * range: [Double](types/Double.md)
    * inherited from: None
 * [dissolvedOxygenFinalQF](dissolvedOxygenFinalQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen final quality flag indicating whether a data product has passed or failed an overall assessment of its quality; detailed in ATBD (1=fail; 0=pass)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenFinalQFSciRvw](dissolvedOxygenFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen final quality flag indicating whether a data product has failed a science review of its quality detailed in NEON.DOC.001113 (1=fail; 0=pass/not-reviewed)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenGapQF](dissolvedOxygenGapQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen quality flag for the gap test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenNullQF](dissolvedOxygenNullQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen quality flag for the null test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenPersistenceQF](dissolvedOxygenPersistenceQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen quality flag for the persistence test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenRangeQF](dissolvedOxygenRangeQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen quality flag for the range test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenSatAlphaQF](dissolvedOxygenSatAlphaQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen saturation quality assurance and quality control report for the alpha quality flag that indicates if one or more quality analysis failed for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenSatBetaQF](dissolvedOxygenSatBetaQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen saturation quality assurance and quality control report for the beta quality flag which indicates if one or more quality analysis could not be run for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenSatConsistQF](dissolvedOxygenSatConsistQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen saturation quality flag for the consistency test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenSatExpUncert](dissolvedOxygenSatExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for dissolved oxygen saturation
    * range: [Double](types/Double.md)
    * inherited from: None
 * [dissolvedOxygenSatFinalQF](dissolvedOxygenSatFinalQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen saturation final quality flag indicating whether a data product has passed or failed an overall assessment of its quality; detailed in ATBD (1=fail; 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [dissolvedOxygenSatFinalQFSciRvw](dissolvedOxygenSatFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen saturation final quality flag indicating whether a data product has failed a science review of its quality detailed in NEON.DOC.001113 (1=fail; 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [dissolvedOxygenSatGapQF](dissolvedOxygenSatGapQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen saturation quality flag for the gap test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenSatNullQF](dissolvedOxygenSatNullQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen saturation quality flag for the null test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenSatPersistQF](dissolvedOxygenSatPersistQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen saturation quality flag for the persistence test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenSatRangeQF](dissolvedOxygenSatRangeQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen saturation quality flag for the range test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenSatSpikeQF](dissolvedOxygenSatSpikeQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen saturation quality flag for the spike test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenSatStepQF](dissolvedOxygenSatStepQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen saturation quality flag for the step test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenSatValidCalQF](dissolvedOxygenSatValidCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check of dissolved oxygen saturation detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenSpikeQF](dissolvedOxygenSpikeQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen quality flag for the spike test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenStepQF](dissolvedOxygenStepQF.md)  <sub>OPT</sub>
    * Description: Dissolved oxygen quality flag for the step test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenValidCalQF](dissolvedOxygenValidCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check of dissolved oxygen detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [fDOMAbsQF](fDOMAbsQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating that fDOM absorbance corrections were applied = 0; unable to be applied = 1; absorbance values were high = 2; calculated correction factor was 1 (i.e. no absorbance correction was made) = 3
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [fDOMAlphaQF](fDOMAlphaQF.md)  <sub>OPT</sub>
    * Description: fDOM quality assurance and quality control report for the alfDOMa quality flag that indicates if one or more quality analysis failed for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [fDOMBetaQF](fDOMBetaQF.md)  <sub>OPT</sub>
    * Description: fDOM quality assurance and quality control report for the beta quality flag which indicates if one or more quality analysis could not be run for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [fDOMConsistQF](fDOMConsistQF.md)  <sub>OPT</sub>
    * Description: fDOM quality flag for the consistency test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [fDOMExpUncert](fDOMExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for fDOM
    * range: [Double](types/Double.md)
    * inherited from: None
 * [fDOMFinalQF](fDOMFinalQF.md)  <sub>OPT</sub>
    * Description: fDOM final quality flag indicating whether a data product has passed or failed an overall assessment of its quality; detailed in ATBD (1=fail; 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [fDOMFinalQFSciRvw](fDOMFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: fDOM final quality flag indicating whether a data product has failed a science review of its quality detailed in NEON.DOC.001113 (1=fail; 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [fDOMGapQF](fDOMGapQF.md)  <sub>OPT</sub>
    * Description: fDOM quality flag for the gap test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [fDOMNullQF](fDOMNullQF.md)  <sub>OPT</sub>
    * Description: fDOM quality flag for the null test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [fDOMPersistenceQF](fDOMPersistenceQF.md)  <sub>OPT</sub>
    * Description: fDOM quality flag for the persistence test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [fDOMRangeQF](fDOMRangeQF.md)  <sub>OPT</sub>
    * Description: fDOM quality flag for the range test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [fDOMSpikeQF](fDOMSpikeQF.md)  <sub>OPT</sub>
    * Description: fDOM quality flag for the spike test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [fDOMStepQF](fDOMStepQF.md)  <sub>OPT</sub>
    * Description: fDOM quality flag for the step test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [fDOMTempQF](fDOMTempQF.md)  <sub>OPT</sub>
    * Description: Quality flag indicating that fDOM temperature corrections were applied = 0 or unable to be applied = 1
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [fDOMValidCalQF](fDOMValidCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check of fDOM detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [pHAlphaQF](pHAlphaQF.md)  <sub>OPT</sub>
    * Description: pH quality assurance and quality control report for the alpha quality flag that indicates if one or more quality analysis failed for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [pHBetaQF](pHBetaQF.md)  <sub>OPT</sub>
    * Description: pH quality assurance and quality control report for the beta quality flag which indicates if one or more quality analysis could not be run for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [pHConsistQF](pHConsistQF.md)  <sub>OPT</sub>
    * Description: pH quality flag for the consistency test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [pHExpUncert](pHExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for pH
    * range: [Double](types/Double.md)
    * inherited from: None
 * [pHFinalQF](pHFinalQF.md)  <sub>OPT</sub>
    * Description: pH final quality flag indicating whether a data product has passed or failed an overall assessment of its quality; detailed in ATBD (1=fail; 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [pHFinalQFSciRvw](pHFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: pH final quality flag indicating whether a data product has failed a science review of its quality detailed in NEON.DOC.001113 (1=fail; 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [pHGapQF](pHGapQF.md)  <sub>OPT</sub>
    * Description: pH quality flag for the gap test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [pHNullQF](pHNullQF.md)  <sub>OPT</sub>
    * Description: pH quality flag for the null test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [pHPersistenceQF](pHPersistenceQF.md)  <sub>OPT</sub>
    * Description: pH quality flag for the persistence test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [pHRangeQF](pHRangeQF.md)  <sub>OPT</sub>
    * Description: pH quality flag for the range test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [pHSpikeQF](pHSpikeQF.md)  <sub>OPT</sub>
    * Description: pH quality flag for the spike test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [pHStepQF](pHStepQF.md)  <sub>OPT</sub>
    * Description: pH quality flag for the step test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [pHValidCalQF](pHValidCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check of pH detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [sensorDepthExpUncert](sensorDepthExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for sensor depth
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sensorDepthFinalQFSciRvw](sensorDepthFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Sensor depth quality flag indicating whether a data product has failed a science review of its quality, detailed in NEON.DOC.001113 (1=fail, 0=pass/not-reviewed)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [specificCondFinalQFSciRvw](specificCondFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Specific conductance final quality flag indicating whether a data product has failed a science review of its quality detailed in NEON.DOC.001113 (1=fail; 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [specificConductanceAlphaQF](specificConductanceAlphaQF.md)  <sub>OPT</sub>
    * Description: Specific conductance quality assurance and quality control report for the alpha quality flag that indicates if one or more quality analysis failed for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [specificConductanceBetaQF](specificConductanceBetaQF.md)  <sub>OPT</sub>
    * Description: Specific conductance quality assurance and quality control report for the beta quality flag which indicates if one or more quality analysis could not be run for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [specificConductanceConsistQF](specificConductanceConsistQF.md)  <sub>OPT</sub>
    * Description: Specific conductance quality flag for the consistency test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [specificConductanceExpUncert](specificConductanceExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for specific conductance
    * range: [Double](types/Double.md)
    * inherited from: None
 * [specificCondFinalQF](specificCondFinalQF.md)  <sub>OPT</sub>
    * Description: Specific conductance final quality flag indicating whether a data product has passed or failed an overall assessment of its quality; detailed in ATBD (1=fail; 0=pass)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [specificConductanceGapQF](specificConductanceGapQF.md)  <sub>OPT</sub>
    * Description: Specific conductance quality flag for the gap test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [specificConductanceNullQF](specificConductanceNullQF.md)  <sub>OPT</sub>
    * Description: Specific conductance quality flag for the null test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [specificConductancePersistQF](specificConductancePersistQF.md)  <sub>OPT</sub>
    * Description: Specific conductance quality flag for the persistence test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [specificConductanceRangeQF](specificConductanceRangeQF.md)  <sub>OPT</sub>
    * Description: Specific conductance quality flag for the range test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [specificConductanceSpikeQF](specificConductanceSpikeQF.md)  <sub>OPT</sub>
    * Description: Specific conductance quality flag for the spike test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e., could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [specificConductanceStepQF](specificConductanceStepQF.md)  <sub>OPT</sub>
    * Description: Specific conductance quality flag for the step test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [turbidityAlphaQF](turbidityAlphaQF.md)  <sub>OPT</sub>
    * Description: Turbidity quality assurance and quality control report for the alturbiditya quality flag that indicates if one or more quality analysis failed for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [turbidityBetaQF](turbidityBetaQF.md)  <sub>OPT</sub>
    * Description: Turbidity quality assurance and quality control report for the beta quality flag which indicates if one or more quality analysis could not be run for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [turbidityConsistQF](turbidityConsistQF.md)  <sub>OPT</sub>
    * Description: Turbidity quality flag for the consistency test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [turbidityExpUncert](turbidityExpUncert.md)  <sub>OPT</sub>
    * Description: Expanded uncertainty for turbidity
    * range: [Double](types/Double.md)
    * inherited from: None
 * [turbidityFinalQF](turbidityFinalQF.md)  <sub>OPT</sub>
    * Description: Turbidity final quality flag indicating whether a data product has passed or failed an overall assessment of its quality; detailed in ATBD (1=fail; 0=pass)
    * range: [String](types/String.md)
    * inherited from: None
 * [turbidityFinalQFSciRvw](turbidityFinalQFSciRvw.md)  <sub>OPT</sub>
    * Description: Turbidity final quality flag indicating whether a data product has failed a science review of its quality detailed in NEON.DOC.001113 (1=fail; 0=pass/not-reviewed)
    * range: [String](types/String.md)
    * inherited from: None
 * [turbidityGapQF](turbidityGapQF.md)  <sub>OPT</sub>
    * Description: Turbidity quality flag for the gap test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [turbidityNullQF](turbidityNullQF.md)  <sub>OPT</sub>
    * Description: Turbidity quality flag for the null test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [turbidityPersistenceQF](turbidityPersistenceQF.md)  <sub>OPT</sub>
    * Description: Turbidity quality flag for the persistence test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [turbidityRangeQF](turbidityRangeQF.md)  <sub>OPT</sub>
    * Description: Turbidity quality flag for the range test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [turbiditySpikeQF](turbiditySpikeQF.md)  <sub>OPT</sub>
    * Description: Turbidity quality flag for the spike test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [turbidityStepQF](turbidityStepQF.md)  <sub>OPT</sub>
    * Description: Turbidity quality flag for the step test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [turbidityValidCalQF](turbidityValidCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the valid calibration check of turbidity detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [sensorDepthAlphaQF](sensorDepthAlphaQF.md)  <sub>OPT</sub>
    * Description: Water depth of measurement quality assurance and quality control report for the alpha quality flag that indicates if one or more quality analysis failed for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [sensorDepthBetaQF](sensorDepthBetaQF.md)  <sub>OPT</sub>
    * Description: Water depth of measurement quality assurance and quality control report for the beta quality flag which indicates if one or more quality analysis could not be run for a datum detailed in NEON.DOC.001113 (1=fail 0=pass -1=NA (i.e could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [sensorDepthConsistQF](sensorDepthConsistQF.md)  <sub>OPT</sub>
    * Description: Water depth of measurement quality flag for the consistency test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [sensorDepthGapQF](sensorDepthGapQF.md)  <sub>OPT</sub>
    * Description: Water depth of measurement quality flag for the gap test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [sensorDepthNullQF](sensorDepthNullQF.md)  <sub>OPT</sub>
    * Description: Water depth of measurement quality flag for the null test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [sensorDepthPersistQF](sensorDepthPersistQF.md)  <sub>OPT</sub>
    * Description: Water depth of measurement quality flag for the persistence test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [sensorDepthRangeQF](sensorDepthRangeQF.md)  <sub>OPT</sub>
    * Description: Water depth of measurement quality flag for the range test detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [spectrumCount](spectrumCount.md)  <sub>OPT</sub>
    * Description: The number of absorbance spectra (AKA SUNA light frames) that were averaged to correct the fDOM and or chla data. Up to 50 light frames will be averaged
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [rawCalibratedfDOM](rawCalibratedfDOM.md)  <sub>OPT</sub>
    * Description: Calibrated fluorescent dissolved organic matter concentration as quinine sulfate equivalents without temperature or absorbance corrections
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlorophyllSuspectCalQF](chlorophyllSuspectCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the suspect calibration check of chlorophyll a detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissolvedOxygenSuspectCalQF](dissolvedOxygenSuspectCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the suspect calibration check of dissolved oxygen detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [dissOxygenSatSuspectCalQF](dissOxygenSatSuspectCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the suspect calibration check of dissolved oxygen saturation detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [fDOMSuspectCalQF](fDOMSuspectCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the suspect calibration check of fDOM detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [pHSuspectCalQF](pHSuspectCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the suspect calibration check of pH detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [sensorDepthSuspectCalQF](sensorDepthSuspectCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the suspect calibration check of sensor depth detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [specificCondSuspectCalQF](specificCondSuspectCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the suspect calibration check of specific conductance detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [turbiditySuspectCalQF](turbiditySuspectCalQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the suspect calibration check of turbidity detailed in NEON.DOC.011081 (1=fail 0=pass -1=NA (i.e. could not be run))
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [sensorDepthFinalQF](sensorDepthFinalQF.md)  <sub>OPT</sub>
    * Description: Water depth final quality flag indicating whether a data product has passed or failed an overall assessment of its quality; detailed in ATBD (1=fail; 0=pass)
    * range: [Integer](types/Integer.md)
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
    * inherited from: None
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
| **Mappings:** | | neon:gsi_fieldSuperParent_pub |
| **In Subsets:** | | DP1.20276.001 |

