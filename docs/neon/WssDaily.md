
# Type: wss_daily




URI: [neon:WssDaily](https://data.neonscience.org/WssDaily)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/)

## Attributes


### Own

 * [date](date.md)  <sub>OPT</sub>
    * Description: Date or date and time of measurement, observation, or collection event
    * range: [Time](types/Time.md)

### Inherited from wss_yearly:

 * [year](year.md)  <sub>OPT</sub>
    * Description: The calendar year in which an observation or measurement was made
    * range: [Time](types/Time.md)
    * inherited from: None
 * [corPresQF](corPresQF.md)  <sub>OPT</sub>
    * Description: Quality flag for summary statistics of pressure corrected to sea level (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [dewTempQF](dewTempQF.md)  <sub>OPT</sub>
    * Description: Quality flag for dew or frost point temperature summary statistics (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [precipQF](precipQF.md)  <sub>OPT</sub>
    * Description: Quality flag for precipitation summary statistics (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [RHQF](RHQF.md)  <sub>OPT</sub>
    * Description: Quality flag for relative humidity summary statistics (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [shortRadQF](shortRadQF.md)  <sub>OPT</sub>
    * Description: Quality flag for incoming shortwave radiation summary statistics (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [staPresQF](staPresQF.md)  <sub>OPT</sub>
    * Description: Quality flag for station pressure summary statistics (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [tempTripleQF](tempTripleQF.md)  <sub>OPT</sub>
    * Description: Quality flag for temperature summary statistics (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [windSpeedQF](windSpeedQF.md)  <sub>OPT</sub>
    * Description: Quality flag for wind speed summary statistics (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [wssCorPres](wssCorPres.md)  <sub>OPT</sub>
    * Description: Mean station pressure corrected to sea level for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssDewTempMaximum](wssDewTempMaximum.md)  <sub>OPT</sub>
    * Description: Maximum dew or frost point temperature for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssDewTempMean](wssDewTempMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of dew or frost point temperature for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssDewTempMinimum](wssDewTempMinimum.md)  <sub>OPT</sub>
    * Description: Minimum dew or frost point temperature for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssDewTempStdErMean](wssDewTempStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for dew or frost point temperature for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssDewTempVariance](wssDewTempVariance.md)  <sub>OPT</sub>
    * Description: Variance in dew or frost point temperature for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssPrecipTotal](wssPrecipTotal.md)  <sub>OPT</sub>
    * Description: Total precipitation observed for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssRHMaximum](wssRHMaximum.md)  <sub>OPT</sub>
    * Description: Maximum relative humidity for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssRHMean](wssRHMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of relative humidity for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssRHMinimum](wssRHMinimum.md)  <sub>OPT</sub>
    * Description: Minimum relative humidity for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssRHStdErMean](wssRHStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for relative humidity for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssRHVariance](wssRHVariance.md)  <sub>OPT</sub>
    * Description: Variance in relative humidity for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssShortRadMaximum](wssShortRadMaximum.md)  <sub>OPT</sub>
    * Description: Maximum Incoming Shortwave Radiation for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssShortRadMean](wssShortRadMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of Incoming Shortwave Radiation for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssShortRadMinimum](wssShortRadMinimum.md)  <sub>OPT</sub>
    * Description: Minimum Incoming Shortwave Radiation for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssShortRadStdErMean](wssShortRadStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for Incoming Shortwave Radiation for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssShortRadVariance](wssShortRadVariance.md)  <sub>OPT</sub>
    * Description: Variance in Incoming Shortwave Radiation for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssStaPresMaximum](wssStaPresMaximum.md)  <sub>OPT</sub>
    * Description: Maximum station pressure for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssStaPresMean](wssStaPresMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of station pressure for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssStaPresMinimum](wssStaPresMinimum.md)  <sub>OPT</sub>
    * Description: Minimum station pressure for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssStaPresStdErMean](wssStaPresStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for station pressure for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssStaPresVariance](wssStaPresVariance.md)  <sub>OPT</sub>
    * Description: Variance in station pressure for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssTempTripleMaximum](wssTempTripleMaximum.md)  <sub>OPT</sub>
    * Description: Maximum triple aspirated air temperature for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssTempTripleMean](wssTempTripleMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of triple aspirated air temperature for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssTempTripleMinimum](wssTempTripleMinimum.md)  <sub>OPT</sub>
    * Description: Minimum triple aspirated air temperature for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssTempTripleStdErMean](wssTempTripleStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for triple aspirated air temperature for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssTempTripleVariance](wssTempTripleVariance.md)  <sub>OPT</sub>
    * Description: Variance in triple aspirated air temperature for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssWindSpeedMaximum](wssWindSpeedMaximum.md)  <sub>OPT</sub>
    * Description: Maximum wind speed for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssWindSpeedMean](wssWindSpeedMean.md)  <sub>OPT</sub>
    * Description: Arithmetic mean of wind speed for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssWindSpeedMinimum](wssWindSpeedMinimum.md)  <sub>OPT</sub>
    * Description: Minimum wind speed for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssWindSpeedStdErMean](wssWindSpeedStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for wind speed for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssWindSpeedVariance](wssWindSpeedVariance.md)  <sub>OPT</sub>
    * Description: Variance in wind speed for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssDewTempNumPts](wssDewTempNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of dew or frost point temperature for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssRHNumPts](wssRHNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of relative humidity for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssShortRadNumPts](wssShortRadNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of Incoming Shortwave Radiation for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssStaPresNumPts](wssStaPresNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of station pressure for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssTempTripleNumPts](wssTempTripleNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of triple aspirated air temperature for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssWindSpeedNumPts](wssWindSpeedNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of wind speed for weather summary statistics
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:wss_daily |
| **In Subsets:** | | DP4.00001.001 |

