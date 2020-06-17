SOURCES = kbase neon mixs
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
target/%.owl: target/%.yaml
	gen-owl $< > $@
target/%-docs: target/%.yaml
	pipenv run gen-markdown --dir $@ $<

deploy-docs:
	$(foreach s,$(SOURCES), cp -pr target/$s/$s-docs/ docs/$s ;)
