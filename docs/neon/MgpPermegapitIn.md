
# Type: mgp_permegapit_in




URI: [neon:MgpPermegapitIn](https://data.neonscience.org/MgpPermegapitIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [fccConstructionContractor](fccConstructionContractor.md)  <sub>OPT</sub>
    * Description: An identifier for the Construction Contractor that excavated TIS soil pit
    * range: [String](types/String.md)
 * [fccConstructionSupervisorA](fccConstructionSupervisorA.md)  <sub>OPT</sub>
    * Description: An identifier for one of the FCC Construction Supervisors present during part or all of the sample or specimen collection
    * range: [String](types/String.md)
 * [fccConstructionSupervisorB](fccConstructionSupervisorB.md)  <sub>OPT</sub>
    * Description: An identifier for one of the FCC Construction Supervisors present during part or all of the sample or specimen collection
    * range: [String](types/String.md)
 * [fccConstructionSupervisorC](fccConstructionSupervisorC.md)  <sub>OPT</sub>
    * Description: An identifier for one of the FCC Construction Supervisors present during part or all of the sample or specimen collection
    * range: [String](types/String.md)
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
 * [rootsCollectedByD](rootsCollectedByD.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who collected the root sample(s) or specimen(s)
    * range: [String](types/String.md)
 * [safetyPersonnelA](safetyPersonnelA.md)  <sub>OPT</sub>
    * Description: An identifier for one of the safety specialists present during part or all of the sample or specimen collection
    * range: [String](types/String.md)
 * [safetyPersonnelB](safetyPersonnelB.md)  <sub>OPT</sub>
    * Description: An identifier for one of the safety specialists present during part or all of the sample or specimen collection
    * range: [String](types/String.md)
 * [safetyPersonnelC](safetyPersonnelC.md)  <sub>OPT</sub>
    * Description: An identifier for one of the safety specialists present during part or all of the sample or specimen collection
    * range: [String](types/String.md)
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

### Inherited from csd_pressureGaugeRelationship_pub:

 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
    * inherited from: None
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

### Inherited from mpr_perpitprofile_pub:

 * [rootsCollectedByA](rootsCollectedByA.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who collected the root sample(s) or specimen(s)
    * range: [String](types/String.md)
 * [rootsCollectedByB](rootsCollectedByB.md)  <sub>OPT</sub>
    * Description: An identifier for one of the people who collected the root sample(s) or specimen(s)
    * range: [String](types/String.md)
 * [maxProfileDepth](maxProfileDepth.md)  <sub>OPT</sub>
    * Description: The bottom most sampling depth per pitProfileID
    * range: [Double](types/Double.md)
    * inherited from: None
 * [totalRootBiomass](totalRootBiomass.md)  <sub>OPT</sub>
    * Description: Total root biomass per horizontal surface area to max pit depth
    * range: [Double](types/Double.md)
    * inherited from: None
 * [depth100RootBiomass](depth100RootBiomass.md)  <sub>OPT</sub>
    * Description: Total root biomass per horizontal surface area to 100 cm depth
    * range: [Double](types/Double.md)
    * inherited from: None

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

### Inherited from spc_perhorizon_in:

 * [horizonTempName](horizonTempName.md)  <sub>OPT</sub>
    * Description: Temporary soil horizon name assigned in the field
    * range: [String](types/String.md)
    * inherited from: None
 * [pitFate](pitFate.md)  <sub>OPT</sub>
    * Description: Fate of the soil pit
    * range: [String](types/String.md)
 * [horizonFate](horizonFate.md)  <sub>OPT</sub>
    * Description: Fate of the soil horizon
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
    * inherited from: None
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
| **Mappings:** | | neon:mgp_permegapit_in |
| **In Subsets:** | | DP0.00096.001 |

