
# Type: cfc_LMA_in




URI: [neon:CfcLMAIn](https://data.neonscience.org/CfcLMAIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [lmaSampleFate](lmaSampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a leaf mass per area sample
    * range: [String](types/String.md)

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

### Inherited from cfc_LMA_pub:

 * [dryMassFraction](dryMassFraction.md)  <sub>OPT</sub>
    * Description: Dry mass divided by fresh mass of a sample
    * range: [Double](types/Double.md)
 * [leafArea](leafArea.md)  <sub>OPT</sub>
    * Description: Area of all leaves or needles scanned
    * range: [Double](types/Double.md)
 * [leafMassPerArea](leafMassPerArea.md)  <sub>OPT</sub>
    * Description: Dry mass per unit area of leaf or needle foliage
    * range: [Double](types/Double.md)
 * [lmaSampleCode](lmaSampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a leaf mass per area sample
    * range: [String](types/String.md)
 * [lmaSampleCondition](lmaSampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a leaf mass per area sample
    * range: [String](types/String.md)
 * [lmaSampleID](lmaSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a leaf mass per area sample
    * range: [String](types/String.md)
 * [percentGreen](percentGreen.md)  <sub>OPT</sub>
    * Description: Visual estimate of percent scanned foliar material that was live and green
    * range: [String](types/String.md)
 * [scanDate](scanDate.md)  <sub>OPT</sub>
    * Description: The date and time a sample is scanned
    * range: [Time](types/Time.md)
 * [scannedBy](scannedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who scanned the sample(s)
    * range: [String](types/String.md)
 * [scannedLeafNumber](scannedLeafNumber.md)  <sub>OPT</sub>
    * Description: Number of leaves or needles scanned
    * range: [String](types/String.md)
 * [weighedBy](weighedBy.md)  <sub>OPT</sub>
    * Description: An identifier for the technician who weighed the sample
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

### Inherited from ltr_massdata_pub:

 * [weighDate](weighDate.md)  <sub>OPT</sub>
    * Description: Date that sample or subsample was weighed
    * range: [Time](types/Time.md)
    * inherited from: None
 * [qaDryMass](qaDryMass.md)  <sub>OPT</sub>
    * Description: Indicates whether 'dryMass' value is associated with 'qa' measurement type
    * range: [String](types/String.md)
    * inherited from: None
 * [ovenStartDate](ovenStartDate.md)  <sub>OPT</sub>
    * Description: The date and time a sample was placed in the drying oven
    * range: [Time](types/Time.md)
 * [ovenEndDate](ovenEndDate.md)  <sub>OPT</sub>
    * Description: The date and time a sample was removed from the drying oven
    * range: [Time](types/Time.md)
 * [fieldSampleBarcode](fieldSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode of a field sample
    * range: [String](types/String.md)
    * inherited from: None
 * [fieldSampleID](fieldSampleID.md)  <sub>OPT</sub>
    * Description: Unique identifier for a field sample
    * range: [String](types/String.md)
    * inherited from: None
 * [functionalGroup](functionalGroup.md)  <sub>OPT</sub>
    * Description: Functional group to which a sample belongs
    * range: [String](types/String.md)
    * inherited from: None
 * [massSampleBarcode](massSampleBarcode.md)  <sub>OPT</sub>
    * Description: Barcode for a mass sample
    * range: [String](types/String.md)
    * inherited from: None
 * [massSampleID](massSampleID.md)  <sub>OPT</sub>
    * Description: Identifier for a mass sample
    * range: [String](types/String.md)
    * inherited from: None

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

### Inherited from sme_microbialBiomass_pub:

 * [biomassCode](biomassCode.md)  <sub>OPT</sub>
    * Description: Barcode of biomass sample
    * range: [String](types/String.md)
    * inherited from: None
 * [biomassID](biomassID.md)  <sub>OPT</sub>
    * Description: Identifier for biomass sample
    * range: [String](types/String.md)
    * inherited from: None
 * [freshMass](freshMass.md)  <sub>OPT</sub>
    * Description: Total fresh mass of a sample
    * range: [Double](types/Double.md)
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
| **Mappings:** | | neon:cfc_LMA_in |

