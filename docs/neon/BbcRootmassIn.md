
# Type: bbc_rootmass_in




URI: [neon:BbcRootmassIn](https://data.neonscience.org/BbcRootmassIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Inherited from amc_cellCountLabSummary_in:

 * [enteredBy](enteredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who entered the data
    * range: [String](types/String.md)
 * [cellCountMethod](cellCountMethod.md)  <sub>OPT</sub>
    * Description: Enumeration method used for microbial cell count
    * range: [String](types/String.md)
    * inherited from: None
 * [countStandardDeviation](countStandardDeviation.md)  <sub>OPT</sub>
    * Description: Long-term average standard deviation values of microbial cell count of the reference image based on repeat visual analysis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [longTermEnumerationDifference](longTermEnumerationDifference.md)  <sub>OPT</sub>
    * Description: Percent difference in enumeration between the reference image count and the quality checked reference image count
    * range: [Double](types/Double.md)
    * inherited from: None
 * [referenceImageCount](referenceImageCount.md)  <sub>OPT</sub>
    * Description: Automated count of the reference image
    * range: [String](types/String.md)
    * inherited from: None
 * [referenceImageID](referenceImageID.md)  <sub>OPT</sub>
    * Description: Identifier for the reference image
    * range: [String](types/String.md)
    * inherited from: None
 * [enumerationDifferenceMax](enumerationDifferenceMax.md)  <sub>OPT</sub>
    * Description: Maximum percent difference in enumeration calculated over the previous analysis year
    * range: [Double](types/Double.md)
    * inherited from: None
 * [enumerationDifferenceMean](enumerationDifferenceMean.md)  <sub>OPT</sub>
    * Description: Mean percent difference in enumeration calculated over the previous analysis year
    * range: [Double](types/Double.md)
    * inherited from: None
 * [enumerationDifferenceMin](enumerationDifferenceMin.md)  <sub>OPT</sub>
    * Description: Minimum percent difference in enumeration calculated over the previous analysis year
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from apl_biomass_pub:

 * [processingDate](processingDate.md)  <sub>OPT</sub>
    * Description: Date that sample was processed (i.e., sorted or pinned) in the domain lab
    * range: [Time](types/Time.md)
    * inherited from: None
 * [dryMass](dryMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of sample or subsample
    * range: [Double](types/Double.md)
 * [wetMass](wetMass.md)  <sub>OPT</sub>
    * Description: Fresh mass of the sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [wetMassSubsample](wetMassSubsample.md)  <sub>OPT</sub>
    * Description: Fresh mass of the subsample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [boatMass](boatMass.md)  <sub>OPT</sub>
    * Description: Mass of the weigh boat
    * range: [Double](types/Double.md)
    * inherited from: None
 * [dryMassBoatMass](dryMassBoatMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of the sample and weigh boat
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ashMassBoatMass](ashMassBoatMass.md)  <sub>OPT</sub>
    * Description: Combusted mass of the sample and weigh boat
    * range: [Double](types/Double.md)
    * inherited from: None
 * [fieldID](fieldID.md)  <sub>OPT</sub>
    * Description: Identifier for sample generated in the field
    * range: [String](types/String.md)
    * inherited from: None
 * [benthicArea](benthicArea.md)  <sub>OPT</sub>
    * Description: Area of the benthos sampled
    * range: [Double](types/Double.md)
    * inherited from: None
 * [adjDryMass](adjDryMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of the sample, multiplied to account for lab subsampling
    * range: [Double](types/Double.md)
    * inherited from: None
 * [adjAshFreeDryMass](adjAshFreeDryMass.md)  <sub>OPT</sub>
    * Description: Combusted mass of the sample, multiplied to account for lab subsampling
    * range: [Double](types/Double.md)
    * inherited from: None
 * [arealAdjDryMass](arealAdjDryMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of the sample, multiplied to account for lab subsampling and the area sampled based on samplerType
    * range: [Double](types/Double.md)
    * inherited from: None
 * [arealAdjAshFreeDryMass](arealAdjAshFreeDryMass.md)  <sub>OPT</sub>
    * Description: Combusted mass of the sample, multiplied to account for lab subsampling and the area sampled based on samplerType
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chemSubsampleID](chemSubsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with chemistry subsample per sampleID
    * range: [String](types/String.md)
    * inherited from: None
 * [chemSubsampleBarcode](chemSubsampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of chemistry subsample
    * range: [String](types/String.md)
    * inherited from: None
 * [fieldIDCode](fieldIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of a fieldID
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from cdw_densitydisk_pub:

 * [dryingHours](dryingHours.md)  <sub>OPT</sub>
    * Description: Number of hours material was in a drying oven until dried to constant weight
    * range: [Double](types/Double.md)
 * [sampleBarcode](sampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a sample
    * range: [String](types/String.md)
    * inherited from: None
 * [subsampleFreshMassRatio](subsampleFreshMassRatio.md)  <sub>OPT</sub>
    * Description: The ratio of subsampleFreshMass to sampleFreshMass
    * range: [Double](types/Double.md)
    * inherited from: None
 * [aDiskHeight](aDiskHeight.md)  <sub>OPT</sub>
    * Description: The height, to the nearest 0.1 cm, of the log cross-sectional disk used for bulk density sampling; measurement location 1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bagNumber](bagNumber.md)  <sub>OPT</sub>
    * Description: Unique value for tracking a field collected sample
    * range: [String](types/String.md)
    * inherited from: None
 * [bDiskHeight](bDiskHeight.md)  <sub>OPT</sub>
    * Description: The height, to the nearest 0.1 cm, of the log cross-sectional disk used for bulk density sampling; measurement location 2
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bulkDensDisk](bulkDensDisk.md)  <sub>OPT</sub>
    * Description: Bulk density of a cdw disk
    * range: [Double](types/Double.md)
    * inherited from: None
 * [diameter](diameter.md)  <sub>OPT</sub>
    * Description: The maximum cross-sectional diameter
    * range: [Double](types/Double.md)
    * inherited from: None
 * [diskDryMass](diskDryMass.md)  <sub>OPT</sub>
    * Description: Calculated oven-dried mass of a cdw disk
    * range: [Double](types/Double.md)
    * inherited from: None
 * [diskFreshMass](diskFreshMass.md)  <sub>OPT</sub>
    * Description: Mass of fresh, undried material
    * range: [Double](types/Double.md)
    * inherited from: None
 * [diskID](diskID.md)  <sub>OPT</sub>
    * Description: Numeric identifier for each log cross-sectional disk sampled for bulk density
    * range: [String](types/String.md)
    * inherited from: None
 * [maxDiskHeight](maxDiskHeight.md)  <sub>OPT</sub>
    * Description: The maximum disk height
    * range: [Double](types/Double.md)
    * inherited from: None
 * [minDiskHeight](minDiskHeight.md)  <sub>OPT</sub>
    * Description: The minimum disk height
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ninetyDiameter](ninetyDiameter.md)  <sub>OPT</sub>
    * Description: The cross-sectional diameter perpendicular to the maximum diameter
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sampleFreshMass](sampleFreshMass.md)  <sub>OPT</sub>
    * Description: Mass of fresh, undried subsample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [qaSample](qaSample.md)  <sub>OPT</sub>
    * Description: Indicates whether sample measurements are replicates for quality assurance purposes
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from cdw_densitylog_pub:

 * [sizeCategory](sizeCategory.md)  <sub>OPT</sub>
    * Description: Categorical size class of an individual or sample
    * range: [String](types/String.md)
 * [vstTagID](vstTagID.md)  <sub>OPT</sub>
    * Description: The vegetation structure tagID value
    * range: [String](types/String.md)
    * inherited from: None
 * [branchBarkCover](branchBarkCover.md)  <sub>OPT</sub>
    * Description: Visually estimated cover class of bark remaining on branches attached to a coarse downed wood particle
    * range: [String](types/String.md)
    * inherited from: None
 * [branchesPresent](branchesPresent.md)  <sub>OPT</sub>
    * Description: Categorical indicator of branches > 1 cm diameter present on a coarse downed wood particle
    * range: [String](types/String.md)
    * inherited from: None
 * [decayClass](decayClass.md)  <sub>OPT</sub>
    * Description: The categorical decay class assigned to a sampled log
    * range: [String](types/String.md)
    * inherited from: None
 * [leavesPresent](leavesPresent.md)  <sub>OPT</sub>
    * Description: Categorical indicator of leaf/needle presence on a coarse downed wood particle
    * range: [String](types/String.md)
    * inherited from: None
 * [logBarkCover](logBarkCover.md)  <sub>OPT</sub>
    * Description: Visually estimated cover class of bark remaining on the bole of a coarse downed wood particle
    * range: [String](types/String.md)
    * inherited from: None
 * [logDistance](logDistance.md)  <sub>OPT</sub>
    * Description: The distance, to the nearest 0.1 meters, from the log to a reference point with known position (typically the transect origin)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [logHandBreakable](logHandBreakable.md)  <sub>OPT</sub>
    * Description: Categorical indicator that the outer-most wood from a coarse downed wood particle can be broken apart by hand
    * range: [String](types/String.md)
    * inherited from: None
 * [logHoldShape](logHoldShape.md)  <sub>OPT</sub>
    * Description: Categorical indicator that a piece of coarse downed wood particle holds its original shape
    * range: [String](types/String.md)
    * inherited from: None
 * [logID](logID.md)  <sub>OPT</sub>
    * Description: Identifier for each log sampled
    * range: [String](types/String.md)
    * inherited from: None
 * [twigsPresent](twigsPresent.md)  <sub>OPT</sub>
    * Description: Categorical indicator of twigs < 1 cm diameter present on a coarse downed wood particle
    * range: [String](types/String.md)
    * inherited from: None
 * [logAzimuth](logAzimuth.md)  <sub>OPT</sub>
    * Description: The azimuth relative to true north, to the nearest degree, measured from the plot centroid facing toward the sampled log
    * range: [String](types/String.md)
    * inherited from: None
 * [mappingMethod](mappingMethod.md)  <sub>OPT</sub>
    * Description: Indicator for whether or not the specified location is mapped and the method used
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleEasting](sampleEasting.md)  <sub>OPT</sub>
    * Description: Easting value of sampled location
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sampleNorthing](sampleNorthing.md)  <sub>OPT</sub>
    * Description: Northing value of sampled location
    * range: [Double](types/Double.md)
    * inherited from: None

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

### Inherited from ltr_massdata_pub:

 * [weighDate](weighDate.md)  <sub>OPT</sub>
    * Description: Date that sample or subsample was weighed
    * range: [Time](types/Time.md)
 * [qaDryMass](qaDryMass.md)  <sub>OPT</sub>
    * Description: Indicates whether 'dryMass' value is associated with 'qa' measurement type
    * range: [String](types/String.md)
 * [ovenStartDate](ovenStartDate.md)  <sub>OPT</sub>
    * Description: The date and time a sample was placed in the drying oven
    * range: [Time](types/Time.md)
 * [ovenEndDate](ovenEndDate.md)  <sub>OPT</sub>
    * Description: The date and time a sample was removed from the drying oven
    * range: [Time](types/Time.md)
 * [fieldSampleBarcode](fieldSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of a field sample
    * range: [String](types/String.md)
    * inherited from: None
 * [fieldSampleID](fieldSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for a field sample
    * range: [String](types/String.md)
    * inherited from: None
 * [functionalGroup](functionalGroup.md)  <sub>OPT</sub>
    * Description: Functional group to which a sample belongs
    * range: [String](types/String.md)
    * inherited from: None
 * [massSampleBarcode](massSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a mass sample
    * range: [String](types/String.md)
    * inherited from: None
 * [massSampleID](massSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a mass sample
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from mam_voucher_in:

 * [fulcrumVersion](fulcrumVersion.md)  <sub>OPT</sub>
    * Description: Version of the Fulcrum application used during data entry
    * range: [String](types/String.md)
 * [platformInfo](platformInfo.md)  <sub>OPT</sub>
    * Description: Operating System and browser information (where applicable) of computer used during data entry
    * range: [String](types/String.md)
 * [voucherSampleFate](voucherSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a voucher sample
    * range: [String](types/String.md)
    * inherited from: None
 * [tagFate](tagFate.md)  <sub>OPT</sub>
    * Description: Fate of domain-level unique identifier used to mark the individual
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from mic_dnaExtraction_in:

 * [subsampleID](subsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with each subsample per sampleID
    * range: [String](types/String.md)
 * [sampleClass](sampleClass.md)  <sub>OPT</sub>
    * Description: Class of a sample
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticSampleFate](geneticSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a genetic sample
    * range: [String](types/String.md)
    * inherited from: None
 * [samplePercent](samplePercent.md)  <sub>OPT</sub>
    * Description: Percent of sample processed
    * range: [Double](types/Double.md)
    * inherited from: None
 * [subsampleCode](subsampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a subsample
    * range: [String](types/String.md)
 * [subsampleFate](subsampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a subsample
    * range: [String](types/String.md)
 * [sequenceAnalysisType](sequenceAnalysisType.md)  <sub>OPT</sub>
    * Description: The general type of sequencing to be conducted on a sample
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from mpr_perrootsample_pub:

 * [pitNamedLocation](pitNamedLocation.md)  <sub>OPT</sub>
    * Description: Named location identifier for the soil pit
    * range: [String](types/String.md)
    * inherited from: None
 * [rootStatus](rootStatus.md)  <sub>OPT</sub>
    * Description: The state of an individual or sample
    * range: [String](types/String.md)
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

### Inherited from vst_shrubgroup_pub:

 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
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
 * [recordedBy](recordedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who recorded the data
    * range: [String](types/String.md)
 * [eventID](eventID.md)  <sub>OPT</sub>
    * Description: An identifier for the set of information associated with the event, which includes information about the place and time of the event
    * range: [String](types/String.md)
    * inherited from: None
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

### Inherited from wc_externalLabDataByAnalyte_in:

 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
    * inherited from: None
 * [coolerTemp](coolerTemp.md)  <sub>OPT</sub>
    * Description: Temperature of the cooler when the sample arrived at the external lab
    * range: [Double](types/Double.md)
    * inherited from: None
 * [externalLabMetadata](externalLabMetadata.md)  <sub>OPT</sub>
    * Description: The external lab's metadata
    * range: [String](types/String.md)
    * inherited from: None
 * [shipmentWarmQF](shipmentWarmQF.md)  <sub>OPT</sub>
    * Description: Quality Flag for cooler arriving at external lab too warm (above 6 C)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [uploadDate](uploadDate.md)  <sub>OPT</sub>
    * Description: Date the file was uploaded
    * range: [Time](types/Time.md)
    * inherited from: None
 * [analyteUnits](analyteUnits.md)  <sub>OPT</sub>
    * Description: Associated units of measure for analyte
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [runID](runID.md)  <sub>OPT</sub>
    * Description: A linking value provided by the external lab that associates the sample data to the run metadata, including QA values
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
| **Mappings:** | | neon:bbc_rootmass_in |

