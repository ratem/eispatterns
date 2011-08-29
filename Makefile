all: deps test

deps: specloud ludibrio should-dsl fluidity extreme_fluidity

specloud:
	@python -c 'import specloud' 2>/dev/null || pip install --no-deps specloud -r https://github.com/hugobr/specloud/raw/master/requirements.txt

ludibrio:
	@python -c 'import ludibrio' 2>/dev/null || pip install -e git+https://github.com/nsigustavo/ludibrio.git#egg=ludibrio

should-dsl:
	@python -c 'import should_dsl' 2>/dev/null || pip install -e git+https://github.com/hugobr/should-dsl.git#egg=should_dsl

fluidity:
	@python -c 'import fluidity' 2>/dev/null || pip install -e git+https://github.com/nsi-iff/fluidity.git#egg=fluidity

extreme_fluidity:
	@python -c 'import xfluidity' 2>/dev/null || pip install -e git+https://github.com/nsi-iff/extreme_fluidity.git#egg=extreme_fluidity

path:
    export PYTHONPATH=.

test: unit

unit: specloud ludibrio should-dsl path
	@echo =======================================
	@echo ========= Running unit specs ==========
	@specloud spec
	@echo

