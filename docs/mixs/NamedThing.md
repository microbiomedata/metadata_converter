
# Type: named thing


a databased entity or concept/class

URI: [https://microbiomedata/schema/mixs/NamedThing](https://microbiomedata/schema/mixs/NamedThing)


![img](http://yuml.me/diagram/nofunky;dir:TB/class/\[NamedThing&#124;id:string;name:string%20%3F;description:string%20%3F;alternate_identifiers:string%20*]^-\[OntologyClass])

## Children

 * [OntologyClass](OntologyClass.md)

## Referenced by class


## Attributes


### Own

 * [alternate identifiers](alternate_identifiers.md)  <sub>0..*</sub>
    * Description: Non-primary identifiers
    * range: [String](types/String.md)
 * [description](description.md)  <sub>OPT</sub>
    * Description: a human-readable description of a thing
    * range: [String](types/String.md)
 * [id](id.md)  <sub>REQ</sub>
    * Description: A unique identifier for a thing. Must be either a CURIE shorthand for a URI or a complete URI
    * range: [String](types/String.md)
 * [name](name.md)  <sub>OPT</sub>
    * Description: A human readable label for an entity
    * range: [String](types/String.md)
