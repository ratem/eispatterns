all: deps test

deps: specloud lettuce ludibrio should-dsl

lettuce:
	@python -c 'import lettuce' 2>/dev/null || pip install lettuce

specloud:
	@python -c 'import specloud' 2>/dev/null || pip install --no-deps specloud -r http://github.com/hugobr/specloud/raw/master/requirements.txt

ludibrio:
	@python -c 'import ludibrio' 2>/dev/null || pip install http://github.com/nsigustavo/ludibrio/tarball/master

should-dsl:
	@python -c 'import should_dsl' 2>/dev/null || pip install http://github.com/hugobr/should-dsl/tarball/master
	
path:
    export PYTHONPATH=..

test: unit acceptance

unit: path specloud ludibrio should-dsl
	@echo =======================================
	@echo ========= Running unit specs ==========
	@specloud spec
	@echo

acceptance: path lettuce
	@echo ==============================================
	@echo ========= Running acceptance specs ===========
	@lettuce
	@echo

