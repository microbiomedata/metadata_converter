
# Type: asc_externalLabBatchQA_in




URI: [neon:AscExternalLabBatchQAIn](https://data.neonscience.org/AscExternalLabBatchQAIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [analyteSampleValue](analyteSampleValue.md)  <sub>OPT</sub>
    * Description: The known value of a given analyte for a sample, with units tied to the analyte
    * range: [Double](types/Double.md)
 * [qaType](qaType.md)  <sub>OPT</sub>
    * Description: Type of quality assurance used in analysis
    * range: [String](types/String.md)
 * [reagentSN](reagentSN.md)  <sub>OPT</sub>
    * Description: Serial number assigned to reagents or standards to trace to the manufacturer certificate of analysis
    * range: [String](types/String.md)
 * [recovery](recovery.md)  <sub>OPT</sub>
    * Description: Recovered amount of the known value or spike
    * range: [Double](types/Double.md)
 * [recoveryLimitLower](recoveryLimitLower.md)  <sub>OPT</sub>
    * Description: Lower limit for percent recovery
    * range: [Double](types/Double.md)
 * [recoveryLimitUpper](recoveryLimitUpper.md)  <sub>OPT</sub>
    * Description: Upper limit for percent recovery
    * range: [Double](types/Double.md)
 * [relativePercentDifference](relativePercentDifference.md)  <sub>OPT</sub>
    * Description: Percent difference between observed values of a sample or standard run in duplicate
    * range: [Double](types/Double.md)
 * [relativePercentLimit](relativePercentLimit.md)  <sub>OPT</sub>
    * Description: Upper limit for relative percent difference
    * range: [Double](types/Double.md)

### Inherited from asi_POMExternalLabDataPerSample_pub:

 * [sampleType](sampleType.md)  <sub>OPT</sub>
    * Description: Type of sample
    * range: [String](types/String.md)
    * inherited from: None
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
 * [analyteConcentration](analyteConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of analyte
    * range: [Double](types/Double.md)
    * inherited from: None
 * [percentFilterAnalyzed](percentFilterAnalyzed.md)  <sub>OPT</sub>
    * Description: Fraction of the filter sampled (%)
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from asp_externalLabData_pub:

 * [analyteSurrogate](analyteSurrogate.md)  <sub>OPT</sub>
    * Description: Indicator for whether an analyte is a surrogate
    * range: [String](types/String.md)
 * [cas](cas.md)  <sub>OPT</sub>
    * Description: Chemical Abstracts Service registry number
    * range: [String](types/String.md)
    * inherited from: None
 * [deptName](deptName.md)  <sub>OPT</sub>
    * Description: External lab department
    * range: [String](types/String.md)
    * inherited from: None
 * [extendedQualifier1](extendedQualifier1.md)  <sub>OPT</sub>
    * Description: First extended data qualifier returned for the sample and analyte
    * range: [String](types/String.md)
    * inherited from: None
 * [extendedQualifier2](extendedQualifier2.md)  <sub>OPT</sub>
    * Description: Second extended data qualifier returned for the sample and analyte
    * range: [String](types/String.md)
    * inherited from: None
 * [extendedQualifier3](extendedQualifier3.md)  <sub>OPT</sub>
    * Description: Third extended data qualifier returned for the sample and analyte
    * range: [String](types/String.md)
    * inherited from: None
 * [extendedQualifier4](extendedQualifier4.md)  <sub>OPT</sub>
    * Description: Fourth extended data qualifier returned for the sample and analyte
    * range: [String](types/String.md)
    * inherited from: None
 * [extendedQualifier5](extendedQualifier5.md)  <sub>OPT</sub>
    * Description: Fifth extended data qualifier returned for the sample and analyte
    * range: [String](types/String.md)
    * inherited from: None
 * [externalQualifier](externalQualifier.md)  <sub>OPT</sub>
    * Description: A data qualifier returned by an external laboratory
    * range: [String](types/String.md)
    * inherited from: None
 * [practicalQuantitationLimit](practicalQuantitationLimit.md)  <sub>OPT</sub>
    * Description: Practical Quantitation Limit.  Synonymous with the EPA term: minimum level
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from cfc_elementsBatchQA_in:

 * [qaQF](qaQF.md)  <sub>OPT</sub>
    * Description: Quality flag for quality control sample
    * range: [String](types/String.md)
 * [knownBoronConc](knownBoronConc.md)  <sub>OPT</sub>
    * Description: Known concentration of boron in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownCalciumConc](knownCalciumConc.md)  <sub>OPT</sub>
    * Description: Known concentration of calcium in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownCopperConc](knownCopperConc.md)  <sub>OPT</sub>
    * Description: Known concentration of copper in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownIronConc](knownIronConc.md)  <sub>OPT</sub>
    * Description: Known concentration of iron in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownMagnesiumConc](knownMagnesiumConc.md)  <sub>OPT</sub>
    * Description: Known concentration of magnesium in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownManganeseConc](knownManganeseConc.md)  <sub>OPT</sub>
    * Description: Known concentration of manganese in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownPhosphorusConc](knownPhosphorusConc.md)  <sub>OPT</sub>
    * Description: Known concentration of phophorus in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownPotassiumConc](knownPotassiumConc.md)  <sub>OPT</sub>
    * Description: Known concentration of potassium in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownSulfurConc](knownSulfurConc.md)  <sub>OPT</sub>
    * Description: Known concentration of sulfur in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [knownZincConc](knownZincConc.md)  <sub>OPT</sub>
    * Description: Known concentration of zinc in standard reference material on a dry mass basis
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from ltr_ligninBatchQA_in:

 * [analysisEndDate](analysisEndDate.md)  <sub>OPT</sub>
    * Description: The end date or dateTime of analysis
    * range: [Time](types/Time.md)
 * [analyticalRepNumber](analyticalRepNumber.md)  <sub>OPT</sub>
    * Description: Number of the analytical replicate
    * range: [String](types/String.md)
    * inherited from: None
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

