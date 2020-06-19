SOURCES = kbase gold neon mixs
EXTS = _datamodel.py .graphql .schema.json .owl -docs

all: $(foreach s,$(SOURCES), $(foreach x,$(EXTS), target/$s/$s$x))
#all: $(foreach s,$(SOURCES), all_$s/$s)
#all_%: 
#	echo $(foreach x,$(EXTS), target/$*.$x)



test:
	pytest tests/*py

# these are then moved to test
downloads/kbase/%:
	curl -L -s https://raw.githubusercontent.com/kbaseIncubator/sample_service_validator_config/master/$* > $@


target/kbase/kbase.yaml: tests/kbase/kbase.yaml
	cp $< $@

target/neon/neon.yaml: tests/neon/neon.yaml
	cp $< $@

target/gold/gold.yaml: tests/gold/gold.yaml
	cp $< $@

target/mixs/mixs.yaml: 
	cp ../nmdc-metadata/schema/mixs.yaml $@
target/mixs/core.yaml: 
	cp ../nmdc-metadata/schema/core.yaml $@
target/mixs/prov.yaml: 
	cp ../nmdc-metadata/schema/prov.yaml $@

#vpath %_datamodel.py target/kbase target/neon

target/%_datamodel.py: target/%.yaml
	gen-py-classes $< > $@
target/%.graphql: target/%.yaml
	gen-graphql $< > $@
target/%.schema.json: target/%.yaml
	gen-json-schema $< > $@
target/%.csv: target/%.yaml
	gen-csv $< > $@
target/%.owl: target/%.yaml
	gen-owl $< > $@
target/%.ttl: target/%.owl
	cp $< $@
target/%-docs: target/%.yaml
	pipenv run gen-markdown --dir $@ $<

tests/gold/gold-schema.tsv:
	./util/sql2tsv.pl tests/gold/schema/*.sql > $@
tests/gold/gold-%-schema.tsv: tests/gold/schema/%.sql
	./util/sql2tsv.pl $< > $@
target/gold/biosample.ttl: tests/gold/biosample.yaml
	gen-owl $< > $@

deploy-docs:
	$(foreach s,$(SOURCES), cp -pr target/$s/$s-docs/ docs/$s ;)

## Matches

ONTS = envo uo
SRC_TTL = $(foreach s,$(SOURCES),target/$s/$s.ttl) $(foreach s,$(ONTS),ontologies/$s.ttl)
mappings/matches.tsv: $(SRC_TTL)
	rdfmatch -w mappings/weights.pro -i mappings/prefixes.ttl $(patsubst %, -i %, $(SRC_TTL)) match > $@
mappings/nomatches-gold-%.tsv: $(SRC_TTL)
	rdfmatch -p gold.vocab  -w mappings/weights.pro -i mappings/prefixes.ttl -i target/gold/gold.ttl -i target/$*/$*.ttl nomatch > $@
mappings/nomatches-biosample-gold-%.tsv: target/gold/biosample.ttl $(SRC_TTL)
	rdfmatch -p gold.vocab --match_prefix $*  -w mappings/weights.pro -i mappings/prefixes.ttl -i $< -i target/$*/$*.ttl nomatch > $@
mappings/%-summary.tsv: mappings/%.tsv
	grep -v ^# $<  | mlr --tsv count-distinct -f subject_source,object_source then sort -nr count > $@

OBO=http://purl.obolibrary.org/obo
ontologies/%.ttl:
	robot convert -I $(OBO)/$*.owl -o $@
