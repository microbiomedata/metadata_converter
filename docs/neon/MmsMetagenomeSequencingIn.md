
# Type: mms_metagenomeSequencing_in




URI: [neon:MmsMetagenomeSequencingIn](https://data.neonscience.org/MmsMetagenomeSequencingIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[MmsMetagenomeSequencingIn&#124;uid:string%20%3F;remarks:string%20%3F;setDate:time%20%3F;collectDate:time%20%3F;subsampleID:string%20%3F;processedDate:time%20%3F;laboratoryName:string%20%3F;internalLabID:string%20%3F;locationID:string%20%3F;analyzedBy:string%20%3F;dataQF:string%20%3F;dnaSampleID:string%20%3F;dnaSampleFate:string%20%3F;dnaSampleCode:string%20%3F;sequencingMethod:string%20%3F;investigation_type:string%20%3F;sequencingConcentration:double%20%3F;sequencerRunID:string%20%3F;sampleTotalReadNumber:string%20%3F;sampleFilteredReadNumber:string%20%3F;averageFilteredReadQuality:double%20%3F;ambiguousBasesNumber:string%20%3F;barcodeSequence:string%20%3F;qaqcStatus:string%20%3F;subsampleCode:string%20%3F;subsampleFate:string%20%3F;instrument_model:string%20%3F;ncbiProjectID:string%20%3F;sequencingFacilityID:string%20%3F;sequencingProtocol:string%20%3F;labPrepMethod:string%20%3F;illuminaAdapterKit:string%20%3F;illuminaIndex1:string%20%3F;illuminaIndex2:string%20%3F;processedSeqFileName:string%20%3F;processedSeqFileNameCode:string%20%3F;processedSeqFileNameFate:string%20%3F;processedSeqFileNameID:string%20%3F])

## Attributes


### Own

 * [ambiguousBasesNumber](ambiguousBasesNumber.md)  <sub>OPT</sub>
    * Description: Number of sequence reads in a quality filtered sample with more than 1 ambiguous base
    * range: [String](types/String.md)
 * [analyzedBy](analyzedBy.md)  <sub>OPT</sub>
    * Description: Name of lab personnel analyzing sample
    * range: [String](types/String.md)
 * [averageFilteredReadQuality](averageFilteredReadQuality.md)  <sub>OPT</sub>
    * Description: Average quality of sequence reads in a sample after quality filtering
    * range: [Double](types/Double.md)
 * [barcodeSequence](barcodeSequence.md)  <sub>OPT</sub>
    * Description: DNA sequence of barcode primer used in a multiplexed DNA sequencing run
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [dnaSampleCode](dnaSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a DNA sample
    * range: [String](types/String.md)
 * [dnaSampleFate](dnaSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a DNA sample
    * range: [String](types/String.md)
 * [dnaSampleID](dnaSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for DNA sample
    * range: [String](types/String.md)
 * [illuminaAdapterKit](illuminaAdapterKit.md)  <sub>OPT</sub>
    * Description: Identifier for the adapter sequences kit manufactured for use with Illumina sequencing technology
    * range: [String](types/String.md)
 * [illuminaIndex1](illuminaIndex1.md)  <sub>OPT</sub>
    * Description: Oligonucleotide sequence of the 5-prime index used to identify a unique sample in an Illumina-based sequencing run
    * range: [String](types/String.md)
 * [illuminaIndex2](illuminaIndex2.md)  <sub>OPT</sub>
    * Description: Oligonucleotide sequence of the 3-prime index used to identify a unique sample in an Illumina-based sequencing run
    * range: [String](types/String.md)
 * [instrument_model](instrument_model.md)  <sub>OPT</sub>
    * Description: The model identifier of the sequencing instrument
    * range: [String](types/String.md)
 * [internalLabID](internalLabID.md)  <sub>OPT</sub>
    * Description: Internal identifier used by the external facility
    * range: [String](types/String.md)
 * [investigation_type](investigation_type.md)  <sub>OPT</sub>
    * Description: Manner in which DNA libraries were constructed for analysis
    * range: [String](types/String.md)
 * [labPrepMethod](labPrepMethod.md)  <sub>OPT</sub>
    * Description: The method, protocol or standard operating procedure used by an analytical laboratory for preparing samples for analysis
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [locationID](locationID.md)  <sub>OPT</sub>
    * Description: Identifier for location where sample was collected
    * range: [String](types/String.md)
 * [ncbiProjectID](ncbiProjectID.md)  <sub>OPT</sub>
    * Description: Identifier for the NCBI project associated with the sample
    * range: [String](types/String.md)
 * [processedDate](processedDate.md)  <sub>OPT</sub>
    * Description: Date or date and time of processing event
    * range: [Time](types/Time.md)
 * [processedSeqFileName](processedSeqFileName.md)  <sub>OPT</sub>
    * Description: File name of quality filtered sequence data
    * range: [String](types/String.md)
 * [processedSeqFileNameCode](processedSeqFileNameCode.md)  <sub>OPT</sub>
    * Description: Barcode of the identifier for processed sequence file name
    * range: [String](types/String.md)
 * [processedSeqFileNameFate](processedSeqFileNameFate.md)  <sub>OPT</sub>
    * Description: Fate of the identifier for processed sequence file name
    * range: [String](types/String.md)
 * [processedSeqFileNameID](processedSeqFileNameID.md)  <sub>OPT</sub>
    * Description: Identifier for processed sequence file name
    * range: [String](types/String.md)
 * [qaqcStatus](qaqcStatus.md)  <sub>OPT</sub>
    * Description: Status of internal QAQC
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleFilteredReadNumber](sampleFilteredReadNumber.md)  <sub>OPT</sub>
    * Description: Number of sequence reads that pass quality filtering
    * range: [String](types/String.md)
 * [sampleTotalReadNumber](sampleTotalReadNumber.md)  <sub>OPT</sub>
    * Description: Total number of sequence reads in a sample
    * range: [String](types/String.md)
 * [sequencerRunID](sequencerRunID.md)  <sub>OPT</sub>
    * Description: Identifier for the sequencing run
    * range: [String](types/String.md)
 * [sequencingConcentration](sequencingConcentration.md)  <sub>OPT</sub>
    * Description: Concentration of nucleic acid used for sequencing
    * range: [Double](types/Double.md)
 * [sequencingFacilityID](sequencingFacilityID.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is sequencing samples
    * range: [String](types/String.md)
 * [sequencingMethod](sequencingMethod.md)  <sub>OPT</sub>
    * Description: Method used for DNA sequencing
    * range: [String](types/String.md)
 * [sequencingProtocol](sequencingProtocol.md)  <sub>OPT</sub>
    * Description: The protocol used to sequence DNA from a sample
    * range: [String](types/String.md)
 * [setDate](setDate.md)  <sub>OPT</sub>
    * Description: Date that trap was set
    * range: [Time](types/Time.md)
 * [subsampleCode](subsampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a subsample
    * range: [String](types/String.md)
 * [subsampleFate](subsampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a subsample
    * range: [String](types/String.md)
 * [subsampleID](subsampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with each subsample per sampleID
    * range: [String](types/String.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:mms_metagenomeSequencing_in |
| **In Subsets:** | | DP0.10107.001 |

