SOURCES = kbase dwc gold neon mixs emp
#EXTS = _datamodel.py .graphql .schema.json .owl -docs .shex
EXTS = .graphql .schema.json .owl -docs .shex

all: $(foreach s,$(SOURCES), $(foreach x,$(EXTS), target/$s/$s$x))
#all: $(foreach s,$(SOURCES), all_$s/$s)
#all_%: 
#	echo $(foreach x,$(EXTS), target/$*.$x)

rebuild: test all

test:
	pytest tests/*py

# these are then moved to test
downloads/kbase/%:
	curl -L -s https://raw.githubusercontent.com/kbaseIncubator/sample_service_validator_config/master/$* > $@
downloads/dwc.csv:
	curl -L -s https://raw.githubusercontent.com/tdwg/dwc/master/vocabulary/term_versions.csv > $@

# run tests to first generate yaml; these are then copied to target area
target/kbase/kbase.yaml: tests/kbase/kbase.yaml
	cp $< $@
target/neon/neon.yaml: tests/neon/neon.yaml
	cp $< $@
target/gold/gold.yaml: tests/gold/gold.yaml
	cp $< $@
target/dwc/dwc.yaml: tests/dwc/dwc.yaml
	cp $< $@

# mixs needs extra stuff
target/mixs/mixs.yaml: 
	cp ../nmdc-metadata/schema/mixs.yaml $@
target/mixs/core.yaml: 
	cp ../nmdc-metadata/schema/core.yaml $@
target/mixs/prov.yaml: 
	cp ../nmdc-metadata/schema/prov.yaml $@



#vpath %_datamodel.py target/kbase target/neon

target/%_datamodel.py: target/%.yaml
	gen-py-classes $< > $@.tmp && mv $@.tmp $@
target/%.graphql: target/%.yaml
	gen-graphql $< > $@.tmp && mv $@.tmp $@
target/%.schema.json: target/%.yaml
	gen-json-schema $< > $@.tmp && mv $@.tmp $@
target/%.shex: target/%.yaml
	gen-shex $< > $@.tmp && mv $@.tmp $@
target/%.csv: target/%.yaml
	gen-csv $< > $@.tmp && mv $@.tmp $@
target/%.owl: target/%.yaml
	gen-owl $< > $@.tmp && mv $@.tmp $@
target/%.ttl: target/%.owl
	cp $< $@
target/%-docs: target/%.yaml
	gen-markdown --dir $@ $<

tests/gold/gold-schema.tsv:
	./util/sql2tsv.pl tests/gold/schema/*.sql > $@.tmp && mv $@.tmp $@
tests/gold/gold-%-schema.tsv: tests/gold/schema/%.sql
	./util/sql2tsv.pl $< > $@.tmp && mv $@.tmp $@
target/gold/biosample.ttl: tests/gold/biosample.yaml
	gen-owl $< > $@.tmp && mv $@.tmp $@

# this is curated
#target/gold/gold-to-mixs.sssom.tsv: ../nmdc-metadata//metadata-translation/src/data/GOLD-to-mixs-map.tsv
#	./util/goldmap2sssom.pl $< > $@.tmp && mv $@.tmp $@
target/gold/gold-to-mixs.sssom.tsv: ../nmdc-metadata//schema/mappings/gold-to-mixs.sssom.tsv
	cp $< $@
target/gold/gold-to-mixs.sssom.ttl: target/gold/gold-to-mixs.sssom.tsv
	sssom convert -i $< -o $@



deploy-docs:
	$(foreach s,$(SOURCES), cp -pr target/$s/$s-docs/ docs/$s ;)

## Matches

ONTS = envo uo bco obi datacite pato agro
SRC_TTL = $(foreach s,$(SOURCES),target/$s/$s.ttl) $(foreach s,$(ONTS),ontologies/$s.ttl)
INC_PRIOR_MAPPINGS = -i target/gold/gold-to-mixs.sssom.ttl
mappings/matches.tsv: $(SRC_TTL)
	rdfmatch $(INC_PRIOR_MAPPINGS) -w mappings/weights.pro -i mappings/prefixes.ttl $(patsubst %, -i %, $(SRC_TTL)) match > $@.tmp && mv $@.tmp $@
mappings/matches-gold-%.tsv: $(SRC_TTL)
	rdfmatch $(INC_PRIOR_MAPPINGS) -p gold.vocab  -w mappings/weights.pro -i mappings/prefixes.ttl -i target/gold/gold.ttl -i target/$*/$*.ttl match > $@.tmp && mv $@.tmp $@
mappings/nomatches-gold-%.tsv: $(SRC_TTL)
	rdfmatch $(INC_PRIOR_MAPPINGS) -p gold.vocab  -w mappings/weights.pro -i mappings/prefixes.ttl -i target/gold/gold.ttl -i target/$*/$*.ttl nomatch > $@.tmp && mv $@.tmp $@
mappings/nomatches-biosample-gold-%.tsv: target/gold/biosample.ttl $(SRC_TTL)
	rdfmatch $(INC_PRIOR_MAPPINGS) -p gold.vocab --match_prefix $*  -w mappings/weights.pro -i mappings/prefixes.ttl -i $< -i target/$*/$*.ttl nomatch > $@.tmp && mv $@.tmp $@
mappings/nomatches-kbase-%.tsv: $(SRC_TTL)
	rdfmatch $(INC_PRIOR_MAPPINGS) -p kbase  -w mappings/weights.pro -i mappings/prefixes.ttl -i target/kbase/kbase.ttl -i target/$*/$*.ttl nomatch > $@.tmp && mv $@.tmp $@

mappings/%-summary.tsv: mappings/%.tsv
	grep -v ^# $<  | mlr --tsv count-distinct -f subject_source,object_source then sort -nr count > $@.tmp && mv $@.tmp $@

OBO=http://purl.obolibrary.org/obo
ontologies/%.ttl:
	robot convert -I $(OBO)/$*.owl -o $@
ontologies/datacite.ttl:
	robot merge -I http://purl.org/spar/datacite.ttl  -o  $@
