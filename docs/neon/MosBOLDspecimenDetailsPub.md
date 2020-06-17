
# Type: mos_BOLDspecimenDetails_pub




URI: [neon:MosBOLDspecimenDetailsPub](https://data.neonscience.org/MosBOLDspecimenDetailsPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [extraInfo](extraInfo.md)  <sub>OPT</sub>
    * Description: A brief note or project term associated with the specimen for rapid analysis
    * range: [String](types/String.md)
 * [notes](notes.md)  <sub>OPT</sub>
    * Description: General notes regarding the specimen
    * range: [String](types/String.md)
 * [tissueDescriptor](tissueDescriptor.md)  <sub>OPT</sub>
    * Description: A brief description of the type of tissue or material analyzed
    * range: [String](types/String.md)

### Inherited from csd_pressureGaugeRelationship_pub:

 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
    * inherited from: None
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
    * inherited from: None
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
    * inherited from: None
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
 * [associatedTaxa](associatedTaxa.md)  <sub>OPT</sub>
    * Description: A list of taxa associated with the taxon at the time of its collection. References to taxa are preceded by the relationship
    * range: [String](types/String.md)
 * [externalURLs](externalURLs.md)  <sub>OPT</sub>
    * Description: Pipe-delimited list of web accessible links that provide additional information about the specimen
    * range: [String](types/String.md)
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

### Inherited from soni_L0prime:

 * [veloXaxs](veloXaxs.md)  <sub>OPT</sub>
    * Description: Linear velocity (velo) of wind in 3-D sonic anemometer along-axis direction (Xaxs), positive backward
    * range: [Double](types/Double.md)
    * inherited from: None
 * [veloYaxs](veloYaxs.md)  <sub>OPT</sub>
    * Description: Linear velocity (velo) of wind in 3-D sonic anemometer cross-axis direction (Yaxs), positive right
    * range: [Double](types/Double.md)
    * inherited from: None
 * [veloZaxs](veloZaxs.md)  <sub>OPT</sub>
    * Description: Linear velocity (velo) of wind in 3-D sonic anemometer vertical-axis direction (Zaxs), positive upwards
    * range: [Double](types/Double.md)
    * inherited from: None
 * [veloSoni](veloSoni.md)  <sub>OPT</sub>
    * Description: Linear velocity (velo) of sound (Soni)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [tempSoni](tempSoni.md)  <sub>OPT</sub>
    * Description: Sonic temperature (TSONIC)
    * range: [String](types/String.md)
    * inherited from: None
 * [qfSoniCode](qfSoniCode.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o5: Wrong embedded sensor code)
    * range: [String](types/String.md)
    * inherited from: None
 * [voucherStatus](voucherStatus.md)  <sub>OPT</sub>
    * Description: Status of the specimen in an accessioning process
    * range: [String](types/String.md)
 * [qfSoniSignalLow](qfSoniSignalLow.md)  <sub>OPT</sub>
    * Description: Sensor signal flag (QFSONIC s4 Low signal amplitude)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniUnrs](qfSoniUnrs.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o1: Sensor unresponsive)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniData](qfSoniData.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o2: No data available)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniTrig](qfSoniTrig.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o3: Sensor trigger source lost)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniComm](qfSoniComm.md)  <sub>OPT</sub>
    * Description: Sensor error flag (QFSONIC,o4: SDM communications error)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniTemp](qfSoniTemp.md)  <sub>OPT</sub>
    * Description: Sensor signal flag (QFSONIC,s1: Axes TSONIC difference > 4K)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniSignalPoor](qfSoniSignalPoor.md)  <sub>OPT</sub>
    * Description: Sensor signal flag (QFSONIC,s2: Poor signal lock)
    * range: [Integer](types/Integer.md)
    * inherited from: None
 * [qfSoniSignalHigh](qfSoniSignalHigh.md)  <sub>OPT</sub>
    * Description: Sensor signal flag (QFSONIC,s3: High signal amplitude)
    * range: [Integer](types/Integer.md)
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
| **Mappings:** | | neon:mos_BOLDspecimenDetails_pub |

