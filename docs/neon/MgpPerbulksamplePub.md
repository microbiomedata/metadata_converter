
# Type: mgp_perbulksample_pub




URI: [neon:MgpPerbulksamplePub](https://data.neonscience.org/MgpPerbulksamplePub)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


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

### Inherited from mgp_perbulksample_in:

 * [bulkDensID](bulkDensID.md)  <sub>OPT</sub>
    * Description: Identifier for bulk density sample
    * range: [String](types/String.md)
 * [bulkDensHorizonProportion](bulkDensHorizonProportion.md)  <sub>OPT</sub>
    * Description: Proportion of horizon represented by bulk density sample on a volume basis
    * range: [Double](types/Double.md)
 * [bulkDensOrientation](bulkDensOrientation.md)  <sub>OPT</sub>
    * Description: Orientation of the coring direction for the bulk density sample
    * range: [String](types/String.md)
    * inherited from: None
 * [bulkDensCoarseFragDensMeas](bulkDensCoarseFragDensMeas.md)  <sub>OPT</sub>
    * Description: Identifies approach used to determine coarse fragment density
    * range: [String](types/String.md)
    * inherited from: None
 * [bulkDensExclCoarseFrag](bulkDensExclCoarseFrag.md)  <sub>OPT</sub>
    * Description: Bulk density of soil excluding coarse fragments (>2 mm)
    * range: [Double](types/Double.md)
 * [bulkDensInclCoarseFrag](bulkDensInclCoarseFrag.md)  <sub>OPT</sub>
    * Description: Bulk density of soil including coarse fragments (>2 mm)
    * range: [Double](types/Double.md)
    * inherited from: None
 * [coarseFragWeight](coarseFragWeight.md)  <sub>OPT</sub>
    * Description: Coarse (>2 mm) fragment occurance expressed on weight basis
    * range: [Double](types/Double.md)
    * inherited from: None
 * [coarseFragVolume](coarseFragVolume.md)  <sub>OPT</sub>
    * Description: Coarse (>2 mm) fragment occurance expressed on volume basis
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from mpr_perrootsample_pub:

 * [pitNamedLocation](pitNamedLocation.md)  <sub>OPT</sub>
    * Description: Named location identifier for the soil pit
    * range: [String](types/String.md)
 * [rootStatus](rootStatus.md)  <sub>OPT</sub>
    * Description: The state of an individual or sample
    * range: [String](types/String.md)
    * inherited from: None
 * [depthIncrementID](depthIncrementID.md)  <sub>OPT</sub>
    * Description: An identifier for the depth increment within a pit profile
    * range: [String](types/String.md)
    * inherited from: None
 * [rootDryMass](rootDryMass.md)  <sub>OPT</sub>
    * Description: Oven-dried mass of root sample or subsample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [incrementRootBiomass](incrementRootBiomass.md)  <sub>OPT</sub>
    * Description: Root biomass per horizontal surface area per depth increment
    * range: [Double](types/Double.md)
    * inherited from: None
 * [incrementRootDensity](incrementRootDensity.md)  <sub>OPT</sub>
    * Description: Root biomass per collected soil volume per depth increment
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from spc_bulkdensity_pub:

 * [bulkDensIDnrcs](bulkDensIDnrcs.md)  <sub>OPT</sub>
    * Description: Identifier used by National Resource Conservation Service (NRCS) for bulk density sample
    * range: [String](types/String.md)
    * inherited from: None
 * [bulkDensSampleType](bulkDensSampleType.md)  <sub>OPT</sub>
    * Description: Type of bulk density sample
    * range: [String](types/String.md)
 * [bulkDensCenterDepth](bulkDensCenterDepth.md)  <sub>OPT</sub>
    * Description: Depth of the vertical center of the bulk sample below the soil surface
    * range: [Double](types/Double.md)
 * [bulkDensDiameter](bulkDensDiameter.md)  <sub>OPT</sub>
    * Description: Diameter of the excavation cavity used for bulk density sampling
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bulkDensLength](bulkDensLength.md)  <sub>OPT</sub>
    * Description: Length of the excavation cavity used for bulk density sampling
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bulkDensVolume](bulkDensVolume.md)  <sub>OPT</sub>
    * Description: Volume of the bulk density sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bulkDensTopDepth](bulkDensTopDepth.md)  <sub>OPT</sub>
    * Description: Top depth of the bulk density sample
    * range: [Double](types/Double.md)
 * [bulkDensBottomDepth](bulkDensBottomDepth.md)  <sub>OPT</sub>
    * Description: Bottom depth of the bulk density sample
    * range: [Double](types/Double.md)
 * [bulkDensWetWeight](bulkDensWetWeight.md)  <sub>OPT</sub>
    * Description: Total weight of the bulk density sample prior to drying
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bulkDensDryWeight](bulkDensDryWeight.md)  <sub>OPT</sub>
    * Description: Total weight of the bulk density sample after drying
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bulkDensCoarseFragWeight](bulkDensCoarseFragWeight.md)  <sub>OPT</sub>
    * Description: Weight of the coarse (>2 mm) fragments in the bulk density sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bulkDensCoarseFragDens](bulkDensCoarseFragDens.md)  <sub>OPT</sub>
    * Description: Density of the coarse (>2 mm) fragments in the bulk density sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bulkDensCode](bulkDensCode.md)  <sub>OPT</sub>
    * Description: Barcode of the bulk density sample
    * range: [String](types/String.md)
    * inherited from: None
 * [bulkDensFieldMoist](bulkDensFieldMoist.md)  <sub>OPT</sub>
    * Description: Weight per unit volume of the <2 mm fraction, measured at field moisture
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bulkDensMethod](bulkDensMethod.md)  <sub>OPT</sub>
    * Description: Method used for bulk density analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [bulkDensMethodPub](bulkDensMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for bulk density analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [bulkDensOvenDry](bulkDensOvenDry.md)  <sub>OPT</sub>
    * Description: Weight per unit volume of the <2 mm fraction, measured on oven dried soil clods
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bulkDensProcessedDate](bulkDensProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for bulk density analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [bulkDensThirdBar](bulkDensThirdBar.md)  <sub>OPT</sub>
    * Description: Weight per unit volume of the <2 mm fraction, measured after equilibration at one third bar water tension
    * range: [Double](types/Double.md)
    * inherited from: None
 * [bulkDensWidth](bulkDensWidth.md)  <sub>OPT</sub>
    * Description: Width of the bulk density sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [fieldWaterContent](fieldWaterContent.md)  <sub>OPT</sub>
    * Description: Water content under field conditions, reported as gravimetric percent on the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [waterRetentionThirdBar](waterRetentionThirdBar.md)  <sub>OPT</sub>
    * Description: Water content after equilibration at one-third bar water tension, reported as gravimetric percent on the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None

### Inherited from spc_particlesize_pub:

 * [nrcsDescriptionID](nrcsDescriptionID.md)  <sub>OPT</sub>
    * Description: NRCS identifier assigned to the soil profile description
    * range: [String](types/String.md)
    * inherited from: None
 * [horizonID](horizonID.md)  <sub>OPT</sub>
    * Description: An identifier for the soil horizon
    * range: [String](types/String.md)
 * [horizonName](horizonName.md)  <sub>OPT</sub>
    * Description: Soil horizon name
    * range: [String](types/String.md)
 * [biogeoIDnrcs](biogeoIDnrcs.md)  <sub>OPT</sub>
    * Description: Identifier used by NRCS for the biogeochemistry sample
    * range: [String](types/String.md)
    * inherited from: None
 * [biogeoSampleType](biogeoSampleType.md)  <sub>OPT</sub>
    * Description: Type of biogeochemistry sample
    * range: [String](types/String.md)
    * inherited from: None
 * [biogeoTopDepth](biogeoTopDepth.md)  <sub>OPT</sub>
    * Description: Top depth of the biogeochemistry sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoBottomDepth](biogeoBottomDepth.md)  <sub>OPT</sub>
    * Description: Bottom depth of the biogeochemistry sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoCenterDepth](biogeoCenterDepth.md)  <sub>OPT</sub>
    * Description: Depth of the center of the biogeochemistry sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [coarseFrag2To5](coarseFrag2To5.md)  <sub>OPT</sub>
    * Description: Coarse fragment (2-5 mm) content of the <20 mm size fraction of the biogeochemistry soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [coarseFrag5To20](coarseFrag5To20.md)  <sub>OPT</sub>
    * Description: Coarse fragment (5-20 mm) content of the <20 mm size fraction of the biogeochemistry soil sample
    * range: [Double](types/Double.md)
    * inherited from: None
 * [biogeoCode](biogeoCode.md)  <sub>OPT</sub>
    * Description: Barcode the biogeochemistry sample
    * range: [String](types/String.md)
    * inherited from: None
 * [carbonateClay](carbonateClay.md)  <sub>OPT</sub>
    * Description: Carbonate clay (<0.002 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [clayFineContent](clayFineContent.md)  <sub>OPT</sub>
    * Description: Fine clay (<0.0002 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [clayTotal](clayTotal.md)  <sub>OPT</sub>
    * Description: Total clay (<0.002 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [horizonCode](horizonCode.md)  <sub>OPT</sub>
    * Description: Barcode of the horizon
    * range: [String](types/String.md)
    * inherited from: None
 * [sandCoarseContent](sandCoarseContent.md)  <sub>OPT</sub>
    * Description: Coarse sand (0.5-1 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sandFineContent](sandFineContent.md)  <sub>OPT</sub>
    * Description: Fine sand (0.105-0.25 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sandMediumContent](sandMediumContent.md)  <sub>OPT</sub>
    * Description: Medium sand (0.25-0.5 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sandTotal](sandTotal.md)  <sub>OPT</sub>
    * Description: Total sand (0.047-2 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [sandVeryFineContent](sandVeryFineContent.md)  <sub>OPT</sub>
    * Description: Very fine sand (0.047-0.105 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [siltCoarseContent](siltCoarseContent.md)  <sub>OPT</sub>
    * Description: Coarse silt (0.02-0.047 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [siltFineContent](siltFineContent.md)  <sub>OPT</sub>
    * Description: Fine silt (0.002-0.02 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [siltTotal](siltTotal.md)  <sub>OPT</sub>
    * Description: Total silt (0.002-0.047 mm) content on a weight basis of the <2 mm fraction
    * range: [Double](types/Double.md)
    * inherited from: None
 * [particleSizeDistProcessedDate](particleSizeDistProcessedDate.md)  <sub>OPT</sub>
    * Description: Date of processing sample for particle size distribution analysis
    * range: [Time](types/Time.md)
    * inherited from: None
 * [particleSizeDistMethod](particleSizeDistMethod.md)  <sub>OPT</sub>
    * Description: Methods used for particle size distribution analysis
    * range: [String](types/String.md)
    * inherited from: None
 * [particleSizeDistMethodPub](particleSizeDistMethodPub.md)  <sub>OPT</sub>
    * Description: Citation for publication describing the methods used for particle size distribution analysis
    * range: [String](types/String.md)
    * inherited from: None

### Inherited from spc_perbiogeosample_in:

 * [labProjID](labProjID.md)  <sub>OPT</sub>
    * Description: Identifier for soil physical properties analyses
    * range: [String](types/String.md)
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
    * inherited from: None
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

### Inherited from spc_perhorizon_pub:

 * [pitID](pitID.md)  <sub>OPT</sub>
    * Description: An identifier for the soil pit
    * range: [String](types/String.md)
 * [horizonTopDepth](horizonTopDepth.md)  <sub>OPT</sub>
    * Description: Depth below the soil surface of the top of a soil horizon
    * range: [Double](types/Double.md)
    * inherited from: None
 * [horizonBottomDepth](horizonBottomDepth.md)  <sub>OPT</sub>
    * Description: Depth below the soil surface of the bottom of a soil horizon
    * range: [Double](types/Double.md)
    * inherited from: None
 * [pitCode](pitCode.md)  <sub>OPT</sub>
    * Description: Barcode of the pit
    * range: [String](types/String.md)
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
| **Mappings:** | | neon:mgp_perbulksample_pub |

