
# Type: scs_archivedata_in




URI: [neon:ScsArchivedataIn](https://data.neonscience.org/ScsArchivedataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [archiveGuid](archiveGuid.md)  <sub>OPT</sub>
    * Description: Globally unique identifier for the archive sample
    * range: [String](types/String.md)
 * [archiveMedium](archiveMedium.md)  <sub>OPT</sub>
    * Description: Method of preservation for the sample or specimen
    * range: [String](types/String.md)
 * [archiveSampleClass](archiveSampleClass.md)  <sub>OPT</sub>
    * Description: Class of an archive sample
    * range: [String](types/String.md)
 * [storageTemperature](storageTemperature.md)  <sub>OPT</sub>
    * Description: The temperature in Centigrade at which the sample is to be stored at the archive facility
    * range: [String](types/String.md)

### Inherited from apl_taxonomyProcessed_pub:

 * [scientificNameAuthorship](scientificNameAuthorship.md)  <sub>OPT</sub>
    * Description: Name of the individual(s) who designated the scientific name of the taxon
    * range: [String](types/String.md)
 * [testMethod](testMethod.md)  <sub>OPT</sub>
    * Description: Method used to conduct test
    * range: [String](types/String.md)
    * inherited from: None
 * [qcTaxonomyStatus](qcTaxonomyStatus.md)  <sub>OPT</sub>
    * Description: Sample chosen as part of 10% of samples for quality control (QC)
    * range: [String](types/String.md)
    * inherited from: None
 * [algalType](algalType.md)  <sub>OPT</sub>
    * Description: Informal taxonomic grouping of algal species
    * range: [String](types/String.md)
    * inherited from: None
 * [algalParameter](algalParameter.md)  <sub>OPT</sub>
    * Description: Parameter used for analysis of algal assemblages
    * range: [String](types/String.md)
    * inherited from: None
 * [algalParameterValue](algalParameterValue.md)  <sub>OPT</sub>
    * Description: Value of the algalParameter
    * range: [Double](types/Double.md)
    * inherited from: None
 * [algalParameterUnit](algalParameterUnit.md)  <sub>OPT</sub>
    * Description: Unit of measure associated with the algalParameter
    * range: [String](types/String.md)
    * inherited from: None
 * [variety](variety.md)  <sub>OPT</sub>
    * Description: The variety (infraspecific name below the rank of infraspecific epithet) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [section](section.md)  <sub>OPT</sub>
    * Description: The scientific name of the section in which the organism is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [superdivision](superdivision.md)  <sub>OPT</sub>
    * Description: The scientific name of the superdivision in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [division](division.md)  <sub>OPT</sub>
    * Description: The scientific name of the division in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subdivision](subdivision.md)  <sub>OPT</sub>
    * Description: The scientific name of the subdivision in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [infradivision](infradivision.md)  <sub>OPT</sub>
    * Description: The scientific name of the infradivision in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [parvdivision](parvdivision.md)  <sub>OPT</sub>
    * Description: The scientific name of the parvdivision in which the taxon is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subsection](subsection.md)  <sub>OPT</sub>
    * Description: The scientific name of the subsection in which the organism is classified
    * range: [String](types/String.md)
    * inherited from: None
 * [subspecies](subspecies.md)  <sub>OPT</sub>
    * Description: The subspecies (infraspecific name below the rank of infraspecific epithet) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [subvariety](subvariety.md)  <sub>OPT</sub>
    * Description: The subvariety (infraspecific name below the rank of variety) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [subform](subform.md)  <sub>OPT</sub>
    * Description: The subform (infraspecific name below the rank of form) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [form](form.md)  <sub>OPT</sub>
    * Description: The form (infraspecific name below the rank of infraspecific epithet) of the scientific name applied to the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [speciesGroup](speciesGroup.md)  <sub>OPT</sub>
    * Description: The unofficial species group into which the taxon is categorized
    * range: [String](types/String.md)
    * inherited from: None
 * [perBottleSampleVolume](perBottleSampleVolume.md)  <sub>OPT</sub>
    * Description: Sample volume per bottle in milliliters
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from bet_barcoding_in:

 * [reproductiveCondition](reproductiveCondition.md)  <sub>OPT</sub>
    * Description: The reproductive condition of the individual at the time of capture. R for reproductive; N for non-reproductive
    * range: [String](types/String.md)
 * [samplingMethod](samplingMethod.md)  <sub>OPT</sub>
    * Description: Name or code for the method used to collect or test a sample
    * range: [String](types/String.md)
    * inherited from: None
 * [collectionCode](collectionCode.md)  <sub>OPT</sub>
    * Description: Code associated with a given collection within an institution. The Collection Code is used in conjunction with Museum ID in order to disambiguate a ID that might be used in different collections within the same institution
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

