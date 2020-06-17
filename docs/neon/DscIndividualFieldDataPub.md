
# Type: dsc_individualFieldData_pub




URI: [neon:DscIndividualFieldDataPub](https://data.neonscience.org/DscIndividualFieldDataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [averageVelocity](averageVelocity.md)  <sub>OPT</sub>
    * Description: Mean velocity from all measured points
    * range: [Double](types/Double.md)
 * [bedVelocity](bedVelocity.md)  <sub>OPT</sub>
    * Description: Velocity of water at the bed
    * range: [Double](types/Double.md)
 * [edgeFactor](edgeFactor.md)  <sub>OPT</sub>
    * Description: Roughness factor used only for right angled cross sections
    * range: [String](types/String.md)
 * [fourFifthDepthVelocity](fourFifthDepthVelocity.md)  <sub>OPT</sub>
    * Description: Velocity of water at 80 percent of the water depth from the bed
    * range: [Double](types/Double.md)
 * [lowVelocityQF](lowVelocityQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for reported velocity below the instrument detection limit
    * range: [Integer](types/Integer.md)
 * [oneFifthDepthVelocity](oneFifthDepthVelocity.md)  <sub>OPT</sub>
    * Description: Velocity of water at 20 percent water depth from the bed
    * range: [Double](types/Double.md)
 * [sectionArea](sectionArea.md)  <sub>OPT</sub>
    * Description: Depth times width of the transect section
    * range: [Double](types/Double.md)
 * [sectionFlow](sectionFlow.md)  <sub>OPT</sub>
    * Description: Calculated flow of water for a section
    * range: [Double](types/Double.md)
 * [stationNumber](stationNumber.md)  <sub>OPT</sub>
    * Description: Numeric identified for station number
    * range: [Integer](types/Integer.md)
 * [streamProfilingMethod](streamProfilingMethod.md)  <sub>OPT</sub>
    * Description: Zero; one; two; three; five; or six point (velocity method - USGS and ISO)
    * range: [String](types/String.md)
 * [surfaceVelocity](surfaceVelocity.md)  <sub>OPT</sub>
    * Description: Velocity of water at the surface
    * range: [Double](types/Double.md)
 * [tapeDistance](tapeDistance.md)  <sub>OPT</sub>
    * Description: Distance along a tape where the point measurement of velocity and depth were taken for a transect
    * range: [Double](types/Double.md)
 * [threeFifthDepthVelocity](threeFifthDepthVelocity.md)  <sub>OPT</sub>
    * Description: Velocity of water at 60 percent of the water depth from the bed
    * range: [Double](types/Double.md)
 * [twoFifthDepthVelocity](twoFifthDepthVelocity.md)  <sub>OPT</sub>
    * Description: Velocity of water at 40 percent of the water depth from the bed
    * range: [Double](types/Double.md)

### Inherited from bat_pointcollection_pub:

 * [waterDepth](waterDepth.md)  <sub>OPT</sub>
    * Description: Depth of water
    * range: [Double](types/Double.md)
 * [substrate](substrate.md)  <sub>OPT</sub>
    * Description: Organic or inorganic surface material at the location
    * range: [String](types/String.md)
    * inherited from: None
 * [gpsDatafile](gpsDatafile.md)  <sub>OPT</sub>
    * Description: Name assigned to GPS file
    * range: [String](types/String.md)
    * inherited from: None
 * [bathymetryDataType](bathymetryDataType.md)  <sub>OPT</sub>
    * Description: Type of bathymetry metadata collected
    * range: [String](types/String.md)
    * inherited from: None
 * [gpsAntennaHeight](gpsAntennaHeight.md)  <sub>OPT</sub>
    * Description: Height of the GPS antenna above the GPS unit
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gpsUsed](gpsUsed.md)  <sub>OPT</sub>
    * Description: GPS unit used to collect the associated latitude and longitude
    * range: [String](types/String.md)
    * inherited from: None
 * [plantsPresent](plantsPresent.md)  <sub>OPT</sub>
    * Description: Indicator of plant presence or absence at the groundtruthing point
    * range: [String](types/String.md)
    * inherited from: None
 * [pointCollectionDate](pointCollectionDate.md)  <sub>OPT</sub>
    * Description: Date and time associated with a point collection
    * range: [Time](types/Time.md)
    * inherited from: None
 * [waypoint](waypoint.md)  <sub>OPT</sub>
    * Description: Location information for a point of interest
    * range: [String](types/String.md)
    * inherited from: None
 * [waypointDescription](waypointDescription.md)  <sub>OPT</sub>
    * Description: Descriptor for the waypoint
    * range: [String](types/String.md)
    * inherited from: None
 * [gpsAccuracy](gpsAccuracy.md)  <sub>OPT</sub>
    * Description: Position accuracy displayed on the gps unit in meters
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gpsAccuracyUnits](gpsAccuracyUnits.md)  <sub>OPT</sub>
    * Description: Unit of measure used to record gps accuracy
    * range: [String](types/String.md)
    * inherited from: None
 * [gpsAccuracyValue](gpsAccuracyValue.md)  <sub>OPT</sub>
    * Description: Position accuracy displayed on the gps unit
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
    * inherited from: None
 * [decimalLongitude](decimalLongitude.md)  <sub>OPT</sub>
    * Description: The geographic longitude (in decimal degrees, WGS84) of the geographic center of the reference area
    * range: [Double](types/Double.md)
    * inherited from: None
 * [geodeticDatum](geodeticDatum.md)  <sub>OPT</sub>
    * Description: Model used to measure horizontal position on the earth
    * range: [String](types/String.md)
    * inherited from: None
 * [coordinateUncertainty](coordinateUncertainty.md)  <sub>OPT</sub>
    * Description: The horizontal distance (in meters) from the given decimalLatitude and decimalLongitude describing the smallest circle containing the whole of the Location. Zero is not a valid value for this term
    * range: [Double](types/Double.md)
    * inherited from: None
 * [elevation](elevation.md)  <sub>OPT</sub>
    * Description: Elevation (in meters) above sea level
    * range: [Double](types/Double.md)
    * inherited from: None
 * [elevationUncertainty](elevationUncertainty.md)  <sub>OPT</sub>
    * Description: Uncertainty in elevation values (in meters)
    * range: [Double](types/Double.md)
    * inherited from: None
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

