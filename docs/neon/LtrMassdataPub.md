
# Type: ltr_massdata_pub




URI: [neon:LtrMassdataPub](https://data.neonscience.org/LtrMassdataPub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [fieldSampleBarcode](fieldSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of a field sample
    * range: [String](types/String.md)
 * [fieldSampleID](fieldSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for a field sample
    * range: [String](types/String.md)
 * [functionalGroup](functionalGroup.md)  <sub>OPT</sub>
    * Description: Functional group to which a sample belongs
    * range: [String](types/String.md)
 * [massSampleBarcode](massSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a mass sample
    * range: [String](types/String.md)
 * [massSampleID](massSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a mass sample
    * range: [String](types/String.md)
 * [ovenEndDate](ovenEndDate.md)  <sub>OPT</sub>
    * Description: The date and time a sample was removed from the drying oven
    * range: [Time](types/Time.md)
 * [ovenStartDate](ovenStartDate.md)  <sub>OPT</sub>
    * Description: The date and time a sample was placed in the drying oven
    * range: [Time](types/Time.md)
 * [qaDryMass](qaDryMass.md)  <sub>OPT</sub>
    * Description: Indicates whether 'dryMass' value is associated with 'qa' measurement type
    * range: [String](types/String.md)
 * [weighDate](weighDate.md)  <sub>OPT</sub>
    * Description: Date that sample or subsample was weighed
    * range: [Time](types/Time.md)

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

### Inherited from mam_perplotnight_pub:

 * [samplingProtocolVersion](samplingProtocolVersion.md)  <sub>OPT</sub>
    * Description: The NEON document number and version where detailed information regarding the sampling method used is available; format NEON.DOC.######vX
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
| **Mappings:** | | neon:ltr_massdata_pub |

