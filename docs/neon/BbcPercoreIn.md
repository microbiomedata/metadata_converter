
# Type: bbc_percore_in




URI: [neon:BbcPercoreIn](https://data.neonscience.org/BbcPercoreIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Inherited from bbc_percore_pub:

 * [bareGround](bareGround.md)  <sub>OPT</sub>
    * Description: Percent of the sampling area from which sample was collected that is bare ground
    * range: [String](types/String.md)
 * [coreDiameter](coreDiameter.md)  <sub>OPT</sub>
    * Description: Diameter of the core sample
    * range: [Double](types/Double.md)
 * [coreID](coreID.md)  <sub>OPT</sub>
    * Description: Identifier for the soil sample within the clipID
    * range: [String](types/String.md)
 * [monolithLength](monolithLength.md)  <sub>OPT</sub>
    * Description: Length of the monolith sample top surface
    * range: [Double](types/Double.md)
 * [monolithWidth](monolithWidth.md)  <sub>OPT</sub>
    * Description: Width of the monolith sample top surface
    * range: [Double](types/Double.md)
 * [rootSampleArea](rootSampleArea.md)  <sub>OPT</sub>
    * Description: Area of soil sample, calculated from coreDiameter or monolith dimensions
    * range: [Double](types/Double.md)
 * [rootSampleDepth](rootSampleDepth.md)  <sub>OPT</sub>
    * Description: Depth to which soil sample was collected
    * range: [Double](types/Double.md)
 * [rootSamplingMethod](rootSamplingMethod.md)  <sub>OPT</sub>
    * Description: Method by which soil sample was collected
    * range: [String](types/String.md)
 * [rootSamplingPossible](rootSamplingPossible.md)  <sub>OPT</sub>
    * Description: Indicator of whether collection of a soil sample was possible
    * range: [String](types/String.md)
 * [wst10cmDist](wst10cmDist.md)  <sub>OPT</sub>
    * Description: Distance to nearest woody stem >= 10 cm diameter at breast height
    * range: [Double](types/Double.md)
 * [wst1cmDist](wst1cmDist.md)  <sub>OPT</sub>
    * Description: Distance to nearest woody stem with diameter at breast height < 10 cm and >= 1 cm
    * range: [Double](types/Double.md)

### Inherited from cfc_fieldData_pub:

 * [clipID](clipID.md)  <sub>OPT</sub>
    * Description: Unique identifier for the clip-harvest location within the plot
    * range: [String](types/String.md)
 * [clipCellNumber](clipCellNumber.md)  <sub>OPT</sub>
    * Description: A numeric identifier for the clip-harvest cell in which herbaceous biomass was sampled
    * range: [String](types/String.md)
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

### Inherited from ltr_chemistrySubsampling_pub:

 * [cnSampleCode](cnSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a carbon-nitrogen sample
    * range: [String](types/String.md)
    * inherited from: None
 * [cnSampleID](cnSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a carbon-nitrogen sample
    * range: [String](types/String.md)
    * inherited from: None
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

### Inherited from mam_perplotnight_pub:

 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
    * range: [String](types/String.md)

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

### Inherited from sls_soilCoreCollection_pub:

 * [coreCoordinateX](coreCoordinateX.md)  <sub>OPT</sub>
    * Description: x location of the soil core relative to the SW corner
    * range: [Double](types/Double.md)
    * inherited from: None
 * [coreCoordinateY](coreCoordinateY.md)  <sub>OPT</sub>
    * Description: y location of the soil core relative to the SW corner
    * range: [Double](types/Double.md)
    * inherited from: None
 * [geneticArchiveSample1Code](geneticArchiveSample1Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 1
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticArchiveSample1ID](geneticArchiveSample1ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 1
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticArchiveSample2Code](geneticArchiveSample2Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 2
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticArchiveSample2ID](geneticArchiveSample2ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 2
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticArchiveSample3Code](geneticArchiveSample3Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 3
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticArchiveSample3ID](geneticArchiveSample3ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 3
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticArchiveSample4Code](geneticArchiveSample4Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 4
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticArchiveSample4ID](geneticArchiveSample4ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 4
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticArchiveSample5Code](geneticArchiveSample5Code.md)  <sub>OPT</sub>
    * Description: Barcode of genetic archive subsample 5
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticArchiveSample5ID](geneticArchiveSample5ID.md)  <sub>OPT</sub>
    * Description: Identifier for genetic archive subsample 5
    * range: [String](types/String.md)
    * inherited from: None
 * [geneticSampleCondition](geneticSampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of genetic sample storage or processing
    * range: [String](types/String.md)
    * inherited from: None
 * [litterDepth](litterDepth.md)  <sub>OPT</sub>
    * Description: Depth of litter layer
    * range: [Double](types/Double.md)
 * [sampleBottomDepth](sampleBottomDepth.md)  <sub>OPT</sub>
    * Description: Depth below the soil surface of the bottom of a soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sampleTopDepth](sampleTopDepth.md)  <sub>OPT</sub>
    * Description: Depth below the soil surface of the top of a soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [soilCoreCount](soilCoreCount.md)  <sub>OPT</sub>
    * Description: Number of soil cores combined per sample
    * range: [String](types/String.md)
    * inherited from: None
 * [soilSamplingDevice](soilSamplingDevice.md)  <sub>OPT</sub>
    * Description: Type of soil collection device used for sampling
    * range: [String](types/String.md)
    * inherited from: None
 * [soilTemp](soilTemp.md)  <sub>OPT</sub>
    * Description: In-situ temperature of soil at approximately 10 cm depth
    * range: [Double](types/Double.md)
    * inherited from: None
 * [incubationMethod](incubationMethod.md)  <sub>OPT</sub>
    * Description: Method used for soil incubation
    * range: [String](types/String.md)
    * inherited from: None
 * [sampleExtent](sampleExtent.md)  <sub>OPT</sub>
    * Description: Extent of the soil sample relative to the local soil horizon conditions
    * range: [String](types/String.md)
    * inherited from: None
 * [standingWaterDepth](standingWaterDepth.md)  <sub>OPT</sub>
    * Description: Depth of standing water present at a sampling location
    * range: [Double](types/Double.md)
    * inherited from: None
 * [incubationCondition](incubationCondition.md)  <sub>OPT</sub>
    * Description: Condition of incubated nitrogen transformation sample upon retrieval
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
| **Mappings:** | | neon:bbc_percore_in |
| **In Subsets:** | | DP0.10067.001 |