### Inherited from ltr_ligninSummary_in:

 * [analyteStandardDeviation](analyteStandardDeviation.md)  <sub>OPT</sub>
    * Description: Long-term average standard deviation values of the analyte, based on analysis of quality assurance reference materials or standards treated as unknowns
    * range: [Double](types/Double.md)
    * inherited from: None
 * [qaReferenceID](qaReferenceID.md)  <sub>OPT</sub>
    * Description: Identifier for quality assurance reference material or standard
    * range: [String](types/String.md)
    * inherited from: None
 * [analyteKnownValue](analyteKnownValue.md)  <sub>OPT</sub>
    * Description: The known value of a given analyte for a quality assurance reference material or standard, with units tied to the analyte
    * range: [Double](types/Double.md)
 * [analytePercentRecovery](analytePercentRecovery.md)  <sub>OPT</sub>
    * Description: Percent recovery of the analyte, based on analysis of quality assurance reference materials or standards treated as unknowns
    * range: [Double](types/Double.md)
    * inherited from: None
 * [analyteObservedValue](analyteObservedValue.md)  <sub>OPT</sub>
    * Description: The measured value of a given analyte for a standard reference material, with units tied to the analyte
    * range: [Double](types/Double.md)
 * [analyteMetricsCount](analyteMetricsCount.md)  <sub>OPT</sub>
    * Description: Count of how many measurements were used to determine analyte metrics
    * range: [String](types/String.md)
    * inherited from: None
 * [qaReportingEndDate](qaReportingEndDate.md)  <sub>OPT</sub>
    * Description: End date for the quality assurance (QA) reporting period
    * range: [Time](types/Time.md)
    * inherited from: None
 * [qaReportingStartDate](qaReportingStartDate.md)  <sub>OPT</sub>
    * Description: Start date for the quality assurance (QA) reporting period
    * range: [Time](types/Time.md)
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
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
    * inherited from: None
 * [runID](runID.md)  <sub>OPT</sub>
    * Description: A linking value provided by the external lab that associates the sample data to the run metadata, including QA values
    * range: [String](types/String.md)

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
| **Mappings:** | | neon:asc_externalLabBatchQA_in |