### Inherited from dpm_externalLab_in:

 * [filterLotID](filterLotID.md)  <sub>OPT</sub>
    * Description: Unique ID of the filter manufacturing lot
    * range: [String](types/String.md)
    * inherited from: None
 * [filterWeighDate](filterWeighDate.md)  <sub>OPT</sub>
    * Description: Date the post-deployment filter was weighed
    * range: [Time](types/Time.md)
    * inherited from: None
 * [filterWeightDelta](filterWeightDelta.md)  <sub>OPT</sub>
    * Description: Change in weight of the filter from pre- to post-deployment
    * range: [Double](types/Double.md)
    * inherited from: None
 * [filterWeightPostDeploy](filterWeightPostDeploy.md)  <sub>OPT</sub>
    * Description: Post-deployment weight of filter
    * range: [Double](types/Double.md)
    * inherited from: None
 * [filterWeightPreDeploy](filterWeightPreDeploy.md)  <sub>OPT</sub>
    * Description: Pre-deployment weight of the clean filter
    * range: [Double](types/Double.md)
    * inherited from: None
 * [labAverageHumidity](labAverageHumidity.md)  <sub>OPT</sub>
    * Description: The historical average humidity of the laboratory at the time of weighing
    * range: [Double](types/Double.md)
    * inherited from: None
 * [labFilterCondition](labFilterCondition.md)  <sub>OPT</sub>
    * Description: Condition of the filter reported in the laboratory
    * range: [String](types/String.md)
    * inherited from: None
 * [labFilterConditionRemarks](labFilterConditionRemarks.md)  <sub>OPT</sub>
    * Description: Additional description of the laboratory filter condition
    * range: [String](types/String.md)
    * inherited from: None
 * [labFilterDamage](labFilterDamage.md)  <sub>OPT</sub>
    * Description: Laboratory description of how the filter is damaged, if at all
    * range: [String](types/String.md)
    * inherited from: None
 * [labFilterDamageRemarks](labFilterDamageRemarks.md)  <sub>OPT</sub>
    * Description: Additional description of possible laboratory damages, e.g., tear, hole, piece missing
    * range: [String](types/String.md)
    * inherited from: None
 * [labQARemarks](labQARemarks.md)  <sub>OPT</sub>
    * Description: Remarks on filter health and data quality from the lab
    * range: [String](types/String.md)
    * inherited from: None
 * [labRelativeHumidity](labRelativeHumidity.md)  <sub>OPT</sub>
    * Description: The relative humidity of the laboratory at the time of weighing
    * range: [Double](types/Double.md)
    * inherited from: None
 * [labTemp](labTemp.md)  <sub>OPT</sub>
    * Description: The temperature of the laboratory at the time of weighing
    * range: [Double](types/Double.md)
    * inherited from: None
 * [archiveStartDate](archiveStartDate.md)  <sub>OPT</sub>
    * Description: Date that the sample was archived
    * range: [Time](types/Time.md)
 * [archiveLocatorID](archiveLocatorID.md)  <sub>OPT</sub>
    * Description: Identifier for the location where filter is archived, as a string containing warehouse, shelf, and box number
    * range: [String](types/String.md)
    * inherited from: None
 * [filterManufactureName](filterManufactureName.md)  <sub>OPT</sub>
    * Description: The manufacturer of the filter
    * range: [String](types/String.md)
    * inherited from: None
 * [filterProductModel](filterProductModel.md)  <sub>OPT</sub>
    * Description: Model number of the filter
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from inv_dnaStandardTaxon_pub:

 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [createdBy](createdBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who created the record
    * range: [String](types/String.md)
    * inherited from: None
 * [dnaStandardSampleCode](dnaStandardSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of DNA standard sample
    * range: [String](types/String.md)
    * inherited from: None
 * [dnaStandardSampleID](dnaStandardSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for the DNA standard sample
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

### Inherited from mam_barcoding_in:

 * [specimenSource](specimenSource.md)  <sub>OPT</sub>
    * Description: Physical source from which individual was obtained
    * range: [String](types/String.md)
    * inherited from: None
 * [archiveID](archiveID.md)  <sub>OPT</sub>
    * Description: Identifier for the archive sample
    * range: [String](types/String.md)
 * [archiveLaboratoryName](archiveLaboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the archive sample
    * range: [String](types/String.md)
 * [archiveFacilityID](archiveFacilityID.md)  <sub>OPT</sub>
    * Description: Identifier at archive facility
    * range: [String](types/String.md)
    * inherited from: None
 * [associatedSpecimens](associatedSpecimens.md)  <sub>OPT</sub>
    * Description: A list of specimens associated with the subject specimen at the time of its collection. References to other specimen identifiers should be preceded by the relationship
    * range: [String](types/String.md)
    * inherited from: None
 * [associatedTaxa](associatedTaxa.md)  <sub>OPT</sub>
    * Description: A list of taxa associated with the taxon at the time of its collection. References to taxa are preceded by the relationship
    * range: [String](types/String.md)
    * inherited from: None
 * [externalURLs](externalURLs.md)  <sub>OPT</sub>
    * Description: Pipe-delimited list of web accessible links that provide additional information about the specimen
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleStatus](sampleStatus.md)  <sub>OPT</sub>
    * Description: Status of sample for downstream processing and/or analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [wellCoordinates](wellCoordinates.md)  <sub>OPT</sub>
    * Description: Location of sample in multi-well storage box or plate
    * range: [String](types/String.md)
    * inherited from: None
 * [identifier](identifier.md)  <sub>OPT</sub>
    * Description: Full name of primary individual who assigned the specimen to a taxonomic group
    * range: [String](types/String.md)
    * inherited from: None
 * [identifierEmail](identifierEmail.md)  <sub>OPT</sub>
    * Description: E-mail address of the primary identifier
    * range: [String](types/String.md)
    * inherited from: None
 * [identifierInstitution](identifierInstitution.md)  <sub>OPT</sub>
    * Description: The full name of the institutional or organizational affiliation of the identifier
    * range: [String](types/String.md)
    * inherited from: None
 * [reproduction](reproduction.md)  <sub>OPT</sub>
    * Description: The presumed method of reproduction
    * range: [String](types/String.md)
    * inherited from: None
 * [trappingDays](trappingDays.md)  <sub>OPT</sub>
    * Description: Decimal days between trap setting and collecting events
    * range: [Double](types/Double.md)
    * inherited from: None
 * [depth](depth.md)  <sub>OPT</sub>
    * Description: For organisms collected beneath the surface of a water body
    * range: [Double](types/Double.md)
    * inherited from: None
 * [depthPrecision](depthPrecision.md)  <sub>OPT</sub>
    * Description: A numerical representation of the precision of the depth given in meters and is represented as greater or less than the depth value
    * range: [Double](types/Double.md)
    * inherited from: None
 * [eventTime](eventTime.md)  <sub>OPT</sub>
    * Description: The time or time of day during which the sample was collected
    * range: [String](types/String.md)
    * inherited from: None
 * [netDepth](netDepth.md)  <sub>OPT</sub>
    * Description: Deployment depth of the net
    * range: [Double](types/Double.md)
    * inherited from: None
 * [plateID](plateID.md)  <sub>OPT</sub>
    * Description: Identifier of the multi-well storage plate
    * range: [String](types/String.md)
    * inherited from: None
 * [BOLDsequenceURL](BOLDsequenceURL.md)  <sub>OPT</sub>
    * Description: Sequence from BOLD
    * range: [String](types/String.md)
    * inherited from: None
 * [BOLDtraceURL](BOLDtraceURL.md)  <sub>OPT</sub>
    * Description: Trace from BOLD
    * range: [String](types/String.md)
    * inherited from: None
 * [NEONsequenceURL](NEONsequenceURL.md)  <sub>OPT</sub>
    * Description: Sequence from BOLD hosted in NEON ECS
    * range: [String](types/String.md)
    * inherited from: None
 * [NEONtraceURL](NEONtraceURL.md)  <sub>OPT</sub>
    * Description: Trace from BOLD hosted in NEON ECS
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from mam_pertrapnight_pub:

 * [nightuid](nightuid.md)  <sub>OPT</sub>
    * Description: Unique ID of associated record in perplotnight table
    * range: [String](types/String.md)
    * inherited from: None
 * [trapCoordinate](trapCoordinate.md)  <sub>OPT</sub>
    * Description: Relative coordinate of the trap within the given plotID (A1 - J10). If row or column coordinate is unknown, X is used
    * range: [String](types/String.md)
    * inherited from: None
 * [trapStatus](trapStatus.md)  <sub>OPT</sub>
    * Description: Categorical descriptor of trap status; 0 - no data; 1 - trap not set; 2 - trap disturbed/door closed but empty; 3 - trap door open or closed w/ spoor left; 4 - >1 capture in one trap; 5 - capture; 6 - trap set and empty
    * range: [String](types/String.md)
    * inherited from: None
 * [sex](sex.md)  <sub>OPT</sub>
    * Description: M for male, F for female, U for unknown
    * range: [String](types/String.md)
 * [lifeStage](lifeStage.md)  <sub>OPT</sub>
    * Description: The age class of the individual at the time the Occurrence was recorded. juvenile = obvious signs of a very young individual, small size, distinctive pelage coloration; subabult; adult
    * range: [String](types/String.md)
 * [testes](testes.md)  <sub>OPT</sub>
    * Description: Condition of the testes at time of capture; if mature: scrotal = testes descended, nonscrotal = testes abdominal
    * range: [String](types/String.md)
    * inherited from: None
 * [nipples](nipples.md)  <sub>OPT</sub>
    * Description: Condition of the nipples at time of capture; if mature: enlarged = nipples enlarged, nonenlarged = nipples not enlarged
    * range: [String](types/String.md)
    * inherited from: None
 * [pregnancyStatus](pregnancyStatus.md)  <sub>OPT</sub>
    * Description: Condition at time of capture; if mature: 'pregnant' | 'not'
    * range: [String](types/String.md)
    * inherited from: None
 * [vagina](vagina.md)  <sub>OPT</sub>
    * Description: Condition of the vagina at time of capture; if mature: swollen, plugged, neither
    * range: [String](types/String.md)
    * inherited from: None
 * [hindfootLength](hindfootLength.md)  <sub>OPT</sub>
    * Description: length of left hindfoot; including claws; in millimeters
    * range: [String](types/String.md)
    * inherited from: None
 * [earLength](earLength.md)  <sub>OPT</sub>
    * Description: length of left ear; in millimeters
    * range: [String](types/String.md)
    * inherited from: None
 * [tailLength](tailLength.md)  <sub>OPT</sub>
    * Description: length of tail; in millimeters
    * range: [String](types/String.md)
    * inherited from: None
 * [totalLength](totalLength.md)  <sub>OPT</sub>
    * Description: total length (head + body); in millimeters
    * range: [String](types/String.md)
    * inherited from: None
 * [weight](weight.md)  <sub>OPT</sub>
    * Description: Live weight as measured with a spring scale; in grams
    * range: [String](types/String.md)
    * inherited from: None
 * [replacedTag](replacedTag.md)  <sub>OPT</sub>
    * Description: Indicates which ear tag was replaced (L#### | R####) or which ear appears to have lost a tag ('left' = left ear tag replaced; 'right' = right ear tag replaced)
    * range: [String](types/String.md)
    * inherited from: None
 * [recapture](recapture.md)  <sub>OPT</sub>
    * Description: Indicates whether or not the captured individual is a recapture; 'Y' for yes, 'N' for no
    * range: [String](types/String.md)
    * inherited from: None
 * [fate](fate.md)  <sub>OPT</sub>
    * Description: The fate of the individual, unless marked and released; 'dead' = dead, 'escaped' = escaped while handling, 'nontarget' = released, non-target species, 'released' = target or opportunistic species released without full processing
    * range: [String](types/String.md)
    * inherited from: None
 * [bloodSampleID](bloodSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the blood sample
    * range: [String](types/String.md)
    * inherited from: None
 * [bloodSampleMethod](bloodSampleMethod.md)  <sub>OPT</sub>
    * Description: Method used to collect the blood sample
    * range: [String](types/String.md)
    * inherited from: None
 * [fecalSampleID](fecalSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the fecal sample
    * range: [String](types/String.md)
    * inherited from: None
 * [fecalSampleCondition](fecalSampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of fecal sample at time of collection; 'fresh' = fresh fecal sample collected from mammal; 'old' = 'Old' fecal sample collected from trap
    * range: [String](types/String.md)
    * inherited from: None
 * [earSampleID](earSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the ear sample
    * range: [String](types/String.md)
    * inherited from: None
 * [hairSampleID](hairSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the hair sample
    * range: [String](types/String.md)
    * inherited from: None
 * [nlcdClass](nlcdClass.md)  <sub>OPT</sub>
    * Description: National Land Cover Database Vegetation Type Name
    * range: [String](types/String.md)
    * inherited from: None
 * [plotType](plotType.md)  <sub>OPT</sub>
    * Description: NEON plot type in which sampling occurred: tower, distributed or gradient
    * range: [String](types/String.md)
    * inherited from: None
 * [trapType](trapType.md)  <sub>OPT</sub>
    * Description: Type of trap from which a sample was collected
    * range: [String](types/String.md)
    * inherited from: None
 * [larvalTicksAttached](larvalTicksAttached.md)  <sub>OPT</sub>
    * Description: Indicates whether larval ticks are observed on the captured individual
    * range: [String](types/String.md)
    * inherited from: None
 * [nymphalTicksAttached](nymphalTicksAttached.md)  <sub>OPT</sub>
    * Description: Indicates whether nymphal ticks are observed on the captured individual
    * range: [String](types/String.md)
    * inherited from: None
 * [adultTicksAttached](adultTicksAttached.md)  <sub>OPT</sub>
    * Description: Indicates whether adult ticks are observed on the captured individual
    * range: [String](types/String.md)
    * inherited from: None
 * [individualCode](individualCode.md)  <sub>OPT</sub>
    * Description: Barcode of an individual
    * range: [String](types/String.md)
    * inherited from: None
 * [bloodSampleBarcode](bloodSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of the blood sample
    * range: [String](types/String.md)
    * inherited from: None
 * [earSampleBarcode](earSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of the ear sample
    * range: [String](types/String.md)
    * inherited from: None
 * [fecalSampleBarcode](fecalSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of the fecal sample
    * range: [String](types/String.md)
    * inherited from: None
 * [hairSampleBarcode](hairSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of the hair sample
    * range: [String](types/String.md)
    * inherited from: None
 * [voucherSampleBarcode](voucherSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of the voucher sample
    * range: [String](types/String.md)
    * inherited from: None
 * [hairSampleContents](hairSampleContents.md)  <sub>OPT</sub>
    * Description: The type(s) of hair collected
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
    * inherited from: None
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
    * inherited from: None
 * [subsampleFate](subsampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a subsample
    * range: [String](types/String.md)
    * inherited from: None
 * [sequenceAnalysisType](sequenceAnalysisType.md)  <sub>OPT</sub>
    * Description: The general type of sequencing to be conducted on a sample
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from spc_perbiogeosample_in:

 * [labProjID](labProjID.md)  <sub>OPT</sub>
    * Description: Identifier for soil physical properties analyses
    * range: [String](types/String.md)
    * inherited from: None
 * [biogeoTotWeight](biogeoTotWeight.md)  <sub>OPT</sub>
    * Description: Total dry weight of the biogeochemistry soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoTotWeight2To5](biogeoTotWeight2To5.md)  <sub>OPT</sub>
    * Description: Total dry weight of the 2-5 mm size fraction of the biogeochemistry soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoTotWeight5To20](biogeoTotWeight5To20.md)  <sub>OPT</sub>
    * Description: Total dry weight of the 5-20 mm size fraction of the biogeochemistry soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoTotWeight20To75](biogeoTotWeight20To75.md)  <sub>OPT</sub>
    * Description: Total dry weight of the 20-75 mm size fraction of the biogeochemistry soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gypsum](gypsum.md)  <sub>OPT</sub>
    * Description: Gypsum content of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [caco3](caco3.md)  <sub>OPT</sub>
    * Description: Carbonate content of the <2 mm fraction experssed as calcium carbonate
    * range: [Double](types/Double.md)
    * inherited from: None
 * [caNh4d](caNh4d.md)  <sub>OPT</sub>
    * Description: Ammonium acetate extractable Calcium from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [kNh4d](kNh4d.md)  <sub>OPT</sub>
    * Description: Ammonium acetate extractable potassium from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [mgNh4d](mgNh4d.md)  <sub>OPT</sub>
    * Description: Ammonium acetate extractable magnesium from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [naNh4d](naNh4d.md)  <sub>OPT</sub>
    * Description: Ammonium acetate extractable sodium from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cecdNh4](cecdNh4.md)  <sub>OPT</sub>
    * Description: Ammonium acetate cation exchange capacity (CEC) of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [alSatCecd33](alSatCecd33.md)  <sub>OPT</sub>
    * Description: Aluminum saturation of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [baseSumCecd10](baseSumCecd10.md)  <sub>OPT</sub>
    * Description: Sum of Ammonium acetate extractable bases from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bsesatCecd10](bsesatCecd10.md)  <sub>OPT</sub>
    * Description: Base saturation of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ececCecd33](ececCecd33.md)  <sub>OPT</sub>
    * Description: Effective cation exchange capacity (CEC) of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [alKcl](alKcl.md)  <sub>OPT</sub>
    * Description: KCl extractable aluminum from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [feKcl](feKcl.md)  <sub>OPT</sub>
    * Description: KCl extractable iron from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [mnKcl](mnKcl.md)  <sub>OPT</sub>
    * Description: KCl extractable manganese from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [phCacl2](phCacl2.md)  <sub>OPT</sub>
    * Description: pH of the <2 mm fraction in CaCl2
    * range: [Double](types/Double.md)
    * inherited from: None
 * [phH2o](phH2o.md)  <sub>OPT</sub>
    * Description: pH of the <2 mm fraction in water
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ec12pre](ec12pre.md)  <sub>OPT</sub>
    * Description: 1:2 Electrical conductivity of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bSatx](bSatx.md)  <sub>OPT</sub>
    * Description: Boron in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [brSatx](brSatx.md)  <sub>OPT</sub>
    * Description: Bromine in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [caSatx](caSatx.md)  <sub>OPT</sub>
    * Description: Calcium in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [clSatx](clSatx.md)  <sub>OPT</sub>
    * Description: Chlorine in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [co3Satx](co3Satx.md)  <sub>OPT</sub>
    * Description: Carbonate in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ecSatp](ecSatp.md)  <sub>OPT</sub>
    * Description: Electrical conductivity of the saturated paste from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [flSatx](flSatx.md)  <sub>OPT</sub>
    * Description: Florine in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [hco3Sx](hco3Sx.md)  <sub>OPT</sub>
    * Description: Bicarbonate in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [kSatx](kSatx.md)  <sub>OPT</sub>
    * Description: Potassium in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [mgSatx](mgSatx.md)  <sub>OPT</sub>
    * Description: Magnesium in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [naSatx](naSatx.md)  <sub>OPT</sub>
    * Description: Sodium in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [no2Satx](no2Satx.md)  <sub>OPT</sub>
    * Description: Nitrite in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [no3Satx](no3Satx.md)  <sub>OPT</sub>
    * Description: Nitrate in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [pSatx](pSatx.md)  <sub>OPT</sub>
    * Description: Phosphate in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [phSp](phSp.md)  <sub>OPT</sub>
    * Description: pH of the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [resist](resist.md)  <sub>OPT</sub>
    * Description: Resistivity of the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [so4Satx](so4Satx.md)  <sub>OPT</sub>
    * Description: Sulfate in the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cTot](cTot.md)  <sub>OPT</sub>
    * Description: Total carbon of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [nTot](nTot.md)  <sub>OPT</sub>
    * Description: Total nitrogen of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sTot](sTot.md)  <sub>OPT</sub>
    * Description: Total sulfur of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [eoc](eoc.md)  <sub>OPT</sub>
    * Description: Estimated organic carbon of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [analysisStartDate](analysisStartDate.md)  <sub>OPT</sub>
    * Description: The start date or dateTime of analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [archiveFate](archiveFate.md)  <sub>OPT</sub>
    * Description: Fate of the Archive sample
    * range: [String](types/String.md)
    * inherited from: None
 * [caco3Conc](caco3Conc.md)  <sub>OPT</sub>
    * Description: Carbonate concentration of the <2 mm fraction expressed as calcium carbonate
    * range: [Double](types/Double.md)
    * inherited from: None
 * [carbonTot](carbonTot.md)  <sub>OPT</sub>
    * Description: Total carbon concentration of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [estimatedOC](estimatedOC.md)  <sub>OPT</sub>
    * Description: Estimated organic carbon concentration of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gypsumConc](gypsumConc.md)  <sub>OPT</sub>
    * Description: Gypsum concentration of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [nitrogenTot](nitrogenTot.md)  <sub>OPT</sub>
    * Description: Total nitrogen concentration of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sulfurTot](sulfurTot.md)  <sub>OPT</sub>
    * Description: Total sulfur concentration of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [waterSatx](waterSatx.md)  <sub>OPT</sub>
    * Description: Water content on a mass basis of the saturation extract from the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoNrcsFate](biogeoNrcsFate.md)  <sub>OPT</sub>
    * Description: Fate of the sample used by NRCS for biogeochemistry measurements
    * range: [String](types/String.md)
    * inherited from: None
 * [sandVeryCoarseContent](sandVeryCoarseContent.md)  <sub>OPT</sub>
    * Description: Very coarse sand (1-2 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [acidity](acidity.md)  <sub>OPT</sub>
    * Description: Extractable acidity measured as the amount of acid neutralized in BaCl2-TEA at pH 8.2
    * range: [Double](types/Double.md)
    * inherited from: None
 * [acidOxalateMethod](acidOxalateMethod.md)  <sub>OPT</sub>
    * Description: Methods used for acid oxalate extraction
    * range: [String](types/String.md)
    * inherited from: None
 * [acidOxalateMethodPub](acidOxalateMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for acid oxalate extraction
    * range: [String](types/String.md)
    * inherited from: None
 * [acidOxalateProcessedDate](acidOxalateProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for acid oxalate extraction
    * range: [Time](types/Time.md)
    * inherited from: None
 * [airDryOvenDryMethod](airDryOvenDryMethod.md)  <sub>OPT</sub>
    * Description: Methods used for air-dried to oven-dried ratio analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [airDryOvenDryMethodPub](airDryOvenDryMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for air-dried to oven-dried ratio analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [airDryOvenDryProcessedDate](airDryOvenDryProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for air-dried to oven-dried ratio analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [airDryOvenDryRatio](airDryOvenDryRatio.md)  <sub>OPT</sub>
    * Description: Airdry to ovendry ratio of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [alCitDithionate](alCitDithionate.md)  <sub>OPT</sub>
    * Description: Dithionite citrate extractable aluminum content, indicates the amount of aluminum substituted for iron in iron oxides, reported as weight percent on the <2mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [alOxalate](alOxalate.md)  <sub>OPT</sub>
    * Description: Total soil Al as estimated by the ammonium oxalate extraction method, reported as weight percent on the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [archiveCode](archiveCode.md)  <sub>OPT</sub>
    * Description: Barcode of the archive sample
    * range: [String](types/String.md)
 * [archiveRemarks](archiveRemarks.md)  <sub>OPT</sub>
    * Description: Remarks from sample archiving
    * range: [String](types/String.md)
    * inherited from: None
 * [Bray1PExtractable](Bray1PExtractable.md)  <sub>OPT</sub>
    * Description: Total phosphorus extracted by the Bray 1 solution
    * range: [Double](types/Double.md)
    * inherited from: None
 * [Bray1PMethod](Bray1PMethod.md)  <sub>OPT</sub>
    * Description: Method used for Bray extraction phosphorus analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [Bray1PMethodPub](Bray1PMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for Bray extraction phosphorus analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [Bray1PProcessedDate](Bray1PProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for Bray extraction phosphorus analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [caco3Method](caco3Method.md)  <sub>OPT</sub>
    * Description: Method used for calcium carbonate analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [caco3MethodPub](caco3MethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for calcium carbonate analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [caco3ProcessedDate](caco3ProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for calcium carbonate analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [cecMethod](cecMethod.md)  <sub>OPT</sub>
    * Description: Method used for cation exchange capacity analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [cecMethodPub](cecMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for cation exchange capacity analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [cecProcessedDate](cecProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for cation exchange capacity analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [citrateDithioMethod](citrateDithioMethod.md)  <sub>OPT</sub>
    * Description: Methods used for citrate dithionate extraction
    * range: [String](types/String.md)
    * inherited from: None
 * [citrateDithioMethodPub](citrateDithioMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for citrate dithionate extraction
    * range: [String](types/String.md)
    * inherited from: None
 * [citrateDithioProcessedDate](citrateDithioProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for citrate dithionate extraction
    * range: [Time](types/Time.md)
    * inherited from: None
 * [ctonRatio](ctonRatio.md)  <sub>OPT</sub>
    * Description: Ratio of total Carbon to total Nitrogen of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ecMethod](ecMethod.md)  <sub>OPT</sub>
    * Description: Method used for electrical conductivity analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [ecMethodPub](ecMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for electrical conductivity analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [ecProcessedDate](ecProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for electrical conductivity analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [extractAcidityMethod](extractAcidityMethod.md)  <sub>OPT</sub>
    * Description: Method used for acidity analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [extractAcidityMethodPub](extractAcidityMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for acidity analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [extractAcidityProcessedDate](extractAcidityProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for acidity analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [feCitDithionate](feCitDithionate.md)  <sub>OPT</sub>
    * Description: Dithionite citrate extractable iron, a general measure of total pedogenic iron, reported as weight percent on the <2mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [feOxalate](feOxalate.md)  <sub>OPT</sub>
    * Description: Total soil noncrystalline iron as measured by the ammonium oxalate extraction method, reported as weight percent on the <2mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [gypsumMethod](gypsumMethod.md)  <sub>OPT</sub>
    * Description: Method used for gypsum analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [gypsumMethodPub](gypsumMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for gypsum analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [gypsumProcessedDate](gypsumProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for gypsum analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [h2oReten15BarMethod](h2oReten15BarMethod.md)  <sub>OPT</sub>
    * Description: Methods used for water retention analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [h2oReten15BarMethodPub](h2oReten15BarMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for water retention analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [h2oReten15BarProcessedDate](h2oReten15BarProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for water retention analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [KClExtractMethod](KClExtractMethod.md)  <sub>OPT</sub>
    * Description: Method used for routine KCl extraction
    * range: [String](types/String.md)
    * inherited from: None
 * [KClExtractMethodPub](KClExtractMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for KCl extraction
    * range: [String](types/String.md)
    * inherited from: None
 * [KClExtractProcessedDate](KClExtractProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for KCl extraction
    * range: [Time](types/Time.md)
    * inherited from: None
 * [MehlichIIIPMethod](MehlichIIIPMethod.md)  <sub>OPT</sub>
    * Description: Method used for Mehlich phosphorus analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [MehlichIIIPMethodPub](MehlichIIIPMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for Mehlich phosphorus analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [MehlichIIIPProcessedDate](MehlichIIIPProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for Mehlich phosphorus analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [MehlichIIITotP](MehlichIIITotP.md)  <sub>OPT</sub>
    * Description: Total phosphorus extracted by the Mehlich III solution
    * range: [Double](types/Double.md)
    * inherited from: None
 * [mnCitDithionate](mnCitDithionate.md)  <sub>OPT</sub>
    * Description: Dithionite citrate extractable manganese content, reported as weight percent on the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [mnOxalate](mnOxalate.md)  <sub>OPT</sub>
    * Description: Total soil manganese content fraction held in noncrystalline compounds as measured by the ammonium oxalate extraction method and reported as milligrams per kilogram on a <2 mm base
    * range: [Double](types/Double.md)
    * inherited from: None
 * [OlsenPExtractable](OlsenPExtractable.md)  <sub>OPT</sub>
    * Description: Total phosphorus extracted by the Olsen solution
    * range: [Double](types/Double.md)
    * inherited from: None
 * [OlsenPMethod](OlsenPMethod.md)  <sub>OPT</sub>
    * Description: Method used for Olsen phosphorus analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [OlsenPMethodPub](OlsenPMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for Olsen phosphorus analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [OlsenPProcessedDate](OlsenPProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for Olsen phosphorus analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [optDensityOxalate](optDensityOxalate.md)  <sub>OPT</sub>
    * Description: Optical density of the ammonium oxalate soil extract
    * range: [Double](types/Double.md)
    * inherited from: None
 * [pOxalate](pOxalate.md)  <sub>OPT</sub>
    * Description: Soil phosphorus measured by the ammonium oxalate extraction method
    * range: [Double](types/Double.md)
    * inherited from: None
 * [processingRemarks](processingRemarks.md)  <sub>OPT</sub>
    * Description: Remarks from sample processing
    * range: [String](types/String.md)
    * inherited from: None
 * [routinepHProcessedDate](routinepHProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for routine pH analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [routinepHMethod](routinepHMethod.md)  <sub>OPT</sub>
    * Description: Method used for routine pH analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [routinepHMethodPub](routinepHMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for routine pH analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [satPasteMethod](satPasteMethod.md)  <sub>OPT</sub>
    * Description: Method used for saturated paste analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [satPasteMethodPub](satPasteMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for saturated paste analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [satPasteProcessedDate](satPasteProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for saturated paste analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [siliconCitrateDithionate](siliconCitrateDithionate.md)  <sub>OPT</sub>
    * Description: Dithionite citrate extractable silicon, reported as weight percent on the <2mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [siOxalate](siOxalate.md)  <sub>OPT</sub>
    * Description: Total soil silica content as measured by the ammonium oxalate extraction method, reported as a weight percent on a <2 mm base
    * range: [Double](types/Double.md)
    * inherited from: None
 * [TotalNCSMethod](TotalNCSMethod.md)  <sub>OPT</sub>
    * Description: Methods used for total carbon, nitrogen and sulfur analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [TotalNCSMethodPub](TotalNCSMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for total carbon, nitrogen and sulfur analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [TotalNCSProcessedDate](TotalNCSProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for total carbon, nitrogen and sulfur analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [waterRetention15Bar](waterRetention15Bar.md)  <sub>OPT</sub>
    * Description: Water content after equilibration at 15 bars water tension, reported as gravimetric percent on the <2 mm fraction
    * range: [Double](types/Double.md)
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
    * inherited from: None
 * [scientificName](scientificName.md)  <sub>OPT</sub>
    * Description: Scientific name, associated with the taxonID. This is the name of the lowest level taxonomic rank that can be determined
    * range: [String](types/String.md)
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
    * inherited from: None
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [endDate](endDate.md)  <sub>OPT</sub>
    * Description: The end date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
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
| **Mappings:** | | neon:scs_archivedata_in |

