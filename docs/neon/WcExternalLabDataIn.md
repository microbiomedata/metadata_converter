
# Type: wc_externalLabData_in




URI: [neon:WcExternalLabDataIn](https://data.neonscience.org/WcExternalLabDataIn)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WcExternalLabDataIn&#124;uid:string%20%3F;siteID:string%20%3F;remarks:string%20%3F;sampleID:string%20%3F;collectDate:time%20%3F;stationID:string%20%3F;startDate:time%20%3F;laboratoryName:string%20%3F;pH:double%20%3F;externalConductance:double%20%3F;waterCarbonate:double%20%3F;waterBicarbonate:double%20%3F;externalANC:double%20%3F;waterCalcium:double%20%3F;waterMagnesium:double%20%3F;waterSodium:double%20%3F;waterPotassium:double%20%3F;waterSulfate:double%20%3F;waterChlorine:double%20%3F;waterManganese:double%20%3F;waterIron:double%20%3F;waterBromine:double%20%3F;waterFluorine:double%20%3F;waterSilica:double%20%3F;totalSuspendedSolids:double%20%3F;totalSuspendedSolidsDryMass:double%20%3F;totalDissolvedSolids:double%20%3F;waterNitrateAndNitriteN:double%20%3F;waterNitriteN:double%20%3F;waterAmmoniumN:double%20%3F;waterOrthophosphateP:double%20%3F;waterTotalNitrogen:double%20%3F;totalDissolvedNitrogen:double%20%3F;dissolvedInorganicCarbon:double%20%3F;dissolvedOrganicCarbon:double%20%3F;waterTotalOrganicCarbon:double%20%3F;waterTotalPhosphorus:double%20%3F;totalDissolvedPhosphorus:double%20%3F;totalParticulateCarbonMass:double%20%3F;totalParticulateNitrogenMass:double%20%3F;uvAbsorbance250:double%20%3F;uvAbsorbance284:double%20%3F;nitriteRunID:string%20%3F;nh4RunID:string%20%3F;OrthoPRunID:string%20%3F;tnRunID:string%20%3F;tdnRunID:string%20%3F;dicRunID:string%20%3F;docRunID:string%20%3F;tocRunID:string%20%3F;tpcnRunDate:time%20%3F;uvBatchID:string%20%3F;coolerTemp:double%20%3F;externalLabMetadata:string%20%3F;internalLabID:string%20%3F;shipmentReceivedDate:time%20%3F;receivedBy:string%20%3F;shipDate:time%20%3F;shipmentID:string%20%3F;shipmentCondition:string%20%3F;shipmentWarmQF:double%20%3F;shipmentLateQF:double%20%3F;uploadDate:time%20%3F;sampleFate:string%20%3F;sampleCode:string%20%3F;dataQF:string%20%3F;sampleCondition:string%20%3F;shipmentLateTest:double%20%3F;nitrateNitriteRunID:string%20%3F])

## Attributes


### Own

 * [OrthoPRunID](OrthoPRunID.md)  <sub>OPT</sub>
    * Description: a linking value provided by the external lab that associates the orthophosphates to the run metadata
    * range: [String](types/String.md)
 * [collectDate](collectDate.md)  <sub>OPT</sub>
    * Description: Date of the collection event
    * range: [Time](types/Time.md)
 * [coolerTemp](coolerTemp.md)  <sub>OPT</sub>
    * Description: Temperature of the cooler when the sample arrived at the external lab
    * range: [Double](types/Double.md)
 * [dataQF](dataQF.md)  <sub>OPT</sub>
    * Description: Data quality flag
    * range: [String](types/String.md)
 * [dicRunID](dicRunID.md)  <sub>OPT</sub>
    * Description: a linking value provided by the external lab that associates the dissolved inorganic carbon to the run metadata
    * range: [String](types/String.md)
 * [dissolvedInorganicCarbon](dissolvedInorganicCarbon.md)  <sub>OPT</sub>
    * Description: Dissolved inorganic carbon concentration
    * range: [Double](types/Double.md)
 * [dissolvedOrganicCarbon](dissolvedOrganicCarbon.md)  <sub>OPT</sub>
    * Description: Dissolved organic carbon concentration
    * range: [Double](types/Double.md)
 * [docRunID](docRunID.md)  <sub>OPT</sub>
    * Description: a linking value provided by the external lab that associates the dissolved organic carbon to the run metadata
    * range: [String](types/String.md)
 * [externalANC](externalANC.md)  <sub>OPT</sub>
    * Description: Acid neutralizing capacity titration result from external lab in milligrams of Calcium Carbonate per liter
    * range: [Double](types/Double.md)
 * [externalConductance](externalConductance.md)  <sub>OPT</sub>
    * Description: Specific conductivity (auto-corrected to 25 degrees C) measured at the external lab
    * range: [Double](types/Double.md)
 * [externalLabMetadata](externalLabMetadata.md)  <sub>OPT</sub>
    * Description: The external lab's metadata
    * range: [String](types/String.md)
 * [internalLabID](internalLabID.md)  <sub>OPT</sub>
    * Description: Internal identifier used by the external facility
    * range: [String](types/String.md)
 * [laboratoryName](laboratoryName.md)  <sub>OPT</sub>
    * Description: Name of the laboratory or facility that is processing the sample
    * range: [String](types/String.md)
 * [nh4RunID](nh4RunID.md)  <sub>OPT</sub>
    * Description: a linking value provided by the external lab that associates the ammonium to the run metadata
    * range: [String](types/String.md)
 * [nitrateNitriteRunID](nitrateNitriteRunID.md)  <sub>OPT</sub>
    * Description: A linking value provided by the external lab that associates the nitrate plus nitrite to the run metadata
    * range: [String](types/String.md)
 * [nitriteRunID](nitriteRunID.md)  <sub>OPT</sub>
    * Description: a linking value provided by the external lab that associates the nitrite to the run metadata
    * range: [String](types/String.md)
 * [pH](pH.md)  <sub>OPT</sub>
    * Description: Measurement of pH in sample
    * range: [Double](types/Double.md)
 * [receivedBy](receivedBy.md)  <sub>OPT</sub>
    * Description: Anonymized name of lab personnel receiving the shipment
    * range: [String](types/String.md)
 * [remarks](remarks.md)  <sub>OPT</sub>
    * Description: Technician notes; free text comments accompanying the record
    * range: [String](types/String.md)
 * [sampleCode](sampleCode.md)  <sub>OPT</sub>
    * Description: Barcode of a sample
    * range: [String](types/String.md)
 * [sampleCondition](sampleCondition.md)  <sub>OPT</sub>
    * Description: Condition of a sample
    * range: [String](types/String.md)
 * [sampleFate](sampleFate.md)  <sub>OPT</sub>
    * Description: Fate of a sample
    * range: [String](types/String.md)
 * [sampleID](sampleID.md)  <sub>OPT</sub>
    * Description: Identifier for sample
    * range: [String](types/String.md)
 * [shipDate](shipDate.md)  <sub>OPT</sub>
    * Description: Date shipment sent by domain lab
    * range: [Time](types/Time.md)
 * [shipmentCondition](shipmentCondition.md)  <sub>OPT</sub>
    * Description: The condition in which the shipment was received
    * range: [String](types/String.md)
 * [shipmentID](shipmentID.md)  <sub>OPT</sub>
    * Description: Unique identifier associated with shipment
    * range: [String](types/String.md)
 * [shipmentLateQF](shipmentLateQF.md)  <sub>OPT</sub>
    * Description: Quality Flag for shipment arriving more than one day after shipment sent
    * range: [Double](types/Double.md)
 * [shipmentLateTest](shipmentLateTest.md)  <sub>OPT</sub>
    * Description: Test for quality flag for shipment arriving more than one day after shipment sent
    * range: [Double](types/Double.md)
 * [shipmentReceivedDate](shipmentReceivedDate.md)  <sub>OPT</sub>
    * Description: Date a sample was received
    * range: [Time](types/Time.md)
 * [shipmentWarmQF](shipmentWarmQF.md)  <sub>OPT</sub>
    * Description: Quality Flag for cooler arriving at external lab too warm (above 6 C)
    * range: [Double](types/Double.md)
 * [siteID](siteID.md)  <sub>OPT</sub>
    * Description: NEON site code
    * range: [String](types/String.md)
 * [startDate](startDate.md)  <sub>OPT</sub>
    * Description: The start date-time or interval during which an event occurred
    * range: [Time](types/Time.md)
 * [stationID](stationID.md)  <sub>OPT</sub>
    * Description: Identifier for station where sample was collected
    * range: [String](types/String.md)
 * [tdnRunID](tdnRunID.md)  <sub>OPT</sub>
    * Description: a linking value provided by the external lab that associates the total dissolved nitrogen to the run metadata
    * range: [String](types/String.md)
 * [tnRunID](tnRunID.md)  <sub>OPT</sub>
    * Description: a linking value provided by the external lab that associates the total nitrogen to the run metadata
    * range: [String](types/String.md)
 * [tocRunID](tocRunID.md)  <sub>OPT</sub>
    * Description: a linking value provided by the external lab that associates the total organic carbon to the run metadata
    * range: [String](types/String.md)
 * [totalDissolvedNitrogen](totalDissolvedNitrogen.md)  <sub>OPT</sub>
    * Description: Total dissolved nitrogen concentration
    * range: [Double](types/Double.md)
 * [totalDissolvedPhosphorus](totalDissolvedPhosphorus.md)  <sub>OPT</sub>
    * Description: Total dissolved phosphorus
    * range: [Double](types/Double.md)
 * [totalDissolvedSolids](totalDissolvedSolids.md)  <sub>OPT</sub>
    * Description: Total dissolved solids concentration
    * range: [Double](types/Double.md)
 * [totalParticulateCarbonMass](totalParticulateCarbonMass.md)  <sub>OPT</sub>
    * Description: Total particulate carbon as milligrams Carbon
    * range: [Double](types/Double.md)
 * [totalParticulateNitrogenMass](totalParticulateNitrogenMass.md)  <sub>OPT</sub>
    * Description: Total particulate nitrogen as milligrams Nitrogen
    * range: [Double](types/Double.md)
 * [totalSuspendedSolids](totalSuspendedSolids.md)  <sub>OPT</sub>
    * Description: Total suspended solids concentration
    * range: [Double](types/Double.md)
 * [totalSuspendedSolidsDryMass](totalSuspendedSolidsDryMass.md)  <sub>OPT</sub>
    * Description: Dry mass of total suspended solids
    * range: [Double](types/Double.md)
 * [tpcnRunDate](tpcnRunDate.md)  <sub>OPT</sub>
    * Description: A linking value provided by the external lab that associates the total carbon or total nitrogen to run date
    * range: [Time](types/Time.md)
 * [uid](uid.md)  <sub>OPT</sub>
    * Description: Unique ID within NEON database; an identifier for the record
    * range: [String](types/String.md)
 * [uploadDate](uploadDate.md)  <sub>OPT</sub>
    * Description: Date the file was uploaded
    * range: [Time](types/Time.md)
 * [uvAbsorbance250](uvAbsorbance250.md)  <sub>OPT</sub>
    * Description: Ultraviolet absorbance at 250nm reported per 1cm path length
    * range: [Double](types/Double.md)
 * [uvAbsorbance284](uvAbsorbance284.md)  <sub>OPT</sub>
    * Description: Ultraviolet absorbance at 284nm reported per 1cm path length
    * range: [Double](types/Double.md)
 * [uvBatchID](uvBatchID.md)  <sub>OPT</sub>
    * Description: a linking value provided by the external lab that associates the ultraviolet absorbance to the batch metadata
    * range: [String](types/String.md)
 * [waterAmmoniumN](waterAmmoniumN.md)  <sub>OPT</sub>
    * Description: Ammonium concentration as milligrams Nitrogen per liter
    * range: [Double](types/Double.md)
 * [waterBicarbonate](waterBicarbonate.md)  <sub>OPT</sub>
    * Description: Bicarbonate concentration
    * range: [Double](types/Double.md)
 * [waterBromine](waterBromine.md)  <sub>OPT</sub>
    * Description: Bromine concentration
    * range: [Double](types/Double.md)
 * [waterCalcium](waterCalcium.md)  <sub>OPT</sub>
    * Description: Calcium concentration
    * range: [Double](types/Double.md)
 * [waterCarbonate](waterCarbonate.md)  <sub>OPT</sub>
    * Description: Carbonate concentration
    * range: [Double](types/Double.md)
 * [waterChlorine](waterChlorine.md)  <sub>OPT</sub>
    * Description: Chlorine concentration
    * range: [Double](types/Double.md)
 * [waterFluorine](waterFluorine.md)  <sub>OPT</sub>
    * Description: Fluorine concentration
    * range: [Double](types/Double.md)
 * [waterIron](waterIron.md)  <sub>OPT</sub>
    * Description: Iron concentration
    * range: [Double](types/Double.md)
 * [waterMagnesium](waterMagnesium.md)  <sub>OPT</sub>
    * Description: Magnesium concentration
    * range: [Double](types/Double.md)
 * [waterManganese](waterManganese.md)  <sub>OPT</sub>
    * Description: Manganese concentration
    * range: [Double](types/Double.md)
 * [waterNitrateAndNitriteN](waterNitrateAndNitriteN.md)  <sub>OPT</sub>
    * Description: Nitrate plus nitrite concentration as milligrams Nitrogen per liter
    * range: [Double](types/Double.md)
 * [waterNitriteN](waterNitriteN.md)  <sub>OPT</sub>
    * Description: Nitrite concentration concentration as milligrams Nitrogen per liter
    * range: [Double](types/Double.md)
 * [waterOrthophosphateP](waterOrthophosphateP.md)  <sub>OPT</sub>
    * Description: Orthophosphate concentration as milligrams Phosphorus per liter
    * range: [Double](types/Double.md)
 * [waterPotassium](waterPotassium.md)  <sub>OPT</sub>
    * Description: Potassium concentration
    * range: [Double](types/Double.md)
 * [waterSilica](waterSilica.md)  <sub>OPT</sub>
    * Description: Silica concentration
    * range: [Double](types/Double.md)
 * [waterSodium](waterSodium.md)  <sub>OPT</sub>
    * Description: Sodium concentration
    * range: [Double](types/Double.md)
 * [waterSulfate](waterSulfate.md)  <sub>OPT</sub>
    * Description: Sulfate concentration
    * range: [Double](types/Double.md)
 * [waterTotalNitrogen](waterTotalNitrogen.md)  <sub>OPT</sub>
    * Description: Total nitrogen concentration
    * range: [Double](types/Double.md)
 * [waterTotalOrganicCarbon](waterTotalOrganicCarbon.md)  <sub>OPT</sub>
    * Description: Total organic carbon
    * range: [Double](types/Double.md)
 * [waterTotalPhosphorus](waterTotalPhosphorus.md)  <sub>OPT</sub>
    * Description: Total phosphorus
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:wc_externalLabData_in |
| **In Subsets:** | | DP0.20286.001 |