### Inherited from sbd_conductivityFieldData_pub:

 * [fullRangeSpCondLinear](fullRangeSpCondLinear.md)  <sub>OPT</sub>
    * Description: Specific conductance calculated using linear method and fullRangeHobo
    * range: [Double](types/Double.md)
    * inherited from: None
 * [fullRangeSpCondNonlinear](fullRangeSpCondNonlinear.md)  <sub>OPT</sub>
    * Description: Specific conductance calculated using non-linear method and fullRangeHobo
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lowRangeSpCondLinear](lowRangeSpCondLinear.md)  <sub>OPT</sub>
    * Description: Specific conductance calculated using linear method and lowRangeHobo
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lowRangeSpCondNonlinear](lowRangeSpCondNonlinear.md)  <sub>OPT</sub>
    * Description: Specific conductance calculated using non-linear method and lowRangeHobo
    * range: [Double](types/Double.md)
    * inherited from: None
 * [recorduid](recorduid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the parent and associated child records
    * range: [String](types/String.md)
 * [dateTimeLogger](dateTimeLogger.md)  <sub>OPT</sub>
    * Description: Local date and time returned by a field data logger
    * range: [Time](types/Time.md)
    * inherited from: None
 * [fullRangeHobo](fullRangeHobo.md)  <sub>OPT</sub>
    * Description: Conductivity from a hobo logger for the full range
    * range: [Double](types/Double.md)
    * inherited from: None
 * [hoboSampleCode](hoboSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of the HOBO conductivity logger file
    * range: [String](types/String.md)
    * inherited from: None
 * [hoboSampleID](hoboSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the HOBO conductivity logger file
    * range: [String](types/String.md)
    * inherited from: None
 * [loggerDataQF](loggerDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for conductiivty logger data
    * range: [String](types/String.md)
    * inherited from: None
 * [lowRangeHobo](lowRangeHobo.md)  <sub>OPT</sub>
    * Description: Conductivity returned from a hobo logger for the low range
    * range: [Double](types/Double.md)
    * inherited from: None
 * [measurementNumber](measurementNumber.md)  <sub>OPT</sub>
    * Description: The number of the measurement in a time series
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from waq_instantaneous_pub:

 * [specificConductance](specificConductance.md)  <sub>OPT</sub>
    * Description: Conductivity auto-corrected to 25 degrees C
    * range: [Double](types/Double.md)
    * inherited from: None
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
    * inherited from: None
 * [dissolvedOxygenSaturation](dissolvedOxygenSaturation.md)  <sub>OPT</sub>
    * Description: Dissolved Oxygen Percent Saturation
    * range: [Double](types/Double.md)
    * inherited from: None
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
    * inherited from: None
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
| **Mappings:** | | neon:dsc_individualFieldData_pub |

