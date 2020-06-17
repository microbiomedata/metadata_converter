
# Type: sls_soilCoreCollection_pub




URI: [neon:SlsSoilCoreCollectionPub](https://data.neonscience.org/SlsSoilCoreCollectionPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [coreCoordinateX](coreCoordinateX.md)  <sub>OPT</sub>
    * Description: x location of the soil core relative to the SW corner
    * range: [Double](types/Double.md)
 * [coreCoordinateY](coreCoordinateY.md)  <sub>OPT</sub>
    * Description: y location of the soil core relative to the SW corner
    * range: [Double](types/Double.md)
 * [geneticArchiveSample1Code](geneticArchiveSample1Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 1
    * range: [String](types/String.md)
 * [geneticArchiveSample1ID](geneticArchiveSample1ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 1
    * range: [String](types/String.md)
 * [geneticArchiveSample2Code](geneticArchiveSample2Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 2
    * range: [String](types/String.md)
 * [geneticArchiveSample2ID](geneticArchiveSample2ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 2
    * range: [String](types/String.md)
 * [geneticArchiveSample3Code](geneticArchiveSample3Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 3
    * range: [String](types/String.md)
 * [geneticArchiveSample3ID](geneticArchiveSample3ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 3
    * range: [String](types/String.md)
 * [geneticArchiveSample4Code](geneticArchiveSample4Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 4
    * range: [String](types/String.md)
 * [geneticArchiveSample4ID](geneticArchiveSample4ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 4
    * range: [String](types/String.md)
 * [geneticArchiveSample5Code](geneticArchiveSample5Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 5
    * range: [String](types/String.md)
 * [geneticArchiveSample5ID](geneticArchiveSample5ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 5
    * range: [String](types/String.md)
 * [geneticSampleCondition](geneticSampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of genetic sample storage or processing
    * range: [String](types/String.md)
 * [incubationCondition](incubationCondition.md)  <sub>OPT</sub>
    * Description: Condition of incubated nitrogen transformation sample upon retrieval
    * range: [String](types/String.md)
 * [incubationMethod](incubationMethod.md)  <sub>OPT</sub>
    * Description: Method used for soil incubation
    * range: [String](types/String.md)
 * [litterDepth](litterDepth.md)  <sub>OPT</sub>
    * Description: Depth of litter layer
    * range: [Double](types/Double.md)
 * [sampleBottomDepth](sampleBottomDepth.md)  <sub>OPT</sub>
    * Description: Depth below the soil surface of the bottom of a soil sample
    * range: [Double](types/Double.md)
 * [sampleExtent](sampleExtent.md)  <sub>OPT</sub>
    * Description: Extent of the soil sample relative to the local soil horizon conditions
    * range: [String](types/String.md)
 * [sampleTopDepth](sampleTopDepth.md)  <sub>OPT</sub>
    * Description: Depth below the soil surface of the top of a soil sample
    * range: [Double](types/Double.md)
 * [soilCoreCount](soilCoreCount.md)  <sub>OPT</sub>
    * Description: Number of soil cores combined per sample
    * range: [String](types/String.md)
 * [soilSamplingDevice](soilSamplingDevice.md)  <sub>OPT</sub>
    * Description: Type of soil collection device used for sampling
    * range: [String](types/String.md)
 * [soilTemp](soilTemp.md)  <sub>OPT</sub>
    * Description: In-situ temperature of soil at approximately 10 cm depth
    * range: [Double](types/Double.md)
 * [standingWaterDepth](standingWaterDepth.md)  <sub>OPT</sub>
    * Description: Depth of standing water present at a sampling location
    * range: [Double](types/Double.md)

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

### Inherited from inv_dnaExtractionStandard_pub:

 * [deprecatedVialID](deprecatedVialID.md)  <sub>OPT</sub>
    * Description: Identifier on vial label, if different from standard ID
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticSampleID](geneticSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for the genetic sample
    * range: [String](types/String.md)
 * [geneticSampleCode](geneticSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a genetic sample
    * range: [String](types/String.md)
 * [nucleicAcidConcentration](nucleicAcidConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of extracted nucleic acids
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sampleMaterial](sampleMaterial.md)  <sub>OPT</sub>
    * Description: The material in which a sample was embedded prior to the sampling event
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleMass](sampleMass.md)  <sub>OPT</sub>
    * Description: Mass of sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [dnaPooledStatus](dnaPooledStatus.md)  <sub>OPT</sub>
    * Description: Indicates whether multiple DNA extracts were pooled
    * range: [String](types/String.md)
    * inherited from: None
 * [dnaProcessedBy](dnaProcessedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the individual who processed the sample(s)
    * range: [String](types/String.md)
    * inherited from: None
 * [nucleicAcidQuantMethod](nucleicAcidQuantMethod.md)  <sub>OPT</sub>
    * Description: Nucleic acid quantitative method
    * range: [String](types/String.md)
    * inherited from: None
 * [nucleicAcidPurity](nucleicAcidPurity.md)  <sub>OPT</sub>
    * Description: Purity of nucleic acid sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [standardCreationLocation](standardCreationLocation.md)  <sub>OPT</sub>
    * Description: Name of the location where the standard sample was created
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

### Inherited from mam_perplotnight_pub:

 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)

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
    * inherited from: None
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
 * [plotType](plotType.md)  <sub>OPT</sub>
    * Description: NEON plot type in which sampling occurred: tower, distributed or gradient
    * range: [String](types/String.md)
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

### Inherited from mos_trapping_pub:

 * [sampleTiming](sampleTiming.md)  <sub>OPT</sub>
    * Description: Timing of the sampling event with regard to the field season
    * range: [String](types/String.md)
 * [fanStatus](fanStatus.md)  <sub>OPT</sub>
    * Description: Indicator of the status of the trap fan at the time of sample collection
    * range: [String](types/String.md)
    * inherited from: None
 * [catchCupStatus](catchCupStatus.md)  <sub>OPT</sub>
    * Description: Indicator of the status of the trap catch cup at the time of sample collection
    * range: [String](types/String.md)
    * inherited from: None
 * [dryIceStatus](dryIceStatus.md)  <sub>OPT</sub>
    * Description: Dry ice status at the time of sample collection
    * range: [String](types/String.md)
    * inherited from: None
 * [nightOrDay](nightOrDay.md)  <sub>OPT</sub>
    * Description: Whether sampling occurred primarily during the day or at night
    * range: [String](types/String.md)
    * inherited from: None
 * [trapHours](trapHours.md)  <sub>OPT</sub>
    * Description: Number of hours between trap setting and collecting events
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from ntr_internalLab_in:

 * [nTransBoutType](nTransBoutType.md)  <sub>OPT</sub>
    * Description: Category of bout in relation to nitrogen transformation sample collection
    * range: [String](types/String.md)
 * [incubationLength](incubationLength.md)  <sub>OPT</sub>
    * Description: Length of soil incubation
    * range: [Double](types/Double.md)
    * inherited from: None
 * [incubationPairID](incubationPairID.md)  <sub>OPT</sub>
    * Description: Identifier for a linked pair of soil samples used to measure net nitrogen transformation rates
    * range: [String](types/String.md)
    * inherited from: None
 * [kclBatchNumber](kclBatchNumber.md)  <sub>OPT</sub>
    * Description: Potassium chloride (KCl) batch number used to extract a set of samples
    * range: [String](types/String.md)
    * inherited from: None
 * [kclVolume](kclVolume.md)  <sub>OPT</sub>
    * Description: Volume potassium chloride (KCl) used to extract soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [soilFreshMass](soilFreshMass.md)  <sub>OPT</sub>
    * Description: Total fresh mass of soil
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from sls_bgcSubsampling_pub:

 * [bgcArchiveCode](bgcArchiveCode.md)  <sub>OPT</sub>
    * Description: Barcode of a biogeochemistry archive sample
    * range: [String](types/String.md)
    * inherited from: None
 * [bgcArchiveID](bgcArchiveID.md)  <sub>OPT</sub>
    * Description: Identifier for a biogeochemistry archive sample
    * range: [String](types/String.md)
    * inherited from: None
 * [horizon](horizon.md)  <sub>OPT</sub>
    * Description: Organic or mineral soil
    * range: [String](types/String.md)
 * [bgcDataQF](bgcDataQF.md)  <sub>OPT</sub>
    * Description: Quality flag for biogeochemistry sample
    * range: [String](types/String.md)
    * inherited from: None
 * [bgcRemarks](bgcRemarks.md)  <sub>OPT</sub>
    * Description: Remarks from biogeochemistry subsample processing
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from sme_microbialBiomass_pub:

 * [biomassCode](biomassCode.md)  <sub>OPT</sub>
    * Description: Barcode of biomass sample
    * range: [String](types/String.md)
 * [biomassID](biomassID.md)  <sub>OPT</sub>
    * Description: Identifier for biomass sample
    * range: [String](types/String.md)
 * [freshMass](freshMass.md)  <sub>OPT</sub>
    * Description: Total fresh mass of a sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid2OH10To0Concentration](lipid2OH10To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 2-hydroxydecanoate, 2OH10:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid2OH12To0Concentration](lipid2OH12To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 2-hydroxydodecanoate, 2OH12:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid2OH14To0Concentration](lipid2OH14To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 2-hydroxytetradecanoate, 2OH14:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid2OH16To0Concentration](lipid2OH16To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 2-hydroxyhexadecanoate, 2OH16:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid3OH12To0Concentration](lipid3OH12To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 3-hydroxydodecanoate, 3OH12:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid3OH14To0Concentration](lipid3OH14To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 3-hydroxytetradecanoate, 3OH14:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [aC15To0Concentration](aC15To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of 12-methyltetradecanoic acid methyl ester, a-c15:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c10To0Concentration](c10To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of decanoate methyl ester, c10:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c11To0Concentration](c11To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of undecanoate methyl ester, c11:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c12To0Concentration](c12To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of dodecanoic acid, or lauric acid, methyl ester, c12:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c13To0Concentration](c13To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of tridecanoic acid methyl ester, c13:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c14To0Concentration](c14To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of tetradecanoic acid, or myristic acid, methyl ester, c14:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c14To1Concentration](c14To1Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-9-tetradecenoic acid, or myristoleic acid, methyl ester, c14:1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c15To0Concentration](c15To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of pentadecanoic acid methyl ester, c15:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c15To1Concentration](c15To1Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-10-pentadecenoic acid methyl ester, c15:1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c16To0Concentration](c16To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of hexadecanoic acid, or palmitic acid, methyl ester, c16:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c17To0Concentration](c17To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of heptadecanoic acid methyl ester, c17:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c17To1Concentration](c17To1Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-10-Heptadecenoic acid methyl ester, c17:1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c18To0Concentration](c18To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of octadecanoic acid, or stearic acid, methyl ester, c18:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c18To1n11Concentration](c18To1n11Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of vaccenic acid or e-octadec-11-enoic acid, c18:1n11
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c18To3n3Concentration](c18To3n3Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis,cis,cis-9,12,15-octadecatrienoic acid, or alpha-linolenic acid, methyl ester, c18:3n3
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c18To3n6Concentration](c18To3n6Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of 6,9,12-octadecatrienoic acid, or gamma-linolenic acid, methyl ester, c18:3n6
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c19To0Concentration](c19To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of nonadecanoic acid methyl ester, c19:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To0Concentration](c20To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of arachidic acid methyl ester, c20:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To1Concentration](c20To1Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-11-eicosenoic acid methyl ester, c20:1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To2Concentration](c20To2Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-11,14-eicosadienoic acid methyl ester, c20:2
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To3n3Concentration](c20To3n3Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-11,14,17-eicosatrienoic acid methyl ester, c20:3n3
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To3n6Concentration](c20To3n6Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-8,11,14-eicosatrienoic acid, or dihomo-gamma-linoleic acid, methyl ester, c20:3n6
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To4n6Concentration](c20To4n6Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-5,8,11,14-eicosatetraenoic acid, or arachidonic acid, methyl ester, c20:4n6
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c20To5n3Concentration](c20To5n3Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-5,8,11,14,17-eicosapentaenoic acid, or eicosapentaenoic acid, methyl ester, c20:5n3
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c21To0Concentration](c21To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of heneicosanoic acid methyl ester, c21:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c22To0Concentration](c22To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of docosanoic acid methyl ester, c22:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c22To1n9Concentration](c22To1n9Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-13-docosenoic acid, or erucic acid, methyl ester, c22:1n9
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c22To2Concentration](c22To2Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-13,16-docosadienoic acid methyl ester, c22:2
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c23To0Concentration](c23To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of tricosanoic acid methyl ester, c23:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c24To0Concentration](c24To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of tetracosanoic acid, or lignoceric acid, methyl ester, c24:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c24To1Concentration](c24To1Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-15-tetracosenoic acid, c24:1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c8To0Concentration](c8To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of octanoate methyl ester, c8:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cis16To1n9Concentration](cis16To1n9Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl hexadecenoic acid, or palmitoleic acid, methyl ester, c16:1n9
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cis18To1n9Concentration](cis18To1n9Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-9-octadecenoic acid, or oleic acid, methyl ester, cis18:1n9
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cis18To2n912Concentration](cis18To2n912Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis,cis-9,12-octadecadienoic acid, or linoleic acid, or 18To2-omega-6, methyl ester, cis18:2n9-12
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cyclo17To0Concentration](cyclo17To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of the cyclopropyl C17To0 fatty acid methyl cis-9,10-methylenehexadecanoate, cyclo17:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cyclo19To0Concentration](cyclo19To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of the cyclopropyl C19To0 fatty acid methyl cis-9,10-methyleneoctadecanoate, cyclo19:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [extractionEfficiency](extractionEfficiency.md)  <sub>OPT</sub>
    * Description: Efficiency of sample extraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [freezeDryMass](freezeDryMass.md)  <sub>OPT</sub>
    * Description: Mass of sample after freeze drying
    * range: [Double](types/Double.md)
    * inherited from: None
 * [i15To0Concentration](i15To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of 13-methyltetradecanoic acid methyl ester, i15:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [i16To0Concentration](i16To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 14-methylpentadecanoate, i16:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [i17To0Concentration](i17To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 15-methylhexadecanoate, i17:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [trans18To1n9Concentration](trans18To1n9Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of trans-9-octadecenoic acid, or elaidic acid, methyl ester, trans18:1n9
    * range: [Double](types/Double.md)
    * inherited from: None
 * [trans18To2n912Concentration](trans18To2n912Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of trans-trans-9,12-octadecadienoic acid, or linoelaidic acid, methyl ester, trans18:2n9-12
    * range: [Double](types/Double.md)
    * inherited from: None
 * [totalLipidConcentration](totalLipidConcentration.md)  <sub>OPT</sub>
    * Description: Total lipid concentration calculated as the sum of all measured individual lipid components
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c16To1Cis11Concentration](c16To1Cis11Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl cis-11-hexadecenoate, 16:1 cis 11
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c17To0AnteisoConcentration](c17To0AnteisoConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 14-methyl-pentadecanoate, 17:0 anteiso
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c19To1Cis10Concentration](c19To1Cis10Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-10-nonadecenoic acid, methyl ester, c18:1
    * range: [Double](types/Double.md)
    * inherited from: None
 * [c22To6CisConcentration](c22To6CisConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of cis-4,7,10,13,16,19-docosahexaenoic acid, methyl ester
    * range: [Double](types/Double.md)
    * inherited from: None
 * [i14To0Concentration](i14To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of tridecanoic acid, 12-methyl-, methyl ester, iso-14:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid10Methyl16To0Concentration](lipid10Methyl16To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of methyl 10-methyl-hexadecanoate, 10 Me-16:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid10Methyl17To0Concentration](lipid10Methyl17To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of heptadecanoic acid methyl ester, 10 Me-17:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [lipid10Methyl18To0Concentration](lipid10Methyl18To0Concentration.md)  <sub>OPT</sub>
    * Description: Concentration of tuberculostearic acid methyl ester, 10 Me-18:0
    * range: [Double](types/Double.md)
    * inherited from: None
 * [extractEffStdConc](extractEffStdConc.md)  <sub>OPT</sub>
    * Description: Concentration of lipid standard used for measuring extraction efficiency with units defined by the analytical laboratory
    * range: [Double](types/Double.md)
    * inherited from: None
 * [analysisResultsQF](analysisResultsQF.md)  <sub>OPT</sub>
    * Description: Quality flag for sample analysis results
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from vst_perplotperyear_pub:

 * [plotSize](plotSize.md)  <sub>OPT</sub>
    * Description: Size (in square meters) of the plot or grid
    * range: [Double](types/Double.md)
    * inherited from: None
 * [easting](easting.md)  <sub>OPT</sub>
    * Description: Geographic coordinate specifying the east-west position of a point on the Earth's surface (Universal Transverse Mercator, UTM)
    * range: [Double](types/Double.md)
 * [northing](northing.md)  <sub>OPT</sub>
    * Description: Geographic coordinate specifying the north-south position of a point on the Earth's surface (Universal Transverse Mercator, UTM)
    * range: [Double](types/Double.md)
 * [utmZone](utmZone.md)  <sub>OPT</sub>
    * Description: UTM zone
    * range: [String](types/String.md)

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
| **Mappings:** | | neon:sls_soilCoreCollection_pub |
| **In Subsets:** | | DP1.10086.001 |

