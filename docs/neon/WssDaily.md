
# Type: wss_daily




URI: [neon:WssDaily](https://data.neonscience.org/WssDaily)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[WssDaily&#124;date:time%20%3F;corPresQF:string%20%3F;dewTempQF:string%20%3F;precipQF:string%20%3F;RHQF:string%20%3F;shortRadQF:string%20%3F;staPresQF:string%20%3F;tempTripleQF:string%20%3F;windSpeedQF:string%20%3F;wssCorPres:double%20%3F;wssDewTempMaximum:double%20%3F;wssDewTempMean:double%20%3F;wssDewTempMinimum:double%20%3F;wssDewTempStdErMean:double%20%3F;wssDewTempVariance:double%20%3F;wssPrecipTotal:double%20%3F;wssRHMaximum:double%20%3F;wssRHMean:double%20%3F;wssRHMinimum:double%20%3F;wssRHStdErMean:double%20%3F;wssRHVariance:double%20%3F;wssShortRadMaximum:double%20%3F;wssShortRadMean:double%20%3F;wssShortRadMinimum:double%20%3F;wssShortRadStdErMean:double%20%3F;wssShortRadVariance:double%20%3F;wssStaPresMaximum:double%20%3F;wssStaPresMean:double%20%3F;wssStaPresMinimum:double%20%3F;wssStaPresStdErMean:double%20%3F;wssStaPresVariance:double%20%3F;wssTempTripleMaximum:double%20%3F;wssTempTripleMean:double%20%3F;wssTempTripleMinimum:double%20%3F;wssTempTripleStdErMean:double%20%3F;wssTempTripleVariance:double%20%3F;wssWindSpeedMaximum:double%20%3F;wssWindSpeedMean:double%20%3F;wssWindSpeedMinimum:double%20%3F;wssWindSpeedStdErMean:double%20%3F;wssWindSpeedVariance:double%20%3F;wssDewTempNumPts:double%20%3F;wssRHNumPts:double%20%3F;wssShortRadNumPts:double%20%3F;wssStaPresNumPts:double%20%3F;wssTempTripleNumPts:double%20%3F;wssWindSpeedNumPts:double%20%3F])

## Attributes


### Own

 * [RHQF](RHQF.md)  <sub>OPT</sub>
    * Description: Quality flag for relative humidity summary statistics (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [corPresQF](corPresQF.md)  <sub>OPT</sub>
    * Description: Quality flag for summary statistics of pressure corrected to sea level (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [date](date.md)  <sub>OPT</sub>
    * Description: Date or date and time of measurement, observation, or collection event
    * range: [Time](types/Time.md)
 * [dewTempQF](dewTempQF.md)  <sub>OPT</sub>
    * Description: Quality flag for dew or frost point temperature summary statistics (1=fail, 0=pass)
    * range: [String](types/String.md)
 * [precipQF](precipQF.md)  <sub>OPT</sub>
    * Description: Quality flag for precipitation summary statistics (1=fail, 0=pass)
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
 * [wssDewTempNumPts](wssDewTempNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of dew or frost point temperature for weather summary statistics
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
 * [wssRHNumPts](wssRHNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of relative humidity for weather summary statistics
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
 * [wssShortRadNumPts](wssShortRadNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of Incoming Shortwave Radiation for weather summary statistics
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
 * [wssStaPresNumPts](wssStaPresNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of station pressure for weather summary statistics
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
 * [wssTempTripleNumPts](wssTempTripleNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of triple aspirated air temperature for weather summary statistics
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
 * [wssWindSpeedNumPts](wssWindSpeedNumPts.md)  <sub>OPT</sub>
    * Description: Number of points used to calculate the arithmetic mean of wind speed for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssWindSpeedStdErMean](wssWindSpeedStdErMean.md)  <sub>OPT</sub>
    * Description: Standard error of the mean for wind speed for weather summary statistics
    * range: [Double](types/Double.md)
 * [wssWindSpeedVariance](wssWindSpeedVariance.md)  <sub>OPT</sub>
    * Description: Variance in wind speed for weather summary statistics
    * range: [Double](types/Double.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:wss_daily |
| **In Subsets:** | | DP4.00001.001 |

