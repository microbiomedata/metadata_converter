
# Type: ntr_externalLab_in




URI: [neon:NtrExternalLabIn](https://data.neonscience.org/NtrExternalLabIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [ammoniumNAnalysisDate](ammoniumNAnalysisDate.md)  <sub>OPT</sub>
    * Description: Date an ammonium sample was analyzed
    * range: [Time](types/Time.md)
 * [ammoniumNAnalyzedBy](ammoniumNAnalyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample for ammonium N
    * range: [String](types/String.md)
 * [ammoniumNInstrument](ammoniumNInstrument.md)  <sub>OPT</sub>
    * Description: Type of instrument used for ammonium analysis
    * range: [String](types/String.md)
 * [ammoniumNMethod](ammoniumNMethod.md)  <sub>OPT</sub>
    * Description: Method used to test sample for ammonium N concentration
    * range: [String](types/String.md)
 * [ammoniumNQF](ammoniumNQF.md)  <sub>OPT</sub>
    * Description: Quality flag for ammonium N values
    * range: [String](types/String.md)
 * [ammoniumNRemarks](ammoniumNRemarks.md)  <sub>OPT</sub>
    * Description: Free text comments accompanying the ammonium record
    * range: [String](types/String.md)
 * [ammoniumNRepNum](ammoniumNRepNum.md)  <sub>OPT</sub>
    * Description: Analytical replicate number for ammonium sample
    * range: [String](types/String.md)
 * [ammoniumNReviewedBy](ammoniumNReviewedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel who reviewed ammonium N data prior to submission
    * range: [String](types/String.md)
 * [ammoniumNRunID](ammoniumNRunID.md)  <sub>OPT</sub>
    * Description: A linking value that associates the ammonium sample data to the run metadata, including QA values
    * range: [String](types/String.md)
 * [kclAmmoniumNConc](kclAmmoniumNConc.md)  <sub>OPT</sub>
    * Description: Concentration of ammonium N in a potassium chloride extract
    * range: [Double](types/Double.md)
 * [kclNitrateNitriteNConc](kclNitrateNitriteNConc.md)  <sub>OPT</sub>
    * Description: Concentration of nitrate + nitrite N in a potassium chloride extract
    * range: [Double](types/Double.md)
 * [kclSampleCode](kclSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a potassium chloride (KCl) extract sample
    * range: [String](types/String.md)
 * [kclSampleFate](kclSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a potassium chloride (KCl) extract sample
    * range: [String](types/String.md)
 * [kclSampleID](kclSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a potassium chloride (KCl) extract sample
    * range: [String](types/String.md)
 * [nitrateNitriteNAnalysisDate](nitrateNitriteNAnalysisDate.md)  <sub>OPT</sub>
    * Description: Date a nitrate + nitrite N sample was analyzed
    * range: [Time](types/Time.md)
 * [nitrateNitriteNAnalyzedBy](nitrateNitriteNAnalyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample for nitrate + nitrite N
    * range: [String](types/String.md)
 * [nitrateNitriteNInstrument](nitrateNitriteNInstrument.md)  <sub>OPT</sub>
    * Description: Type of instrument used for nitrate + nitrite N analysis
    * range: [String](types/String.md)
 * [nitrateNitriteNMethod](nitrateNitriteNMethod.md)  <sub>OPT</sub>
    * Description: Method used to test sample for nitrate + nitrite N concentration
    * range: [String](types/String.md)
 * [nitrateNitriteNQF](nitrateNitriteNQF.md)  <sub>OPT</sub>
    * Description: Quality flag for nitrate + nitrite N values
    * range: [String](types/String.md)
 * [nitrateNitriteNRemarks](nitrateNitriteNRemarks.md)  <sub>OPT</sub>
    * Description: Free text comments accompanying the nitrate + nitrite N record
    * range: [String](types/String.md)
 * [nitrateNitriteNRepNum](nitrateNitriteNRepNum.md)  <sub>OPT</sub>
    * Description: Analytical replicate number for nitrate + nitrite N sample
    * range: [String](types/String.md)
 * [nitrateNitriteNReviewedBy](nitrateNitriteNReviewedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel who reviewed nitrite + nitrate N data prior to submission
    * range: [String](types/String.md)
 * [nitrateNitriteNRunID](nitrateNitriteNRunID.md)  <sub>OPT</sub>
    * Description: a linking value provided by the external lab that associates the nitrate plus nitrite to the run metadata
    * range: [String](types/String.md)

### Inherited from asi_externalLabH2OIsotopes_pub:

 * [receivedBy](receivedBy.md)  <sub>OPT</sub>
    * Description: Anonymized name of lab personnel receiving the shipment
    * range: [String](types/String.md)
    * inherited from: None
 * [receivedDate](receivedDate.md)  <sub>OPT</sub>
    * Description: Date a sample was received
    * range: [Time](types/Time.md)
 * [d18OsdWater](d18OsdWater.md)  <sub>OPT</sub>
    * Description: Standard deviation of d18O of replicate H2O samples
    * range: [Double](types/Double.md)
    * inherited from: None
 * [d2HsdWater](d2HsdWater.md)  <sub>OPT</sub>
    * Description: Standard deviation of d2H of replicate H2O samples
    * range: [Double](types/Double.md)
    * inherited from: None
 * [instrumentSN](instrumentSN.md)  <sub>OPT</sub>
    * Description: Serial number of instrument used to analyze sample
    * range: [String](types/String.md)
    * inherited from: None
 * [isotopeH2OExternalLabQF](isotopeH2OExternalLabQF.md)  <sub>OPT</sub>
    * Description: Quality flag for samples with high standard deviation (del2Hsd >=0.75 or del18Osd>=0.2) of H2O isotope samples. High standard deviations are flagged with a 1, else flag set to 0
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from cfc_chlorophyll_pub:

 * [extractionStartDate](extractionStartDate.md)  <sub>OPT</sub>
    * Description: The start date-time for an extraction event
    * range: [Time](types/Time.md)
    * inherited from: None
 * [receivedCondition](receivedCondition.md)  <sub>OPT</sub>
    * Description: Condition of the sample on the date it was received
    * range: [String](types/String.md)
 * [chlCarotWavelength1](chlCarotWavelength1.md)  <sub>OPT</sub>
    * Description: The first wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength1Abs](chlCarotWavelength1Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the first wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength2](chlCarotWavelength2.md)  <sub>OPT</sub>
    * Description: The second wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength2Abs](chlCarotWavelength2Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the second wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength3](chlCarotWavelength3.md)  <sub>OPT</sub>
    * Description: The third wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength3Abs](chlCarotWavelength3Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the third wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength4](chlCarotWavelength4.md)  <sub>OPT</sub>
    * Description: The fourth wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlCarotWavelength4Abs](chlCarotWavelength4Abs.md)  <sub>OPT</sub>
    * Description: Absorbance values for the fourth wavelength used to measure chlorophyll and carotenoid content
    * range: [Double](types/Double.md)
    * inherited from: None
 * [chlorophyllSampleCode](chlorophyllSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a chlorophyll sample
    * range: [String](types/String.md)
    * inherited from: None
 * [chlorophyllSampleID](chlorophyllSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a chlorophyll sample
    * range: [String](types/String.md)
    * inherited from: None
 * [extractCarotConc](extractCarotConc.md)  <sub>OPT</sub>
    * Description: Calculated total carotenoid concentration of the extract solution, dilution-corrected as needed
    * range: [Double](types/Double.md)
    * inherited from: None
 * [extractChlAConc](extractChlAConc.md)  <sub>OPT</sub>
    * Description: Calculated chlorophyll A concentration of the extract solution, dilution-corrected as needed
    * range: [Double](types/Double.md)
    * inherited from: None
 * [extractChlBConc](extractChlBConc.md)  <sub>OPT</sub>
    * Description: Calculated chlorophyll B concentration of the extract solution, dilution-corrected as needed
    * range: [Double](types/Double.md)
    * inherited from: None
 * [extractionLength](extractionLength.md)  <sub>OPT</sub>
    * Description: The duration of an extraction event
    * range: [Double](types/Double.md)
    * inherited from: None
 * [handlingQF](handlingQF.md)  <sub>OPT</sub>
    * Description: Quality flag for sample handling
    * range: [String](types/String.md)
    * inherited from: None
 * [relativeAccuracyScale](relativeAccuracyScale.md)  <sub>OPT</sub>
    * Description: Indicator for the mean relative accuracy of standards analyzed as unknowns with a run of samples
    * range: [String](types/String.md)
    * inherited from: None
 * [solventVolume](solventVolume.md)  <sub>OPT</sub>
    * Description: Volume of solvent used in the extraction
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

### Inherited from inv_taxonomyRaw_pub:

 * [targetTaxaPresent](targetTaxaPresent.md)  <sub>OPT</sub>
    * Description: Indicator of whether the sample contained individuals of the target taxa
    * range: [String](types/String.md)
    * inherited from: None
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
 * [internalLabID](internalLabID.md)  <sub>OPT</sub>
    * Description: Internal identifier used by the external facility
    * range: [String](types/String.md)
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
| **Mappings:** | | neon:ntr_externalLab_in |

