
# Type: cfc_foliarStableIsotopes_pub




URI: [neon:CfcFoliarStableIsotopesPub](https://data.neonscience.org/CfcFoliarStableIsotopesPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Inherited from apl_taxonomyProcessed_pub:

 * [scientificNameAuthorship](scientificNameAuthorship.md)  <sub>OPT</sub>
    * Description: Name of the individual(s) who designated the scientific name of the taxon
    * range: [String](types/String.md)
    * inherited from: None
 * [testMethod](testMethod.md)  <sub>OPT</sub>
    * Description: Method used to conduct test
    * range: [String](types/String.md)
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
 * [analyzedBy](analyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample
    * range: [String](types/String.md)
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

### Inherited from fsp_boutMetadata_pub:

 * [instrument](instrument.md)  <sub>OPT</sub>
    * Description: Type of instrument used for the analysis
    * range: [String](types/String.md)
 * [wavelengthIncrement](wavelengthIncrement.md)  <sub>OPT</sub>
    * Description: Increment size of wavelength
    * range: [Double](types/Double.md)
    * inherited from: None
 * [fieldSpectrometerSettings](fieldSpectrometerSettings.md)  <sub>OPT</sub>
    * Description: Settings used in the field spectrometer software
    * range: [String](types/String.md)
    * inherited from: None
 * [foreopticConnection](foreopticConnection.md)  <sub>OPT</sub>
    * Description: Foreoptic connection used to make measurements
    * range: [String](types/String.md)
    * inherited from: None
 * [foreopticType](foreopticType.md)  <sub>OPT</sub>
    * Description: Type of foreoptic used to make measurements
    * range: [String](types/String.md)
    * inherited from: None
 * [lightSource](lightSource.md)  <sub>OPT</sub>
    * Description: Description of the light source used for measurements
    * range: [String](types/String.md)
    * inherited from: None
 * [measurementQuantity](measurementQuantity.md)  <sub>OPT</sub>
    * Description: Type of measurement
    * range: [String](types/String.md)
    * inherited from: None
 * [measurementUnits](measurementUnits.md)  <sub>OPT</sub>
    * Description: Units of measurement
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from fsp_spectralData_pub:

 * [reviewedBy](reviewedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel who reviewed the data prior to submission
    * range: [String](types/String.md)
 * [downloadFileName](downloadFileName.md)  <sub>OPT</sub>
    * Description: The name of the user-downloaded file that is linked to the record
    * range: [String](types/String.md)
    * inherited from: None
 * [downloadFileUrl](downloadFileUrl.md)  <sub>OPT</sub>
    * Description: The URL of the file linked to the record
    * range: [String](types/String.md)
    * inherited from: None
 * [software](software.md)  <sub>OPT</sub>
    * Description: Name and version of the software used to process the data
    * range: [String](types/String.md)
    * inherited from: None
 * [spectralSampleCode](spectralSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a spectral sample
    * range: [String](types/String.md)
    * inherited from: None
 * [spectralSampleID](spectralSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a spectral sample
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

### Inherited from ltr_chemistrySubsampling_pub:

 * [cnSampleCode](cnSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a carbon-nitrogen sample
    * range: [String](types/String.md)
 * [cnSampleID](cnSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a carbon-nitrogen sample
    * range: [String](types/String.md)
 * [archiveSampleBarcode](archiveSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for an archive sample
    * range: [String](types/String.md)
    * inherited from: None
 * [archiveSampleID](archiveSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for an archive sample
    * range: [String](types/String.md)
    * inherited from: None
 * [massSampleBarcodeList](massSampleBarcodeList.md)  <sub>OPT</sub>
    * Description: List of barcodes of mass samples
    * range: [String](types/String.md)
    * inherited from: None
 * [massSampleIDList](massSampleIDList.md)  <sub>OPT</sub>
    * Description: List of unique identifiers for mass samples
    * range: [String](types/String.md)
    * inherited from: None
 * [massSampleMixtureBarcode](massSampleMixtureBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of a mixture of mass samples
    * range: [String](types/String.md)
    * inherited from: None
 * [massSampleMixtureID](massSampleMixtureID.md)  <sub>OPT</sub>
    * Description: Identifier for a mixture of mass samples
    * range: [String](types/String.md)
    * inherited from: None
 * [toxicodendronPossible](toxicodendronPossible.md)  <sub>OPT</sub>
    * Description: Indicator for whether a sample may contain Toxicodendron spp
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from ltr_ligninBatchQA_in:

 * [analysisEndDate](analysisEndDate.md)  <sub>OPT</sub>
    * Description: The end date or dateTime of analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [analyticalRepNumber](analyticalRepNumber.md)  <sub>OPT</sub>
    * Description: Number of the analytical replicate
    * range: [String](types/String.md)
 * [celluloseKnown](celluloseKnown.md)  <sub>OPT</sub>
    * Description: Known percent cellulose in quality assurance material or standard on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [cellulosePercent](cellulosePercent.md)  <sub>OPT</sub>
    * Description: Percent cellulose on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ligninKnown](ligninKnown.md)  <sub>OPT</sub>
    * Description: Known percent lignin in quality assurance material or standard on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [ligninPercent](ligninPercent.md)  <sub>OPT</sub>
    * Description: Percent lignin on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [qaMaterialQF](qaMaterialQF.md)  <sub>OPT</sub>
    * Description: Quality flag for the quality assurance material
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from ltr_litterStableIsotopes_pub:

 * [d13C](d13C.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of 13C:12C in a sample, relative to Vienna Pee Dee Belemnite
    * range: [Double](types/Double.md)

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
    * inherited from: None
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

### Inherited from sls_soilStableIsotopes_pub:

 * [cnIsotopeQF](cnIsotopeQF.md)  <sub>OPT</sub>
    * Description: Quality flag for stable isotope values outside the calibration range
    * range: [String](types/String.md)
 * [d15N](d15N.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of 15N:14N in a sample, relative to atmospheric N2
    * range: [Double](types/Double.md)
 * [isotopeAccuracyQF](isotopeAccuracyQF.md)  <sub>OPT</sub>
    * Description: Quality flag for accuracy of stable isotope values of QA materials associated with the run
    * range: [String](types/String.md)
 * [organicd13C](organicd13C.md)  <sub>OPT</sub>
    * Description: Measure of the ratio of 13C:12C in soil organic carbon, relative to Vienna Pee Dee Belemnite
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
| **Mappings:** | | neon:cfc_foliarStableIsotopes_pub |
| **In Subsets:** | | DP1.10053.001 |

