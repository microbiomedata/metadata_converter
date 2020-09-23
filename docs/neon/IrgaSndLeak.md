
# Type: irgaSndLeak




URI: [neon:IrgaSndLeak](https://data.neonscience.org/IrgaSndLeak)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/[IrgaSndLeak&#124;qfTrapIn:integer%20%3F;qfTrapOut:integer%20%3F;qfLeak:integer%20%3F;qfHeatSoni:integer%20%3F;qfHeatTube:integer%20%3F;qfHeatCap:integer%20%3F;qfHeatVali:integer%20%3F])

## Attributes


### Own

 * [qfHeatCap](qfHeatCap.md)  <sub>OPT</sub>
    * Description: Qualifying flag (qf) indicating the status of the heater (Heat) for the rain cap (Cap; 0 = heater off [default], 1 = heater on)
    * range: [Integer](types/Integer.md)
 * [qfHeatSoni](qfHeatSoni.md)  <sub>OPT</sub>
    * Description: Qualifying flag (qf) indicating the status of the heater (Heat; heated 3-D sonic (Soni) anemometer only; 0 = off [default], 1 = on)
    * range: [Integer](types/Integer.md)
 * [qfHeatTube](qfHeatTube.md)  <sub>OPT</sub>
    * Description: Qualifying flag (qf) indicating the status of the heater (Heat) for the intake tube (Tube; 0 = heater on [default], 1 = heater off)
    * range: [Integer](types/Integer.md)
 * [qfHeatVali](qfHeatVali.md)  <sub>OPT</sub>
    * Description: Qualifying flag (qf) indicating the status of the heater (Heat) for the validation gas (Vali) path (0 = heater off [default], 1 = heater on)
    * range: [Integer](types/Integer.md)
 * [qfLeak](qfLeak.md)  <sub>OPT</sub>
    * Description: Qualifying flag (qf) indicating the status of the samling line leak (Leak) test master solenoid (0 = leak test not being performed [default], 1 = leak test being perfomed)
    * range: [Integer](types/Integer.md)
 * [qfTrapIn](qfTrapIn.md)  <sub>OPT</sub>
    * Description: Qualifying flag (qf) indicating the status of the water trap (Trap) inlet (In) solenoid (0 = open [default], 1 = close)
    * range: [Integer](types/Integer.md)
 * [qfTrapOut](qfTrapOut.md)  <sub>OPT</sub>
    * Description: Qualifying flag (qf) indicating the status of the water trap (Trap) vent (Out) solenoid (0 = close [default], 1 = open)
    * range: [Integer](types/Integer.md)

## Other properties

|  |  |  |
| --- | --- | --- |
| **Mappings:** | | neon:irgaSndLeak |
| **In Subsets:** | | DP0.00008.001 |

