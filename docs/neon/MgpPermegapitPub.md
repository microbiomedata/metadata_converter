
# Type: mgp_permegapit_pub




URI: [neon:MgpPermegapitPub](https://data.neonscience.org/MgpPermegapitPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


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

### Inherited from mam_perplotnight_pub:

 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)

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

### Inherited from mgp_permegapit_in:

 * [recordedByB](recordedByB.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who recorded the data
    * range: [String](types/String.md)
 * [recordedByC](recordedByC.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who recorded the data
    * range: [String](types/String.md)
 * [recordedByD](recordedByD.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who recorded the data
    * range: [String](types/String.md)
 * [recordedByE](recordedByE.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who recorded the data
    * range: [String](types/String.md)
 * [rootsCollectedByC](rootsCollectedByC.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who collected the root sample(s) or specimen(s)
    * range: [String](types/String.md)
    * inherited from: None
 * [rootsCollectedByD](rootsCollectedByD.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who collected the root sample(s) or specimen(s)
    * range: [String](types/String.md)
    * inherited from: None
 * [safetyPersonnelA](safetyPersonnelA.md)  <sub>OPT</sub>
    * Description: An identifier for one of the safety specialists present during part or all of the sample or specimen collection
    * range: [String](types/String.md)
    * inherited from: None
 * [safetyPersonnelB](safetyPersonnelB.md)  <sub>OPT</sub>
    * Description: An identifier for one of the safety specialists present during part or all of the sample or specimen collection
    * range: [String](types/String.md)
    * inherited from: None
 * [safetyPersonnelC](safetyPersonnelC.md)  <sub>OPT</sub>
    * Description: An identifier for one of the safety specialists present during part or all of the sample or specimen collection
    * range: [String](types/String.md)
    * inherited from: None
 * [fccConstructionSupervisorA](fccConstructionSupervisorA.md)  <sub>OPT</sub>
    * Description: An identifier for one of the FCC Construction Supervisors present during part or all of the sample or specimen collection
    * range: [String](types/String.md)
    * inherited from: None
 * [fccConstructionSupervisorB](fccConstructionSupervisorB.md)  <sub>OPT</sub>
    * Description: An identifier for one of the FCC Construction Supervisors present during part or all of the sample or specimen collection
    * range: [String](types/String.md)
    * inherited from: None
 * [fccConstructionSupervisorC](fccConstructionSupervisorC.md)  <sub>OPT</sub>
    * Description: An identifier for one of the FCC Construction Supervisors present during part or all of the sample or specimen collection
    * range: [String](types/String.md)
    * inherited from: None
 * [fccConstructionContractor](fccConstructionContractor.md)  <sub>OPT</sub>
    * Description: An identifier for the Construction Contractor that excavated TIS soil pit
    * range: [String](types/String.md)
    * inherited from: None
 * [soilProfileDescriberB](soilProfileDescriberB.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who described the soil profile
    * range: [String](types/String.md)
 * [soilProfileDescriberC](soilProfileDescriberC.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who described the soil profile
    * range: [String](types/String.md)
 * [soilProfileDescriberD](soilProfileDescriberD.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who described the soil profile
    * range: [String](types/String.md)
 * [soilProfileDescriberE](soilProfileDescriberE.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who described the soil profile
    * range: [String](types/String.md)
 * [soilProfileDescriberF](soilProfileDescriberF.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who described the soil profile
    * range: [String](types/String.md)

### Inherited from mpr_perrootsample_pub:

 * [pitNamedLocation](pitNamedLocation.md)  <sub>OPT</sub>
    * Description: Named location identifier for the soil pit
    * range: [String](types/String.md)
 * [rootStatus](rootStatus.md)  <sub>OPT</sub>
    * Description: The state of an individual or sample
    * range: [String](types/String.md)
    * inherited from: None
 * [depthIncrementID](depthIncrementID.md)  <sub>OPT</sub>
    * Description: An identifier for the depth increment within a pit profile
    * range: [String](types/String.md)
    * inherited from: None
 * [rootDryMass](rootDryMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of root sample or subsample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [incrementRootBiomass](incrementRootBiomass.md)  <sub>OPT</sub>
    * Description: Root biomass per horizontal surface area per depth increment
    * range: [Double](types/Double.md)
    * inherited from: None
 * [incrementRootDensity](incrementRootDensity.md)  <sub>OPT</sub>
    * Description: Root biomass per collected soil volume per depth increment
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from spc_particlesize_pub:

 * [nrcsDescriptionID](nrcsDescriptionID.md)  <sub>OPT</sub>
    * Description: NRCS identifier assigned to the soil profile description
    * range: [String](types/String.md)
 * [horizonID](horizonID.md)  <sub>OPT</sub>
    * Description: An identifier for the soil horizon
    * range: [String](types/String.md)
    * inherited from: None
 * [horizonName](horizonName.md)  <sub>OPT</sub>
    * Description: Soil horizon name
    * range: [String](types/String.md)
    * inherited from: None
 * [biogeoIDnrcs](biogeoIDnrcs.md)  <sub>OPT</sub>
    * Description: Identifier used by NRCS for the biogeochemistry sample
    * range: [String](types/String.md)
    * inherited from: None
 * [biogeoSampleType](biogeoSampleType.md)  <sub>OPT</sub>
    * Description: Type of biogeochemistry sample
    * range: [String](types/String.md)
    * inherited from: None
 * [biogeoTopDepth](biogeoTopDepth.md)  <sub>OPT</sub>
    * Description: Top depth of the biogeochemistry sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoBottomDepth](biogeoBottomDepth.md)  <sub>OPT</sub>
    * Description: Bottom depth of the biogeochemistry sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoCenterDepth](biogeoCenterDepth.md)  <sub>OPT</sub>
    * Description: Depth of the center of the biogeochemistry sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [coarseFrag2To5](coarseFrag2To5.md)  <sub>OPT</sub>
    * Description: Coarse fragment (2-5 mm) content of the <20 mm size fraction of the biogeochemistry soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [coarseFrag5To20](coarseFrag5To20.md)  <sub>OPT</sub>
    * Description: Coarse fragment (5-20 mm) content of the <20 mm size fraction of the biogeochemistry soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoCode](biogeoCode.md)  <sub>OPT</sub>
    * Description: Barcode the biogeochemistry sample
    * range: [String](types/String.md)
    * inherited from: None
 * [carbonateClay](carbonateClay.md)  <sub>OPT</sub>
    * Description: Carbonate clay (<0.002 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [clayFineContent](clayFineContent.md)  <sub>OPT</sub>
    * Description: Fine clay (<0.0002 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [clayTotal](clayTotal.md)  <sub>OPT</sub>
    * Description: Total clay (<0.002 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [horizonCode](horizonCode.md)  <sub>OPT</sub>
    * Description: Barcode of the horizon
    * range: [String](types/String.md)
    * inherited from: None
 * [sandCoarseContent](sandCoarseContent.md)  <sub>OPT</sub>
    * Description: Coarse sand (0.5-1 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sandFineContent](sandFineContent.md)  <sub>OPT</sub>
    * Description: Fine sand (0.105-0.25 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sandMediumContent](sandMediumContent.md)  <sub>OPT</sub>
    * Description: Medium sand (0.25-0.5 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sandTotal](sandTotal.md)  <sub>OPT</sub>
    * Description: Total sand (0.047-2 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sandVeryFineContent](sandVeryFineContent.md)  <sub>OPT</sub>
    * Description: Very fine sand (0.047-0.105 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [siltCoarseContent](siltCoarseContent.md)  <sub>OPT</sub>
    * Description: Coarse silt (0.02-0.047 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [siltFineContent](siltFineContent.md)  <sub>OPT</sub>
    * Description: Fine silt (0.002-0.02 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [siltTotal](siltTotal.md)  <sub>OPT</sub>
    * Description: Total silt (0.002-0.047 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [particleSizeDistProcessedDate](particleSizeDistProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for particle size distribution analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [particleSizeDistMethod](particleSizeDistMethod.md)  <sub>OPT</sub>
    * Description: Methods used for particle size distribution analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [particleSizeDistMethodPub](particleSizeDistMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for particle size distribution analysis
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from spc_perhorizon_pub:

 * [pitID](pitID.md)  <sub>OPT</sub>
    * Description: An identifier for the soil pit
    * range: [String](types/String.md)
 * [horizonTopDepth](horizonTopDepth.md)  <sub>OPT</sub>
    * Description: Depth below the soil surface of the top of a soil horizon
    * range: [Double](types/Double.md)
    * inherited from: None
 * [horizonBottomDepth](horizonBottomDepth.md)  <sub>OPT</sub>
    * Description: Depth below the soil surface of the bottom of a soil horizon
    * range: [Double](types/Double.md)
    * inherited from: None
 * [pitCode](pitCode.md)  <sub>OPT</sub>
    * Description: Barcode of the pit
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from spc_perplot_pub:

 * [pitDepth](pitDepth.md)  <sub>OPT</sub>
    * Description: Depth of the bottom of the soil pit below the soil surface
    * range: [Double](types/Double.md)
 * [recordedByA](recordedByA.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who recorded the data
    * range: [String](types/String.md)
 * [soilProfileDescriberA](soilProfileDescriberA.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who described the soil profile
    * range: [String](types/String.md)
 * [soilProfileDescriberInst](soilProfileDescriberInst.md)  <sub>OPT</sub>
    * Description: Institution of the person/people that performed the soil profile description
    * range: [String](types/String.md)
 * [soilSeries](soilSeries.md)  <sub>OPT</sub>
    * Description: Soil taxonomy at the series level
    * range: [String](types/String.md)
 * [soilFamily](soilFamily.md)  <sub>OPT</sub>
    * Description: Soil taxonomy at the family level
    * range: [String](types/String.md)
 * [soilSubgroup](soilSubgroup.md)  <sub>OPT</sub>
    * Description: Soil taxonomy at the subgroup level
    * range: [String](types/String.md)
 * [soilGreatGroup](soilGreatGroup.md)  <sub>OPT</sub>
    * Description: Soil taxonomy at the great group level
    * range: [String](types/String.md)
 * [soilSuborder](soilSuborder.md)  <sub>OPT</sub>
    * Description: Soil taxonomy at the suborder level
    * range: [String](types/String.md)
 * [soilOrder](soilOrder.md)  <sub>OPT</sub>
    * Description: Soil taxonomy at the order level
    * range: [String](types/String.md)
 * [referenceCorner](referenceCorner.md)  <sub>OPT</sub>
    * Description: Reference corner from which distance and compass bearing were measured
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleBearing](sampleBearing.md)  <sub>OPT</sub>
    * Description: Compass bearing of the sample location from a plot reference corner
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sampleDistance](sampleDistance.md)  <sub>OPT</sub>
    * Description: Distance of the sample location from a plot reference corner
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sampleRelativeLocation](sampleRelativeLocation.md)  <sub>OPT</sub>
    * Description: Relative position of a sample location
    * range: [String](types/String.md)
    * inherited from: None
 * [soilSamplingMethod](soilSamplingMethod.md)  <sub>OPT</sub>
    * Description: The methodology used for collecting soil at a plot (pit or core)
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
    * inherited from: None
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
| **Mappings:** | | neon:mgp_permegapit_pub |
| **In Subsets:** | | DP1.00096.001 |

