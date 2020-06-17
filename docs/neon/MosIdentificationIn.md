
# Type: mos_identification_in




URI: [neon:MosIdentificationIn](https://data.neonscience.org/MosIdentificationIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


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

### Inherited from fsp_sampleMetadata_in:

 * [individualFate](individualFate.md)  <sub>OPT</sub>
    * Description: Fate of a tagged individual
    * range: [String](types/String.md)

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
    * inherited from: None
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
    * inherited from: None
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

### Inherited from mos_archivepooling_pub:

 * [archiveVialIDList](archiveVialIDList.md)  <sub>OPT</sub>
    * Description: Identifier(s) for the vial(s) containing specimens for archive
    * range: [String](types/String.md)
    * inherited from: None
 * [archivedCount](archivedCount.md)  <sub>OPT</sub>
    * Description: Number of individuals in the archive vial
    * range: [String](types/String.md)
    * inherited from: None
 * [archiveIDCode](archiveIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of the Archive sample
    * range: [String](types/String.md)

### Inherited from mos_expertTaxonomistIDRaw_pub:

 * [individualIDList](individualIDList.md)  <sub>OPT</sub>
    * Description: List of individualIDs
    * range: [String](types/String.md)

### Inherited from mos_pathogenresults_in:

 * [sampleCompromised](sampleCompromised.md)  <sub>OPT</sub>
    * Description: Indicator of compromised sample integrity; 'other' requires further specification in remarks
    * range: [String](types/String.md)
 * [testingVialIDFate](testingVialIDFate.md)  <sub>OPT</sub>
    * Description: Fate of the vial containing specimens for testing (e.g., pathogen testing, chemical analysis, etc.)
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
    * inherited from: None
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

### Inherited from tck_pathogen_pub:

 * [testingID](testingID.md)  <sub>OPT</sub>
    * Description: Identifier for the group of specimens for testing
    * range: [String](types/String.md)
 * [testResult](testResult.md)  <sub>OPT</sub>
    * Description: Result of the test
    * range: [String](types/String.md)
    * inherited from: None
 * [testPathogenName](testPathogenName.md)  <sub>OPT</sub>
    * Description: The name of the pathogen
    * range: [String](types/String.md)
    * inherited from: None
 * [testedBy](testedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who tested the sample
    * range: [String](types/String.md)
    * inherited from: None
 * [testingIDCode](testingIDCode.md)  <sub>OPT</sub>
    * Description: Barcode of a test sample
    * range: [String](types/String.md)

### Inherited from tck_pathogenresults_in:

 * [testingIDFate](testingIDFate.md)  <sub>OPT</sub>
    * Description: Fate of a test sample
    * range: [String](types/String.md)

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
| **Mappings:** | | neon:mos_identification_in |

