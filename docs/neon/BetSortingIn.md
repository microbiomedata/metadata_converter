
# Type: bet_sorting_in




URI: [neon:BetSortingIn](https://data.neonscience.org/BetSortingIn)


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
 * [dryMass](dryMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of sample or subsample
    * range: [Double](types/Double.md)
    * inherited from: None
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

### Inherited from asi_POMExternalLabDataPerSample_pub:

 * [sampleType](sampleType.md)  <sub>OPT</sub>
    * Description: Type of sample
    * range: [String](types/String.md)
 * [sampleVolumeFiltered](sampleVolumeFiltered.md)  <sub>OPT</sub>
    * Description: Volume of water filtered onto the filter for external analysis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [externalRemarks](externalRemarks.md)  <sub>OPT</sub>
    * Description: External lab notes; free text comments accompanying the record
    * range: [String](types/String.md)
    * inherited from: None
 * [analyte](analyte.md)  <sub>OPT</sub>
    * Description: Analyte or parameter measured
    * range: [String](types/String.md)
    * inherited from: None
 * [method](method.md)  <sub>OPT</sub>
    * Description: Published method used for analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [analysisDate](analysisDate.md)  <sub>OPT</sub>
    * Description: Date that the sample was analyzed
    * range: [Time](types/Time.md)
    * inherited from: None
 * [analyzedBy](analyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample
    * range: [String](types/String.md)
    * inherited from: None
 * [filterSize](filterSize.md)  <sub>OPT</sub>
    * Description: Filter diameter
    * range: [Double](types/Double.md)
    * inherited from: None
 * [plantAlgaeLabUnits](plantAlgaeLabUnits.md)  <sub>OPT</sub>
    * Description: Standard units of measure used by the plant and algae external laboratory
    * range: [String](types/String.md)
    * inherited from: None
 * [externalLabDataQF](externalLabDataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag for external lab data
    * range: [String](types/String.md)
    * inherited from: None
 * [batchID](batchID.md)  <sub>OPT</sub>
    * Description: Identifier for batch or analytical run
    * range: [String](types/String.md)
    * inherited from: None
 * [analyteConcentration](analyteConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of analyte
    * range: [Double](types/Double.md)
    * inherited from: None
 * [percentFilterAnalyzed](percentFilterAnalyzed.md)  <sub>OPT</sub>
    * Description: Fraction of the filter sampled (%)
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from bet_sorting_pub:

 * [etOHChangeDate](etOHChangeDate.md)  <sub>OPT</sub>
    * Description: Date the ethanol rinse was completed
    * range: [Time](types/Time.md)

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

### Inherited from inv_taxonomyRaw_pub:

 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
 * [individualCount](individualCount.md)  <sub>OPT</sub>
    * Description: Number of individuals of the same type
    * range: [String](types/String.md)
 * [identifiedDate](identifiedDate.md)  <sub>OPT</sub>
    * Description: Date on which the sample, individual, or specimen was identified
    * range: [Time](types/Time.md)
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
    * inherited from: None
 * [superphylum](superphylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the superphylum in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [infraphylum](infraphylum.md)  <sub>OPT</sub>
    * Description: The scientific name of the infraphylum in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from ltr_pertrap_pub:

 * [trapID](trapID.md)  <sub>OPT</sub>
    * Description: Identifier for trap
    * range: [String](types/String.md)
 * [trapPlacement](trapPlacement.md)  <sub>OPT</sub>
    * Description: Strategy for selecting plot location
    * range: [String](types/String.md)
    * inherited from: None
 * [trapSize](trapSize.md)  <sub>OPT</sub>
    * Description: Size of trap
    * range: [Double](types/Double.md)
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
 * [identifiedBy](identifiedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who identified the specimen
    * range: [String](types/String.md)
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

### Inherited from mic_dnaExtraction_in:

 * [subsampleID](subsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with each subsample per sampleID
    * range: [String](types/String.md)
 * [sampleClass](sampleClass.md)  <sub>OPT</sub>
    * Description: Class of a sample
    * range: [String](types/String.md)
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

### Inherited from vst_shrubgroup_pub:

 * [plotID](plotID.md)  <sub>OPT</sub>
    * Description: Plot identifier (NEON site code_XXX)
    * range: [String](types/String.md)
 * [identificationReferences](identificationReferences.md)  <sub>OPT</sub>
    * Description: A list of sources (concatenated and semicolon separated) used to derive the specific taxon concept; including field guide editions, books, or versions of NEON keys used
    * range: [String](types/String.md)
 * [taxonID](taxonID.md)  <sub>OPT</sub>
    * Description: Species code, based on one or more sources
    * range: [String](types/String.md)
 * [identificationQualifier](identificationQualifier.md)  <sub>OPT</sub>
    * Description: A standard term to express the determiner's doubts about the Identification
    * range: [String](types/String.md)
 * [measuredBy](measuredBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who measured or collected the data
    * range: [String](types/String.md)
    * inherited from: None
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
| **Mappings:** | | neon:bet_sorting_in |

