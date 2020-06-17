
# Type: bry_productivity_pub




URI: [neon:BryProductivityPub](https://data.neonscience.org/BryProductivityPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [bryType](bryType.md)  <sub>OPT</sub>
    * Description: Describes the dominant type of bryophyte present in a clipped sample
    * range: [String](types/String.md)
 * [collectRemarks](collectRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the collect activity
    * range: [String](types/String.md)
 * [growthInterval](growthInterval.md)  <sub>OPT</sub>
    * Description: The number of growing days between when sampling began and the collection event
    * range: [String](types/String.md)
 * [missingNetCount](missingNetCount.md)  <sub>OPT</sub>
    * Description: A per clipID count of nets missing since set event
    * range: [String](types/String.md)
 * [sampledNetCount](sampledNetCount.md)  <sub>OPT</sub>
    * Description: A per clipID count of nets sampled
    * range: [String](types/String.md)
 * [setBy](setBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who set the trap
    * range: [String](types/String.md)
 * [setNetCount](setNetCount.md)  <sub>OPT</sub>
    * Description: A per clipID count of nets set for sample collection
    * range: [String](types/String.md)
 * [setRemarks](setRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the set activity
    * range: [String](types/String.md)
 * [storageHours](storageHours.md)  <sub>OPT</sub>
    * Description: Total number of hours clipped biomass was stored between collection and processing
    * range: [Double](types/Double.md)
 * [totalSampledArea](totalSampledArea.md)  <sub>OPT</sub>
    * Description: Total area sampled
    * range: [Double](types/Double.md)
 * [weighRemarks](weighRemarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the weigh activity
    * range: [String](types/String.md)

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

### Inherited from cfc_fieldData_pub:

 * [clipID](clipID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the clip-harvest location within the plot
    * range: [String](types/String.md)
 * [clipCellNumber](clipCellNumber.md)  <sub>OPT</sub>
    * Description: A numeric identifier for the clip-harvest cell in which herbaceous biomass was sampled
    * range: [String](types/String.md)
    * inherited from: None
 * [clipLength](clipLength.md)  <sub>OPT</sub>
    * Description: The length of the clip-harvest area in meters
    * range: [Double](types/Double.md)
    * inherited from: None
 * [clipWidth](clipWidth.md)  <sub>OPT</sub>
    * Description: The width of the clip-harvest area in meters
    * range: [Double](types/Double.md)
    * inherited from: None
 * [vstTag](vstTag.md)  <sub>OPT</sub>
    * Description: Indicator for whether a tagID is associated with vegetation structure measurements
    * range: [String](types/String.md)
    * inherited from: None
 * [percentCoverClip](percentCoverClip.md)  <sub>OPT</sub>
    * Description: Ocular estimate of percent cover of all vegetation in the clip strip
    * range: [Double](types/Double.md)
    * inherited from: None
 * [subsample1Height](subsample1Height.md)  <sub>OPT</sub>
    * Description: Vertical distance from ground to height of first canopy subsample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [subsample2Height](subsample2Height.md)  <sub>OPT</sub>
    * Description: Vertical distance from ground to height of second canopy subsample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [subsample3Height](subsample3Height.md)  <sub>OPT</sub>
    * Description: Vertical distance from ground to height of third canopy subsample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlorophyllSampleCondition](chlorophyllSampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a chlorophyll sample
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

### Inherited from inv_taxonomyRaw_pub:

 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
 * [individualCount](individualCount.md)  <sub>OPT</sub>
    * Description: Number of individuals of the same type
    * range: [String](types/String.md)
    * inherited from: None
 * [identifiedDate](identifiedDate.md)  <sub>OPT</sub>
    * Description: Date on which the sample, individual, or specimen was identified
    * range: [Time](types/Time.md)
    * inherited from: None
 * [identificationRemarks](identificationRemarks.md)  <sub>OPT</sub>
    * Description: Comments or notes about the identification
    * range: [String](types/String.md)
    * inherited from: None
 * [kingdom](kingdom.md)  <sub>OPT</sub>
    * Description: The scientific name of the kingdom in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [phylum](phylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the phylum or division in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [class](class.md)  <sub>OPT</sub>
    * Description: The scientific name of the class in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [order](order.md)  <sub>OPT</sub>
    * Description: The scientific name of the order in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [family](family.md)  <sub>OPT</sub>
    * Description: The scientific name of the family in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subfamily](subfamily.md)  <sub>OPT</sub>
    * Description: The scientific name of the subfamily in which the organism is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [genus](genus.md)  <sub>OPT</sub>
    * Description: The scientific name of the genus in which the organism is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subgenus](subgenus.md)  <sub>OPT</sub>
    * Description: The scientific name of the subgenus in which the taxon is classified. Values should include the genus to avoid homonym confusion
    * range: [String](types/String.md)
    * inherited from: None
 * [specificEpithet](specificEpithet.md)  <sub>OPT</sub>
    * Description: The specific epithet (second part of the species name) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [infraspecificEpithet](infraspecificEpithet.md)  <sub>OPT</sub>
    * Description: The infraspecific epithet (scientific name below the rank of species) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [tribe](tribe.md)  <sub>OPT</sub>
    * Description: The scientific name of the tribe in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [taxonDatabaseName](taxonDatabaseName.md)  <sub>OPT</sub>
    * Description: Name of the taxonomic database
    * range: [String](types/String.md)
    * inherited from: None
 * [taxonDatabaseID](taxonDatabaseID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the taxon within the database
    * range: [String](types/String.md)
    * inherited from: None
 * [subsamplePercent](subsamplePercent.md)  <sub>OPT</sub>
    * Description: Percent of the total sample contained in the subsample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [invertebrateLifeStage](invertebrateLifeStage.md)  <sub>OPT</sub>
    * Description: Macroinvertebrate stage of development (larva, pupa, adult)
    * range: [String](types/String.md)
    * inherited from: None
 * [sizeClass](sizeClass.md)  <sub>OPT</sub>
    * Description: Size class of individual(s)
    * range: [String](types/String.md)
    * inherited from: None
 * [immatureSpecimen](immatureSpecimen.md)  <sub>OPT</sub>
    * Description: Sample contains immature specimen(s) for which target level of identification cannot be achieved
    * range: [String](types/String.md)
    * inherited from: None
 * [distinctTaxon](distinctTaxon.md)  <sub>OPT</sub>
    * Description: Taxon is known to be distinct within the sample, used for species richness metrics
    * range: [String](types/String.md)
    * inherited from: None
 * [qcChecked](qcChecked.md)  <sub>OPT</sub>
    * Description: Whether or not QC procedure was performed
    * range: [String](types/String.md)
    * inherited from: None
 * [indeterminateSpecies](indeterminateSpecies.md)  <sub>OPT</sub>
    * Description: Sample contains specimen(s) not well-described in the literature, not all taxa for a group are included in the literature, or observed characters are such that they do not fit described taxa. See accompanying identificationRemarks
    * range: [String](types/String.md)
    * inherited from: None
 * [subphylum](subphylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the subphylum in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subclass](subclass.md)  <sub>OPT</sub>
    * Description: The scientific name of the subclass in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [infraclass](infraclass.md)  <sub>OPT</sub>
    * Description: The scientific name of the infraclass in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [superorder](superorder.md)  <sub>OPT</sub>
    * Description: The scientific name of the superorder in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [suborder](suborder.md)  <sub>OPT</sub>
    * Description: The scientific name of the suborder in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [infraorder](infraorder.md)  <sub>OPT</sub>
    * Description: The scientific name of the infraorder in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [superfamily](superfamily.md)  <sub>OPT</sub>
    * Description: The scientific name of the superfamily in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subtribe](subtribe.md)  <sub>OPT</sub>
    * Description: The scientific name of the subtribe in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [estimatedTotalCount](estimatedTotalCount.md)  <sub>OPT</sub>
    * Description: Estimated total count of individuals within a sample, of given taxon, life stage, and size class
    * range: [Double](types/Double.md)
    * inherited from: None
 * [subkingdom](subkingdom.md)  <sub>OPT</sub>
    * Description: The scientific name of the subkingdom in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [infrakingdom](infrakingdom.md)  <sub>OPT</sub>
    * Description: The scientific name of the infrakingdom in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [superclass](superclass.md)  <sub>OPT</sub>
    * Description: The scientific name of the superclass in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [superphylum](superphylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the superphylum in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [infraphylum](infraphylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the infraphylum in which the taxon is classified
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
    * inherited from: None
 * [ovenEndDate](ovenEndDate.md)  <sub>OPT</sub>
    * Description: The date and time a sample was removed from the drying oven
    * range: [Time](types/Time.md)
    * inherited from: None
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
| **Mappings:** | | neon:bry_productivity_pub |
| **In Subsets:** | | DP1.10035.001 |

